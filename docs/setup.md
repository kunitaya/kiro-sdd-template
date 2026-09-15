# Setup and Customization

This document covers **adoption-time customization** of the template. It does not
describe daily development operation.

For clone/worktree startup, permissions installation, Issue start/resume, validation,
review, and recovery procedures, use the
[Development Operations Runbook](development-operations-runbook.md).

## Adoption principle

Do **not** simplify mature generic controls merely because the target project differs
from the source project. The intended transformation is:

```text
mature source workflow
    ↓
remove / parameterize product-domain specifics
    ↓
preserve generic lifecycle, safety, review, isolation, and validation semantics
```

Not:

```text
mature source workflow
    ↓
rewrite as a shorter approximation
```

## Required project decisions

An adopting repository must decide and record the following before routine development:

1. Define the authoritative requirements/domain specification and adapt the authority
   precedence in `AGENTS.md` only when the repository has a different legitimate
   authority model.
2. Define project-specific security, sensitive-data, compliance, and invariant rules.
3. Adapt `.kiro/steering/source-development.md` and `test-development.md` file-match
   patterns to the repository layout.
4. Define the actual validation commands/toolchain and provision required tools through
   the environment/bootstrap process.
5. Adapt the project-specific constants at the top of `scripts/bootstrap-workspace`
   without weakening its generic state machine.
6. Review `templates/permissions.yaml` and add only the project-specific permission
   rules that are actually required. The active Kiro workspace permission file is
   stored outside the repository.
7. Configure repository Git hooks with `git config core.hooksPath .githooks`.
8. Validate Kiro's installed native Spec structure, Task Execution, hook behavior, and
   diagnostics. Reconcile the templates when Kiro changes.
9. Decide which automated reviewer, if any, supplements Independent Review.
10. Review `scripts/finalize_spec.py` transport assumptions. The included helper targets
    `github.com`, `main`, the `gh` CLI, and the repository's two Git hooks.

## Repository skeleton

The template keeps common top-level development directories present from the first
commit:

```text
src/
tests/
docs/
docs/spec-archive/
```

A `.gitkeep` preserves an otherwise-empty directory. Remove it once real tracked content
exists. Keep `docs/spec-archive/` available for finalized Spec delivery.

## Kiro permissions template

The repository contains a reviewed source template at:

```text
templates/permissions.yaml
```

Kiro 1.0 stores the active workspace-scoped file outside the repository:

```text
~/.kiro/workspace-roots/<hash>/permissions.yaml
```

This prevents a cloned repository from granting itself trust. The repository template
is therefore a source for human-reviewed installation, not an active permission file.

During adoption:

- remove no generic `DENY`/`ASK` guard merely for convenience;
- add project-specific paths, tools, hosts, or exact commands only when required;
- keep destructive or authority-changing operations human-supervised;
- do not add project credentials, secrets, customer data, or local absolute paths;
- keep the permission template consistent with `AGENTS.md` and `#execution`.

The operational copy/install procedure belongs to the
[Development Operations Runbook](development-operations-runbook.md).

## Python/uv bootstrap adaptation points

`scripts/bootstrap-workspace` is generalized directly from the production bootstrap.
For a Python/uv adopting project, normally change only:

- `EXPECTED_PROJECT_NAME` — `[project].name` from `pyproject.toml`;
- `SOURCE_IMPORT_NAME` — import name of the project's source package;
- `SOURCE_PATH_RELATIVE` — repository-relative path that owns that import;
- `UV_SYNC_EXTRA` — optional uv extra used for the development environment;
- `REQUIRED_IMPORTS` — optional runtime imports that must succeed before READY.

The checked-in placeholder values intentionally fail closed.

The bootstrap-state fingerprint includes the SHA-256 of
`scripts/bootstrap-workspace` itself in addition to the worktree/runtime/dependency
inputs. Any adaptation or bootstrap-logic change therefore invalidates the prior READY
state.

If the adopting repository does not use Python/uv, replace the implementation with a
stack-equivalent readiness mechanism preserving the same isolation contract, or remove
the bootstrap script, hook, and corresponding lifecycle checkpoints together.

## Workspace bootstrap contract

The bootstrap is a readiness boundary, not merely an installer. Preserve these generic
properties:

- resolve the physical owning Git worktree at runtime;
- reject missing/inconsistent dependency lock state before mutation;
- reject shared mutable environments, including symlinked or mounted `.venv` paths;
- reject foreign/symlinked bootstrap lock metadata;
- verify configured project identity before mutation;
- verify runtime and imported project source belong to this worktree;
- fingerprint root, runtime, manifest, lockfile, and bootstrap configuration;
- strictly parse and atomically replace bootstrap state;
- serialize mutating bootstrap operations with an exclusive lock;
- hold a shared lock for the full non-mutating `--check`;
- fail closed when readiness metadata is absent, invalid, or stale;
- verify configured required imports before READY.

## Spec templates

Templates under `.kiro/specs/_templates/` preserve Kiro native workflow concepts while
adding repository governance. Do not remove sections merely to make the template
shorter.

When adapting them:

1. inspect the installed Kiro native artifact shape;
2. preserve native sections and task lifecycle;
3. retain repository workspace/traceability/invariant/matrix/delivery controls;
4. validate references and task-graph recognition where diagnostics exist;
5. run applicable Markdown/config checks using provisioned tools;
6. record unavailable diagnostics as unavailable rather than PASS.

Daily Spec execution belongs to `.kiro/specs/README.md` and the operations runbook.

## Final delivery contract

`scripts/finalize-spec` is generalized directly from the production reviewed-delivery
helper. Repository identity is derived from `origin`; the delivery state machine is
preserved rather than reimplemented as a simple archive command.

The generic contract includes:

- repository root and dedicated attached branch verification;
- fetch/push origin verification for the same GitHub repository;
- configured/executable Git hooks;
- rejection of in-progress merge/cherry-pick/revert/rebase operations;
- concrete independent PASS evidence on the owning PR;
- exact reviewed/mechanical tree-state validation;
- same-repository PR and expected base/head validation;
- regular-file/symlink containment checks for Spec/archive paths;
- unrelated-change rejection;
- resumable two-phase archive/Ready/completion publication.

If the Git host or delivery model differs, adapt the transport/interface boundary while
preserving these invariants.

## Validation baseline

The template includes `.markdownlint.json` as the shared Markdown baseline.

Shell/Python scripts should also receive syntax/static/runtime validation appropriate to
the adopting environment. Missing tools or unavailable diagnostics remain unverified;
they are not PASS.

## Native Kiro compatibility

These files augment Kiro rather than reimplement it. Permissions, Multi-root behavior,
Spec Task Execution, hooks, and diagnostics may change with Kiro releases.

Treat product behavior separately from repository-controlled invariants and revalidate
assumptions when the installed Kiro version changes.

## What remains project-specific

Keep these in the adopting repository rather than this generic template:

- product/domain requirements and terminology;
- customer-specific configuration;
- production-data and compliance details;
- product schemas and domain identities;
- business-specific scale assumptions;
- Issue-specific design decisions and execution history;
- project-specific dependency extras, import smoke tests, runtime versions, and
  permission exceptions.

The template owns development governance. The adopting repository owns product truth.
