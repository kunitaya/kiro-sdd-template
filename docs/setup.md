# Setup and Customization

This template is a reusable starting point, not a zero-configuration framework. Adopt it by copying the policy/workflow files into a target repository and then explicitly replacing project-specific integration points.

## Required project decisions

1. Define the authoritative requirements/domain specification and update `AGENTS.md` authority precedence if needed.
2. Define language exceptions, security/sensitive-data rules, and project-specific invariants.
3. Adapt `.kiro/steering/source-development.md` and `test-development.md` file-match patterns to the repository layout.
4. Adapt validation commands/toolchain and ensure required tools are provisioned outside task-time lint execution.
5. Decide whether Python/uv bootstrap applies. If not, replace `scripts/bootstrap-workspace` while preserving a stable mutating form plus non-mutating `--check` contract, or remove the bootstrap hook/checkpoints together.
6. Configure Git hooks with `git config core.hooksPath .githooks` if adopting the included guards.
7. Review Kiro hook behavior on the installed IDE version. Do not assume `PreTaskExec` command hooks block execution unless verified.
8. Decide which automated reviewer, if any, supplements Independent Review.
9. Decide whether `scripts/finalize-spec` is sufficient or whether the project needs a richer validated delivery helper.

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
create/copy Spec artifacts
    ↓
validate + publish Spec to Draft PR
    ↓
Independent Spec Review
    ↓
start native Kiro tasks
```

Never share `.venv` or other mutable project environments between worktrees through symlinks. For another stack, apply the same ownership principle to its generated environment/cache where mutation could cross task boundaries.

## Native Kiro compatibility

The templates augment Kiro's native artifact concepts rather than replacing them. When Kiro changes native Spec structure, task execution, hooks, or diagnostics, inspect the installed behavior and reconcile the template instead of freezing assumptions indefinitely.

## What should remain project-specific

Do not move domain requirements, customer-specific configuration, production data rules, product schemas, business terminology, or Issue-specific decisions into this reusable template. The template owns development governance; the adopting repository owns product truth.