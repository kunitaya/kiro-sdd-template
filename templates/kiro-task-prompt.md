# Kiro Task Prompt Template

Use after the intended native Spec task is already selected in Kiro, or for a bounded non-Spec/Direct Change task.

```text
Before starting, read repository-root AGENTS.md and load the applicable steering references named below.

Task:
<task identity and phase>

Objective:
<1-3 lines describing the required outcome>

Relevant requirements / acceptance criteria:
- <IDs only; do not paste large source documents>

Required guidance:
- #execution
- <#sdd-workflow / #review / #workspace-isolation / #execution-efficiency / #spec-task-execution as applicable>

Acceptance criteria for this bounded work:
- <observable result>

Non-goals / boundaries:
- <explicit exclusions>

Execution:
Use the smallest change that satisfies the task. Inspect the directly relevant implementation and tests. Reuse existing responsibility/invariant owners. Do not broaden into adjacent Issues.

For Spec implementation, this prompt supplements a task already started through Kiro native Spec Task Execution. Do not infer, select, or start another unchecked tasks.md item.

Verification:
Run minimum sufficient focused checks for this bounded outcome. Reuse still-valid evidence; do not repeat repository-wide validation at each execution slice.

Stop condition:
Stop when the bounded outcome is verified and no BLOCKING issue remains, or when a material authority/design conflict or external dependency prevents truthful completion.

Final report:
State completed outcome, validation actually run, changed/published state, and remaining BLOCKING/unverified items.
```

Do not duplicate full Issue/Spec/steering text into the prompt. Another steering file may require a short
delegation-time constraint to be restated; preserve those explicit requirements.
