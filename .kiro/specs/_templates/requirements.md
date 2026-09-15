# Requirements Document

## Introduction

**Spec:** `<title>`

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

The main root may be referenced only for baseline comparison unless
explicitly authorized by this spec.
```

Do not put a machine-specific absolute filesystem path in this block. The owning
root is logical in the artifact and verified from Git at runtime.

## Source

- GitHub Issue: `#<number>` — `<title>`
- Driving authoritative requirement IDs: `<IDs, or "none — corrective work / operator utility">`

## Glossary

State Spec-specific or domain terms needed by a reviewer. Reference an existing
authoritative definition instead of duplicating it.

- `<Term>`: `<definition or authoritative reference>`

## Change type / Spec tier

Choose one:

- [ ] Tier 1 — persistence / identity / security / lifecycle / correctness-critical
- [ ] Tier 2 — normal feature / corrective issue / behavior-preserving refactor
- [ ] Tier 3 — helper / operator utility / bounded verification / documentation

Spec kind: [ ] Standard  [ ] Lightweight

## Requirements

Use Kiro's native requirements structure. Create as many coherent Requirement sections
as the scope needs; do not collapse a multi-requirement change into one placeholder
merely because traceability exists below.

### Requirement 1: `<short title>`

**User Story:** As a `<role>`, I want `<feature/behavior>`, so that `<benefit>`.

#### Acceptance Criteria

1. WHEN `<event>`, THE `<system/component>` SHALL `<observable behavior>`.
2. IF `<condition>`, THEN THE `<system/component>` SHALL `<observable behavior>`.

### Requirement 2: `<short title>`

**User Story:** As a `<role>`, I want `<feature/behavior>`, so that `<benefit>`.

#### Acceptance Criteria

1. WHEN `<event>`, THE `<system/component>` SHALL `<observable behavior>`.

[Continue with additional native Requirement sections as needed.]

## Requirement Source Traceability

Map each native Requirement / Acceptance Criterion above to the authoritative source it
satisfies. This table is traceability, not a second requirement specification.

| Kiro Requirement / AC | Governing source | Notes |
| --- | --- | --- |
| Requirement 1 / AC 1 |  |  |

## Invariant inventory

List every condition that must remain true after this change, including behavior that
must not change during refactoring.

| # | Invariant | Why it matters | Currently enforced by |
| --- | --- | --- | --- |
| 1 |  |  |  |

## Out of scope

State explicitly what the Spec will not do, especially adjacent work that could be
tempting to absorb opportunistically.

## Open questions / conflicts

State conflicts or ambiguities against authoritative sources. Do not resolve them by
convenient reinterpretation; stop and escalate material conflicts.
