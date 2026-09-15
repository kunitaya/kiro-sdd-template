---
inclusion: manual
description: Shell, Git, file-editing, lint, bootstrap, scratch, and delegation conventions. Load with #execution.
---

# Execution Defaults

Run project commands from the repository root unless the command semantically requires another directory. Resolve that root with `git rev-parse --show-toplevel`.

## Command selection

Inspect active permissions when available. Reuse a correct already-allowed invocation. Do not alter executable paths, wrappers, or argument forms merely to evade ASK/DENY. Repository-owned scripts use repository-relative paths from the root.

## File operations

Use dedicated file-reading/editing tools when the environment provides them for tracked-file reads/edits. Shell remains appropriate for locating, counting, comparing, querying, Git inspection, and executing project tools. Do not substitute destructive shell cleanup for a denied dedicated deletion operation.

## Lint and provisioned tools

Run existing tools directly through PATH or the project's declared environment. Do not use `npx`, `npm exec`, `pnpm dlx`, `yarn dlx`, `uvx`, or equivalent acquisition runners for lint. Do not install/upgrade tools during lint or delegated validation. Missing tools are reported as unrun checks, never PASS.

Delegation that may lint must pass the known invocation/readiness state and repeat: run from repository root, use existing provisioned tools, no acquisition/install/upgrade, report missing tools.

## Scratch

Use `.local/kiro-scratch/` for generic agent scratch; never `/tmp` for project scratch. Leave routine scratch in place. Protect secrets/sensitive data according to project policy.

## Workspace bootstrap

If `scripts/bootstrap-workspace` is present, the workspace owner runs the mutating form when initialization/repair is needed and confirms:

```bash
./scripts/bootstrap-workspace --check
```

before native Spec task execution. A `PreTaskExec` command hook may surface readiness diagnostics, but projects must not assume the hook blocks task start unless that behavior has been verified for their Kiro version.

## Pre-change inspection

Before edits identify the Issue/task, directly relevant requirements/invariants, existing implementation/tests, and working-tree state. Preserve existing user changes.

## Git hooks and delivery

For new clones/worktrees configure `core.hooksPath` to `.githooks` when this template's hooks are adopted. Follow the dedicated-branch workflow in `AGENTS.md`. Stage only intended files, inspect diff/status before commit/push, and never bypass hooks.

## Delegation

Parent agents own repository-level understanding and integration. Delegated edits remain bound to the same worktree/environment and project safety rules. After a subagent returns, independently inspect actual file contents/diff/status before accepting or publishing its work.