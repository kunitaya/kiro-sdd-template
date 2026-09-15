# Development Operations Runbook

English (authoritative) | [日本語](development-operations-runbook.ja.md)

## Purpose

This runbook is the human-facing procedure for preparing and operating a development
workspace after this template has been adopted into a repository.

It intentionally does not restate repository policy or template-customization details:

- `AGENTS.md` owns repository-wide development and safety policy.
- `.kiro/steering/` owns scoped execution, review, workspace, and SDD guidance.
- `docs/setup.md` owns one-time adoption and customization decisions.
- `.kiro/specs/README.md` owns the Spec directory and lifecycle conventions.
- this runbook owns the repeatable operator sequence for day-to-day development.

When those sources differ, follow their authority rules rather than this procedural summary.

## 1. One-time setup for a clone or machine

### 1.1 Clone and enter the repository

```bash
git clone <repository-url>
cd <repository-directory>
```

Confirm that the directory you opened is the intended repository root:

```bash
git rev-parse --show-toplevel
git remote -v
git branch --show-current
```

### 1.2 Enable repository Git hooks

Configure the repository-managed hooks:

```bash
git config core.hooksPath .githooks
git config core.hooksPath
```

Do not bypass the hooks with `--no-verify` or an alternate `core.hooksPath`.

### 1.3 Install the workspace permission policy

The reviewed permission template is:

```text
templates/permissions.yaml
```

Kiro stores the active workspace-scoped permission file outside the repository at:

```text
~/.kiro/workspace-roots/<hash>/permissions.yaml
```

This separation is intentional: a cloned repository must not be able to grant itself
trust. Open the exact repository/worktree root in Kiro and use the workspace trust entry
Kiro associates with that root. Do not invent or hard-code the `<hash>`.

Copy the reviewed template into that workspace-scoped file manually, then review any
project-specific additions before use. Do not ask the agent to modify its own active
permission file.

The template uses Kiro's capability rules:

- `deny` blocks the operation;
- `ask` requires human approval;
- `allow` pre-approves the operation;
- more restrictive rules win when scopes overlap.

An `ASK` or `DENY` result is a control boundary. Do not change command spelling, paths,
or tools merely to evade it.

Official Kiro references:

- <https://kiro.dev/docs/ide/whats-new-v1/permissions/>
- <https://kiro.dev/docs/cli/chat/configuration/>

### 1.4 Prepare the project environment

For Python/uv projects using the included bootstrap, complete the adoption-specific
settings described in `docs/setup.md`, then run:

```bash
./scripts/bootstrap-workspace
./scripts/bootstrap-workspace --check
```

Proceed only after the check reports READY.

For another stack, use the repository's approved replacement readiness procedure. Do not
replace readiness with a simple "tool exists" check.

### 1.5 Confirm required tools

Check the tools the repository actually uses, for example:

```bash
command -v git
command -v gh
command -v kiro
command -v uv
command -v markdownlint
```

Workspace/bootstrap provisioning owns dependencies. If a required validation tool is
missing, report that check as unavailable instead of installing or upgrading it during
the task.

## 2. Start a new Issue

### 2.1 Update the baseline

From the main working copy:

```bash
git switch main
git pull --ff-only
git status
```

Confirm that `main` is clean before creating the task branch/worktree.

### 2.2 Create a dedicated branch/worktree

Use one Issue per branch and PR. When using a separate worktree, create it from the
updated baseline, for example:

```bash
git worktree add ../<worktree-directory> -b <branch-name> main
```

Open only that new worktree as the implementation root.

Workspace-isolation rules are defined in
`.kiro/steering/workspace-isolation.md`; this runbook does not duplicate them.

### 2.3 Initialize the new worktree

In the new worktree:

```bash
git config core.hooksPath .githooks
git branch --show-current
git status
./scripts/bootstrap-workspace
./scripts/bootstrap-workspace --check
```

Kiro workspace permissions are scoped to the workspace root. Verify that the permission
file associated with this exact worktree root has the reviewed template; do not assume a
different worktree's trust entry applies.

### 2.4 Open Kiro at the worktree root

Open the worktree root, not a parent directory containing multiple task worktrees.

Before implementation:

1. confirm root, branch, and repository identity;
2. confirm workspace READY;
3. load the applicable steering;
4. select Direct Change or the appropriate Spec route via `#sdd-workflow`.

For Spec work, implementation tasks start through Kiro's native Spec Task Execution
interface. A supplementary chat prompt does not substitute for native task selection.

## 3. Daily start or resume

At the beginning of a session, or after interruption, verify actual state before relying
on a prior progress summary:

```bash
git rev-parse --show-toplevel
git branch --show-current
git status
./scripts/bootstrap-workspace --check
```

Then inspect the active Issue/PR and, for Spec work, the current `tasks.md` progress
record.

If the bootstrap script or dependency inputs changed, rerun the mutating bootstrap before
continuing.

## 4. Command and tool operation

Follow `AGENTS.md` and `#execution` for the detailed command policy. Operationally:

- run project executables from the repository root using repository-relative paths;
- use provisioned tools directly through PATH or the project-local environment;
- do not use `npx`, `npm exec`, `pnpm dlx`, `yarn dlx`, or `uvx` as a lint runner;
- do not install a missing validation tool during an implementation task;
- do not bypass `ASK`/`DENY` permissions;
- use `.local/kiro-scratch/` for disposable project scratch, not `/tmp`.

The permission template permits routine read/validation/development operations while
keeping destructive Git/filesystem actions and trust-boundary changes denied or
human-supervised.

## 5. Validation

Use the commands defined by the adopting repository. Typical template-level checks
include:

```bash
markdownlint "**/*.md"
sh -n scripts/bootstrap-workspace
sh -n scripts/finalize-spec
python3 -m py_compile scripts/finalize_spec.py
```

Run only the validation that is applicable to the changed scope, and record unrun or
unavailable checks truthfully.

Kiro native Spec diagnostics are separate from Markdown or source-code linting. When the
installed Kiro version exposes the required diagnostics, run them for Spec changes.

## 6. Publish and review

Use the same dedicated branch and Draft PR throughout one change.

For Spec-driven work, the detailed gate sequence belongs to `.kiro/specs/README.md` and
`#review`. At an operational level:

1. publish the reviewable Spec or implementation revision;
2. obtain the required independent review;
3. resolve BLOCKING findings;
4. revalidate only evidence invalidated by the correction;
5. keep optional improvements separate from gate-blocking work.

Automated reviewers are supplemental evidence only. Unavailable quota or service state
is not PASS.

## 7. Finalize a reviewed Spec

After the required final independent review PASS, use the reviewed full commit SHA and
the concrete PASS record URL:

```bash
./scripts/finalize-spec \
  --spec <issue-number>-<slug> \
  --pr <pr-number> \
  --reviewed-commit <full-reviewed-sha> \
  --review-url <independent-pass-url>
```

The finalizer owns the mechanical archive/Ready transition and recovery from its
recognized partial states. Do not reproduce those state transitions manually.

Merge remains a human/operator action unless explicitly delegated.

## 8. Common failure and recovery paths

| Condition | Operator action |
| --- | --- |
| `bootstrap-workspace --check` is not READY | Run the mutating bootstrap, inspect its reason token, and correct the reported ownership/dependency/configuration problem. |
| Permission result is `ASK` | Approve only if the exact command and side effects are intended; otherwise deny and use the documented operation. |
| Permission result is `DENY` | Stop. Do not attempt an equivalent spelling or alternate tool to bypass the rule. |
| Wrong root/branch is open | Stop repository-changing work and reopen the owning worktree root. |
| Required tool is missing | Record the validation as unavailable and return to the environment-provisioning process. |
| Spec task state is unclear after interruption | Inspect actual files/diff and `tasks.md`; preserve still-valid evidence and resume from the first incomplete bounded task. |
| Finalizer reports BLOCKED | Preserve the current state and address the reported PR/tree/review condition; rerun the same helper rather than manually reconstructing delivery. |
| Kiro product behavior differs from this runbook | Check the current Kiro documentation/version and update the template through review rather than silently changing local procedure. |

## 9. Maintaining the permissions template

`templates/permissions.yaml` is a reviewed source template, not the active trust file.

When a repository needs additional permission rules:

1. classify the rule as generic development policy or project-specific adaptation;
2. keep secrets and trust-store paths denied;
3. prefer exact/narrow command forms over broad wildcards;
4. keep destructive or authority-changing operations as `ASK` or `DENY`;
5. change the repository template through a normal PR;
6. after review/merge, manually update the active workspace-scoped file.

Do not commit the active file from `~/.kiro/workspace-roots/<hash>/` into the repository.
