---
inclusion: manual
description: Shell, Git, file operations, command permissions, lint/tool provisioning, bootstrap, scratch, delegation, and publication conventions. Load with #execution.
---

# Execution Defaults

Follow repository-root `AGENTS.md` as the authoritative policy. This file provides
operational detail and must not weaken task scope, workspace isolation, permission, Git,
or review rules.

## Repository root and working directory

Resolve the owning worktree with:

```bash
git rev-parse --show-toplevel
```

Run project-related commands from that root unless a command semantically requires
another working directory. Do not infer root identity from `.venv`, the current shell
path, or a path persisted in a Spec.

Repository-owned scripts are invoked from the root by repository-relative path, for
example:

```bash
./scripts/bootstrap-workspace --check
./scripts/finalize-spec --check ...
```

Do not replace these with absolute worktree paths merely because the absolute path is
known; absolute paths couple execution to one machine/worktree and often create avoidable
permission mismatches.

## Permission-aware command selection

When the active environment exposes an execution permission policy, inspect it before
selecting command forms. Reuse the context while the workspace/policy remains unchanged.

Choose an already-allowed form only when it is also semantically correct: target,
working directory, runtime, arguments, and side effects must match the task. Permission
matching alone is not correctness.

Do not:

- change executable aliases/paths or argument shape merely to avoid ASK;
- wrap a denied operation in Python/shell/a helper to evade policy;
- mutate permission configuration merely to get an operation through;
- try successive equivalent command spellings after DENY hoping one bypasses the rule;
- infer an unseen permission grants authority.

If no correct allowed form exists, report/request only the concrete capability actually
needed through the environment's normal mechanism.

## File reading and editing

Use dedicated repository/file tools for tracked-file content reads and edits when the
execution environment provides them. Do not choose an approval-requiring shell rewrite
when a dedicated editor can perform the authorized edit transparently.

Purpose-based rule:

- locate/search/count/compare/query/validate -> shell or repository search tools may be
  appropriate;
- read tracked file content -> dedicated reader when available;
- modify tracked file content -> dedicated editor when available;
- direct deletion -> dedicated deletion tool when available/required by the environment.

Do not substitute `sed -i`, `perl -pi`, `tee`, shell redirection, or Python one-liners for
tracked-file edits merely for convenience when dedicated edit tools exist. Do not wrap
a denied deletion in another command/script.

Shell remains appropriate for project tools, read-only Git inspection, `rg`/`grep`
location discovery, structured queries, validation, and generated/untracked output.

## Lint and provisioned tools

Tool provisioning belongs to workspace/environment setup, not lint execution.

- Use tools directly through PATH unless a project-local execution environment is
  specified.
- Use repository/project runtime paths when the project declares them.
- Do not use package acquisition/execution runners to perform lint: `npx`, `npm exec`,
  `pnpm dlx`, `yarn dlx`, `uvx`, or equivalents.
- Do not install/upgrade dependencies or linters merely because a task delegated lint.
- Reuse a known working invocation while environment evidence remains valid.
- If a required tool is missing/broken, report the exact command/check that could not
  run. Missing validation is not PASS.

Delegation that may run lint/validation must pass the known invocation/readiness state
and repeat these constraints to subagents.

## Scratch files

Generic agent scratch belongs only under:

```text
.local/kiro-scratch/
```

Do not use `/tmp` for project scratch. Remain at repository root and address scratch by
repository-relative path. Scratch is disposable and must not become authoritative input
or evidence merely because it exists.

Protect secrets, credentials, production data, customer data, personal data, and other
sensitive artifacts according to the adopting project's security policy. Routine scratch
cleanup is unnecessary and must not be used as an excuse for destructive commands.

## Workspace bootstrap

When the repository adopts `scripts/bootstrap-workspace`, the workspace owner uses the
mutating form only for initialization/repair and confirms the non-mutating check before
native task execution:

```bash
./scripts/bootstrap-workspace
./scripts/bootstrap-workspace --check
```

The included Python/uv reference implementation intentionally validates more than
interpreter existence: lock consistency, worktree-bound environment ownership, stale
manifest/lock/runtime fingerprint, and concurrent bootstrap mutation.

A `PreTaskExec` hook may surface the check result. Unless the installed Kiro version is
confirmed to block on the hook result, treat it as a diagnostic signal and retain the
explicit READY confirmation in the workflow.

If a project replaces the bootstrap implementation, preserve the fail-closed,
non-mutating readiness contract or remove the hook/checkpoints together. Do not weaken
`--check` into an existence probe while still presenting it as a readiness gate.

## Pre-change inspection

Before editing:

1. identify the owning Issue/task and current lifecycle phase;
2. identify directly relevant authoritative requirements/invariants;
3. inspect current implementation and relevant tests before deciding how to change it;
4. inspect working-tree/branch state and preserve existing user changes;
5. confirm the owning workspace/root when worktree or Multi-root context is involved.

Use targeted lookup first, then expand only on concrete dependency/invariant triggers
under `#task-prompt`.

## Git hook setup

New clones/worktrees using the included hooks configure:

```bash
git config core.hooksPath .githooks
git config --get core.hooksPath
```

Expected value:

```text
.githooks
```

Do not bypass, disable, replace, or temporarily modify hooks to make commit/push succeed.

Before commit or push:

1. verify current branch;
2. confirm it is the intended non-main branch;
3. inspect `git status` and intended diff;
4. explicitly stage only task-scoped changes;
5. let normal hooks run;
6. after commit/push, verify published branch/PR state when the lifecycle depends on it.

## Feature-branch publication

Normal publication sequence:

```text
inspect -> edit -> focused validation -> final required validation
-> inspect diff/status -> stage intended files -> commit -> non-force push
-> create/update the owning Draft PR -> verify published state
```

Do not create duplicate PRs for the same Issue/branch merely because a later phase is
starting. Spec and implementation normally remain in one Draft PR.

Merge is not part of ordinary agent publication unless explicitly delegated.

## Delegation

Parent agents own repository-level understanding, decomposition, integration, and final
truthfulness. A subagent is an execution helper, not an excuse to outsource context
rediscovery or safety policy.

Every delegation involving file edits should state, concisely:

- owning repository/worktree/root;
- bounded objective and allowed scope;
- relevant files/symbols or narrow discovery target;
- required steering references;
- use dedicated file read/edit tools when available; no shell rewrite workaround;
- existing runtime/tool invocation; do not create new environments or install/upgrade
  dependencies without authority;
- project scratch under `.local/kiro-scratch/`, never `/tmp`;
- no cross-root edits or uncommitted-state borrowing;
- focused validation and explicit stop condition.

After a subagent returns, do not rely solely on its summary. Independently inspect the
actual changed files and diff/status before staging, committing, or reporting completion.

If a subagent is interrupted/denied, treat affected state as unverified until inspected.
Do not assume no file changed and do not assume a present change was produced through an
allowed mechanism.

## Review corrections

Before editing a required review correction, apply `#review`: summarize cause, affected
paths, behavior boundary, and verification. Then proceed without inventing a new approval
gate.

## Final Spec delivery

`scripts/finalize-spec` is an intentionally narrow reviewed-state transition. It must be
run from repository root after Independent Code / Requirements Review PASS with:

- full reviewed commit SHA;
- concrete PASS comment/review URL;
- owning PR number;
- active Spec directory name.

Use `--check` for read-only preflight. Do not manually imitate only part of the helper's
archive/Ready sequence when the repository policy requires the helper, because doing so
can break the reviewed-state and ordering guarantees.

The helper never merges. Merge remains the operator/human action unless explicitly
delegated.
