---
inclusion: fileMatch
fileMatchPattern: "src/**"
description: Generic source-code design and implementation guidance.
---

# Source Development

Implement the smallest change that fully satisfies the task. Inspect existing ownership boundaries and reuse established mechanisms before creating a second path for the same responsibility.

Preserve public/internal contracts and non-functional constraints that the authoritative requirements define. Treat performance, determinism, idempotency, concurrency, confidentiality, and failure behavior as design constraints when they are part of the affected contract.

For optimization, measure first when practical, identify the actual bottleneck, and preserve correctness while improving it. Avoid speculative generalized infrastructure.

Prefer cohesive responsibilities, explicit boundaries, dependency direction, and substitutable abstractions where they materially reduce coupling or duplicated logic; do not perform architecture cleanup unrelated to the task.