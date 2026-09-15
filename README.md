# kiro-sdd-template

English (authoritative) | [日本語](README.ja.md)

A reusable Kiro-based Spec-Driven Development environment generalized from a
production-style AI-assisted workflow. The goal is to preserve mature development
governance and safety controls while keeping product/domain truth in the adopting
repository.

This is **not** a shortened rewrite of the source workflow. The reusable rules retain
the original process depth where that depth is project-independent: requirement
authority, native Spec structure, worktree isolation, deterministic workspace
readiness, review convergence, fail-closed delivery, and human merge authority.

## Included components

| Path | Purpose |
| --- | --- |
| `AGENTS.md` | Repository-wide authority, scope, Git safety, verification, review, and SDD policy |
| `.kiro/steering/` | Scoped SDD, execution, review, documentation, testing, source, workspace, and task guidance |
| `.kiro/specs/_templates/` | Native-compatible requirements, design, bugfix, and tasks templates with governance/matrices |
| `.kiro/hooks/workspace-bootstrap-check.json` | `PreTaskExec` workspace-readiness diagnostic hook |
| `.githooks/` | Guards against direct commit/push to `main` |
| `scripts/bootstrap-workspace` | Deterministic Python/uv per-worktree bootstrap with fail-closed non-mutating `--check` |
| `scripts/finalize-spec` / `scripts/finalize_spec.py` | Validated mechanical post-review Spec delivery and Draft-to-Ready transition |
| `templates/kiro-task-prompt.md` | Bounded task-prompt template |
| `docs/setup.md` | Adoption and customization guide |
| `.markdownlint.json` | Shared Markdown validation baseline |

## Core workflow

```text
Authoritative project requirements + GitHub Issue
    ↓
Choose Direct Change or a Kiro Spec by semantic risk
    ↓
Requirements/Design/Bugfix artifacts -> tasks.md
    ↓
Validate and publish to a dedicated branch + Draft PR
    ↓
Supplemental automated review, if available
    ↓
Independent Spec Review
    ↓
Implementation authorization
    ↓
Native Kiro Spec Task Execution
    ↓
Implementation + proportionate validation
    ↓
Final validation + publication to the same Draft PR
    ↓
Supplemental automated re-review, if available
    ↓
Independent Code / Requirements Review
    ↓
Required fixes / delta review
    ↓
Validated mechanical Spec archive + Draft PR Ready
    ↓
Human merge gate
```

Key principles:

- higher-authority requirements are never rewritten to fit current code;
- one Issue normally owns one branch and one PR;
- Kiro's native artifact/task lifecycle is preserved rather than replaced by a custom
  mini-format;
- task prompts carry task-specific facts, not duplicated repository policy;
- worktrees are isolated at runtime by root/branch/repository identity;
- workspace READY means the current worktree/runtime/dependency state matches the
  recorded bootstrap fingerprint, not merely that an interpreter exists;
- lint/validation uses already-provisioned tools rather than package-acquisition
  runners;
- verification is risk-based and reusable rather than repeated mechanically;
- automated review is supplemental evidence, not an authority;
- only BLOCKING findings create mandatory correction rounds;
- final delivery validates review evidence, PR/branch state, completion state, clean
  reviewed HEAD, and Git safety controls before archival/Ready;
- merge remains a human/operator decision unless explicitly delegated.

## Workspace and bootstrap model

Each Git worktree is treated as its own mutable development environment. The included
bootstrap is the reference implementation for Python/uv repositories. It validates:

- repository/worktree resolution;
- required tooling;
- `uv.lock` consistency before sync;
- rejection of symlinked or separately mounted `.venv` environments;
- `.venv` interpreter binding to the current worktree;
- a state fingerprint covering physical repository root, Python version,
  `pyproject.toml`, and `uv.lock`;
- serialized mutating bootstrap operations; and
- a fail-closed, non-mutating `--check` path used by the Kiro readiness hook.

```bash
./scripts/bootstrap-workspace          # initialize/repair READY
./scripts/bootstrap-workspace --check  # non-mutating readiness verification
```

Projects using another technology stack should **replace the implementation without
weakening the contract**. If they do not want workspace bootstrap/readiness enforcement,
they should remove the script, hook, and corresponding lifecycle checkpoints together.

The Kiro `PreTaskExec` hook surfaces readiness diagnostics. Do not assume the hook
itself blocks task start unless that behavior has been verified for the installed Kiro
version; the workspace owner remains responsible for confirming READY before native
task execution.

## Native Spec compatibility

The files under `.kiro/specs/_templates/` augment Kiro's native Spec artifacts. They
preserve native workflow concepts and expected sections while adding repository
workspace identity, requirement traceability, invariant inventories, review matrices,
resumable task state, and delivery checkpoints.

When Kiro changes its native Spec structures, task execution, hooks, or diagnostics,
inspect the installed behavior and reconcile the template. Do not freeze an obsolete
native contract merely because it was once copied into this repository.

## Review and delivery

Independent Spec Review asks whether implementation can begin without guessing about
material behavior. Independent Code / Requirements Review evaluates the resulting
implementation against requirements and affected invariants. High-risk state,
identity/provenance, persistence, status/NULL, security, or lifecycle changes use the
applicable structural/adversarial matrices.

`scripts/finalize-spec` is deliberately fail-closed. It does **not** decide that review
passed. The caller supplies a full independently reviewed commit SHA and concrete PASS
record URL. Before archival it requires, among other things:

- clean working tree/index at exactly the reviewed commit;
- configured/executable repository Git hooks;
- an open Draft PR whose head/base match the current branch and `main`;
- remote PR HEAD equal to the reviewed commit;
- complete Spec artifacts;
- every task/review checkpoint complete except the two final mechanical checkpoints;
- no pre-existing archive destination.

It then performs only the mechanical post-review transition: mark the two final
checkpoints, record the PASS reference, archive the Spec, commit/push the reviewed
mechanical change, and transition the same Draft PR to Ready. Merge remains manual.

## Adoption

Read [Setup and Customization](docs/setup.md). An adopting repository must explicitly
define or adapt:

- authoritative project/domain requirements;
- project-specific invariants and security/sensitive-data rules;
- source/test file-match patterns;
- validation commands and tool provisioning;
- environment/bootstrap implementation for its stack;
- automated-review integration, if any;
- GitHub host/repository conventions if they differ from the included helper's
  `github.com` assumptions.

Do not move domain requirements, customer-specific configuration, product schemas,
business terminology, or Issue-specific history into this reusable template.

Configure the included Git hooks after cloning/creating a worktree:

```bash
git config core.hooksPath .githooks
```

## Language policy

English is authoritative for repository/GitHub artifacts. `README.ja.md` is a reference
translation and must be updated with this README whenever its meaning changes.
Interactive operator communication may use the operator's preferred language.

## Status

The reusable governance and SDD environment is included. Adopting repositories still
require explicit project customization and validation against their installed Kiro and
toolchain versions.

## Project status and affiliation

This is independently maintained and unofficial. It is not an official product of, or
endorsed by, Kiro, OpenAI, or their developers.

## License

[MIT License](LICENSE)
