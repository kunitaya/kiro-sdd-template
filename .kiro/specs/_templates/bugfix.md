# Bugfix Requirements: `<title>`

## Introduction

**Spec:** `<title>`

Use the Bugfix workflow for correction of defective implemented behavior. A complex, critical-path, high-cost-regression, or persistence/security-sensitive defect remains a Bugfix Spec; increase tier/review intensity rather than converting it to a Feature Spec merely because the correction is difficult.

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

The main root may be referenced only for baseline comparison unless explicitly authorized by this spec.
```

Do not persist an absolute filesystem path in this block. Runtime identity is verified from the actual worktree.

## Source

- GitHub Issue: `#<number>` — `<title>`
- Governing requirement / contract IDs: `<IDs, or "none — corrective work">`

## Glossary

Define only terms needed to understand this correction. Reference an authoritative definition instead of restating it when one already exists.

- `<Term>`: `<definition or authoritative reference>`

## Change type / Spec tier

Choose one:

- [ ] Tier 1 — persistence / identity / security / lifecycle / correctness-critical
- [ ] Tier 2 — normal corrective issue / behavior-preserving refactor
- [ ] Tier 3 — bounded tooling / operator utility / documentation

Spec kind: [ ] Standard  [ ] Lightweight

## Requirement inventory

Map the bugfix behavior below to the actual governing source. This table is traceability, not a second requirements authority. Keep distinct Issue acceptance criteria distinct when they impose different corrected/preserved behavior.

| Bugfix item | Governing source | Notes |
| --- | --- | --- |
| 1.1 / 2.1 / 3.1 |  |  |

## 1. Current Behavior

Use numbered `1.x` items for reproducible observed behavior. Distinguish confirmed behavior from hypotheses. Record the smallest realistic counterexample that proves the defect.

1.1 `<observable defective behavior>`

## 2. Expected Behavior

Use numbered `2.x` items for behavior required after correction. Do not silently broaden the Issue or invent a stronger contract merely because a different design is possible.

2.1 `<required corrected behavior>`

## 3. Unchanged Behavior

Use numbered `3.x` items for contracts the correction must preserve. These are binding regression boundaries, not optional context.

3.1 `<behavior that must remain unchanged>`

## Reproduction / evidence

Record the minimum evidence that establishes Current Behavior: trigger/input, command or call path, and observed result. Keep confirmed reproduction separate from expected/planned reproduction.

Before advancing to design, either:

- record a confirmed reproduction/counterexample; or
- state explicitly why reproduction is pending/unavailable and what design/task must establish before the defect can be considered confirmed.

Do not silently treat an unexecuted reproduction plan as observed behavior.

## Invariant inventory

List conditions that must remain true through the correction, including behavior-preservation constraints and applicable state/identity/persistence/security invariants.

| # | Invariant | Why it matters | Currently enforced by |
| --- | --- | --- | --- |
| 1 |  |  |  |

## Correction boundary

Summarize the smallest authorized behavior change and the surfaces that must not change. This does not replace `design.md`; it prevents a local defect correction from absorbing adjacent redesign during root-cause analysis.

- Behavior that must change:
- Behavior that must remain unchanged:
- Adjacent defects intentionally excluded:

## Out of scope

State adjacent defects, cleanup, redesign, or future behavior this bugfix will not address.

## Open questions / conflicts

State unresolved conflicts against the Issue, authoritative requirements, repository policy, or reproduction evidence. Do not resolve them by convenient reinterpretation.
