# Spec Design: `<title>`

## Overview

Use this template for Feature Specs (Requirements-First or Design-First) and Quick Specs. For a Bugfix Spec, copy `_templates/bugfix-design.md` to the Spec's `design.md` instead.

Preserve the native design sections below. Instantiate repository-added matrices only where materially applicable; for unrelated matrices, state `Not applicable — <reason>`. Keep design at material contracts, ownership, and boundaries rather than implementation steps or a test-case catalog.

Use the declared review tier and the actually affected surfaces to decide matrix depth. A Tier 1 label does not require filling unrelated matrices mechanically, and a lower tier does not waive a matrix when the change materially affects that contract.

### Starting a Design-First Spec

Fill this section only when `requirements.md` does not exist yet. Declare the following before design work, then carry the declarations into the derived `requirements.md`:

```text
STRICT WORKSPACE ISOLATION

This spec belongs exclusively to the workspace root containing this file
(resolved at runtime via `git rev-parse --show-toplevel`; see
.kiro/steering/workspace-isolation.md).

Repository: <repository name>
GitHub Issue: #<number>
Branch: <branch-name>
Allowed modification scope: <paths, or "repository-wide within this root">
Prohibited cross-root operations:
- edit files in another workspace root
- run repository-changing commands against another root
- use another worktree's uncommitted state as implementation truth
- copy uncommitted changes between worktrees
```

- Kiro workflow: Feature Spec — Design-First
- GitHub Issue: `#<number>` — `<title>`
- Repository risk classification: [ ] Standard  [ ] Lightweight
- Review tier: [ ] Tier 1  [ ] Tier 2  [ ] Tier 3
- Authoritative requirement IDs / governing sources:
- Relevant invariants:
- Allowed structural change:
- Forbidden behavioral change:
- Technical / non-functional constraints:
- Design rationale:

Once Kiro derives `requirements.md`, reconcile it against the authoritative sources and these invariants before accepting `tasks.md`. If reconciliation reveals that a material semantic boundary remains unresolved, revise requirements/design before task decomposition rather than letting implementation choose by accident.

## Architecture

### Approach

Describe what changes, where, and why the selected design is appropriate. Reference the affected modules/files and responsibility boundaries. Identify the authoritative owner for each material rule introduced or moved; avoid creating a second path that can diverge.

### Refactoring Invariant Declaration

Required whenever the change includes behavior-preserving refactoring.

- Behavioral invariants:
- Public API / CLI invariants:
- Persistence / schema invariants:
- Identity / provenance invariants:
- Error / status invariants:
- Security invariants:
- Performance assumptions:
- Allowed structural changes:
- Forbidden behavioral changes:
- Regression-test coverage:

Any newly required behavior change is not silently absorbed into refactoring. Reconcile it against the Issue and authoritative requirements first.

## Components and Interfaces

Describe components, modules, classes, commands, APIs, or responsibilities introduced or changed, how they interact, and which owner controls each material invariant. If no component/interface changes, state `Not applicable — <reason>`.

When an existing legacy/compatibility path remains, state whether it is authoritative, delegated to the new owner, compatibility-only, or retired. Do not leave two paths apparently authoritative for the same rule.

## Data Models

Describe persisted/structured state introduced or changed, including ownership and historical/lifecycle scope.

### NULL / status matrix

Required when status/NULL semantics are affected.

| Field | NULL meaning | NOT NULL domain | Valid combinations | Invalid combinations |
| --- | --- | --- | --- | --- |

Explicitly distinguish row absence from an explicit status when they have different meaning.

### Structural enforcement matrix

Required when schema, constraints, or other structurally enforceable invariants are affected.

| Invariant | Enforced by | Application-only justification if applicable |
| --- | --- | --- |

Prefer structural enforcement for contradictions the datastore/type system can reliably prevent. If an invariant remains application-only, explain why a structural rule would be incorrect or impractical.

### Identity / provenance matrix

Required when identity, ownership, origin, derivation, or historical references are affected.

| Identity kind | Source components | Scope / owner | Stability boundary | Reuse / comparison scope | Enforcement |
| --- | --- | --- | --- | --- | --- |

State whether stability means within one database/history/run, across reruns, or across rebuilds. Do not use a stronger word such as `stable` without fixing the intended scope when different readings would change implementation.

### Lifecycle / state-transition matrix

Required when stateful entities or terminal/history semantics are affected.

| From state | Event / action | To state | Allowed? | Enforcement / evidence |
| --- | --- | --- | --- | --- |

Cover restart/resume, failure, terminal immutability, and selection/presentation eligibility when applicable.

## Correctness Properties

### Property 1: `<property name>`

**Validates: Requirements 1.1, 1.2**

State the contract-level property the design must preserve or establish. Reference this Spec's native Requirement/Acceptance-Criterion numbers here; trace authoritative source IDs through `requirements.md` rather than substituting them for native references.

Add further properties only for additional material contracts.

### Adversarial counterexample matrix

Required when invalid states, security boundaries, corruption, cross-scope references, or silent-failure risks are materially affected.

| Attempted invalid state | Why it must be impossible | How it is refused |
| --- | --- | --- |

Derive cases from real requirements/invariants. Do not invent speculative categories solely to fill the table.

### Reproducibility / canonicalization matrix

Required when values are hashed, canonicalized, signed, versioned, or reused across runs.

| Logical input | Canonical representation | Exact hashed/signed value | Downstream consumed value | Version | Persisted provenance | Reuse/comparison conditions |
| --- | --- | --- | --- | --- | --- | --- |

If the hashed/canonicalized value intentionally differs from the next consumed value, state why. An accidental intermediate rendering difference is not an acceptable design.

## Error Handling

Describe error/failure modes introduced or changed and how they are surfaced. Include failure isolation/retry/resume boundaries when material. If none change, state `Not applicable — <reason>`.

## Testing Strategy

### Stage-appropriate validation plan / evidence

For each material claim, identify the minimum sufficient evidence, the appropriate layer, and the stopping condition. During Spec authoring, plan validation rather than demanding implementation proof before code exists.

Use focused validation for child/execution-slice outcomes, parent integration checks for interactions, and broader/full regression at the final checkpoint when scope/risk or repository policy requires it. Reuse still-valid prior evidence and identify only the delta that new changes invalidate.

When reusing evidence, record its revision/result; do not claim it executed at a later revision.

### Unit Tests

Identify unit-level contracts/boundaries requiring focused evidence, or explain why another layer is sufficient.

### Property-Based Tests

Identify useful invariants/input dimensions when proportionate. Do not add a dependency merely because this section exists.

### Integration / Runtime Tests

Identify required integration, persistence, external-interface, native-runtime, or end-to-end evidence. Explicitly separate synthetic evidence from still-pending native/production-like verification.

## Documentation Impact

Identify living documentation, traceability, migration, or operator documentation that must change if this design is implemented. Keep reusable docs focused on current truth; keep Issue/Spec execution chronology in the change record rather than copying it into living policy.
