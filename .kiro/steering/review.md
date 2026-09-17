---
inclusion: manual
description: Independent review procedure, convergence rules, correction analysis, high-risk matrices, evidence reuse, and PASS/reopening policy. Load with #review.
---

# Review Procedure

This document supplies detailed review procedure under `AGENTS.md` > Review Protocol.
`AGENTS.md` remains authoritative for repository-wide severity and gate rules.

## Review objective

A review exists to decide a lifecycle gate truthfully. It is not an open-ended search for every possible improvement.

- **Independent Spec Review** asks whether implementation can proceed without guessing about material behavior and whether requirements/design/tasks form a coherent, executable plan.
- **Independent Code / Requirements Review** asks whether the resulting implementation satisfies the applicable requirements and invariants with sufficient evidence.

Once the applicable exit criteria are satisfied and no BLOCKING finding remains, end the gate. Do not hold it open for stylistic cleanup, theoretical completeness, or optional future-proofing.

## Required initial review sequence

For every substantive initial review:

1. read authoritative sources according to repository precedence;
2. identify the complete affected requirement/invariant scope, including materially adjacent contracts;
3. build an explicit invariant checklist before concluding;
4. review the resulting system/design state, not only changed lines;
5. when one defect pattern is found, horizontally inspect materially analogous relationships;
6. attempt realistic invalid/adversarial states for affected high-risk boundaries;
7. complete the planned pass before reporting findings rather than drip-feeding one blocker per round;
8. choose proportionate evidence for each claim and stop once it is sufficiently established for the current gate.

Examples of horizontal inspection include analogous run/scope ownership, derived identity, nullable uniqueness, denormalized facts, immutability/history, and version/hash/configuration relationships.

## Finding severity and correction threshold

A finding is BLOCKING only when it prevents an explicit requirement, acceptance criterion, material correctness/security invariant, lifecycle gate, or truthful PASS/result.

Do not create a mandatory correction round solely for cleaner architecture/naming, extra telemetry, optional abstraction, speculative defensive work, future extensibility, additional tests after sufficient evidence exists, non-material documentation expansion, or theoretical edge cases without realistic requirement impact.

Adjacent genuine defects that do not block the current task are reported separately.

## Stage-appropriate precision

Spec review and implementation review use different evidence burdens. During Spec review, block on missing or contradictory material semantics, not missing implementation-level proof for code that does not exist yet. During implementation review, observable behavior, persistence, security, concurrency, and failure handling should use executable evidence where practical.

Start from documented dependency contracts. Inspect dependency internals only when an observed discrepancy, documented limitation, or private/undefined behavior leaves a material in-scope question unresolved.

## Verification proportionality and reuse

Before non-trivial verification, identify the claim/risk, minimum sufficient evidence, appropriate layer, stopping condition, and whether exhaustive traversal is actually required.

Once a claim has sufficient primary evidence, do not repeat a functionally equivalent lookup/check against unchanged evidence merely to gain extra confidence. Revalidation is warranted when code, dependencies, environment, requirement scope, or a new finding invalidates the prior evidence.

This applies especially to expensive evidence such as full regression: reuse a passing result at the reviewed revision while its assumptions remain valid. If reused later, record the original revision/result plus the new delta checks; never claim the old suite executed at the new revision.

An external/source lookup that cannot be confirmed after a reasonable bounded attempt should be recorded as unconfirmed rather than retried through multiple equivalent transports indefinitely.

## Before implementing review corrections

Whenever a review returns required corrections, summarize before editing:

1. **Cause** — confirmed mistaken assumption/omission; distinguish facts from hypotheses.
2. **Affected paths** — producers, callers, consumers, analogous paths, and governing requirements/invariants.
3. **Behavior boundary** — behavior that must change and behavior that must remain unchanged, including material failure/rerun/concurrency cases.
4. **Verification** — checks that detect the original defect and regressions, with expected outcomes.

This is a concise correction plan/evidence summary, not a request for hidden reasoning and not a new approval gate. Proceed with the already-authorized correction after stating it.

## Correction re-review before first PASS

Verify every previous BLOCKING finding, any NON-BLOCKING item the correction claims to fix, defects introduced by the correction, materially changed invariants, and analogous relationships exposed by the pattern.

Do not restart the entire initial review from zero unless the correction materially changes architecture, requirement scope, state/identity/security/persistence semantics, public/internal contract, or another premise of the earlier review.

## PASS as a baseline and gate reopening

A PASS is accepted evidence for the reviewed repository state. Subsequent commits use delta re-review unless new information or changes materially invalidate the prior exit criteria.

Reopen for material requirement/acceptance changes, architecture/API/schema/security/identity/lifecycle/status/NULL contract changes, substantial scope broadening, a confirmed new BLOCKING defect, or a material factual premise proven false.

Do not reopen solely for formatting, wording cleanup, alternative testing techniques, optional improvements, or later NON-BLOCKING automated findings.

## Automated review findings

Automated review is supplemental evidence. A clean automated review supports convergence but does not replace Independent Review. A later automated finding after PASS does not automatically revoke PASS. Classify findings under the same BLOCKING rule. Pending/quota/unavailable review is reported as such, never as PASS.

## Requirement and invariant inventory

Before reviewing a high-risk change, identify all governing requirements and derive the conditions that must remain true. Do not let a requirement disappear between Issue -> Spec -> implementation -> tests -> persisted/runtime behavior.

## State-transition matrix

When state/lifecycle is affected:

| From state | Event/action | To state | Allowed? | Enforcement/evidence |
| --- | --- | --- | --- | --- |

Check impossible/repeated transitions, failure/rollback, restart/resume, and historical state where relevant.

## Identity / provenance matrix

When identity, ownership, derivation, origin, or traceability is affected:

| Identity kind | Source components | Scope/owner | Derived/reused how | Enforcement/evidence |
| --- | --- | --- | --- | --- |

Verify derived identity cannot detach from source facts, cross the wrong scope, or silently merge distinct sources.

## NULL / status matrix

When status/skip/error/NULL semantics are affected:

| Field/status | NULL meaning | Non-NULL domain | Valid combinations | Invalid combinations |
| --- | --- | --- | --- | --- |

Explicitly review unknown/incomplete/not-evaluated/error representability. Do not convert uncertainty into a definitive negative for storage convenience.

## Structural enforcement matrix

When a relationship can be structurally enforced:

| Invariant | PK/FK/composite FK/UNIQUE/CHECK/trigger/type/other | Application-only justification |
| --- | --- | --- |

Prefer structural enforcement when the datastore/type system can reliably prevent contradictions.

## Data-model review checklist

When persistence/schema/identity/history is materially affected, inspect the applicable items rather than applying this list mechanically to unrelated work:

- primary/natural/derived identity semantics;
- parent ownership, foreign/composite keys, UNIQUE and NULL behavior;
- CHECK constraints and representability gaps;
- denormalized facts and drift prevention;
- scope/run isolation and configuration/version consistency;
- historical/terminal immutability, rerun/resume/idempotency;
- every material status/skip/error state; and
- traceability from result back to its owning source/evidence.

## Reproducibility / canonicalization checklist

When a value is hashed, canonicalized, signed, versioned, or reused across runs, identify as applicable:

1. logical input;
2. exact canonical representation;
3. exact bytes/value hashed or signed;
4. exact value consumed by the next system boundary;
5. version identifier;
6. persisted provenance; and
7. conditions under which reuse/comparison is valid.

Any intentional difference between hashed/canonicalized material and downstream-consumed material must be explicit rather than an accidental rendering artifact.

## Adversarial counterexamples

Construct realistic states the requirements say must be impossible and determine whether final design/implementation rejects them. Examples include cross-scope references, stale/mismatched versions, inconsistent duplicated facts, forbidden transitions, missing mandatory evidence, aliased mutable ownership, and partial-failure states. Do not fabricate speculative cases merely to fill a matrix.

## Executable validation

When executable validation is necessary, test the real final design/implementation or schema. A simplified stand-in may explore an idea but does not prove the production contract. Expected values come from requirements, independent fixtures/oracles, or external contracts rather than the same implementation under test.

## Review output

Conclude explicitly with `Decision: PASS`, `Decision: PASS WITH NON-BLOCKING FINDINGS`, or `Decision: BLOCKED` / equivalent repository-required status. For PASS, keep optional suggestions short. For a blocked gate, report the material blockers from the completed pass together so one correction round can address them coherently.