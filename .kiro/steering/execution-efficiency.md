---
inclusion: manual
description: Bounded execution slices, delegation, durable progress, stall/retry policy, and validation cadence. Load with #execution-efficiency.
---

# Execution Efficiency

A `tasks.md` task is a reviewable outcome, not necessarily one model invocation. Use visible child tasks for material independently verifiable outcomes; keep low-level mechanics internal.

## Task versus execution slice

Use child tasks when a parent task contains bounded outcomes whose completion is independently useful for review or resumption. Smaller mechanics remain internal execution slices. Do not create a checkbox per file, command, or tool call.

If execution reveals that a task still hides several material outcomes, make that decomposition visible in `tasks.md` before continuing. Preserve approved scope, dependencies, and validation; material design changes use the existing review process.

## Parallel execution decisions

Assess dependencies, overlapping edits, and shared mutable resources before parallel execution. Do not invent serial dependencies between independent outcomes, but do not run work concurrently when ownership or isolation is ambiguous.

Record material parallel candidates and serialization constraints in the plan. Parallel capability does not require spawning agents when coordination cost outweighs the benefit.

## Durable progress and resumption

`tasks.md` owns durable task progress. After a material child completes, record its verified result, evidence, and remaining integration work concisely.

After interruption or restart:

1. confirm the owning workspace/branch and current authorization;
2. inspect actual files, diff/status, and recorded evidence;
3. reconcile completed, partial, and unstarted work;
4. preserve still-valid completed work and rerun only invalidated or missing checks;
5. correct stale progress records before resuming the next bounded action.

A checkbox or previous agent summary is not proof that the actual working state is complete. Do not replay all children merely because the parent remains unchecked.

## Parent-agent responsibility

Before delegating non-trivial work, the parent agent owns the repository-level understanding step:

- inspect the relevant implementation and tests;
- resolve responsibility boundaries and sequence;
- identify the files/functions actually relevant to each slice;
- identify only the requirements/invariants that the slice can materially affect;
- decide whether delegation has concrete value over direct parent execution;
- integrate completed slices and decide when the owning `tasks.md` task is complete.

Do not make each subagent rediscover repository architecture, Issue history, Spec interpretation, and implementation planning that the parent has already resolved.

Delegation is optional. If the parent already has sufficient context and the remaining edit is small and bounded, direct execution is preferable to unnecessary delegation overhead.

## Bounded subagent prompts

Subagent prompts contain only the bounded objective, relevant files/discovery target, affected requirements/invariants, explicit boundaries/non-goals, focused validation scope, and stop condition. Follow `#task-prompt`.

Do not paste the complete Issue, Spec, policy corpus, or repository history unless required for the slice. Preserve any short delegation-time constraint another steering file explicitly requires.

A subagent must not broaden its slice into the remainder of the parent task. Report newly discovered wider dependencies to the parent for replanning.

## Stall and retry policy

After the first stalled, timed-out, or infrastructure-aborted large invocation:

1. preserve any work/evidence already produced;
2. inspect whether delegated scope or supplied context was unnecessarily large;
3. reduce the execution slice and/or prompt context before retrying when practical;
4. move discovery/integration back to the parent when the original prompt mixed discovery, design, implementation, and validation.

Do not repeatedly retry the same oversized prompt unchanged. One unchanged retry is acceptable only when the invocation is already small and bounded and there is concrete reason to treat the failure as transient.

When a slice genuinely requires an expensive long-running check, first publish the already-focused-validated implementation state through the repository's normal commit/push rules when that publication is authorized. This prevents an execution-limit abort during the expensive check from discarding completed verified work. Do not publish partially verified or unsafe state merely to checkpoint it.

## Validation cadence

Validation scope follows execution level:

- **child / execution slice** — minimum focused evidence for the changed result and directly affected contracts;
- **parent task** — interaction/integration risks, reusing still-valid child evidence;
- **final Issue / Spec** — repository-wide gates or full regression only where required by scope, risk, or project policy.

Child completion alone never triggers a full regression suite. A parent delegation prompt must not request a full repository suite for a child/slice unless it states the concrete risk that focused checks cannot establish.

Reuse evidence while its tested boundary, relevant code, dependencies, and environment remain unchanged. Rerun only missing or invalidated checks, or an explicitly required gate. Do not describe an older check as executed at a newer revision; record the reused revision/evidence truthfully.

A finished implementation may require a full regression suite without requiring every intermediate slice to run that suite.

## Context reuse

Parent analysis is reusable work. Once a relevant fact has been established, do not ask multiple subagents to independently re-derive it unless independent verification is itself required.

Prefer:

```text
parent: inspect / understand / plan once
    ↓
subagent: bounded implementation slice
    ↓
parent: integrate
    ↓
next bounded slice
```

rather than repeated repository rediscovery by each subagent.

## Completion boundary

Completion of an execution slice does not mark the `tasks.md` task complete. The parent completes the task only after required children are verified and integrated, traced acceptance criteria/invariants are satisfied, task-level validation is complete, and no BLOCKING issue remains.

Stop once those conditions are met. Do not keep spawning agents, broadening validation, or adding cleanup merely because more certainty or polish is possible.