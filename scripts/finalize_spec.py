"""Fail-closed mechanical Spec delivery after independent review.

This helper never decides that review passed. The caller supplies the independently
reviewed commit and PASS record URL. The helper verifies repository/branch/PR state,
completion checkboxes, clean reviewed state, Git hooks, and archive ordering before
performing the mechanical archive + Draft-to-Ready transition.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
from pathlib import Path


FINAL_REVIEW_MARKER = "<!-- final-review -->"
FINALIZE_MARKER = "<!-- finalize-spec -->"


class Blocked(RuntimeError):
    pass


def run(*args: str) -> str:
    result = subprocess.run(args, capture_output=True, text=True, check=False)
    if result.returncode:
        stderr = result.stderr.strip()
        raise Blocked(f"Command failed: {' '.join(args)}" + (f"\n{stderr}" if stderr else ""))
    return result.stdout.strip()


def git(*args: str) -> str:
    return run("git", *args)


def parse_origin_repo() -> str:
    url = git("remote", "get-url", "origin")
    patterns = (
        r"https://github\.com/([^/]+/[^/]+?)(?:\.git)?$",
        r"git@github\.com:([^/]+/[^/]+?)(?:\.git)?$",
        r"ssh://git@github\.com/([^/]+/[^/]+?)(?:\.git)?$",
    )
    for pattern in patterns:
        match = re.fullmatch(pattern, url)
        if match:
            return match.group(1)
    raise Blocked("origin must be a direct github.com repository URL; adapt finalize_spec.py for another host.")


def pr_state(repo: str, number: int) -> dict:
    payload = run(
        "gh", "pr", "view", str(number), "--repo", repo,
        "--json", "number,state,isDraft,headRefName,headRefOid,baseRefName,url",
    )
    return json.loads(payload)


def checkbox_state(line: str) -> str | None:
    match = re.match(r"^\s*- \[([ x~-])\] ", line)
    return match.group(1) if match else None


def validate_tasks(tasks_path: Path) -> list[str]:
    lines = tasks_path.read_text(encoding="utf-8").splitlines(keepends=True)
    final_review = [i for i, line in enumerate(lines) if FINAL_REVIEW_MARKER in line]
    finalize = [i for i, line in enumerate(lines) if FINALIZE_MARKER in line]
    if len(final_review) != 1 or len(finalize) != 1:
        raise Blocked("tasks.md must contain exactly one final-review marker and one finalize-spec marker.")

    allowed_unchecked = {final_review[0], finalize[0]}
    for index, line in enumerate(lines):
        state = checkbox_state(line)
        if state in {" ", "~", "-"} and index not in allowed_unchecked:
            raise Blocked(f"Incomplete task/review checkpoint remains in tasks.md at line {index + 1}.")

    for index in allowed_unchecked:
        if checkbox_state(lines[index]) != " ":
            raise Blocked("Final review/finalize checkpoints must be unchecked before mechanical delivery.")
    return lines


def complete_tasks(lines: list[str], reviewed_commit: str, review_url: str) -> str:
    output: list[str] = []
    for line in lines:
        if FINAL_REVIEW_MARKER in line or FINALIZE_MARKER in line:
            line = line.replace("- [ ]", "- [x]", 1)
        output.append(line)
    text = "".join(output).rstrip()
    return text + f"\n\nDelivery completed after independent review at `{reviewed_commit}`: {review_url}\n"


def validate_review_url(review_url: str, repo: str, pr_number: int) -> None:
    prefix = f"https://github.com/{repo}/pull/{pr_number}#"
    if not review_url.startswith(prefix):
        raise Blocked("review-url must point to the owning PR's independent PASS record.")
    suffix = review_url[len(prefix):]
    if not re.fullmatch(r"(?:issuecomment-|pullrequestreview-)[0-9]+", suffix):
        raise Blocked("review-url must identify a concrete PR comment or review record.")


def validate_environment(args: argparse.Namespace) -> tuple[str, str, dict, Path, Path, list[str]]:
    root = Path(git("rev-parse", "--show-toplevel")).resolve()
    if Path.cwd().resolve() != root:
        raise Blocked("Run from the owning repository root.")

    branch = git("symbolic-ref", "--quiet", "--short", "HEAD")
    if not branch or branch == "main":
        raise Blocked("A dedicated attached non-main branch is required.")
    if git("config", "--get", "core.hooksPath") != ".githooks":
        raise Blocked("Configure core.hooksPath=.githooks before delivery.")
    for hook in ("pre-commit", "pre-push"):
        path = root / ".githooks" / hook
        if path.is_symlink() or not path.is_file() or not os.access(path, os.X_OK):
            raise Blocked(f"Repository hook missing or not executable: {path.relative_to(root)}")

    if git("status", "--porcelain"):
        raise Blocked("Working tree/index must be clean before finalization.")
    head = git("rev-parse", "HEAD")
    if head != args.reviewed_commit:
        raise Blocked("HEAD must equal the independently reviewed commit before mechanical delivery.")
    if not re.fullmatch(r"[0-9a-f]{40}", args.reviewed_commit):
        raise Blocked("reviewed-commit must be a full 40-character commit SHA.")

    if not re.fullmatch(r"[1-9][0-9]*-[a-z0-9]+(?:-[a-z0-9]+)*", args.spec):
        raise Blocked("spec must be an Issue-number-based directory name such as 123-short-slug.")

    repo = parse_origin_repo()
    validate_review_url(args.review_url, repo, args.pr)
    pr = pr_state(repo, args.pr)
    if pr["state"] != "OPEN" or not pr["isDraft"]:
        raise Blocked("Owning PR must be open and Draft before finalization.")
    if pr["baseRefName"] != "main" or pr["headRefName"] != branch:
        raise Blocked("PR base/head does not match main and the current branch.")
    if pr["headRefOid"] != head:
        raise Blocked("Remote PR HEAD must equal the independently reviewed commit.")

    source = root / ".kiro" / "specs" / args.spec
    target = root / "docs" / "spec-archive" / args.spec
    if source.is_symlink() or not source.is_dir():
        raise Blocked(f"Active Spec not found or unsafe: {source.relative_to(root)}")
    if target.exists() or target.is_symlink():
        raise Blocked(f"Archive destination already exists: {target.relative_to(root)}")
    required = [source / "design.md", source / "tasks.md"]
    if not all(path.is_file() and not path.is_symlink() for path in required):
        raise Blocked("Reviewed Spec must contain regular design.md and tasks.md files.")
    if not any((source / name).is_file() for name in ("requirements.md", "bugfix.md")):
        raise Blocked("Reviewed Spec must contain requirements.md or bugfix.md.")

    lines = validate_tasks(source / "tasks.md")
    return repo, branch, pr, source, target, lines


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--spec", required=True)
    parser.add_argument("--pr", type=int, required=True)
    parser.add_argument("--reviewed-commit", required=True)
    parser.add_argument("--review-url", required=True)
    parser.add_argument("--check", action="store_true", help="read-only preflight")
    args = parser.parse_args()

    try:
        repo, branch, _pr, source, target, task_lines = validate_environment(args)
        if args.check:
            print("READY: reviewed mechanical delivery can proceed; approval was supplied by the caller.")
            return

        target.parent.mkdir(parents=True, exist_ok=True)
        source.rename(target)
        tasks = target / "tasks.md"
        tasks.write_text(complete_tasks(task_lines, args.reviewed_commit, args.review_url), encoding="utf-8")

        changed = git("status", "--porcelain")
        if not changed:
            raise Blocked("Expected archive changes were not produced.")
        for line in changed.splitlines():
            path = line[3:]
            if not (path.startswith(f".kiro/specs/{args.spec}/") or path.startswith(f"docs/spec-archive/{args.spec}/")):
                raise Blocked(f"Unexpected concurrent change detected: {path}")

        git("add", "--", str(source.relative_to(Path.cwd())), str(target.relative_to(Path.cwd())))
        git("diff", "--cached", "--check")
        git("commit", "-m", f"docs: finalize reviewed Spec {args.spec}")
        git("push", "origin", f"HEAD:refs/heads/{branch}")

        published = pr_state(repo, args.pr)
        current = git("rev-parse", "HEAD")
        if published["headRefOid"] != current or not published["isDraft"]:
            raise Blocked("Published PR state changed unexpectedly before Ready transition.")

        run("gh", "pr", "ready", str(args.pr), "--repo", repo)
        final = pr_state(repo, args.pr)
        if final["isDraft"] or final["headRefOid"] != current:
            raise Blocked("Draft-to-Ready transition was not confirmed at the published finalization commit.")

        print(f"DONE: Spec archived and PR #{args.pr} marked Ready. Merge remains manual.")
    except (Blocked, OSError, ValueError, json.JSONDecodeError) as exc:
        parser.exit(1, f"BLOCKED: {exc}\n")


if __name__ == "__main__":
    main()
