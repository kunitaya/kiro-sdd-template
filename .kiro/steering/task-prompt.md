---
inclusion: manual
description: Standard bounded task-prompt contract and targeted lookup policy. Load with #task-prompt.
---

# Standard Task-Prompt Contract

A bounded task prompt normally contains only:

1. task identity / lifecycle phase;
2. objective;
3. relevant requirement or acceptance-criterion IDs;
4. bounded acceptance criteria;
5. required steering references by name;
6. non-goals / explicit boundaries;
7. stop condition.

Do not duplicate large repository policy. Name the owning guidance (`#execution`, `#review`, etc.) and include only task-specific facts. Preserve any delegation-time sentence another steering file explicitly requires.

## Targeted lookup

Start with the named requirements, traceability rows, design surfaces, code, and tests directly relevant to the task. Expand only when a concrete dependency, adjacent invariant, or review finding establishes a reason. Re-narrow after resolving it.

This never reduces the required scope of an Independent Review; review guidance defines that task's relevant surface.

Prefer deterministic checks and durable task evidence over repeated chat refinement when they answer the same question.