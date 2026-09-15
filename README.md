# kiro-sdd-template

English (authoritative) | [日本語](README.ja.md)

A reusable Kiro-based Spec-Driven Development environment generalized from a
production-style AI-assisted workflow. Product/domain truth remains in the adopting
repository; mature project-independent governance and safety controls remain here.

This is **not** a shortened rewrite of the source workflow.

## Start here

Use the document that owns the question you are trying to answer:

| Document | Purpose |
| --- | --- |
| `docs/setup.md` | One-time adoption and project-specific customization |
| `docs/development-operations-runbook.md` | Daily development workspace operations, English authoritative |
| `docs/development-operations-runbook.ja.md` | Daily development workspace operations, Japanese reference |
| `AGENTS.md` | Repository-wide AI development and safety policy |
| `.kiro/steering/` | Scoped execution, review, workspace, SDD, source, and test guidance |
| `.kiro/specs/README.md` | Spec directory and lifecycle conventions |

Keep those responsibilities separate. Prefer links to the owning document over copying
its detailed rules or procedures into another file.

## Included components

| Path | Purpose |
| --- | --- |
| `.kiro/specs/_templates/` | Native-compatible requirements, design, bugfix, and tasks templates |
| `.kiro/hooks/workspace-bootstrap-check.json` | `PreTaskExec` readiness diagnostic |
| `.githooks/` | Guards against direct commit/push to `main` |
| `scripts/bootstrap-workspace` | Deterministic Python/uv per-worktree bootstrap |
| `scripts/finalize-spec` / `scripts/finalize_spec.py` | Fail-closed reviewed Spec delivery |
| `templates/permissions.yaml` | Reviewed source template for Kiro workspace permissions |
| `templates/kiro-task-prompt.md` | Bounded task-prompt template |
| `.markdownlint.json` | Shared Markdown validation baseline |
| `src/`, `tests/`, `docs/` | Generic tracked repository skeleton |

## Operating model

For a new adopting repository, begin with
[Setup and Customization](docs/setup.md).

For normal Issue/worktree startup, Kiro workspace permissions, readiness checks,
validation, review handoff, finalization, and recovery, use the
[Development Operations Runbook](docs/development-operations-runbook.md).

The detailed SDD and review lifecycle is owned by `#sdd-workflow`, `#review`, and
`.kiro/specs/README.md`; this README intentionally does not duplicate it.

## Kiro permissions

`templates/permissions.yaml` is a reviewed **source template**, not an active trust file.
Kiro keeps workspace-scoped permissions outside the repository so a clone cannot grant
itself trust. Installation and verification are documented in the operations runbook;
project-specific permission adaptations belong in `docs/setup.md`.

## Language policy

English is authoritative for repository/GitHub artifacts.

Human-facing documents used routinely for setup or operations may have a Japanese
reference translation. The development operations runbook is intentionally maintained in
both English and Japanese and must be updated together.

AI-facing policy, steering, and Spec templates remain English unless the adopting
repository explicitly defines another authority model.

## Status

The reusable governance and SDD environment is included. Adopting repositories still
need explicit project customization and validation against their installed Kiro and
toolchain versions.

## Project status and affiliation

This is independently maintained and unofficial. It is not an official product of, or
endorsed by, Kiro, OpenAI, or their developers.

## License

[MIT License](LICENSE)
