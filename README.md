# kiro-sdd-template

English (authoritative) | [日本語](README.ja.md)

A reusable Kiro-based Spec-Driven Development environment generalized from a
production-style AI-assisted workflow. Product/domain truth remains in the adopting
repository; mature project-independent governance and safety controls remain here.

This is **not** a shortened rewrite of the source workflow.

## Documentation map

| Document | Purpose |
| --- | --- |
| `README.md` / `README.ja.md` | Overview and entry points |
| `docs/setup.md` | One-time adoption and project-specific customization |
| `docs/development-operations-runbook.md` | Daily development operations runbook, English authoritative |
| `docs/development-operations-runbook.ja.md` | Daily development operations runbook, Japanese reference |
| `AGENTS.md` | Repository-wide AI development and safety policy |
| `.kiro/steering/` | Scoped execution, review, workspace, SDD, source, and test guidance |
| `.kiro/specs/README.md` | Spec directory and lifecycle conventions |

Keep those responsibilities separate. Prefer stable links over duplicating detailed
policy or operating procedures across files.

## Included components

| Path | Purpose |
| --- | --- |
| `.kiro/specs/_templates/` | Native-compatible requirements, design, bugfix, and tasks templates |
| `.kiro/hooks/workspace-bootstrap-check.json` | `PreTaskExec` readiness diagnostic |
| `.githooks/` | Guards against direct commit/push to `main` |
| `scripts/bootstrap-workspace` | Deterministic Python/uv per-worktree bootstrap |
| `scripts/finalize-spec` / `scripts/finalize_spec.py` | Fail-closed reviewed Spec delivery |
| `templates/permissions.yaml` | Reviewed Kiro workspace-permissions source template |
| `templates/kiro-task-prompt.md` | Bounded task-prompt template |
| `.markdownlint.json` | Shared Markdown validation baseline |
| `src/`, `tests/`, `docs/` | Generic tracked repository skeleton |

## Core workflow

```text
Authoritative project requirements + GitHub Issue
    ↓
Choose Direct Change or Kiro Spec by semantic risk
    ↓
Requirements / Design / Bugfix -> tasks.md
    ↓
Dedicated branch/worktree + Draft PR
    ↓
Independent Spec Review
    ↓
Native Kiro Spec Task Execution
    ↓
Implementation + proportionate validation
    ↓
Independent Code / Requirements Review
    ↓
Reviewed mechanical Spec delivery + PR Ready
    ↓
Human merge gate
```

Detailed lifecycle rules live in `#sdd-workflow`, `#review`, and
`.kiro/specs/README.md`.

## Core principles

- higher-authority requirements are never rewritten to fit current code;
- one Issue normally owns one branch and one PR;
- Kiro native artifact/task lifecycle is preserved;
- worktrees are isolated by runtime root/branch/repository identity;
- workspace READY represents the current worktree/runtime/dependency/bootstrap state;
- validation uses already-provisioned tools rather than task-time package acquisition;
- automated review is supplemental evidence, not an authority;
- only BLOCKING findings create mandatory correction rounds;
- final delivery is fail-closed and merge remains a human/operator decision unless
  explicitly delegated.

## Kiro permissions

`templates/permissions.yaml` is a **source template**, not the active trust file.

Kiro 1.0 stores workspace-scoped permissions outside the repository:

```text
~/.kiro/workspace-roots/<hash>/permissions.yaml
```

This prevents a clone from granting itself trust. Install and review the active
workspace copy manually.

The template preserves generic safety rules and intentionally omits product-specific
paths, package/import names, fixed runtime versions, test-only environment variables,
and domain-specific documentation hosts.

See the
[Development Operations Runbook](docs/development-operations-runbook.md)
for daily installation/verification procedure and
[Setup and Customization](docs/setup.md)
for project-specific adaptation.

## Workspace readiness and delivery

The included bootstrap and finalizer are production-derived safety mechanisms.

Do not rewrite them as shorter approximations. Adapt only documented project/transport
boundaries and preserve their generic state machines.

- Bootstrap customization contract: [Setup and Customization](docs/setup.md)
- Daily READY procedure: [Development Operations Runbook](docs/development-operations-runbook.md)
- Spec delivery lifecycle: [.kiro/specs/README.md](.kiro/specs/README.md)

## Language policy

English is authoritative for repository/GitHub artifacts.

Human-facing documents that are used routinely for setup or operations may have a
Japanese reference translation. The daily operations runbook is intentionally maintained
in both English and Japanese and must be updated together.

AI-facing policy, steering, and Spec templates remain English unless the adopting
repository explicitly defines another authoritative language model.

## Status

The reusable governance and SDD environment is included. Adopting repositories still
need explicit project customization and validation against their installed Kiro and
toolchain versions.

## Project status and affiliation

This is independently maintained and unofficial. It is not an official product of, or
endorsed by, Kiro, OpenAI, or their developers.

## License

[MIT License](LICENSE)
