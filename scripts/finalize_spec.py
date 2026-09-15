"""Publish mechanical post-review Spec delivery; never decide review approval.

Generalized directly from the production helper in
koseikensetsu/mailbox-privacy-analyzer. Repository identity is derived from
origin instead of being hard-coded; the reviewed-delivery state machine is
otherwise preserved.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import stat
import subprocess
import tempfile
from pathlib import Path


MARKER = "<!-- finalize-spec -->"
REVIEW_MARKER = "<!-- final-review -->"
BASE_BRANCH = "main"


class Blocked(RuntimeError):
    """The current state does not permit mechanical delivery."""


def run(*args: str) -> str:
    result = subprocess.run(args, capture_output=True, text=True, check=False)
    if result.returncode:
        stderr = result.stderr.strip()
        rendered = " ".join(args[:2])
        raise Blocked(f"Command failed: {rendered}" + (f"\n{stderr}" if stderr else ""))
    return result.stdout.strip()


def git(*args: str) -> str:
    return run("git", *args)


def blob(data: bytes) -> str:
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()


def tree(revision: str) -> dict[str, tuple[str, str]]:
    result: dict[str, tuple[str, str]] = {}
    for record in git("ls-tree", "-rz", revision).split("\0"):
        if record:
            metadata, path = record.split("\t", 1)
            mode, kind, oid = metadata.split()
            if kind != "blob":
                raise Blocked("Submodules are not supported by this delivery helper.")
            result[path] = (mode, oid)
    return result


def parse_github_repository(url: str) -> str:
    patterns = (
        r"https://github\.com/([^/]+/[^/]+?)(?:\.git)?$",
        r"git@github\.com:([^/]+/[^/]+?)(?:\.git)?$",
        r"ssh://git@github\.com/([^/]+/[^/]+?)(?:\.git)?$",
    )
    for pattern in patterns:
        match = re.fullmatch(pattern, url)
        if match:
            return match.group(1)
    raise Blocked(f"Unsupported origin URL: {url}")


def repository_from_origin() -> str:
    urls = (
        git("remote", "get-url", "--all", "origin").splitlines()
        + git("remote", "get-url", "--push", "--all", "origin").splitlines()
    )
    if not urls:
        raise Blocked("origin must have fetch and push URLs.")
    repositories = {parse_github_repository(url) for url in urls}
    if len(repositories) != 1:
        raise Blocked("All origin fetch/push URLs must identify the same GitHub repository.")
    return repositories.pop()


def pr_state(repository: str, number: int) -> dict:
    return json.loads(
        run(
            "gh",
            "pr",
            "view",
            str(number),
            "--repo",
            repository,
            "--json",
            "number,state,isDraft,headRefName,headRefOid,"
            "headRepository,headRepositoryOwner,baseRefName",
        )
    )


def check_pr(pr: dict, branch: str, repository: str) -> None:
    owner, name = repository.split("/", 1)
    if (
        pr["state"] != "OPEN"
        or pr["baseRefName"] != BASE_BRANCH
        or pr["headRefName"] != branch
        or pr["headRepository"]["name"] != name
        or pr["headRepositoryOwner"]["login"] != owner
    ):
        raise Blocked(
            f"Expected an open, same-repository Issue PR targeting {BASE_BRANCH}."
        )


def remote_check(branch: str, repository: str) -> None:
    urls = (
        git("remote", "get-url", "--all", "origin").splitlines()
        + git("remote", "get-url", "--push", "--all", "origin").splitlines()
    )
    allowed = {
        f"https://github.com/{repository}.git",
        f"https://github.com/{repository}",
        f"git@github.com:{repository}.git",
        f"ssh://git@github.com/{repository}.git",
    }
    if not urls or any(url not in allowed for url in urls):
        raise Blocked("origin must point directly to the owning GitHub repository.")
    if not branch or branch == BASE_BRANCH:
        raise Blocked("A dedicated, attached Issue branch is required.")
    if git("config", "--get", "core.hooksPath") != ".githooks":
        raise Blocked("Configure repository Git hooks before delivery.")
    for hook in ("pre-commit", "pre-push"):
        path = Path(".githooks") / hook
        if path.is_symlink() or not path.is_file() or not os.access(path, os.X_OK):
            raise Blocked(f"Repository hook is missing or not executable: {path}")


def record_review(original: bytes) -> bytes:
    """Allow only the explicitly marked final-review checkbox to change after PASS."""
    lines = original.decode("utf-8").splitlines(keepends=True)
    matches = [i for i, line in enumerate(lines) if REVIEW_MARKER in line]
    if len(matches) > 1:
        raise Blocked("Expected at most one final-review checkpoint.")
    if matches:
        index = matches[0]
        if not re.match(r"^- \[[ x]\] .+", lines[index]) or MARKER in lines[index]:
            raise Blocked("Invalid final-review checkpoint.")
        lines[index] = lines[index].replace("- [ ]", "- [x]", 1)
    return "".join(lines).encode()


def task_completion(original: bytes, revision: str, review_url: str) -> bytes:
    text = original.decode("utf-8")
    lines = text.splitlines(keepends=True)
    matches = [i for i, line in enumerate(lines) if MARKER in line]
    if len(matches) != 1 or not re.match(r"^- \[ \] .+", lines[matches[0]]):
        raise Blocked("Expected one unchecked finalize-spec delivery checkpoint.")
    for index, line in enumerate(lines):
        if index != matches[0] and re.match(r"\s*- \[(?: |~|-)\]", line):
            raise Blocked("Other task/review checkpoints remain incomplete.")
    lines[matches[0]] = lines[matches[0]].replace("- [ ]", "- [x]", 1)
    return (
        "".join(lines).rstrip()
        + "\n\n"
        + f"Delivery completed after independent review at `{revision}`: {review_url}\n"
    ).encode()


def safe_path(path: Path) -> None:
    root = Path.cwd()
    if not path.resolve().is_relative_to(root):
        raise Blocked(f"Path escapes owning worktree: {path}")
    for part in (path, *path.parents):
        if part == Path("."):
            break
        if part.is_symlink():
            raise Blocked(f"Symlink in delivery path: {part}")


def atomic_write(path: Path, content: bytes) -> None:
    """Replace only a fully written file; failed staging is disposable ignored scratch."""
    scratch = Path(".local/kiro-scratch")
    safe_path(scratch)
    scratch.mkdir(parents=True, exist_ok=True)
    if scratch.stat().st_dev != path.parent.stat().st_dev:
        raise Blocked("Scratch and Spec must share a filesystem for atomic replacement.")
    mode = stat.S_IMODE(path.stat().st_mode)
    with tempfile.NamedTemporaryFile(
        dir=scratch, prefix="finalize-spec-", delete=False
    ) as staged:
        staged.write(content)
        staged.flush()
        os.fsync(staged.fileno())
        os.fchmod(staged.fileno(), mode)
        name = staged.name
    os.replace(name, path)


def working_spec(source: str, target: str) -> dict[str, tuple[str, str]]:
    result: dict[str, tuple[str, str]] = {}
    for directory in (Path(source), Path(target)):
        safe_path(directory)
        if not directory.exists():
            continue
        for path in directory.rglob("*"):
            safe_path(path)
            if path.is_dir():
                continue
            if not path.is_file():
                raise Blocked(f"Unexpected file type: {path}")
            mode = "100755" if path.stat().st_mode & stat.S_IXUSR else "100644"
            result[path.as_posix()] = (mode, blob(path.read_bytes()))
    return result


def finalize(args: argparse.Namespace) -> None:
    root = Path(git("rev-parse", "--show-toplevel"))
    if root.resolve() != Path.cwd().resolve():
        raise Blocked("Run from the owning repository root.")
    if not re.fullmatch(r"[1-9][0-9]*-[a-z0-9]+(?:-[a-z0-9]+)*", args.spec):
        raise Blocked("Use the Issue-number-based Spec directory name, not a path.")
    if not re.fullmatch(r"[0-9a-f]{40}", args.reviewed_commit):
        raise Blocked("Use the full independently reviewed commit SHA.")

    repository = repository_from_origin()
    prefix = f"https://github.com/{repository}/pull/{args.pr}#"
    if not args.review_url.startswith(prefix) or not re.fullmatch(
        r"(?:issuecomment-|pullrequestreview-)[0-9]+",
        args.review_url[len(prefix) :],
    ):
        raise Blocked("Provide the independent PASS record URL on this PR.")

    branch = git("symbolic-ref", "--quiet", "--short", "HEAD")
    remote_check(branch, repository)

    operations = (
        "MERGE_HEAD",
        "CHERRY_PICK_HEAD",
        "REVERT_HEAD",
        "rebase-merge",
        "rebase-apply",
    )
    for operation in operations:
        if Path(git("rev-parse", "--git-path", operation)).exists():
            raise Blocked("Finish the existing Git operation before delivery.")

    git("merge-base", "--is-ancestor", args.reviewed_commit, "HEAD")
    baseline = tree(args.reviewed_commit)
    source = f".kiro/specs/{args.spec}"
    target = f"docs/spec-archive/{args.spec}"
    original_spec = {
        path: entry for path, entry in baseline.items() if path.startswith(source + "/")
    }
    if (
        f"{source}/tasks.md" not in original_spec
        or f"{source}/design.md" not in original_spec
        or not any(
            f"{source}/{name}" in original_spec
            for name in ("requirements.md", "bugfix.md")
        )
        or any(path.startswith(target + "/") for path in baseline)
        or any(mode not in ("100644", "100755") for mode, _ in original_spec.values())
    ):
        raise Blocked(
            "Reviewed Spec is incomplete, contains symlinks, or archive already exists."
        )

    original = subprocess.check_output(
        ["git", "show", f"{args.reviewed_commit}:{source}/tasks.md"]
    )
    reviewed = record_review(original)
    completed = task_completion(reviewed, args.reviewed_commit, args.review_url)
    reviewed_spec = dict(original_spec)
    reviewed_spec[f"{source}/tasks.md"] = (
        original_spec[f"{source}/tasks.md"][0],
        blob(reviewed),
    )
    moved_spec = {
        target + path[len(source) :]: entry for path, entry in original_spec.items()
    }
    archived_spec = {
        target + path[len(source) :]: entry for path, entry in reviewed_spec.items()
    }
    done_spec = dict(archived_spec)
    done_spec[f"{target}/tasks.md"] = (
        original_spec[f"{source}/tasks.md"][0],
        blob(completed),
    )
    outside = {path: entry for path, entry in baseline.items() if path not in original_spec}
    done_tree = outside | done_spec
    states = [
        baseline,
        outside | reviewed_spec,
        outside | moved_spec,
        outside | archived_spec,
        done_tree,
    ]

    head = tree("HEAD")
    if head not in states:
        raise Blocked("Changes since review are not this helper's exact mechanical delivery.")

    pr = pr_state(repository, args.pr)
    check_pr(pr, branch, repository)
    remote = git("ls-remote", "origin", f"refs/heads/{branch}").split()
    if not remote or remote[0] != pr["headRefOid"]:
        raise Blocked("PR and remote branch differ; retry after resolving the remote state.")
    git("merge-base", "--is-ancestor", pr["headRefOid"], "HEAD")
    if tree(pr["headRefOid"]) not in states:
        raise Blocked("Remote branch has unrecognized changes.")
    if not pr["isDraft"] and tree(pr["headRefOid"]) in (
        baseline,
        outside | reviewed_spec,
    ):
        raise Blocked("PR was made Ready before archive publication; inspect manually.")

    changed = (
        git("diff", "--cached", "--name-only", "-z").split("\0")
        + git("diff", "--name-only", "-z").split("\0")
        + git("ls-files", "--others", "--exclude-standard", "-z").split("\0")
    )
    if any(
        path
        and not (path.startswith(source + "/") or path.startswith(target + "/"))
        for path in changed
    ):
        raise Blocked("Unrelated local changes must be resolved before delivery.")

    current = working_spec(source, target)
    if current not in (original_spec, reviewed_spec, moved_spec, archived_spec, done_spec):
        raise Blocked("Local Spec differs from the reviewed files or expected delivery state.")
    if current == done_spec and pr["isDraft"]:
        raise Blocked("Completion record exists while PR is Draft; inspect manually.")

    if args.check:
        print("READY: mechanical delivery can run; review approval was supplied by the caller.")
        return

    if (
        head == done_tree
        and current == done_spec
        and pr["headRefOid"] == git("rev-parse", "HEAD")
    ):
        print(f"DONE: Spec delivery for PR #{args.pr} was already published; no changes.")
        return

    def publish(message: str) -> None:
        if git("symbolic-ref", "--quiet", "--short", "HEAD") != branch:
            raise Blocked("Branch changed during delivery.")
        remote_check(branch, repository)
        paths = sorted(
            set(
                git("diff", "--cached", "--name-only", "-z").split("\0")
                + git("diff", "--name-only", "-z").split("\0")
                + git("ls-files", "--others", "--exclude-standard", "-z").split("\0")
            )
            - {""}
        )
        if any(
            not (path.startswith(source + "/") or path.startswith(target + "/"))
            for path in paths
        ):
            raise Blocked("Concurrent unrelated edit detected.")
        if paths:
            git("add", "--", *paths)
        staged = tree(git("write-tree"))
        if staged not in (outside | archived_spec, done_tree):
            raise Blocked("Staged tree is not the expected mechanical archive/completion.")
        git("diff", "--cached", "--check")
        if git("diff", "--cached", "--name-only"):
            git("commit", "-m", message)
        if tree("HEAD") != staged or git("status", "--porcelain"):
            raise Blocked("Commit/hooks changed the expected tree; inspect before publication.")
        git("push", "origin", f"HEAD:refs/heads/{branch}")
        observed = pr_state(repository, args.pr)
        check_pr(observed, branch, repository)
        if observed["headRefOid"] != git("rev-parse", "HEAD"):
            raise Blocked("PR has not confirmed the pushed revision; rerun the same command.")

    if current in (original_spec, reviewed_spec):
        Path(target).parent.mkdir(parents=True, exist_ok=True)
        if Path(target).exists():
            raise Blocked("Archive destination already exists.")
        Path(source).rename(target)
    if current != done_spec:
        atomic_write(Path(target, "tasks.md"), reviewed)

    publish(f"docs: archive completed Spec {args.spec}")
    observed = pr_state(repository, args.pr)
    check_pr(observed, branch, repository)
    if observed["headRefOid"] != git("rev-parse", "HEAD"):
        raise Blocked("PR changed before Ready transition.")
    if observed["isDraft"]:
        run("gh", "pr", "ready", str(args.pr), "--repo", repository)
    observed = pr_state(repository, args.pr)
    check_pr(observed, branch, repository)
    if observed["isDraft"] or observed["headRefOid"] != git("rev-parse", "HEAD"):
        raise Blocked("Ready transition not confirmed; completion remains unchecked.")

    atomic_write(Path(target, "tasks.md"), completed)
    publish(f"docs: record completed Spec delivery {args.spec}")
    if pr_state(repository, args.pr)["isDraft"]:
        raise Blocked("PR returned to Draft during publication; inspect manually.")
    print(f"DONE: Spec archived, published, and PR #{args.pr} Ready. Merge remains manual.")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--spec", required=True, help="Issue-number-slug")
    parser.add_argument("--pr", required=True, type=int)
    parser.add_argument("--reviewed-commit", required=True)
    parser.add_argument(
        "--review-url",
        required=True,
        help="Caller-supplied independent PASS; not inferred or self-approved",
    )
    parser.add_argument("--check", action="store_true", help="Read-only preflight")
    args = parser.parse_args()
    try:
        finalize(args)
    except (Blocked, OSError, ValueError, subprocess.CalledProcessError) as exc:
        parser.exit(1, f"BLOCKED: {exc}\n")


if __name__ == "__main__":
    main()
