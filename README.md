# kiro-sdd-template

English (authoritative) | [日本語](README.ja.md)

A reusable Kiro-based Spec-Driven Development environment extracted from a production-style AI-assisted workflow and generalized so product/domain-specific rules remain in the adopting repository.

It includes repository-wide agent policy, scoped steering, native-compatible Spec templates, worktree isolation, task-execution rules, bootstrap/readiness integration, Git safety hooks, bounded delegation guidance, independent review rules, and delivery mechanics.

## Included components

| Path | Purpose |
| --- | --- |
| `AGENTS.md` | Repository-wide authority, scope, safety, verification, review, and SDD policy |
| `.kiro/steering/` | Scoped SDD, execution, review, documentation, testing, source, workspace, and task guidance |
| `.kiro/specs/_templates/` | Requirements, design, bugfix, and tasks templates augmenting Kiro native artifacts |
| `.kiro/hooks/workspace-bootstrap-check.json` | `PreTaskExec` readiness diagnostic hook |
| `.githooks/` | Guards against direct commit/push to `main` |
| `scripts/bootstrap-workspace` | Generic Python/uv per-worktree bootstrap example with non-mutating `--check` |
| `scripts/finalize-spec` | Minimal mechanical Spec archive helper |
| `templates/kiro-task-prompt.md` | Bounded task-prompt template |
| `docs/setup.md` | Adoption and customization guide |

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
Independent Spec Review
    ↓
Native Kiro Spec Task Execution
    ↓
Implementation + proportionate validation
    ↓
Independent Code / Requirements Review
    ↓
Archive Spec -> Draft PR Ready
    ↓
Human merge gate
```

Key principles:

- higher-authority requirements are not rewritten to fit current code;
- one Issue normally owns one branch and one PR;
- task prompts carry task-specific facts, not duplicated repository policy;
- native Spec Task Execution is preserved for implementation tasks;
- worktrees are isolated at runtime by root/branch/repository identity;
- verification is risk-based and reusable instead of repeated mechanically;
- automated review is supplemental evidence, not an authority;
- only BLOCKING findings create mandatory correction rounds;
- merge remains a human/operator decision unless explicitly delegated.

## Workspace and bootstrap model

The template treats each Git worktree as its own mutable development environment. The included bootstrap script is deliberately an example for Python/uv repositories; projects using another stack should replace it while retaining the useful contract:

```bash
./scripts/bootstrap-workspace          # initialize/repair
./scripts/bootstrap-workspace --check  # non-mutating readiness check
```

The Kiro `PreTaskExec` hook surfaces the check result. Do not assume the hook itself blocks task start unless verified for the installed Kiro version; the workspace owner remains responsible for confirming READY before native task execution.

For lint, use provisioned tools directly. Do not use package-acquisition runners such as `npx`/`npm exec`/`pnpm dlx`/`yarn dlx` merely to execute lint.

## Adoption

Read [Setup and Customization](docs/setup.md). In particular, replace domain/product requirements, project validation commands, security rules, source/test paths, environment bootstrap details, and any automated reviewer integration. Keep project-specific business semantics out of this template.

Configure included Git hooks after cloning/creating a worktree:

```bash
git config core.hooksPath .githooks
```

## Language policy

English is authoritative for repository/GitHub artifacts. `README.ja.md` is a reference translation and must be updated with this README when its meaning changes. Operator-facing interactive communication may use the operator's preferred language.

## Status

The reusable governance and SDD environment is now included. Adopting repositories still require explicit project customization; this repository is a template, not a universal product configuration.

## Project status and affiliation

This is independently maintained and unofficial. It is not an official product of, or endorsed by, Kiro, OpenAI, or their developers.

## License

[MIT License](LICENSE)
