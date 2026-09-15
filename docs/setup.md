# Setup and Customization

This repository is a reusable development-governance template, not a zero-configuration
framework. Adopt it by preserving the generic safety/process contracts and replacing
only the integration points that are genuinely project- or stack-specific.

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

1. Define the authoritative requirements/domain specification and adapt the authority
   precedence in `AGENTS.md` only when the target repository has a different legitimate
   authority model.
2. Define project-specific security, sensitive-data, compliance, and invariant rules.
3. Adapt `.kiro/steering/source-development.md` and `test-development.md` file-match
   patterns to the repository layout.
4. Define the actual validation commands/toolchain and ensure required tools are
   provisioned outside task-time lint execution.
5. Adapt the project-specific constants at the top of `scripts/bootstrap-workspace`.
   Do not rewrite its generic state machine merely to make it shorter.
6. Configure repository Git hooks with `git config core.hooksPath .githooks` when using
   the included safety guards.
7. Validate Kiro's installed native Spec structure, Task Execution, hook behavior, and
   diagnostics. Reconcile the templates to the installed version when Kiro changes.
8. Decide which automated reviewer, if any, supplements Independent Review. Quota or
   availability failures are recorded truthfully and never converted into PASS.
9. Review `scripts/finalize_spec.py` assumptions. The included helper targets
   `github.com`, `main` as the base branch, `gh` CLI, and this repository's two Git hook
   names. Adapt those interfaces without weakening the reviewed-delivery state machine.

## Repository skeleton

The template keeps common top-level development directories present from the first
commit, even before a project has populated them:

```text
src/
tests/
docs/
docs/spec-archive/
```

Each currently contains a `.gitkeep` where needed so Git preserves the directory.
Adopting projects may remove a `.gitkeep` once real tracked content exists in that
folder. Keep `docs/spec-archive/` available for finalized Spec delivery.

## Python/uv bootstrap adaptation points

`scripts/bootstrap-workspace` is generalized directly from the production bootstrap.
The safety flow is intentionally retained. For a Python/uv adopting project, normally
change only the constants near the top of the script:

- `EXPECTED_PROJECT_NAME` — `[project].name` from `pyproject.toml`;
- `SOURCE_IMPORT_NAME` — import name of the project's source package;
- `SOURCE_PATH_RELATIVE` — repository-relative path that owns that import;
- `UV_SYNC_EXTRA` — optional uv extra used for the development environment;
- `REQUIRED_IMPORTS` — optional runtime imports that must succeed before READY.

The checked-in placeholder values intentionally fail closed. Configure them before
using the bootstrap or its Kiro `PreTaskExec` readiness hook.

If the adopting repository does not use Python/uv, replace the implementation with a
stack-equivalent bootstrap while preserving the same readiness and isolation contract,
or remove the script, hook, and corresponding lifecycle checkpoints together.

## Workspace bootstrap contract

The included implementation is not merely a convenience installer. It is a readiness
boundary. Its generic properties are:

- resolve the physical owning Git worktree at runtime;
- reject missing/inconsistent dependency lock state before mutation;
- reject shared mutable environments, including symlinked or mounted `.venv` paths;
- reject foreign/symlinked bootstrap lock metadata;
- verify the configured project identity before mutation;
- verify that the runtime and imported project source belong to this worktree;
- fingerprint the owning root, runtime version, project manifest, and lockfile;
- strictly parse and atomically replace bootstrap state;
- serialize mutating bootstrap operations with an exclusive lock;
- hold a shared lock for the full non-mutating `--check` verification;
- make `--check` fail closed when metadata is absent, invalid, or stale;
- verify the configured required imports before reporting READY;
- never claim READY merely because an interpreter exists.

For another stack, translate those properties to the equivalent environment manager and
identity markers. Do not retain the Kiro readiness hook while replacing `--check` with a
weak existence test.

## New worktree workflow

```text
create dedicated branch/worktree
    ↓
open that worktree as the project root
    ↓
configure repository hooks
    ↓
run ./scripts/bootstrap-workspace        (when applicable)
    ↓
run ./scripts/bootstrap-workspace --check
    ↓
create/copy native-compatible Spec artifacts
    ↓
validate + publish Spec to Draft PR
    ↓
Independent Spec Review
    ↓
start native Kiro implementation tasks
```

Never share mutable project environments between worktrees through symlinks or mounts.
For non-Python stacks, apply the same ownership principle to generated environments or
caches when cross-worktree mutation would break isolation.

## Spec templates

The templates under `.kiro/specs/_templates/` intentionally preserve substantial
native sections. Do not delete a section solely to make the template shorter. Remove or
parameterize only content that is actually tied to one product/domain.

When modifying templates:

1. inspect the installed Kiro native artifact shape;
2. preserve the native sections and task lifecycle;
3. keep repository-added workspace/traceability/invariant/matrix/delivery sections;
4. validate native references and task graph recognition where diagnostics exist;
5. run the repository Markdown/config checks using provisioned tools;
6. record unavailable diagnostics as unavailable rather than PASS.

## Final delivery contract

`scripts/finalize-spec` is generalized directly from the production reviewed-delivery
helper. Repository identity is derived from `origin`; the delivery state machine is
preserved rather than reimplemented as a simpler archive command.

Before it may alter the repository it verifies, among other things:

- repository root and dedicated attached branch;
- fetch and push origin URLs identify the same owning GitHub repository;
- configured/executable Git hooks;
- no in-progress merge, cherry-pick, revert, or rebase operation;
- concrete independent PASS URL belongs to the owning PR;
- reviewed commit is an ancestor of the current exact allowed delivery state;
- owning PR is the same-repository PR for the current branch targeting `main`;
- remote PR state belongs to one of the explicitly allowed mechanical states;
- required Spec artifacts exist as ordinary tracked blobs;
- Spec/archive paths contain no symlink escape or unexpected file type;
- no unrelated local change exists;
- only recognized reviewed/archive/completion trees may be staged and published.

Delivery is deliberately two-phase. It archives and publishes the reviewed Spec first,
then changes the Draft PR to Ready, confirms that transition, records final completion,
and publishes the completion record. Partial mechanical states are recognized so a
safe retry can continue without pretending an interrupted delivery fully completed.
Merge remains manual.

If your Git host or delivery model differs, adapt only the transport/interface boundary
while keeping these invariants or document an explicit replacement with equivalent
safety.

## Validation baseline

The template includes `.markdownlint.json` as a reusable baseline derived from the
source workflow. Adopting projects may extend it, but should not disable checks merely
to hide template-format defects.

Shell/Python scripts should also receive syntax/static/runtime validation appropriate to
the target environment before the template is declared production-ready. If that
validation cannot run in the current environment, report it as pending; do not claim
PASS.

## Native Kiro compatibility

These files augment Kiro rather than reimplement it. Multi-root behavior, Spec task
execution concurrency, hook semantics, and diagnostics may evolve with Kiro releases.
Treat documented/observed product behavior separately from repository-controlled
invariants and revalidate assumptions when the installed version changes.

## What remains project-specific

Keep the following in the adopting repository, not this generic template:

- product/domain requirements and terminology;
- customer-specific configuration;
- production-data and compliance details;
- product schemas and domain identities;
- business-specific scale assumptions;
- Issue-specific design decisions and execution history;
- one project's requirement IDs or forensic/application semantics.

The template owns development governance. The adopting repository owns product truth.
