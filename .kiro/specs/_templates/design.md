# Spec Design: `<title>`

## Overview

Describe the chosen design and material boundaries. For Design-First, also declare the first-artifact workspace block, Issue, review tier, governing sources, relevant invariants, allowed structural change, forbidden behavioral change, and technical constraints before design work begins.

## Architecture

### Approach

`<what changes, where, why this design>`

### Refactoring invariant declaration

Complete when refactoring is involved:

- Behavioral invariants:
- Public API / CLI invariants:
- Persistence / schema invariants:
- Identity / provenance invariants:
- Error / status invariants:
- Security invariants:
- Performance assumptions:
- Allowed structural changes:
- Forbidden behavioral changes:

## Components and Interfaces

`<changed responsibilities/contracts or N/A>`

## Data Models

### NULL / status matrix

| Field | NULL meaning | NOT NULL domain | Valid combinations | Invalid combinations |
| --- | --- | --- | --- | --- |

### Structural enforcement matrix

| Invariant | Enforced by | Application-only justification if applicable |
| --- | --- | --- |

## Correctness Properties

### Property 1: `<name>`

**Validates: Requirements 1.1**

`<material correctness property>`

#### State-transition matrix

| From | Event/action | To | Forbidden? |
| --- | --- | --- | --- |

#### Identity / provenance matrix

| Identity kind | Source | Derived from | Ownership | Reuse scope |
| --- | --- | --- | --- | --- |

#### Adversarial counterexample matrix

| Attempted invalid state | Why impossible | How refused |
| --- | --- | --- |

Mark unrelated matrices `Not applicable — <reason>` rather than inventing entries.

## Error Handling

`<new/changed failure modes and surfacing, or N/A>`

## Testing Strategy

Define minimum sufficient evidence and stopping conditions for each material claim. Use executable evidence where behavior requires it; test the actual final implementation/schema rather than a simplified stand-in.