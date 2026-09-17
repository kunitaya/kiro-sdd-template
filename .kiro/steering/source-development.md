---
inclusion: fileMatch
fileMatchPattern: "src/**"
description: Generic source-code design, scale/performance, and implementation guidance.
---

# Source Development

Implement the smallest coherent change that fully satisfies the task. Inspect existing ownership boundaries and reuse established mechanisms before creating a second path for the same responsibility.

Preserve public/internal contracts and non-functional constraints that authoritative requirements define. Treat performance, determinism, idempotency, concurrency, confidentiality, failure behavior, and recoverability as design constraints when they are part of the affected contract.

## Scale and performance checklist

Before changing an architecture or processing boundary where workload size can matter, consider the applicable items:

- avoidable O(N²) or repeated whole-set scans;
- unbounded whole-input materialization or memory growth;
- repeated I/O, hashing, parsing, normalization, serialization, or traversal;
- database transaction/access patterns at realistic row counts;
- resource lifetime for files, handles, native objects, workers, and temporary artifacts;
- whether batching, streaming, bounded queues, or later parallelism can be added without redesigning the API;
- rerun/resume and failure isolation at scale;
- observability needed to identify actual bottlenecks; and
- security/confidentiality effects of high-volume logging or temporary data.

Do not defer a structural bottleneck merely by saying it can be optimized later when the chosen API/data model would force a redesign. Equally, do not introduce multiprocessing, async pipelines, native extensions, distributed processing, or generalized infrastructure without evidence that the workload needs them.

Preferred optimization order:

1. sound algorithms, data structures, ownership, and I/O boundaries;
2. remove structural bottlenecks and unnecessary repeated work;
3. measure representative workloads;
4. optimize measured bottlenecks with batching/concurrency where justified;
5. consider micro-optimization or native acceleration only after profiling.

## Design principles

Prefer cohesive responsibilities and explicit ownership boundaries.

- **SRP:** keep unrelated orchestration, persistence, validation, telemetry, domain rules, and dependency integration from accumulating in one component merely because they share a call path.
- **OCP:** use existing extension points for real variants; do not build extension frameworks for hypothetical ones.
- **DRY:** keep an authoritative rule owned in one place; syntactic similarity alone is not a reason to merge distinct responsibilities.
- **DIP:** isolate external libraries/providers/storage behind a project-owned boundary when multiple implementations, leakage, or testability justify it; do not add interfaces/factories solely to satisfy the principle abstractly.

Avoid over-engineering. The goal is the smallest design with clear ownership, one source for each domain rule, useful extension points where variation is real, and no speculative indirection.

## Implementation approach

For each implementation outcome:

1. identify applicable requirement/acceptance-criterion IDs and invariants;
2. inspect affected production code and tests;
3. identify the exact existing gap and relevant non-functional/scale constraints;
4. implement the minimum coherent change without creating a second authoritative path;
5. add/update focused tests that establish the contract;
6. define minimum sufficient validation and its stopping condition before expensive checks;
7. run focused validation, then broader regression only at the appropriate checkpoint;
8. inspect the final diff for unintended scope expansion.

Do not weaken tests or requirements to make an implementation pass. For defect corrections, add a regression test when practical.