# Bugfix Design: `<title>`

## Overview

Copy this template to the Bugfix Spec's `design.md` after the applicable review
of `bugfix.md`. It is a design template, not an additional Spec artifact.
Read scope, tier, requirement inventory, and workspace isolation from `bugfix.md`;
do not invent a Feature-style `requirements.md` for this workflow.

Retain the native Bugfix design sections below. Instantiate repository-added matrices
only where materially affected. A concise `Not applicable — <reason>` is sufficient
for unrelated matrices.

## Glossary

Define Spec-specific terms needed to understand the correction, or reference their
authoritative owner.

## Bug Details

### Bug Condition

Reference `bugfix.md` Current Behavior (`1.x`) items. Identify the affected production
entry point, triggering condition, and observable failure. Distinguish confirmed facts
from hypotheses and pending reproduction.

### Examples

Reference recorded reproduction evidence or describe the minimum synthetic
counterexample and a relevant unaffected control. Do not duplicate large fixtures.

## Expected Behavior

Reference the numbered Expected Behavior (`2.x`) items from `bugfix.md` and explain the
observable contract the correction must establish.

### Preservation Requirements

Reference numbered Unchanged Behavior (`3.x`) items and applicable invariants. Identify
adjacent behavior the correction must preserve; this is binding scope, not optional
cleanup.

## Hypothesized Root Cause

Trace the mechanism producing the defect to actual code and ownership boundaries.
Explain why current behavior violates the expected contract. State what inspection or
reproduction confirms and what remains hypothetical.

## Correctness Properties

### Property 1: Corrected behavior

**Validates: Requirements 2.1**

Replace this example with the property established by the fix. Reference actual
numbered Expected Behavior items from `bugfix.md`.

### Property 2: Preservation of unaffected behavior

**Validates: Requirements 3.1**

Replace this example with the preservation property. Add properties only for material
contracts and reference existing `2.x` / `3.x` items.

#### State-transition matrix

Required when stateful entities are affected.

| From state | Event / action | To state | Forbidden? |
| --- | --- | --- | --- |

#### Identity / provenance matrix

Required when identity, ownership, origin, or evidence relationships are affected.

| Identity kind | Source | Derived from | Ownership | Reuse scope |
| --- | --- | --- | --- | --- |

#### Adversarial counterexample matrix

Required when invalid states, security boundaries, corruption, or silent-failure risks
are materially affected.

| Attempted invalid state | Why it must be impossible | How it is refused |
| --- | --- | --- |

## Fix Implementation

### Changes required

Describe the smallest coherent correction, affected owners/interfaces, and why it fixes
the cause while preserving declared unchanged behavior. Keep low-level execution steps
in the executor's plan.

### Refactoring Invariant Declaration

Complete when the correction includes behavior-preserving refactoring.

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

## Components and Interfaces

Identify changed components, public/internal contracts, and producer/consumer ownership.
If none change, state `Not applicable — <reason>`.

## Data Models

### NULL / status matrix

Required when status/NULL semantics are affected.

| Field | NULL meaning | NOT NULL domain | Valid combinations | Invalid combinations |
| --- | --- | --- | --- | --- |

### Structural enforcement matrix

Required when schema/constraints or other enforceable structural invariants are affected.

| Invariant | Enforced by | Application-only justification if applicable |
| --- | --- | --- |

## Error Handling

Describe new/changed failure modes and how each is surfaced. If none change, state
`Not applicable — <reason>`.

## Testing Strategy

### Validation approach

Use minimum sufficient evidence for affected risks and state stopping conditions. Plan
against the actual production code/schema when behavior or persistence is affected.
Record executed checks separately from planned checks and identify reusable evidence
with revision, scope, and limitations.

### Fix Checking

Show how the original counterexample reaches the corrected code and satisfies the
Expected Behavior properties. Expected values come from the contract or independent
evidence, not the implementation under test.

### Preservation Checking

Show how unchanged paths continue to satisfy preservation properties, including
material adjacent invariants.

### Unit Tests

Identify affected unit-level contracts, or explain why another layer provides
sufficient evidence.

### Property-Based Tests

Identify useful invariants and input dimensions when proportionate. Do not require a
new dependency merely because this heading exists.

### Integration Tests

Identify necessary production-path, persistence, and boundary evidence. State any
native/runtime boundary that still requires separate evidence.

## Documentation Impact

Identify supporting-document and traceability updates required after correction and
verification. Do not rewrite authoritative requirements to match defective behavior.
