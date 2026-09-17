---
inclusion: manual
description: Generic Kiro SDD lifecycle, Direct Change eligibility, workflow selection, review intensity, task design, publication, automated-review handling, and delivery boundaries. Load with #sdd-workflow.
---

# Kiro SDD Workflow

`AGENTS.md` is authoritative for repository-wide policy. This steering file defines the Kiro-specific lifecycle and must not weaken higher-authority project requirements or Issue acceptance criteria.

## Lifecycle

All supported Spec entry styles converge on the same downstream lifecycle:

```text
Authoritative requirements + GitHub Issue + AGENTS.md
    ↓
Route / workflow selection
    ↓
Native first artifact(s)
    ↓
Required inter-phase review / reconciliation
    ↓
tasks.md
    ↓
Spec format/reference/config validation
    ↓
Spec publication: commit + push + same Draft PR
    ↓
Supplemental automated review, if configured/available
    ↓
Independent Spec Review
    ↓
Implementation authorization
    ↓
Native Kiro Spec Task Execution per tasks.md task
    ↓
Implementation + focused validation per task
    ↓
Final automated validation
    ↓
Implementation publication to the same Draft PR
    ↓
Supplemental automated re-review, if configured/available
    ↓
Independent Code / Requirements Review
    ↓
Required corrections + delta re-review
    ↓
Fail-closed reviewed mechanical Spec delivery
    ↓
Archive active Spec + Draft PR Ready
    ↓
HUMAN MERGE GATE
```

A Spec reduces ambiguity before implementation; it does not replace independent review and does not authorize Kiro to self-certify merge readiness.

## Route selection

### Spec route

Use a Spec for substantive design or implementation work. Diff size is not decisive. Use a Spec whenever implementation must decide or change a material contract, including requirements, externally observable behavior, state/lifecycle meaning, identity/provenance, persistence/schema semantics, security boundaries, responsibility boundaries, or architecture ownership.

### Direct Change route

Direct Change is a non-Spec path only when the correction method is fully determined before implementation. All must hold:

- no authoritative requirement or Issue acceptance criterion changes;
- no API/CLI/external contract changes;
- no new data-model/persistence semantics are decided;
- no identity/provenance or state/lifecycle/status semantics change;
- no security or architecture/responsibility boundary changes;
- implementation is bounded with no unresolved semantic/design question.

Mechanical enforcement of an already-established contract may qualify even when the diff is large. A one-line semantic change does not qualify merely because it is small. Resolve uncertainty toward a Spec.

Direct Change lifecycle:

```text
GitHub Issue
    ↓
Implementation + risk-based validation
    ↓
Commit / push dedicated branch
    ↓
Create Draft PR
    ↓
Supplemental automated review if configured
    ↓
Independent Code / Requirements Review
    ↓
Required fixes / delta review
    ↓
Draft PR Ready
    ↓
Human merge
```

If implementation reveals an unresolved design/semantic decision, stop and promote the change to the appropriate Spec before continuing.

## Kiro workflow selection

- **Requirements-First**: `requirements.md` -> required requirements review -> `design.md` -> required design/invariant review -> `tasks.md`.
- **Design-First**: `design.md` first, then Kiro-derived `requirements.md`; reconcile derived requirements against authoritative sources/invariants before accepting `tasks.md`.
- **Quick Spec**: compact native requirements/design flow for bounded scope. It normally has no separate inter-phase stop, but Standard-risk Quick Specs reconcile requirements and design/invariants inside Independent Spec Review.
- **Bugfix**: `bugfix.md` -> applicable bug analysis/review -> `design.md` using the Bugfix design structure -> `tasks.md`.

A complex or high-risk defect remains a Bugfix Spec; increase review tier/intensity rather than changing workflow merely because the correction is difficult.

Always inspect installed Kiro native templates/diagnostics when revising repository templates. Repository templates augment native artifacts; they do not invent a replacement grammar.

## Standard versus Lightweight

Use Standard when the change affects high-risk/materially coupled contracts or implementation would otherwise infer substantial design. Lightweight may be used for bounded lower-risk changes whose material behavior/ownership are already clear.

Lightweight does not waive authoritative-source reconciliation, workspace declaration, acceptance criteria/invariants, sufficient validation planning, Independent Spec Review, or Independent Code / Requirements Review.

## Review-intensity tiers

- **Tier 1** — persistence, identity/provenance, security, lifecycle/state, correctness/evidence-critical contracts. Use all applicable state, identity, NULL/status, structural-enforcement, adversarial, immutability, or reproducibility reasoning.
- **Tier 2** — normal features, corrective issues, behavior-preserving refactors. Focus on affected requirements, preserved contracts, regression risk, ownership, and realistic failure paths.
- **Tier 3** — bounded helper/tooling/operator/documentation work. Use minimum sufficient review; do not impose Tier-1 completeness unless the work crosses a high-risk boundary.

Tier changes depth, not requirement authority or truthfulness standards.

## Lifecycle-gate state and `tasks.md`

`tasks.md` is the durable progress/gate record consumed by native execution. When a lifecycle gate actually changes state, update the corresponding checkbox/checkpoint in the same action that records the new state.

Examples:

- Independent Spec Review PASS and implementation-authorization checkbox must agree;
- Spec/implementation publication checkpoints are checked only after GitHub state is actually published/verified;
- final review/finalization markers represent their real completed state, not an intention to perform them.

Do not leave a gate unchecked after it has actually passed or pre-check a gate that has not happened. Native automation may treat the checkbox literally.

## Spec publication checkpoint

Independent Spec Review must review an actual published repository state, not transient chat content. Before requesting it:

1. complete the selected workflow's required native artifacts/metadata;
2. complete required inter-phase review/reconciliation;
3. validate native Spec format/references/task graph where diagnostics exist;
4. run applicable Markdown/config checks using provisioned tools;
5. record unavailable diagnostics as unavailable rather than PASS;
6. confirm the dedicated non-main branch/worktree;
7. commit and push the Spec artifacts;
8. create or update the owning Draft PR and verify the published state.

The Draft PR is the reviewable delivery surface. The owning PR should include the repository's normal Issue linkage/closing keyword. Do not add closing keywords for merely related Issues unless that PR fully satisfies their closure criteria.

Creating/updating the PR does not authorize implementation or merge.

## Automated review

Automated review (for example GitHub Copilot) is supplemental evidence. Distinguish:

1. **pending** — review has not completed for the current relevant revision;
2. **completed** — review completed, with zero or more findings;
3. **unavailable** — quota/service/configuration prevents the review itself from running.

Do not infer a clean completed review from silence. Pending and unavailable are not PASS.

Classify completed findings independently against requirements/invariants. Correct confirmed BLOCKING findings; NON-BLOCKING improvements do not automatically create a correction loop; INVALID/out-of-scope suggestions do not change the gate.

If a repository defines a fallback supplemental reviewer for the unavailable state, it may be used at the same authority level as the automated reviewer it replaces. The fallback remains supplemental and never substitutes for Independent Review or authorizes merge. Stop using the fallback once the normal reviewer becomes available again.

## Independent Spec Review and authorization

Independent Spec Review asks whether a compliant implementation can be produced without guessing about material behavior. It checks Issue/requirement coverage, consistency, feasibility, material correctness/security boundaries, task executability, and validation planning at the appropriate tier.

Implementation begins only after an independent reviewer explicitly grants PASS at a recorded revision. `tasks.md` owns the implementation-authorization gate and must be synchronized with that decision. Self-checks, automated reviews, hooks, or author self-review do not satisfy independence.

## Native task execution

Each Spec implementation task is started through Kiro's native Spec Task Execution UI. Do not use normal chat to infer/select/start the first unchecked task. Supplementary chat context is allowed after the intended task is selected natively.

The native `tasks.md` task is the outer lifecycle/review boundary. Internal bounded slices/delegation remain allowed under `#execution-efficiency`.

## Task design rules

A task is a reviewable outcome, not a file list and not necessarily one model call.

- Put implementation and necessary validation together.
- Use child tasks only for material bounded outcomes with useful independent progress state.
- Record real dependencies only; do not serialize independent work for appearance.
- State external dependencies explicitly on every task/child whose execution depends on them; `Run all Tasks` cannot infer another Issue merge/operator gate.
- Do not run automatic task execution across an unsatisfied external dependency.
- If native execution cannot honor a child dependency, execute affected children individually in the declared order.
- Do not defer all tests to a final test-only task when earlier outcomes need tests to be truthfully complete.
- Keep routine publication/review/archive steps in delivery checkpoints, outside the implementation dependency graph.
- Preserve resumable progress/evidence in `tasks.md`; after interruption reconcile it against actual files/diff before resuming.

## Validation cadence

Focused validation belongs with the changed outcome. Parent integration validates cross-child interactions and remaining risks. Repository-wide/full regression belongs at the final checkpoint when scope/risk or project policy requires it.

Do not mechanically rerun full regression after every slice. Reuse valid evidence while code, dependencies, runtime, and tested boundary remain unchanged. Record the revision that produced reused evidence; never imply it ran at a newer revision. Missing/unrun required validation is a reported gap, not PASS.

## One Issue, one branch, one PR

Normally one change owns one GitHub Issue, one dedicated branch/worktree, and one PR. Spec and implementation remain in the same Draft PR so reviewers can follow requirement -> design -> implementation history.

If the repository deliberately uses another mapping, document it explicitly without weakening branch/review safety.

## Final reviewed delivery

After Independent Code / Requirements Review PASS and required corrections, Spec archival is a mechanical transition of an already-reviewed state, not an opportunity for new implementation changes.

Use:

```bash
./scripts/finalize-spec --spec <issue-number>-<slug> --pr <pr-number> \
  --reviewed-commit <full-reviewed-sha> --review-url <independent-pass-url>
```

The helper never decides review approval. It fail-closes unless reviewed state, branch/PR state, required checkboxes, Git safety controls, and archive/Ready ordering are satisfied. `--check` is read-only preflight.

A final-review checkbox may be recorded mechanically after PASS when repository policy explicitly allows that marker-only update; such recording does not alter the reviewed implementation. Keep exactly the marker/checkpoint shape expected by the repository helper rather than duplicating final-review/finalization steps.

The finalization helper is outside native implementation task execution: do not run it via `Start Task` / `Run all Tasks`, and do not recreate the active Spec after it archives the Spec. On a fail-closed finalization error, fix the reported prerequisite and rerun the same operation; do not bypass it with force/reset or a manual partial imitation of the archive/Ready sequence.

Merge into `main` remains the human/operator gate unless explicitly delegated. Review PASS, Ready state, or successful finalization never implicitly authorizes merge.