---
inclusion: manual
description: Start Spec implementation tasks through Kiro native Spec Task Execution. Load with #spec-task-execution.
---

# Native Spec Task Execution

For Spec-driven implementation in Kiro IDE, start each `tasks.md` implementation task through Kiro's native Spec Task Execution UI (for example `Start Task`). A normal chat prompt must not infer, select, start, or resume an unchecked Spec task.

This preserves visible task state and the native `PreTaskExec` / `PostTaskExec` lifecycle. Supplemental chat context is allowed after the intended task is selected natively.

The native task remains the outer review/completion boundary; internal bounded execution slices and subagents are still allowed under `#execution-efficiency`.

If work was started outside the native path, report that limitation truthfully. Do not claim native task status or hook lifecycle was observed, and do not replay completed work merely to repair UI history unless explicitly requested.

Direct Change work is not governed by this rule.