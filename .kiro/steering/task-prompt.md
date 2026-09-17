---
inclusion: manual
description: Standard bounded task-prompt contract, validation-scope field, guidance-load preflight, and targeted lookup policy. Load with #task-prompt.
---

# Standard Task-Prompt Contract

A bounded task prompt normally contains only:

1. task identity / lifecycle phase;
2. objective;
3. relevant requirement or acceptance-criterion IDs;
4. bounded acceptance criteria;
5. validation scope for this bounded work;
6. required steering references by name;
7. non-goals / explicit boundaries;
8. stop condition.

Task-specific facts remain in the prompt. Repository-wide policy does not. Name the owning guidance (`#execution`, `#review`, `#execution-efficiency`, etc.) instead of pasting its normative body. Preserve any short delegation-time sentence another steering file explicitly requires.

## Validation scope is explicit

State the focused validation this bounded work is expected to run: affected tests, paths, lint/type checks, or a narrow executable probe. Do not phrase a child/slice prompt as requiring repository-wide regression unless `#execution-efficiency` identifies the concrete risk that focused checks cannot establish.

This field prevents validation scope from expanding accidentally just because a parent task eventually has a broader final gate.

## Required-guidance preflight

Before proceeding past prompt setup, confirm that every guidance name listed as required was actually loaded. An unavailable automatic/file-match load falls back to the repository's supported manual load mechanism.

Confirm only that the guidance was loaded. Do not ask the executing agent to restate, quote, or summarize the guidance merely to prove it read the file; that recreates the policy-copy overhead this contract is intended to avoid.

If required guidance cannot be loaded or resolved, report the gap and stop rather than proceeding as if it had been applied.

## Targeted lookup

Start with the named requirements, traceability rows, design surfaces, code, and tests directly relevant to the task. Do not preload large reference documents in full merely because the task could theoretically touch them.

Expand beyond the targeted lookup only when a concrete trigger appears:

- a dependency from the targeted material must also be satisfied;
- an adjacent invariant is plausibly affected;
- a review finding identifies a gap outside the initial lookup.

Expand only to the newly established dependency/invariant, then re-narrow. Do not use one concrete dependency as license for unrestricted repository reading.

This never reduces the required scope of an Independent Review; `#review` defines that review task's relevant surface and required matrices/checklist.

## Prefer deterministic evidence

Prefer deterministic checks and durable task evidence over repeated chat refinement when they answer the same question. Once a stable artifact/check has settled a claim, do not keep relitigating it through free-form prompts unless new evidence invalidates the conclusion.

This does not prohibit genuine clarification of an ambiguous requirement, design conflict, or operator decision.