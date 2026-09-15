---
inclusion: manual
description: Independent review procedure, convergence rules, correction analysis, high-risk matrices, evidence selection, and PASS/reopening policy. Load with #review.
---

# Review Procedure

This document supplies detailed review procedure under `AGENTS.md` > Review Protocol.
`AGENTS.md` remains authoritative for repository-wide severity and gate rules.

## Review objective

A review exists to decide a lifecycle gate truthfully. It is not an open-ended search
for every possible improvement.

- **Independent Spec Review** asks whether implementation can proceed without guessing
  about material behavior and whether requirements/design/tasks form a coherent,
  executable plan.
- **Independent Code / Requirements Review** asks whether the resulting implementation
  satisfies the applicable requirements and invariants with sufficient evidence.

Once the applicable exit criteria are satisfied and no BLOCKING finding remains, end
the gate. Do not hold it open for stylistic cleanup, theoretical completeness, or
optional future-proofing.

## Required initial review sequence

For every substantive initial review:

1. Read the authoritative sources according to repository precedence.
2. Identify the complete affected requirement/invariant scope. Do not limit review to
   IDs named by the PR when adjacent contracts are materially affected.
3. Build an explicit invariant checklist before concluding the review.
4. Review the resulting system/design state, not only changed lines.
5. When one defect pattern is found, horizontally inspect materially analogous
   relationships before declaring the pass complete.
6. Attempt realistic invalid/adversarial states for affected high-risk boundaries.
7. Complete the planned pass before reporting findings; do not stop after the first
   blocker and then drip-feed unrelated findings in multiple rounds.
8. Choose proportionate evidence for each claim and stop verification when the claim is
   established sufficiently for the current gate.

Examples of horizontal inspection:

- one run/scope ownership defect -> inspect analogous scoped parent/child relationships;
- one derived identity defect -> inspect other derived identities using the same source
  assumptions;
- one nullable uniqueness defect -> inspect analogous nullable natural/composite keys;
- one duplicated fact drifting -> inspect other denormalized copies of that fact;
- one immutability/history defect -> inspect other historical references and update
  paths;
- one version/hash/config mismatch -> inspect analogous versioned identities and
  persisted configuration relationships.

## Finding severity and correction threshold

A finding is BLOCKING only when it prevents an explicit requirement, acceptance
criterion, material correctness/security invariant, lifecycle gate, or truthful
PASS/result.

Do not create a mandatory correction round solely for:

- cleaner architecture or naming;
- extra telemetry/observability;
- optional abstraction or deduplication;
- defensive programming beyond the current contract;
- future extensibility;
- additional tests after sufficient evidence already exists;
- documentation expansion that does not resolve ambiguity;
- theoretical edge cases without a requirement or realistic material risk.

Adjacent genuine defects that do not block the current task are reported separately.

## Stage-appropriate precision

Spec review and implementation review use different evidence burdens.

During Spec review, block on missing/contradictory material semantics, not on the absence
of executable proof for details that do not exist yet. Structural invariants may be
established by design structure, direct source inspection, static/type constraints, or
another adequate method.

During implementation review, observable behavior, persistence semantics, security,
concurrency, and failure handling should use executable evidence where practical. Tests
alone do not prove requirement coverage, but reviewers should not re-prove standard
library/dependency internals without a concrete unresolved in-scope question.

Start from documented dependency contracts. Expand into dependency internals only when
an observed discrepancy, documented limitation, or private/undefined behavior leaves a
material question unresolved.

## Verification proportionality and reuse

Before running non-trivial verification, identify:

1. the property/risk being proven;
2. minimum sufficient evidence;
3. the appropriate layer (static/unit/integration/runtime/native/end-to-end);
4. the stopping condition; and
5. whether full/exhaustive traversal is genuinely needed.

Once a claim has sufficient primary evidence, do not repeat an equivalent lookup/check
against unchanged evidence merely to obtain more confidence. Revalidation is warranted
when code, dependencies, environment, requirement scope, or a new finding invalidates
the previous evidence.

## Before implementing review corrections

Whenever a review returns required corrections, summarize these four points before
editing:

1. **Cause** — the confirmed mistaken assumption/omission behind the defect; distinguish
   facts from hypotheses.
2. **Affected paths** — relevant producers, callers, consumers, analogous paths, and
   governing requirements/invariants.
3. **Behavior boundary** — behavior that must change and behavior that must remain
   unchanged, including material failure/rerun/concurrency cases.
4. **Verification** — checks that detect the original defect and regressions, with
   expected outcomes.

This is a concise correction plan/evidence summary, not a request for hidden reasoning
and not a new approval gate. After stating it, proceed with the already-authorized
correction.

## Correction re-review before first PASS

A correction re-review verifies:

- every previous BLOCKING finding;
- any NON-BLOCKING item the correction claims to fix;
- defects newly introduced by the correction;
- invariants whose assumptions/surface materially changed; and
- analogous relationships when the correction exposes a pattern.

Do not automatically restart the entire initial review from zero when unchanged areas
retain valid evidence. Restart the full checklist only if the correction materially
changes the architecture, requirement scope, state/identity/security/persistence model,
public/internal contract, or another premise on which the earlier review depended.

## PASS as a baseline and gate reopening

A PASS is accepted evidence for the reviewed repository state. Subsequent commits use
delta re-review unless a gate-reopening condition occurs.

Reopen a passed gate only when new information or subsequent changes materially
invalidate the prior exit criteria, for example:

- authoritative requirement / explicit acceptance criterion changes;
- architecture, API, schema, security, identity, lifecycle, state, status/NULL, or other
  material contract changes;
- a correction broadens the affected surface beyond the prior review premise;
- a confirmed new BLOCKING defect is found; or
- a material factual premise supporting the PASS is proven false/incomplete.

Do not reopen solely for formatting, wording cleanup, alternative testing techniques,
optional design improvements, or later NON-BLOCKING automated findings.

## Automated review findings

Automated review is supplemental evidence.

- A clean automated review supports convergence but does not replace Independent Review.
- A later automated finding after PASS does not automatically revoke PASS.
- Classify it under the same BLOCKING rule.
- Correct genuine blockers; optional findings may be recorded or addressed without
  withholding the next stage.
- Pending/quota/unavailable automated review is reported as such, never as PASS.

## Requirement and invariant inventory

Before reviewing a high-risk change, identify all governing requirements and derive the
conditions that must always remain true. Do not let a requirement disappear between
Issue -> Spec -> implementation -> tests -> persisted/runtime behavior.

## State-transition matrix

Whenever state/lifecycle is affected, inspect every material allowed/forbidden
transition:

| From state | Event/action | To state | Allowed? | Enforcement/evidence |
| --- | --- | --- | --- | --- |

Check impossible transitions, repeated transitions, failure/rollback semantics,
restart/resume behavior, and historical state where relevant.

## Identity / provenance matrix

Whenever identity, ownership, derivation, origin, or traceability is affected:

| Identity kind | Source components | Scope/owner | Derived/reused how | Enforcement/evidence |
| --- | --- | --- | --- | --- |

Verify that derived identity cannot detach from its source facts, cross the wrong scope,
or silently merge distinct sources.

## NULL / status matrix

Whenever status/skip/error/NULL semantics are affected:

| Field/status | NULL meaning | Non-NULL domain | Valid combinations | Invalid combinations |
| --- | --- | --- | --- | --- |

Explicitly review representability of unknown/incomplete/not-evaluated/error states.
Do not convert uncertainty into a definitive negative merely because storage or code is
easier that way.

## Structural enforcement matrix

Whenever a relationship can be structurally enforced, review whether it should be:

| Invariant | PK/FK/composite FK/UNIQUE/CHECK/trigger/type/other | Application-only justification |
| --- | --- | --- |

Prefer structural enforcement for contradictions the datastore/type system can reliably
prevent. Application discipline is justified only when structural enforcement cannot
represent the actual contract or would create another material defect.

## Adversarial counterexamples

Construct realistic states that the requirements say must be impossible and determine
whether the final design/implementation rejects them. Examples include cross-scope
references, stale/mismatched versions, inconsistent duplicated facts, forbidden state
transitions, missing mandatory evidence, aliased/shared mutable ownership, and partial
failure states.

Do not fabricate speculative attack cases unrelated to the affected contract merely to
make a matrix look complete.

## Executable validation

When executable validation is necessary, test the real final design/implementation or
schema. A hand-written simplified stand-in may explore an idea but does not prove the
production contract.

Expected values must come from requirements, independent fixtures/oracles, or another
external contract — not from the same implementation under test.

## Review output

Conclude explicitly:

```text
Decision: PASS
```

or:

```text
Decision: BLOCKED

Blocking findings:
1. ...
```

For PASS, keep optional suggestions short and do not manufacture improvement work. For
BLOCKED, report the material blockers found in the completed pass together so one
correction round can address them coherently.
