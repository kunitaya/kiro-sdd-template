---
inclusion: manual
description: Generic Kiro SDD lifecycle, Direct Change route, review tiers, and delivery boundaries. Load with #sdd-workflow.
---

# Kiro SDD Workflow

`AGENTS.md` is authoritative for repository-wide policy. This file defines the reusable Kiro lifecycle.

## Route selection

Use a Spec for substantive design or implementation work. Direct Change is allowed only when the correction method is already fully determined and no new requirement, contract, state/lifecycle, identity/provenance, persistence/schema semantics, security boundary, or architecture responsibility decision is required. Resolve doubt toward a Spec.

Supported Spec entry styles:

- Requirements-First: `requirements.md` -> `design.md` -> `tasks.md`
- Design-First: `design.md` -> derived/reconciled `requirements.md` -> `tasks.md`
- Quick Spec: compact requirements/design flow with no unnecessary inter-phase stop
- Bugfix: `bugfix.md` -> `design.md` -> `tasks.md`

## Lifecycle

```text
Authoritative requirements + GitHub Issue + AGENTS.md
    ↓
Select route/workflow and review intensity
    ↓
Create Spec artifacts from .kiro/specs/_templates/
    ↓
Validate and publish Spec on dedicated branch / same Draft PR
    ↓
Supplemental automated review, if configured
    ↓
Independent Spec Review
    ↓
Implementation authorization
    ↓
Start each implementation task through Kiro native Spec Task Execution
    ↓
Implement + focused validation per task
    ↓
Final validation
    ↓
Publish implementation to the same Draft PR
    ↓
Supplemental automated review, if configured
    ↓
Independent Code / Requirements Review
    ↓
Required fixes and delta re-review
    ↓
Archive completed Spec under docs/spec-archive/
    ↓
Draft -> Ready
    ↓
HUMAN MERGE GATE
```

One Issue normally owns one branch and one PR. Spec and implementation stay in that PR. Merge is not implied by review PASS.

## Review intensity

Use the lowest tier that still matches semantic risk:

- Tier 1: persistence, identity/provenance, security, lifecycle/state, evidence/correctness-critical contracts.
- Tier 2: normal features, corrective issues, behavior-preserving refactors.
- Tier 3: bounded tooling, operator utilities, documentation, isolated configuration.

Tier affects review depth, not whether explicit requirements and acceptance criteria must be satisfied.

## Spec publication checkpoint

Before Independent Spec Review, publish a reviewable repository state: complete required artifacts, run applicable format/Markdown/config checks, commit and push the dedicated branch, and create/update the Draft PR with owning-Issue linkage.

## Implementation task design

Each task is a reviewable outcome with its own sufficient validation. Do not split merely by file or defer a child's required tests to a final test-only task. Use dependencies only when real. Record resumable child progress when a parent task spans multiple material outcomes.

## Automated review

Automated review is supplemental evidence. Classify findings independently. Only findings that meet `AGENTS.md`'s BLOCKING rule require a correction round. Pending/unavailable automated review must be reported truthfully.

## Direct Change delivery

```text
GitHub Issue -> implementation + validation -> commit/push -> Draft PR
-> Independent Code / Requirements Review -> required fixes -> Ready -> human merge
```

Promote Direct Change to a Spec immediately if implementation reveals a design or semantic decision.

## Final delivery

After Independent Code / Requirements Review PASS and required fixes, archive the active Spec to `docs/spec-archive/<issue-number>-<slug>/`, then mark the existing Draft PR Ready. Projects may use `scripts/finalize-spec` to automate this mechanical transition after adapting its configuration.