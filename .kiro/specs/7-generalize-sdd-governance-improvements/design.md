# Spec Design: `Generalize recent SDD governance improvements from production use`

## Overview

This change updates the generic SDD template by moving reusable process knowledge from a production-adopting repository into the existing generic owners. It intentionally does not mirror production files. The design keeps each rule in the narrowest existing owner and updates artifact templates only where they must expose or consume that rule.

## Architecture

### Approach

Use the existing policy layering:

```text
AGENTS.md
  -> repository-wide generic authority and routing
.kiro/steering/*.md
  -> reusable scoped/on-demand operational detail
.kiro/specs/_templates/*.md
  -> native-compatible artifact scaffolds that reference steering
/templates/kiro-task-prompt.md
  -> reusable bounded prompt surface
```

Do not expand `AGENTS.md` unless a new repository-wide rule cannot be owned safely by an existing steering file. For this Issue, all new detail fits existing steering/template owners, so `AGENTS.md` remains unchanged.

### Responsibility mapping

| Concern | Owner |
| --- | --- |
| Durable execution slices, parent responsibility, stalls, resumption, validation cadence | `.kiro/steering/execution-efficiency.md` |
| Bounded prompt fields, targeted lookup, guidance-load preflight | `.kiro/steering/task-prompt.md` |
| Reusable prompt scaffold | `templates/kiro-task-prompt.md` |
| Lifecycle/gate synchronization, external dependencies, automated review states | `.kiro/steering/sdd-workflow.md` |
| Task progress/delivery state | `.kiro/specs/_templates/tasks.md` |
| Test/evidence reuse boundaries | `.kiro/steering/test-development.md` |
| Bugfix workflow semantics | `.kiro/specs/_templates/bugfix.md` |
| Review convergence, data-model/reproducibility checks | `.kiro/steering/review.md` |
| Generic scale/design principles | `.kiro/steering/source-development.md` |
| Living-doc vs Spec-history behavior | `.kiro/steering/documentation-policy.md` |
| Design/requirements native scaffolding | `.kiro/specs/_templates/design.md`, `.kiro/specs/_templates/requirements.md` |

No mandatory generic PostTaskExec lint hook is added because the production hook encodes Python/project-specific commands.

## Components and Interfaces

No source-code API or product interface changes are introduced. The changed interfaces are development-process contracts consumed by Kiro/agents and humans:

- steering guidance contracts;
- Spec artifact templates;
- reusable task-prompt template.

The existing `#name` guidance-routing contract remains unchanged.

## Data Models

Not applicable — no persistence/schema model is changed.

## Correctness Properties

### Property 1: Execution work can resume without replaying valid completed slices

**Validates: Requirements 1.1, 1.2, 1.3, 1.4, 1.5**

Durable task state plus actual file/diff/evidence inspection must determine resumption. Parent agents retain integration authority and do not replay verified child work merely because the parent checkbox remains incomplete.

### Property 2: Validation scope matches execution scope

**Validates: Requirements 1.5, 1.6, 1.7, 2.1, 4.1, 4.2, 4.3, 4.4**

A child/slice receives focused validation; parent integration adds cross-slice evidence; final gates run broad checks where required. Evidence reuse remains revision-truthful and never converts an unavailable check into PASS.

### Property 3: Lifecycle state is synchronized and cannot cross unsatisfied external gates

**Validates: Requirements 3.1, 3.2, 3.3, 3.4, 3.5, 3.6, 3.7**

`tasks.md` remains the durable lifecycle state owner. Actual approval/publication changes update its corresponding checkpoint state in the same action. External gates are represented explicitly rather than encoded as artificial task ordering.

### Property 4: Workflow kind is not inferred from risk alone

**Validates: Requirements 5.1, 5.2, 5.3**

A defect remains a Bugfix workflow even when Tier 1 / Standard review is warranted. Risk controls review depth, not the semantic entry workflow.

### Property 5: Genericization does not import adopter-specific policy

**Validates: Requirements 6.1, 6.2, 6.3, 6.4, 6.5, 6.6, 6.7**

New text must express reusable process behavior without mailbox/PII/forensic domain assumptions, Python-only commands, production repository IDs, or chronological operational evidence.

#### Adversarial counterexample matrix

| Attempted invalid state | Why it must be impossible | How it is refused |
| --- | --- | --- |
| Child prompt requests full repository regression by default | Recreates unnecessary cost and execution-limit risk | Execution-efficiency/task-prompt guidance requires focused child validation unless concrete risk justifies full suite. |
| Parent reports old full-suite evidence as run at new SHA | Misrepresents validation evidence | Test-development requires recording original revision/context for reused evidence. |
| External Issue merge is encoded only as task ordering | `Run all Tasks` may cross a gate it cannot observe | SDD workflow/tasks template requires explicit external dependency and stop boundary. |
| High-risk defect is converted to Feature Spec only because it is high-risk | Changes workflow semantics and loses Bugfix Current/Expected/Unchanged contract | Bugfix guidance separates workflow type from review tier. |
| Production Python lint hook becomes mandatory template behavior | Breaks portability | Explicit non-goal; hook remains project-specific. |
| Generic docs narrate production Issue chronology | Bloats template and embeds adopter history | Documentation policy keeps reusable docs current-state/rationale oriented. |

## Error Handling

Policy/tooling limitations remain explicit:

- missing/unavailable validation is reported, not PASS;
- unavailable supplemental automated review is reported as unavailable and does not satisfy independent review;
- interrupted/denied delegation leaves affected state unverified until actual files/diff are inspected;
- missing required guidance load is a stop condition for a bounded task prompt.

## Testing Strategy

### Stage-appropriate validation plan / evidence

This is documentation/governance work. Validation should establish internal cross-reference and Markdown correctness rather than run adopting-project source tests.

Minimum sufficient evidence:

1. inspect final changed files for consistent ownership and no project-specific leakage;
2. run repository Markdown/config checks with already-provisioned tools when available;
3. verify required referenced files/headings/markers exist through direct inspection/search;
4. inspect final diff for unintended `AGENTS.md`, hook, permission, or runtime-specific changes.

Stop once the artifact set is internally consistent, applicable lint/checks pass or unavailable checks are truthfully recorded, and no BLOCKING policy contradiction remains.

### Unit Tests

Not applicable — no executable library behavior is changed.

### Property-Based Tests

Not applicable — no data-processing implementation is changed.

### Integration / Runtime Tests

Use static/document validation only for this Issue. Do not require Kiro product-runtime certification for these text changes unless a concrete changed rule depends on undocumented runtime behavior.

## Documentation Impact

The changed steering and templates are themselves the documentation impact. README updates are needed only if a user-facing repository capability or setup step changes; no such new capability is introduced here.