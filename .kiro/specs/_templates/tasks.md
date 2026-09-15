# Implementation Plan: `<title>`

## Overview

Each task describes a reviewable outcome with sufficient validation. Do not split work
merely by file or defer tests for earlier logic into a final test-only task. Use parent
tasks for substantial outcomes and numbered child checkboxes for bounded, verifiable
progress when useful. Keep low-level execution mechanics in the executor plan; durable
completion/resumption state belongs here.

Apply `#execution-efficiency` when recording dependencies, parallel candidates,
serialization constraints, resumption, and validation cadence.

## Task Dependency Graph

State only real dependencies. Tasks in the same wave may start independently. External
dependencies (for example, another Issue merging first) are written on the affected task
because `Run all Tasks` cannot infer them.

```json
{
  "waves": [
    { "wave": 1, "tasks": [1] },
    { "wave": 2, "tasks": [2] }
  ]
}
```

Confirm instantiated task/graph recognition with the installed Kiro diagnostics before
accepting the plan. If native execution cannot honor a child dependency, start those
children individually in the declared order rather than running across the boundary.

## Tasks

- [ ] 1. IMPLEMENTATION-AUTHORIZATION GATE
  - Outcome: Independent Spec Review PASS by a party other than the authoring agent,
    explicitly authorizing implementation at a recorded revision.
  - Validation: record the independent review link, revision, and outcome; resolve all
    BLOCKING findings. Supplemental automated review does not satisfy this gate.
  - Update this checkbox and the authorization delivery checkpoint together when the
    actual approval is recorded. Do not self-complete the gate or start implementation
    while it is unchecked.

- [ ] 2. `<reviewable implementation outcome>` — traces to: `<Requirement N.M / Bugfix 2.x or 3.x / invariant>`
  - Outcome: `<combined result and material boundaries>`
  - Validation: `<sufficient integration evidence; reuse valid child evidence>`
  - [ ] 2.1 `<first bounded outcome>`
    - Depends on: Task 1.
    - Outcome / traces to: `<observable result and requirement/invariant>`
    - Validation: `<focused evidence sufficient to accept this result>`
  - [ ] 2.2 `<next bounded outcome>`
    - Depends on: 2.1 `<replace with actual dependency>`.
    - Outcome / traces to: `<observable result and requirement/invariant>`
    - Validation: `<focused evidence including preserved behavior>`

Replace/add/remove children to match the actual design. Check a child only after its
result is verified; check the parent only after required children and parent integration
validation are complete.

## Notes

For Bugfix Specs, preserve traceability from reproduction through the fix to Expected
and Unchanged Behavior evidence. Include negative/adversarial, persistence,
confidentiality, concurrency, or lifecycle checks when those risks are actually
affected; do not fabricate categories merely to fill the template.

### Progress and resumption

Keep this record concise and omit unused placeholder rows.

| Task / child | Verified result and evidence | Remaining work / next action |
| --- | --- | --- |
| `<ID>` | `<result; check/result and revision or change state>` | `<next bounded action or none>` |

- Current task / child: `<ID or none>`
- Incomplete changes and unrun/failed checks: `<concise state or none>`
- Blockers / safe next action: `<dependency or next action>`

After interruption, inspect actual files/diff and evidence before reconciling this
record. Preserve valid completed work and rerun only invalidated or missing checks.

### Validation scope

| Level | Sufficient evidence |
| --- | --- |
| Child / execution slice | Minimum focused checks for the changed result and directly affected contracts/invariants. |
| Parent integration | Cross-child interactions and remaining integration risks; reuse valid child evidence. |
| Final Spec / Issue | Required overall gates and full regression where scope/risk requires it. |

### Automated validation

Record checks actually run, results, still-valid evidence reused, and remaining gates.
Unavailable diagnostics or tools remain explicitly unverified; they are not PASS.
Update project traceability when the adopting repository requires it.

### Delivery checkpoints

Routine delivery checkpoints are not numbered implementation tasks and do not enter the
Task Dependency Graph. Check items only when actually completed and record concise
revision/evidence links.

- Owning Issue: `#<number>`
- Draft PR: `<link; the PR must link/close the owning Issue according to repository policy>`
- Task completion / validation evidence and remaining gates: `<concise record or links>`

#### Inter-phase reviews

Retain only the review stops required by the selected workflow. Quick Spec normally
omits separate requirements/design stops; any reconciliation required by repository
policy is recorded at Independent Spec Review.

- [ ] Complete the applicable Requirements / Bug Analysis review and record revision/outcome.
- [ ] Complete the applicable Design / Invariant review and any Design-First reconciliation.

#### Spec publication and independent approval

- [ ] Complete the workflow's required artifact set and native metadata.
- [ ] Validate Spec format, references, task/graph consistency, and applicable Markdown/config checks.
- [ ] Commit/push the Spec on the dedicated branch and create/update the same Draft PR.
- [ ] Request/handle configured supplemental automated review truthfully, including unavailable/quota states.
- [ ] Obtain Independent Spec Review implementation authorization; record revision/outcome and check Task 1 in the same action.

#### Implementation and validation

- [ ] Confirm the owning workspace is READY before native task execution when bootstrap is configured.
- [ ] Complete authorized implementation tasks with sufficient evidence.
- [ ] Complete required final automated validation; record commands, revision, results, and justified limitations.
- [ ] Commit/push implementation on the same branch, update the same Draft PR, and complete required supplemental review handling.

#### Independent review and final delivery

- [ ] Independent Code / Requirements Review PASS. <!-- final-review -->
- [ ] Finalize reviewed Spec delivery using the repository helper. <!-- finalize-spec -->

The final review must be performed by a party other than the implementing agent when
repository policy requires independence. Resolve confirmed BLOCKING findings and obtain
any required delta re-review before recording PASS.

After final review, use the full reviewed commit SHA and the PASS record URL. Do not
infer approval from this checkbox. From the owning repository root:

```bash
./scripts/finalize-spec --spec <issue-number>-<slug> --pr <pr-number> \
  --reviewed-commit <full-reviewed-sha> --review-url <independent-pass-url>
```

`--check` performs read-only preflight. The helper must fail closed if review evidence,
branch/PR state, completion checkboxes, clean reviewed state, Git safety controls, or
archive/Ready ordering are not satisfied. It performs only the reviewed mechanical
delivery transition; it never decides that a review passed.

Merge remains an operator/human action unless explicitly delegated.
