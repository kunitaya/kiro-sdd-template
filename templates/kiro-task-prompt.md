# Kiro Task Prompt Template

Use after the intended native Spec task is already selected in Kiro, or for a bounded non-Spec/Direct Change task.

```text
Before starting, read repository-root AGENTS.md and load the applicable steering references named below. Confirm that each required guidance item was loaded; do not restate or summarize its contents merely to prove loading.

Task:
<task identity and phase>

Objective:
<1-3 lines describing the required outcome>

Relevant requirements / acceptance criteria:
- <IDs only; do not paste large source documents>

Acceptance criteria for this bounded work:
- <observable result>

Validation scope:
- <focused tests / lint / type checks / narrow probes for this bounded outcome>
- <state any intentionally reused still-valid evidence>

Required guidance:
- #execution
- #task-prompt
- <#sdd-workflow / #review / #workspace-isolation / #execution-efficiency / #spec-task-execution as applicable>

Non-goals / boundaries:
- <explicit exclusions>

Execution:
Use the smallest change that satisfies the task. Inspect the directly relevant implementation and tests. Reuse existing responsibility/invariant owners. Start with targeted lookup and expand only for a concrete dependency, adjacent invariant, or review finding. Do not broaden into adjacent Issues.

For Spec implementation, this prompt supplements a task already started through Kiro native Spec Task Execution. Do not infer, select, or start another unchecked tasks.md item.

Verification:
Run only the minimum sufficient checks declared above for this bounded outcome. Reuse still-valid evidence; do not repeat repository-wide validation at each execution slice. If broader validation is genuinely required, state the concrete risk that focused checks cannot establish.

Stop condition:
Stop when the bounded outcome is verified and no BLOCKING issue remains, or when a material authority/design conflict or external dependency prevents truthful completion.

Final report:
State completed outcome, validation actually run or reused, changed/published state, and remaining BLOCKING/unverified items.
```

Do not duplicate full Issue/Spec/steering text into the prompt. Another steering file may require a short delegation-time constraint to be restated; preserve those explicit requirements.
