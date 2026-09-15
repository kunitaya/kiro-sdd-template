---
inclusion: manual
description: Independent review procedure, convergence rules, structural/adversarial matrices, and correction review. Load with #review.
---

# Review Procedure

For a substantive initial review:

1. read authoritative sources in repository precedence;
2. identify complete affected requirement/invariant scope;
3. build an explicit invariant checklist;
4. review the resulting system/design, not only changed lines;
5. horizontally inspect materially analogous relationships when a defect pattern appears;
6. attempt realistic invalid/adversarial states for affected high-risk boundaries;
7. complete the planned pass before reporting findings;
8. choose proportionate evidence and stop once sufficient.

Passing tests do not by themselves prove requirement coverage. Conversely, do not require implementation-level proof during Spec review when material semantics are already sufficiently defined.

Before required review corrections, summarize: cause, affected paths, behavior boundary, and verification. Then proceed with the authorized correction without adding a new approval gate.

Before the first PASS, correction review verifies prior BLOCKING findings and affected invariants. After PASS, use delta re-review unless a material contract/requirement/security/state/identity premise changed or a new confirmed BLOCKING defect invalidates the prior exit criteria.

For changes involving state, identity/provenance, persistence/schema, NULL/status, security, immutability, or similar high-risk contracts, apply the applicable matrices:

- requirement inventory;
- invariant inventory;
- state-transition matrix;
- identity/provenance matrix;
- NULL/status matrix;
- structural-enforcement matrix;
- adversarial counterexample matrix.

Executable validation must test the actual final design/implementation rather than a hand-written simplified stand-in when behavior proof is required.