# AGENTS.md

## Purpose

This repository uses AI-assisted, requirements-driven development. Preserve requirement authority, change scope,
reproducibility, repository safety, and reviewability while avoiding duplicated policy and unnecessary model work.

Project-specific product requirements, domain invariants, validation commands, and security constraints belong in the
adopting repository. This file defines reusable development-process policy only.

## Authority precedence

When sources disagree, use this order unless the adopting project explicitly defines a stricter order:

1. Authoritative project requirements and domain specifications.
2. Explicitly approved architecture/security contracts referenced by those requirements.
3. The GitHub Issue driving the change: scope, purpose, constraints, and acceptance criteria. An Issue must not silently
   redefine an authoritative requirement.
4. This `AGENTS.md`.
5. Applicable `.kiro/steering/` guidance.
6. The active Spec artifacts in their workflow-defined order.
7. Existing implementation and tests.

Do not reinterpret a higher-authority source merely to match current code. Raise genuine conflicts explicitly.

## Living documentation

Reusable documentation describes the current intended state or process, not a chronological Issue diary. Preserve
durable rationale, but keep Issue-specific execution history and evidence in the Issue, PR, Spec progress record, or an
ADR when one is actually warranted.

## Language policy

Repository and GitHub artifacts are English by default: code comments, technical documentation, Specs, commit messages,
Issue/PR text, and review records. Interactive communication with the operator may use the operator's preferred
language. A project may explicitly define additional translated reference documents, but one language/version must
remain authoritative.

## Task scope

Keep changes limited to the explicit Issue or task. Before editing, identify the owning Issue/task, applicable
requirements, affected implementation/tests, and current working-tree state.

Do not silently broaden work into adjacent defects, redesign unrelated components, or alter authoritative requirements
merely to simplify implementation. Report non-blocking adjacent defects separately.

## Workspace isolation

Every task belongs to the Git worktree root resolved at runtime by `git rev-parse --show-toplevel`. Never treat an
absolute path committed in a Spec as authoritative workspace identity.

Do not edit another workspace root, run repository-changing commands against another root, use another worktree's
uncommitted state as implementation truth, or copy uncommitted changes across worktrees. Load `#workspace-isolation`
for Multi-root Workspace or parallel-worktree work.

## Git workflow and repository safety

All changes use a dedicated non-`main` branch. Before commit or push, verify the current branch and intended
repository/worktree. Never bypass repository hooks.

Prohibited unless the operator explicitly authorizes the specific action and the environment permits it:

```text
git commit --no-verify
git commit -n
git push --no-verify
git reset
git clean
git restore
git checkout -- <path>
git branch -D
git branch -d
git push --force
git push -f
git push --delete
```

Normal non-force pushes of a dedicated working branch and creation/update of its Issue/PR are permitted when required by
the task. Merge remains a human/operator action unless explicitly delegated.

Repository-managed hooks live in `.githooks/`. New clones/worktrees must configure:

```bash
git config core.hooksPath .githooks
```

## Permission-aware command selection

Inspect the active execution permission policy before selecting commands when the environment exposes one. Use an
already-allowed command form that has the correct target, working directory, runtime, arguments, and side effects. Do
not mutate permission policy or try equivalent spellings to evade ASK/DENY decisions.

Use commands directly through PATH unless the project specifies a repository-owned script or project runtime. Run
repository-owned scripts from the repository root using repository-relative paths.

## Provisioned tools and lint

Environment/workspace setup owns tool provisioning. Agents and subagents must not install or upgrade tools merely to run
lint or validation. Do not use package-acquisition runners such as `npx`, `npm exec`, `pnpm dlx`, `yarn dlx`, or `uvx`
for lint execution.

Use already-provisioned commands or project-local tool paths. If a required tool is unavailable, report the exact unrun
check rather than substituting an unverified tool or claiming PASS.

## Scratch files

Generic disposable agent scratch belongs under:

```text
.local/kiro-scratch/
```

Do not use `/tmp` for project scratch. Keep secrets, credentials, production data, customer data, or other sensitive
evidence out of scratch unless the adopting project's explicit security policy permits it. Routine scratch cleanup is
not part of task completion.

## Verification proportionality

For each non-trivial validation, identify the property/risk it proves, the minimum sufficient evidence, the appropriate
layer, and the stopping condition. Prefer focused checks during implementation and broader regression at the final
checkpoint when required by scope.

Do not rerun expensive repository-wide validation after every internal execution slice unless that slice can only be
validated truthfully at that level. Reuse still-valid evidence when code, dependencies, and environment have not
invalidated it.

## Review protocol

Independent review asks whether the relevant lifecycle gate can truthfully pass, not whether the artifact can be
polished indefinitely.

A finding is BLOCKING when it prevents satisfaction of an explicit requirement, acceptance criterion,
correctness/security invariant, required lifecycle gate, or truthful PASS/result. Cleaner architecture, extra telemetry,
naming improvements, future-proofing, or optional defensive work are not BLOCKING by themselves.

### Independent Spec Review

Confirm:

- Issue/requirement coverage;
- consistency across requirements/design/tasks;
- feasibility in the current repository/tooling;
- material correctness/security boundaries;
- task dependency/executability;
- sufficient validation planning for the affected risk.

PASS once implementation can proceed without guessing about material behavior.

### Independent Code / Requirements Review

Review the resulting system state against the applicable requirements and invariants, not only the diff. Use
implementation-level evidence appropriate to the risk. For state, identity, persistence, security, or other high-risk
boundaries, include structural/adversarial inspection when materially relevant.

Stop the review once the gate criteria are satisfied and no BLOCKING finding remains.

## Spec-Driven Development

Substantive implementation or design work uses a Kiro Spec unless it qualifies for the Direct Change route in
`#sdd-workflow` or is a truly trivial non-development edit.

A Spec never adds, removes, weakens, or overrides higher-authority requirements or Issue acceptance criteria. Choose the
Kiro workflow and review intensity according to semantic risk, not diff size.

Spec implementation tasks must be started through Kiro's native Spec Task Execution interface. A chat prompt may
supplement an already-started task but must not infer/select/start an incomplete `tasks.md` task. Load
`#spec-task-execution` before starting Spec implementation.

## Guidance routing

Load the following guidance when its scope applies. If an automatic/file-match load is unavailable, load the same file
manually rather than proceeding without it.

| Name | File | Use before |
| --- | --- | --- |
| `#sdd-workflow` | `.kiro/steering/sdd-workflow.md` | route selection or any Spec lifecycle work |
| `#review` | `.kiro/steering/review.md` | substantive independent review or review-fix planning |
| `#workspace-isolation` | `.kiro/steering/workspace-isolation.md` | worktree, Multi-root, parallel/cross-root work |
| `#execution` | `.kiro/steering/execution.md` | shell, Git, file edits, delegation, project commands |
| `#documentation-policy` | `.kiro/steering/documentation-policy.md` | reusable documentation or Spec editing |
| `#source-development` | `.kiro/steering/source-development.md` | source-code design/implementation |
| `#test-development` | `.kiro/steering/test-development.md` | test planning/execution/completion verification |
| `#execution-efficiency` | `.kiro/steering/execution-efficiency.md` | decomposing/delegating an approved implementation task |
| `#spec-task-execution` | `.kiro/steering/spec-task-execution.md` | starting a Spec `tasks.md` implementation task |
| `#task-prompt` | `.kiro/steering/task-prompt.md` | preparing a bounded Kiro/subagent task prompt |

`.kiro/specs/README.md` defines the Spec directory convention and template use.
