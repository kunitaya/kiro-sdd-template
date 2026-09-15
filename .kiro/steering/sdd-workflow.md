---
inclusion: manual
description: Generic Kiro SDD lifecycle, Direct Change eligibility, workflow selection, review intensity, task design, publication, automated-review handling, and delivery boundaries. Load with #sdd-workflow.
---

# Kiro SDD Workflow

`AGENTS.md` is authoritative for repository-wide policy. This steering file defines the
Kiro-specific lifecycle and must not weaken higher-authority project requirements or
Issue acceptance criteria.

## Lifecycle

All supported Spec entry styles converge on the same implementation and delivery
lifecycle:

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

A Spec reduces ambiguity before implementation; it does not replace independent review
and does not authorize Kiro to self-certify merge readiness.

## Route selection

### Spec route

Use a Spec for substantive design or implementation work. Diff size is not the deciding
factor. Use a Spec whenever implementation must decide or change any material contract,
including requirements, externally observable behavior, state/lifecycle meaning,
identity/provenance, persistence/schema semantics, security boundaries, responsibility
boundaries, or architecture ownership.

### Direct Change route

Direct Change is a non-Spec delivery path only when the correction method is already
fully determined before implementation begins. All of the following must hold:

- no authoritative requirement or Issue acceptance criterion changes;
- no API/CLI/external contract changes;
- no new data-model or persistence semantics are decided;
- no identity/provenance semantics change;
- no state/lifecycle/status meaning changes;
- no security boundary changes;
- no module responsibility/architecture boundary moves;
- implementation is a bounded correction with no unresolved semantic/design question.

Mechanical enforcement of an already-established contract may qualify even when the
diff is large. A one-line semantic change does not qualify merely because it is small.
Resolve uncertainty toward a Spec.

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

If implementation reveals an unresolved design/semantic decision, stop and promote the
change to the appropriate Spec before continuing.

## Kiro workflow selection

Supported entry styles:

- **Requirements-First**: `requirements.md` -> review as required -> `design.md` ->
  design/invariant review as required -> `tasks.md`.
- **Design-First**: `design.md` first, then Kiro-derived `requirements.md`; reconcile
  the derived requirements against authoritative sources/invariants before accepting
  `tasks.md`.
- **Quick Spec**: compact native requirements/design flow when scope is bounded and the
  workflow can safely avoid unnecessary inter-phase stops. Quick does not mean weaker
  authority or no Independent Spec Review.
- **Bugfix**: `bugfix.md` -> applicable bug analysis/review -> `design.md` using the
  native Bugfix design sections -> `tasks.md`.

Always inspect the installed Kiro native templates/diagnostics when revising repository
templates. Repository templates augment native artifacts; they do not invent a shorter
replacement grammar.

## Standard versus Lightweight

Use Standard when the change affects high-risk or materially coupled contracts, or when
implementation would otherwise need to infer substantial design. Lightweight may be
used for bounded lower-risk changes whose material behavior and ownership are already
clear but still benefit from derived requirements/design/tasks.

Lightweight does not waive:

- authoritative-source reconciliation;
- required workspace declaration;
- acceptance criteria/invariants;
- sufficient validation planning;
- Independent Spec Review before implementation;
- Independent Code / Requirements Review after implementation.

## Review-intensity tiers

Review intensity follows semantic risk:

- **Tier 1** — persistence, identity/provenance, security, lifecycle/state,
  correctness/evidence-critical contracts. Use all applicable state, identity,
  NULL/status, structural-enforcement, adversarial, immutability, or reproducibility
  reasoning.
- **Tier 2** — normal features, corrective issues, behavior-preserving refactors. Focus
  on affected requirements, preserved contracts, regression risk, ownership, and
  realistic failure paths.
- **Tier 3** — bounded helper/tooling/operator/documentation work. Use minimum sufficient
  review; do not impose Tier-1 completeness unless the helper can itself create false
  authoritative results or cross a high-risk boundary.

Tier changes depth, not requirement authority or truthfulness standards.

## Spec publication checkpoint

Independent Spec Review must review an actual published repository state, not transient
chat content. Before requesting it:

1. complete the selected workflow's required native artifacts and metadata;
2. validate native Spec format/references/task graph where diagnostics exist;
3. run applicable Markdown/config checks using provisioned tools;
4. record unavailable diagnostics as unavailable rather than PASS;
5. confirm the dedicated non-main branch and intended worktree;
6. commit and push the Spec artifacts;
7. create or update the owning Draft PR; use the same PR for later implementation.

A Draft PR is the reviewable delivery surface. Creating/updating it does not authorize
merge or implementation.

## Automated review

Automated review (for example GitHub Copilot) is supplemental evidence.

- Request it at repository-defined publication checkpoints when configured.
- Retrieve actual findings/state; do not infer a clean review from silence.
- Classify each finding independently against requirements/invariants.
- Correct confirmed BLOCKING findings.
- NON-BLOCKING improvements do not automatically create a correction loop.
- INVALID/out-of-scope suggestions do not change the gate.
- Quota, unavailable service, pending review, or reviewer configuration failure is
  reported truthfully and does not become PASS.
- Automated review never substitutes for required Independent Review or authorizes
  merge.

## Independent Spec Review and authorization

Independent Spec Review asks whether a compliant implementation can be produced without
guessing about material behavior. It checks Issue/requirement coverage, consistency,
feasibility, material correctness/security boundaries, task executability, and
validation planning at the appropriate tier.

Implementation begins only after the independent reviewer explicitly grants PASS at a
recorded revision. `tasks.md` owns the implementation-authorization gate and its durable
state. A Kiro self-check, automated review, hook, or author self-review does not satisfy
an independence requirement.

## Native task execution

Each Spec implementation task is started through Kiro's native Spec Task Execution UI.
Do not use a normal chat instruction to infer/select/start the first unchecked task.
Supplementary chat context is allowed only after the intended task is selected through
the native lifecycle.

The native `tasks.md` task is the outer lifecycle/review boundary. Parent agents may
still decompose internal execution into bounded slices under `#execution-efficiency`.

## Task design rules

A task is a reviewable outcome, not a file list and not necessarily one model call.

- Put implementation and the validation needed for that result together.
- Use child tasks only for material bounded outcomes with independently useful progress
  state; do not create a checkbox for every file/tool call.
- Record real dependencies only. Do not serialize independent work merely to make the
  graph look orderly.
- State external dependencies explicitly; `Run all Tasks` cannot infer another Issue's
  merge or operator gate.
- Do not defer all tests to a final test-only task when earlier outcomes require tests
  to be truthfully complete.
- Keep routine publication/review/archive steps in delivery checkpoints, outside the
  implementation dependency graph.
- Preserve resumable progress/evidence in `tasks.md`; after interruption reconcile it
  against actual files/diff before resuming.

## Validation cadence

Focused validation belongs with the changed outcome. Parent integration validates
cross-child interactions and remaining risks. Repository-wide/full regression belongs
at the final checkpoint when scope/risk or project policy requires it.

Do not mechanically rerun full regression after every slice. Reuse valid evidence while
its code, dependencies, runtime, and tested boundary remain unchanged. Missing/unrun
required validation is a reported gap, not PASS.

## One Issue, one branch, one PR

Normally one change owns one GitHub Issue, one dedicated branch/worktree, and one PR.
The Spec and implementation remain in the same Draft PR so reviewers can follow the
full requirement->design->implementation history without reconciling unrelated PRs.

If the repository deliberately uses a different mapping, document it explicitly and
adapt workspace/delivery tooling without weakening branch/review safety.

## Final reviewed delivery

After Independent Code / Requirements Review PASS and required corrections, final
Spec archival is a **mechanical transition of an already-reviewed state**, not another
opportunity for implementation changes.

Use:

```bash
./scripts/finalize-spec --spec <issue-number>-<slug> --pr <pr-number> \
  --reviewed-commit <full-reviewed-sha> --review-url <independent-pass-url>
```

The helper never decides review approval. The caller supplies the PASS evidence. The
helper fail-closes unless the worktree/index are clean at exactly the reviewed commit,
Git hooks are configured/executable, the owning PR is open/Draft at that commit, the
Spec is complete, ordinary task/review checkpoints are complete, and the archive target
does not already exist.

Only after those checks does it mark the final review/finalization records, archive the
Spec, commit/push the mechanical delivery change, and transition the same PR to Ready.
`--check` is read-only preflight.

Merge into `main` remains the human/operator gate unless explicitly delegated. Review
PASS, Ready state, or a completed finalize helper never implicitly authorizes merge.
