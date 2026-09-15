---
inclusion: fileMatch
fileMatchPattern: "tests/**"
description: Generic test planning and validation guidance.
---

# Test Development

Tests prove affected requirements/invariants and preserve relevant existing behavior. Add the minimum evidence needed to detect the defect or establish the new contract.

Prefer focused unit/integration tests during implementation. Use broader regression at the final checkpoint when required by risk/scope. Include boundary, failure, rerun/concurrency, persistence, or adversarial cases when those semantics are materially affected.

Do not make tests encode an implementation accident as a new requirement. Do not weaken requirements to keep existing tests green. If a required test/tool cannot run, report the limitation and the unverified claim truthfully.