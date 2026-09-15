# Bugfix Requirements: `<title>`

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

Do not persist an absolute filesystem path in this block. Runtime identity is
verified from the actual worktree.

## Source

- GitHub Issue: `#<number>` — `<title>`
- Governing requirement / contract IDs: `<IDs, or "none — corrective work">`

## Glossary

Define only terms needed to understand this correction. Reference an authoritative
definition instead of restating it when one already exists.

- `<Term>`: `<definition or authoritative reference>`

## Change type / Spec tier

Choose one:

- [ ] Tier 1 — persistence / identity / security / lifecycle / correctness-critical
- [ ] Tier 2 — normal corrective issue / behavior-preserving refactor
- [ ] Tier 3 — bounded tooling / operator utility / documentation

Spec kind: [ ] Standard  [ ] Lightweight

## Requirement inventory

Map the bugfix behavior below to the actual governing source. This table is
traceability, not a second requirements authority.

| Bugfix item | Governing source | Notes |
| --- | --- | --- |
| 1.1 / 2.1 / 3.1 |  |  |

## 1. Current Behavior

Use numbered `1.x` items for reproducible observed behavior. Distinguish confirmed
behavior from hypotheses. Record the smallest counterexample that proves the defect.

1.1 `<observable defective behavior>`

## 2. Expected Behavior

Use numbered `2.x` items for the behavior required after correction. Do not silently
broaden the Issue or create a new contract merely because a stronger design is possible.

2.1 `<required corrected behavior>`

## 3. Unchanged Behavior

Use numbered `3.x` items for contracts and behavior the correction must preserve.
These are binding regression boundaries.

3.1 `<behavior that must remain unchanged>`

## Reproduction / evidence

Describe the minimum evidence that establishes Current Behavior. Keep planned and
executed evidence distinct; do not claim an unrun reproduction passed.

## Invariant inventory

List conditions that must remain true through the correction, including behavior-
preservation constraints for refactoring.

| # | Invariant | Why it matters | Currently enforced by |
| --- | --- | --- | --- |
| 1 |  |  |  |

## Out of scope

State adjacent defects, cleanup, redesign, or future behavior that this bugfix will not
address.

## Open questions / conflicts

State unresolved conflicts against the Issue, authoritative requirements, or repository
policy. Do not resolve them by convenient reinterpretation.
