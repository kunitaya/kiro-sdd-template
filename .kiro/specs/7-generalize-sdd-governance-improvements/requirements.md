# Requirements Document

## Introduction

**Spec:** `Generalize recent SDD governance improvements from production use`

```text
STRICT WORKSPACE ISOLATION

This spec belongs exclusively to the workspace root containing this file
(resolved at runtime via `git rev-parse --show-toplevel`; see
.kiro/steering/workspace-isolation.md).

Repository: kiro-sdd-template
GitHub Issue: #7
Branch: feat/7-generalize-sdd-governance-improvements
Allowed modification scope: repository-wide within this root
Prohibited cross-root operations:
- edit files in another workspace root
- run repository-changing commands against another root
- use another worktree's uncommitted state as implementation truth
- copy uncommitted changes between worktrees

The main root may be referenced only for baseline comparison unless
explicitly authorized by this spec.
```

## Source

- GitHub Issue: `#7` — `Generalize recent SDD governance improvements from production use`
- Driving authoritative requirement IDs: none — reusable development-process governance
- Reference implementation source: current `koseikensetsu/mailbox-privacy-analyzer` main process/steering/template behavior, generalized rather than copied verbatim

## Glossary

- **production-derived improvement**: reusable process knowledge observed in an adopting repository and suitable for genericization without importing domain-specific requirements or runtime assumptions.
- **execution slice**: an internal bounded unit used to carry out an already-approved task without becoming a separate lifecycle gate.
- **evidence reuse**: reuse of still-valid validation/review evidence when its code, dependency, runtime, and contract assumptions remain unchanged.

## Change type / Spec tier

- [ ] Tier 1 — persistence / identity / security / lifecycle / correctness-critical
- [x] Tier 2 — normal feature / corrective issue / behavior-preserving refactor
- [ ] Tier 3 — helper / operator utility / bounded verification / documentation

Spec kind: [x] Standard  [ ] Lightweight

## Requirements

### Requirement 1: Generalize execution and delegation efficiency

**User Story:** As a maintainer, I want reusable execution guidance to preserve durable progress and bounded validation, so that interrupted or delegated work can resume without repeated repository discovery or unnecessary full-suite work.

#### Acceptance Criteria

1. THE template SHALL define parent ownership of repository-level understanding, decomposition, integration, and final task truthfulness.
2. THE template SHALL distinguish reviewable `tasks.md` outcomes from internal execution slices and SHALL keep material resumable progress in durable task state.
3. AFTER interruption or delegation failure, THE template SHALL require inspection of actual files/diff/evidence before resuming or reporting completion.
4. AFTER a stalled oversized invocation, THE template SHALL require re-planning or scope/context reduction before repeated retries unless the operation is already small and bounded with a concrete transient-failure reason.
5. THE template SHALL define validation scope by execution level: focused slice/child evidence, parent integration evidence, and final repository/Issue gates where required.
6. Delegated slice prompts SHALL NOT request repository-wide/full regression unless a concrete risk makes focused validation insufficient.
7. WHEN a delegated slice must run an expensive long-running check, THE template SHALL preserve already-focused-verified work before that check where the adopting repository's publication rules permit it.

### Requirement 2: Make task prompts explicit, bounded, and lookup-efficient

**User Story:** As a parent agent, I want task prompts to carry only task-specific facts and explicit validation scope, so that subagents do not waste context rediscovering policy or expand work without a concrete reason.

#### Acceptance Criteria

1. The standard task-prompt contract SHALL include an explicit `validation scope` field separate from acceptance criteria.
2. The prompt contract SHALL reference applicable guidance by name rather than copying large policy bodies.
3. The template SHALL define targeted lookup first and expansion only after a concrete dependency, adjacent invariant, or review finding establishes the need.
4. The template SHALL require bounded preflight confirmation that named guidance was loaded, without requiring the agent to restate that guidance.
5. The task-prompt template SHALL preserve the rule that native Spec implementation tasks are selected through Kiro's native Spec Task Execution before supplemental prompt context is applied.

### Requirement 3: Strengthen lifecycle, external-gate, and delivery-state semantics

**User Story:** As an operator, I want the SDD lifecycle and `tasks.md` state to represent the actual gate state, so that native execution does not run past unsatisfied approvals or remain blocked by stale bookkeeping.

#### Acceptance Criteria

1. WHEN a lifecycle gate changes state, the template SHALL require its authoritative `tasks.md` checkbox/checkpoint state to be updated in the same action.
2. The template SHALL distinguish internal task dependencies from external dependencies such as another Issue/PR merge and SHALL prevent automatic execution from crossing an unsatisfied external gate.
3. Spec publication SHALL mean a reviewable published branch/Draft-PR state, not only locally complete files.
4. The owning PR SHALL preserve owning-Issue linkage while related Issues SHALL NOT be closed merely because they are dependencies.
5. Supplemental automated review SHALL distinguish pending, completed, and unavailable/quota states; unavailable review SHALL NOT be reported as PASS.
6. The template SHALL preserve one Issue/branch/PR lifecycle and the human merge boundary.
7. Final reviewed Spec delivery SHALL remain a mechanical transition using supplied review evidence, not a self-approval mechanism.

### Requirement 4: Strengthen validation cadence and evidence reuse

**User Story:** As a reviewer or implementer, I want validation requirements to reuse still-valid evidence and distinguish focused from final checks, so that development remains efficient without overstating what was run at a new revision.

#### Acceptance Criteria

1. Test guidance SHALL distinguish child/slice, parent integration, final Issue/Spec, and correction/delta validation scopes.
2. Previously valid full-suite or expensive evidence MAY be reused only for surfaces whose assumptions remain unchanged.
3. Reused evidence SHALL retain the original revision/context; the template SHALL forbid describing an older full-suite run as newly executed at a later SHA.
4. Required unavailable validation SHALL remain explicitly unverified rather than silently waived or reported as PASS.

### Requirement 5: Keep Bugfix workflow type separate from review intensity

**User Story:** As a maintainer, I want complex defects to remain Bugfix Specs while review intensity increases independently, so that workflow semantics are not distorted merely because a defect is high-risk.

#### Acceptance Criteria

1. A complex, critical-path, or costly-regression defect SHALL remain in Bugfix workflow when the task is defect correction; review tier/Spec kind SHALL carry the increased rigor.
2. Bugfix artifacts SHALL preserve numbered Current (`1.x`), Expected (`2.x`), and Unchanged (`3.x`) behavior as binding references.
3. Reproduction/evidence status SHALL be explicit before design proceeds; an unrun reproduction SHALL NOT be represented as confirmed behavior.

### Requirement 6: Selectively genericize review, source-development, and documentation knowledge

**User Story:** As a template adopter, I want broadly reusable high-value guidance without mailbox-specific policy, so that the template improves while remaining compact and portable.

#### Acceptance Criteria

1. Review guidance SHALL discourage repeated equivalent re-verification after a claim has sufficient unchanged primary evidence.
2. Review guidance SHALL include applicability-scoped data-model and reproducibility checks for changes that affect persistence, identity, hashing/canonicalization, or comparable contracts.
3. Source-development guidance SHALL include generic scale/performance checks for complexity, memory, repeated I/O/work, transaction/access patterns, resource lifetime, bounded processing, rerun/resume, observability, and volume-related security where materially applicable.
4. Source-development guidance SHALL preserve cohesive ownership and SRP/OCP/DRY/DIP principles while explicitly avoiding speculative abstraction.
5. Documentation guidance SHALL distinguish reusable living documentation from Issue-specific Spec execution history and SHALL preserve rationale while removing unnecessary chronology.
6. Design and requirements templates SHALL remain native-compatible and SHALL include only concise generic clarifications needed by these policies.
7. The change SHALL NOT import mailbox-specific product requirements, PII/forensic domain rules, Python-only mandatory commands, or production-specific historical evidence into the generic template.

## Requirement Source Traceability

| Kiro Requirement / AC | Governing source | Notes |
| --- | --- | --- |
| Requirement 1 | Issue #7 scope 1; production-derived `execution-efficiency.md` behavior | Generalize durable progress, parent responsibility, stall handling, and validation cadence. |
| Requirement 2 | Issue #7 scope 1; production-derived `task-prompt.md` behavior | Add explicit validation scope, targeted lookup, and bounded guidance-load preflight. |
| Requirement 3 | Issue #7 scope 1; production-derived `sdd-workflow.md` and `tasks.md` behavior | Keep lifecycle state truthful and external gates explicit. |
| Requirement 4 | Issue #7 scope 1; production-derived `test-development.md` behavior | Reuse still-valid evidence without misreporting execution at a later revision. |
| Requirement 5 | Issue #7 scope 1; production-derived Bugfix workflow behavior | Workflow kind and review intensity remain orthogonal. |
| Requirement 6 | Issue #7 scope 2 | Selective genericization only; preserve template portability. |

## Invariant inventory

| # | Invariant | Why it matters | Currently enforced by |
| --- | --- | --- | --- |
| 1 | The template remains generic rather than adopting one project's product/security/runtime rules. | Portability is the repository's purpose. | `AGENTS.md` Purpose/authority boundary and Issue #7 non-goals. |
| 2 | Independent review and human merge authority are not weakened. | Process improvements must not become self-approval. | `AGENTS.md`, `#sdd-workflow`. |
| 3 | Kiro native artifact/task lifecycle remains the outer execution boundary. | Genericization must not replace native Spec semantics with custom chat-only workflow. | `#spec-task-execution`, `.kiro/specs/README.md`. |
| 4 | Validation efficiency never turns missing evidence into PASS. | Evidence reuse is safe only when assumptions remain valid and limitations stay explicit. | `AGENTS.md` Verification proportionality and `#review`. |
| 5 | Policy ownership stays centralized; templates reference steering instead of duplicating full rules. | Prevents drift and unnecessary context. | `AGENTS.md` Guidance routing and current template design. |

## Out of scope

- Mirroring `mailbox-privacy-analyzer` files verbatim.
- Importing mailbox/PII/forensic requirements or security rules.
- Adding Python-specific lint commands or the production repository's PostTaskExec hook as mandatory generic behavior.
- Replacing template repository authority or merge policy.
- Reworking workspace isolation or native task execution where current generic behavior already captures the reusable contract.
- Synchronizing implementation helper scripts solely by file size/version; script behavior requires its own concrete comparison if later changed.

## Open questions / conflicts

No material conflict was found between Issue #7 and current template policy. The main design constraint is to preserve compact generic ownership while adding the production-derived behavior above.