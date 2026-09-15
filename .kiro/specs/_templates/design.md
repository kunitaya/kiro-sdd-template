# Spec Design: `<title>`

## Overview

Use this template for Feature Specs (Requirements-First or Design-First) and Quick
Specs. For a Bugfix Spec, copy `_templates/bugfix-design.md` to the Spec's
`design.md` instead.

Preserve the native design sections below. Instantiate repository-added matrices only
where materially applicable; for unrelated matrices, state `Not applicable — <reason>`.
Keep design at material contracts, ownership, and boundaries rather than implementation
steps or a test-case catalog.

### Starting a Design-First Spec

Fill this section only when `requirements.md` does not exist yet. Declare the following
before design work, then carry the declarations into the derived `requirements.md`:

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

Once Kiro derives `requirements.md`, reconcile it against the authoritative sources and
these invariants before accepting `tasks.md`.

## Architecture

### Approach

Describe what changes, where, and why the selected design is appropriate. Reference the
affected modules/files and responsibility boundaries.

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

Any newly required behavior change is not silently absorbed into refactoring. Reconcile
it against the Issue and authoritative requirements first.

## Components and Interfaces

Describe components, modules, classes, commands, APIs, or responsibilities introduced
or changed, how they interact, and which owner controls each material invariant. If no
component/interface changes, state `Not applicable — <reason>`.

## Data Models

### NULL / status matrix

Required when status/NULL semantics are affected.

| Field | NULL meaning | NOT NULL domain | Valid combinations | Invalid combinations |
| --- | --- | --- | --- | --- |

### Structural enforcement matrix

Required when schema, constraints, or other structurally enforceable invariants are
affected.

| Invariant | Enforced by | Application-only justification if applicable |
| --- | --- | --- |

## Correctness Properties

### Property 1: `<property name>`

**Validates: Requirements 1.1, 1.2**

State the contract-level property the design must preserve or establish. Reference this
Spec's native Requirement/Acceptance-Criterion numbers here; trace authoritative source
IDs through `requirements.md` rather than substituting them for native references.

Add further properties only for additional material contracts.

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

## Error Handling

Describe error/failure modes introduced or changed and how they are surfaced. If none
change, state `Not applicable — <reason>`.

## Testing Strategy

### Stage-appropriate validation plan / evidence

Identify the minimum sufficient evidence and stopping condition for each material claim.
During Spec authoring, plan validation rather than demanding implementation-level proof
before code exists. Structural/documentation claims may be established by direct/static
inspection. Use executable evidence where behavior materially requires it and test the
actual implementation/schema rather than a simplified stand-in.

### Unit Tests

Identify unit-level contracts and boundaries requiring focused evidence, or explain why
another layer is sufficient.

### Property-Based Tests

Identify useful invariants/input dimensions when proportionate. Do not add a dependency
merely because this section exists.

### Integration / Runtime Tests

Identify required integration, persistence, external-interface, native-runtime, or
end-to-end evidence. Explicitly separate synthetic evidence from still-pending native
or production-like verification.

## Documentation Impact

Identify living documentation, traceability, migration, or operator documentation that
must change if this design is implemented.
