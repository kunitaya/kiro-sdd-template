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
5. Decide whether the included Python/uv bootstrap applies. If not, replace the
   implementation while preserving the same safety properties, or remove the script,
   hook, and lifecycle checkpoints together.
6. Configure repository Git hooks with `git config core.hooksPath .githooks` when using
   the included safety guards.
7. Validate Kiro's installed native Spec structure, Task Execution, hook behavior, and
   diagnostics. Reconcile the templates to the installed version when Kiro changes.
8. Decide which automated reviewer, if any, supplements Independent Review. Quota or
   availability failures are recorded truthfully and never converted into PASS.
9. Review `scripts/finalize_spec.py` assumptions. The included helper targets
   `github.com`, `main` as the base branch, `gh` CLI, and this repository's two Git hook
   names. Adapt these interfaces without weakening the fail-closed review/delivery
   invariants if your environment differs.

## Workspace bootstrap contract

The included Python/uv implementation is not merely a convenience installer. It is a
readiness boundary. Its generic properties are:

- resolve the physical owning Git worktree at runtime;
- reject missing/inconsistent dependency lock state before mutation;
- reject shared mutable environments (symlink / separate mount);
- verify that the runtime belongs to this worktree;
- fingerprint the owning root, runtime version, project manifest, and lockfile;
- serialize mutating bootstrap operations;
- make `--check` non-mutating and fail closed when state is stale;
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

`scripts/finalize-spec` is a reviewed-state transition, not a general file mover.
Before it may alter the repository it verifies:

- repository root and dedicated attached branch;
- configured/executable Git hooks;
- clean working tree/index;
- HEAD exactly equals the supplied independently reviewed full SHA;
- concrete independent PASS URL belongs to the owning PR;
- owning PR is open, Draft, targets `main`, and points at the reviewed SHA;
- required Spec artifacts exist as regular files;
- all task/review checkpoints except the final review/finalization markers are done;
- no archive destination already exists.

The helper then makes only the mechanical post-review changes, commits/pushes them, and
transitions the same PR from Draft to Ready. It never merges and never self-approves.

If your Git host or delivery model differs, adapt the transport/interface while keeping
these invariants or document an explicit replacement with equivalent safety.

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
