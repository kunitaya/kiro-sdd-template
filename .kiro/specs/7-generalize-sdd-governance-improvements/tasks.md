# Implementation Plan: `Generalize recent SDD governance improvements from production use`

## Overview

This plan applies the genericized process improvements in two implementation waves after Independent Spec Review authorization. The first wave updates high-confidence execution/workflow/task surfaces. The second wave selectively updates review/source/document/template surfaces without importing adopter-specific policy.

## Task Dependency Graph

```json
{
  "waves": [
    { "wave": 1, "tasks": [1] },
    { "wave": 2, "tasks": [2] },
    { "wave": 3, "tasks": [3] }
  ]
}
```

Task 1 is the implementation-authorization gate. Task 2 and Task 3 are intentionally separated by responsibility, not by file count. Task 3 depends on Task 2 only so the final genericization pass can reconcile wording against the concrete high-confidence updates already applied.

## Tasks

- [ ] 1. IMPLEMENTATION-AUTHORIZATION GATE
  - Outcome: Independent Spec Review PASS by a party other than the authoring agent, explicitly authorizing implementation at a recorded revision.
  - Validation: record the independent review link, revision, and outcome; resolve all BLOCKING findings. Supplemental automated review does not satisfy this gate.
  - Update this checkbox and the authorization delivery checkpoint together when the actual approval is recorded. Do not self-complete the gate or start implementation while it is unchecked.

- [ ] 2. Apply high-confidence generic workflow/execution improvements — traces to: Requirements 1, 2, 3, 4, 5
  - Depends on: Task 1.
  - Outcome: update execution efficiency, task prompts, test validation cadence, SDD lifecycle/task state, and Bugfix workflow guidance using generic language and existing ownership boundaries.
  - Validation: focused Markdown/cross-reference inspection for the changed files; verify no project-specific commands/IDs/domain policy were introduced.
  - [ ] 2.1 Update `.kiro/steering/execution-efficiency.md` with durable progress/resumption, parent responsibility, stall/retry boundaries, focused delegated validation, and expensive-check preservation guidance.
  - [ ] 2.2 Update `.kiro/steering/task-prompt.md` and `templates/kiro-task-prompt.md` with explicit validation scope, targeted lookup, bounded guidance-load preflight, and deterministic-check preference.
  - [ ] 2.3 Update `.kiro/steering/test-development.md` with slice/parent/final/correction validation cadence and revision-truthful evidence reuse.
  - [ ] 2.4 Update `.kiro/steering/sdd-workflow.md` and `.kiro/specs/_templates/tasks.md` with lifecycle-checkbox synchronization, explicit external gates, publication semantics, automated-review state handling, and final-delivery boundaries.
  - [ ] 2.5 Update `.kiro/specs/_templates/bugfix.md` so workflow kind remains Bugfix for defect correction while review tier/Spec kind carries rigor; strengthen numbered behavior/reproduction guidance.

- [ ] 3. Selectively genericize review/source/document/template improvements — traces to: Requirement 6
  - Depends on: Task 2.
  - Outcome: add only broadly reusable convergence/evidence/scale/documentation/template clarifications while keeping generic policy compact and adopter-neutral.
  - Validation: inspect the combined diff for duplicated policy, project-specific leakage, and ownership drift; run applicable Markdown/config checks with provisioned tools if available.
  - [ ] 3.1 Update `.kiro/steering/review.md` with concise no-equivalent-reverification, applicability-scoped data-model checks, and reproducibility review checklist.
  - [ ] 3.2 Update `.kiro/steering/source-development.md` with generic scale/performance checklist, measure-before-optimize ordering, cohesive ownership principles, and over-engineering guardrails.
  - [ ] 3.3 Update `.kiro/steering/documentation-policy.md` with explicit living-doc versus Issue-specific Spec-history treatment and rationale/chronology separation.
  - [ ] 3.4 Update `.kiro/specs/_templates/design.md` and `.kiro/specs/_templates/requirements.md` only where concise generic wording is needed to consume the updated steering; preserve native-compatible structure.

## Notes

### Progress and resumption

| Task / child | Verified result and evidence | Remaining work / next action |
| --- | --- | --- |
| Spec authoring | `requirements.md`, `design.md`, and `tasks.md` created on `feat/7-generalize-sdd-governance-improvements`. | Publish Draft PR and obtain Independent Spec Review. |

- Current task / child: Task 1 gate pending.
- Incomplete changes and unrun/failed checks: production/template implementation files are intentionally unchanged before authorization; Markdown/native Spec diagnostics not yet recorded.
- Blockers / safe next action: publish the Spec state, then obtain Independent Spec Review before Task 2.

### Validation scope

| Level | Sufficient evidence |
| --- | --- |
| Child / execution slice | Focused Markdown/content/cross-reference inspection for the changed steering/template surface. |
| Parent integration | Check ownership consistency, no duplicated policy, no adopter-specific leakage, and reference integrity across all changed generic files. |
| Final Spec / Issue | Applicable repository Markdown/config checks plus final diff inspection; no adopting-project runtime suite is required for documentation-only behavior. |

### Automated validation

Record actual checks and unavailable diagnostics truthfully. Use already-provisioned tooling only; do not install or acquire packages to run lint.

### Delivery checkpoints

- Owning Issue: `#7`
- Draft PR: `<pending>`
- Task completion / validation evidence and remaining gates: Spec authored; implementation authorization pending.

#### Inter-phase reviews

- [ ] Complete the applicable Requirements review and record revision/outcome.
- [ ] Complete the applicable Design / Invariant review and record revision/outcome.

#### Spec publication and independent approval

- [x] Complete the workflow's required artifact set and native metadata.
- [ ] Validate Spec format, references, task/graph consistency, and applicable Markdown/config checks.
- [ ] Commit/push the Spec on the dedicated branch and create/update the same Draft PR.
- [ ] Request/handle configured supplemental automated review truthfully, including unavailable/quota states.
- [ ] Obtain Independent Spec Review implementation authorization; record revision/outcome and check Task 1 in the same action.

#### Implementation and validation

- [ ] Complete authorized implementation tasks with sufficient evidence.
- [ ] Complete required final automated validation; record commands, revision, results, and justified limitations.
- [ ] Commit/push implementation on the same branch, update the same Draft PR, and complete required supplemental review handling.

#### Independent review and final delivery

- [ ] Independent Code / Requirements Review PASS. <!-- final-review -->
- [ ] Finalize reviewed Spec delivery using the repository helper. <!-- finalize-spec -->

Merge remains an operator/human action unless explicitly delegated.