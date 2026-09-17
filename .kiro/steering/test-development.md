---
inclusion: fileMatch
fileMatchPattern: "tests/**"
description: Generic test planning, layered validation cadence, and evidence-reuse guidance.
---

# Test Development

Tests prove affected requirements/invariants and preserve relevant existing behavior. Add the minimum evidence needed to detect the defect or establish the new contract.

## Validation cadence

Use validation that matches the execution level:

- child / execution slice: focused tests and checks for the changed result;
- parent integration: cross-child interactions and directly affected regression surface;
- final Issue / Spec checkpoint: broader regression or repository-wide gates when required by scope, risk, or project policy.

Do not run a full repository suite after every child merely because the finished implementation eventually requires one. Conversely, do not defer a child's necessary focused checks to final delivery.

## Evidence reuse and delta validation

Reuse a prior passing result while the code, dependencies, runtime/environment, and tested boundary that support it remain unchanged. Rerun checks whose assumptions were invalidated by subsequent changes.

At correction or delta checkpoints, combine still-valid prior evidence with checks of the changed and directly affected boundaries. Repeat a full suite when the change has repository-wide impact, materially invalidates the prior full-suite evidence, or an explicit gate requires it.

Record evidence truthfully: an older suite run may support an unchanged surface at a newer revision, but it must not be described as having executed at that newer revision. Record the revision/result being reused and the new delta checks separately.

## Test quality

Prefer focused unit/integration tests during implementation. Include boundary, failure, rerun/concurrency, persistence, NULL/status, or adversarial cases when those semantics are materially affected.

Do not make tests encode an implementation accident as a new requirement. Do not weaken requirements to keep existing tests green. A passing suite does not by itself prove requirement compliance; compare implementation and tests against the governing contract.

If a required test/tool cannot run, report the exact limitation and the unverified claim truthfully. Unrun validation is not PASS.