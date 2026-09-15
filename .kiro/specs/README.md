# Kiro Specs

`.kiro/specs/` contains active derived Specs. They never override authoritative requirements, Issue acceptance criteria, or `AGENTS.md`.

## Layout

```text
.kiro/specs/
  README.md
  _templates/
    requirements.md
    design.md
    bugfix.md
    bugfix-design.md
    tasks.md
  <issue-number>-<slug>/
    <workflow artifacts>
```

Copy templates; do not edit them in place for one Issue. Preserve Kiro's native artifact structure and add the governance/matrix sections supplied here.

Each Spec first artifact declares logical workspace identity (repository, Issue, branch, allowed scope), never an absolute filesystem path. Use `.kiro/steering/workspace-isolation.md` for runtime verification.

Active Specs remain here until Independent Code / Requirements Review and required fixes are complete. Then archive to `docs/spec-archive/<issue-number>-<slug>/` before the PR becomes Ready.

Choose Requirements-First, Design-First, Quick Spec, or Bugfix under `#sdd-workflow`. Validate artifact format/references and applicable Markdown/config checks before publication. Start implementation only after Independent Spec Review authorizes it. Start each implementation task through Kiro native Spec Task Execution.

Routine delivery checkpoints live in `tasks.md`, not duplicated across artifacts.