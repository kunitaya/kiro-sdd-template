# kiro-sdd-template

English (authoritative) | [日本語](README.ja.md)

A template for Kiro-based spec-driven development, with shared agent instructions, scoped steering, and implementation and review workflows.

This project is intended for individual developers and teams who want to reuse a requirements-driven development process across repositories.

> **Status: Under construction.** The repository currently contains this README, its Japanese reference translation, and `LICENSE`. Agent instructions, steering, Spec templates, and setup instructions are planned. It is not yet a ready-to-use development environment.

## Purpose

Make the relationship between requirements, change scope, design, implementation, verification, and review explicit. Provide reusable guidance that projects can adapt to their own requirements, technology stack, and development environment.

## Workflow principles to preserve

The planned template will preserve these principles when the reusable rules are introduced:

- **Requirements remain authoritative.** A change Issue defines scope and acceptance criteria within the project's authoritative requirements. Specs, implementation, and tests must not silently redefine those requirements.
- **Separate policy from execution guidance.** `AGENTS.md` defines shared repository rules. Scoped steering supplies operational detail. Task prompts focus on the assignment instead of duplicating repository-wide policy.
- **Choose the change route by semantic risk.** Substantive design and implementation work uses a Spec. A Direct Change route is reserved for corrections whose method is already fully determined and that introduce no new design or contract decisions; it still requires verification and independent implementation review. Small diff size alone does not justify skipping a Spec.
- **Keep Spec and implementation review distinct.** Independent Spec Review checks whether implementation can proceed without guessing about material behavior. Independent Code / Requirements Review checks the resulting implementation against the requirements and relevant invariants.
- **Preserve Kiro's native task lifecycle.** Spec implementation tasks are started through Kiro's Spec Task Execution interface. Supplementary chat prompts do not select or start incomplete tasks.
- **Use proportionate verification and conclusive reviews.** Gather sufficient evidence for the affected requirements and risks. Blocking findings require correction; optional improvements alone do not justify another correction round.
- **Treat automated review as supporting evidence.** Automated suggestions must be assessed against the task and its requirements. They do not replace independent review or authorize a merge.
- **Deliver through dedicated branches and pull requests.** Keep a change's Spec and implementation in the same Draft PR where applicable. Stop at the appropriate independent-review handoff. Complete required reviews and Spec archival before marking a Spec-driven PR ready; merge remains a human decision unless explicitly delegated.
- **Describe current rules directly.** Reusable documentation explains the current intended process and its rationale. Issue-specific execution history and verification evidence remain in their appropriate records.

The detailed route criteria, review gates, and execution procedures will be provided by the planned agent instructions and steering. This overview does not claim that those files or controls have already been installed.

## Language policy

English is the default language for repository and GitHub artifacts, including:

- this README, `AGENTS.md`, steering, Specs, and technical documentation;
- code comments, docstrings, test names, and technical identifiers;
- commit messages, Issue and PR titles and bodies, comments, and review records.

Interactive reports to the human operator may use the operator's preferred language. For this repository's maintenance workflow, those reports are in Japanese. Reports persisted in the repository or on GitHub remain in English.

`README.ja.md` is an explicitly permitted reference translation of this README. The English version remains authoritative; the Japanese version must not independently redefine rules. Update both files in the same change whenever README content changes, keeping their meaning synchronized. This exception does not extend to `AGENTS.md`, steering, Specs, or reports persisted on GitHub.

## Planned contents

The following components are not yet included. Their paths and setup instructions will be documented as they are added.

| Component | Purpose |
| --- | --- |
| `AGENTS.md` | Authority, scope, language, repository safety, and review policy |
| `.kiro/steering/` | Scoped workflow, execution, workspace isolation, documentation, and review guidance |
| Spec templates | Requirements, design, and task artifacts appropriate to the selected workflow |
| Task prompt templates | Task-specific objectives, constraints, verification, and handoff conditions |
| Review templates | Independent Spec Review and Independent Code / Requirements Review |
| Setup and customization guide | Project adaptation and configuration of repository and environment controls |

## Adoption and contributions

Setup and compatibility guidance will be added after the template components are available and verified. Projects adopting the template will need to define their authoritative requirements, acceptance criteria, validation commands, and environment-specific controls.

Use [Issues](https://github.com/kunitaya/kiro-sdd-template/issues) for suggestions and defects. Keep contributions focused, write repository and GitHub content in English, and submit changes through a dedicated branch and pull request. Changes to the Japanese README follow the reference-translation policy above.

## Project status and affiliation

This is an independently maintained, unofficial template. It is not an official product of, or endorsed by, the developers of Kiro or OpenAI.

## License

[MIT License](LICENSE)
