# Setup and Customization

English (authoritative) | [日本語](setup.ja.md)

This document covers **adoption-time customization** of the template. It does not own
daily development operation.

For clone/worktree startup, permissions installation, Issue start/resume, validation,
review, finalization, and recovery, use the
[Development Operations Runbook](development-operations-runbook.md).

## Adoption principle

Generalize or adapt only what is truly project- or stack-specific. Preserve mature,
project-independent lifecycle, safety, review, isolation, and validation controls.

Do not rewrite an existing safety mechanism as a shorter approximation merely because
the adopting project differs from the source project.

## Required project decisions

Before routine development, an adopting repository must decide and record:

1. authoritative requirements and the repository authority model;
2. project-specific security, sensitive-data, compliance, and invariant rules;
3. source/test layout and applicable steering file-match patterns;
4. validation commands and how required tools are provisioned;
5. project-specific bootstrap settings or an approved replacement readiness mechanism;
6. project-specific permission additions to `templates/permissions.yaml`;
7. Git hook usage (`core.hooksPath=.githooks` when the included hooks are retained);
8. installed Kiro behavior for native Specs, Task Execution, hooks, diagnostics, and
   permissions;
9. optional automated-review integration;
10. any transport differences from the included GitHub/`gh` finalizer assumptions.

## Repository skeleton

The template keeps common development directories present from the first commit:

```text
src/
tests/
docs/
docs/spec-archive/
```

A `.gitkeep` preserves an otherwise-empty directory. Remove it after real tracked
content exists. Keep `docs/spec-archive/` when using the included Spec finalizer.

## Kiro permissions adaptation

The reviewed source template is:

```text
templates/permissions.yaml
```

The active workspace-scoped permission file is stored outside the repository under the
Kiro workspace trust directory. The operations runbook owns the installation procedure.

During adoption:

- retain generic secret/trust/destructive-operation guards unless an explicit reviewed
  replacement provides equivalent protection;
- add project-specific paths, tools, exact commands, or documentation hosts only when
  required;
- keep destructive or authority-changing operations `ASK` or `DENY` unless there is a
  documented reason to do otherwise;
- do not add credentials, customer data, local absolute paths, or machine-specific
  hashes to the repository template;
- keep permissions consistent with `AGENTS.md` and `#execution`;
- use provisioned lint tools directly; do not add package-acquisition runners merely to
  execute lint.

The template intentionally omits product-specific input/output semantics, package/import
names, fixed runtime versions, test-only environment variables, and domain-only hosts.

## Python/uv bootstrap adaptation

For a Python/uv project using the included bootstrap, normally change only the explicit
adaptation constants near the top of `scripts/bootstrap-workspace`:

- `EXPECTED_PROJECT_NAME` — `[project].name` from `pyproject.toml`;
- `SOURCE_IMPORT_NAME` — import name of the project's source package;
- `SOURCE_PATH_RELATIVE` — repository-relative path that owns that import;
- `UV_SYNC_EXTRA` — optional uv extra used for the development environment;
- `REQUIRED_IMPORTS` — optional imports that must succeed before READY.

The checked-in placeholders intentionally fail closed. The bootstrap fingerprints its
own script/configuration, so changing these settings invalidates the previous READY
state.

The generic readiness and isolation contract is owned by `#execution` and the bootstrap
implementation itself; do not duplicate or weaken that state machine here.

If the project does not use Python/uv, replace the implementation with a stack-equivalent
readiness mechanism or remove the bootstrap script, readiness hook, and corresponding
lifecycle checkpoints together.

## Spec and steering adaptation

Templates under `.kiro/specs/_templates/` preserve Kiro native workflow concepts while
adding repository governance. Adapt product/domain content and repository-specific
traceability, but do not remove native or safety sections merely to shorten the files.

Adapt `.kiro/steering/source-development.md` and `test-development.md` to the actual
source/test layout. Keep other steering changes limited to genuine environment or policy
differences.

Daily Spec execution is owned by `.kiro/specs/README.md` and the operations runbook.

## Finalizer adaptation

`scripts/finalize-spec` / `scripts/finalize_spec.py` assume GitHub, `main` as the base
branch, the `gh` CLI, and the included repository hooks.

If the Git host or delivery model differs, adapt the transport/interface boundary while
preserving the reviewed mechanical-delivery state machine. Detailed delivery behavior is
owned by `#execution`, `.kiro/specs/README.md`, and the implementation; do not duplicate
it here.

## Validation and Kiro compatibility

The template includes `.markdownlint.json` as a shared Markdown baseline. Define the
adopting repository's actual source/test/static-analysis commands and provision those
tools during environment setup.

Kiro product behavior can evolve independently of repository policy. Revalidate native
Spec behavior, permissions, hooks, diagnostics, and Multi-root behavior against the
installed Kiro version when those surfaces change.

Unavailable tools or diagnostics are recorded as unverified, never as PASS.

## What remains project-specific

Keep these in the adopting repository rather than in the generic template:

- product/domain requirements and terminology;
- customer-specific configuration and sensitive-data rules;
- production-data handling and compliance details;
- product schemas and domain identities;
- Issue-specific design decisions and execution history;
- dependency extras, import smoke tests, runtime versions, and permission exceptions
  that are required only by that project.

The template owns reusable development governance. The adopting repository owns product
truth.
