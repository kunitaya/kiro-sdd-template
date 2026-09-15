---
inclusion: manual
description: Bounded execution slices, delegation, resumption, stall handling, and validation cadence. Load with #execution-efficiency.
---

# Execution Efficiency

A `tasks.md` task is a reviewable outcome, not necessarily one model invocation. Use visible child tasks for material independently verifiable outcomes; keep low-level mechanics internal.

Before delegation, the parent inspects relevant implementation/tests, resolves responsibility boundaries and sequence, identifies affected requirements/invariants, and decides whether delegation has concrete value. Do not make each subagent rediscover the repository.

Subagent prompts contain only the bounded objective, relevant files/discovery target, affected invariants, boundaries/non-goals, and focused validation. Do not paste the complete Issue/Spec/policy unless required.

After interruption, reconcile actual files/diff and durable progress records. Preserve valid completed work and rerun only missing/invalidated checks.

After a first stalled large invocation, reduce scope/context or move discovery/integration back to the parent. Do not repeatedly retry the same oversized prompt unchanged.

Validation scope follows execution level:

- slice/child: minimum focused evidence;
- parent task: interaction/integration risks, reusing valid child evidence;
- final Issue/Spec: repository-wide gates or full regression only where required.

Stop once acceptance criteria, required validation, and BLOCKING findings are resolved.