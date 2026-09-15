# Implementation Plan: `<title>`

## Task Dependency Graph

```json
{
  "waves": [
    { "wave": 1, "tasks": [1] },
    { "wave": 2, "tasks": [2] }
  ]
}
```

## Tasks

- [ ] 1. IMPLEMENTATION-AUTHORIZATION GATE
  - Outcome: Independent Spec Review PASS by a party other than the author, at a recorded revision.
  - Validation: all BLOCKING findings resolved; review evidence recorded.

- [ ] 2. `<reviewable implementation outcome>` — traces to: `<Requirement/AC/invariant>`
  - Outcome: `<combined result and boundaries>`
  - Validation: `<sufficient integration evidence>`
  - [ ] 2.1 `<bounded child outcome>`
    - Depends on: Task 1.
    - Outcome / traces to: `<result and requirement IDs>`
    - Validation: `<focused evidence>`

## Progress and resumption

| Task / child | Verified result and evidence | Remaining work / next action |
| --- | --- | --- |
| `<ID>` |  |  |

- Current task / child: `<ID or none>`
- Incomplete changes / unrun checks: `<state>`
- Blockers / safe next action: `<state>`

## Delivery checkpoints

- Owning Issue: `#<number>`
- Draft PR: `<link>`

### Spec publication and approval

- [ ] Complete required artifacts/native metadata.
- [ ] Validate Spec format/references and applicable Markdown/config checks.
- [ ] Commit/push Spec on dedicated branch and create/update the same Draft PR.
- [ ] Handle configured supplemental automated review truthfully.
- [ ] Obtain Independent Spec Review authorization and check Task 1.

### Implementation and validation

- [ ] Confirm workspace readiness before native task execution when bootstrap is configured.
- [ ] Complete authorized implementation tasks with sufficient evidence.
- [ ] Complete required final automated validation.
- [ ] Commit/push implementation on the same branch and update the same Draft PR.

### Independent review and final delivery

- [ ] Independent Code / Requirements Review PASS. <!-- final-review -->
- [ ] Archive the completed Spec under `docs/spec-archive/<issue-number>-<slug>/` and transition the existing Draft PR to Ready. <!-- finalize-spec -->

Merge remains the operator/human action unless explicitly delegated.