# Kiro Specs

This directory holds **active derived specifications** produced through Kiro's
Spec-Driven Development workflow. A Spec never adds, removes, weakens, or overrides an
authoritative project requirement, GitHub Issue acceptance criterion, or repository
policy. If a conflict exists, stop and report it rather than reinterpreting either side.

`_templates/*` are repository-augmented versions of Kiro's native Spec artifacts, not a
replacement grammar. Preserve native artifact sections/headings and layer repository
governance, traceability, invariants, matrices, and delivery state around them.

## Directory convention

```text
.kiro/specs/
    README.md
    _templates/
        requirements.md
        design.md
        bugfix.md
        bugfix-design.md
        tasks.md
    <issue-number>-<slug>/
        <workflow-specific first artifact>
        design.md
        tasks.md
```

`<issue-number>-<slug>` starts with the owning GitHub Issue number. One directory holds
one workflow's artifact set. Requirements-First / Quick Spec use `requirements.md`;
Bugfix uses `bugfix.md`; Design-First begins with `design.md` and adds a reconciled
`requirements.md` before tasks are accepted.

`.kiro/specs/` contains only active Specs. After Independent Code / Requirements Review
PASS and required fixes, the delivery helper moves the Spec to
`docs/spec-archive/<issue-number>-<slug>/` before the existing Draft PR is made Ready.
Do not maintain a second active `_archive` hierarchy.

## Starting a Spec

1. Load `#sdd-workflow` and choose Requirements-First, Design-First, Quick Spec, or
   Bugfix according to the change and installed Kiro capabilities.
2. Copy the relevant native-compatible template(s); never edit `_templates/` in place
   for a single Issue.
3. Fill the `STRICT WORKSPACE ISOLATION` block in the workflow's first artifact with
   repository, Issue, branch, and allowed scope. Never put an absolute filesystem path
   there; runtime identity comes from Git.
4. Declare review tier / Spec kind and map the applicable authoritative sources.
5. Work artifacts in the selected native order and honor required inter-phase review or
   reconciliation gates.
6. Validate Spec format/references, task graph, and applicable Markdown/config checks.
   Record unavailable native diagnostics as unavailable rather than PASS.
7. Publish the Spec to the owning dedicated branch and the same Draft PR used for the
   implementation lifecycle.
8. Obtain Independent Spec Review authorization before implementation.
9. Start each implementation task through Kiro's native Spec Task Execution UI. A
   supplementary chat prompt may add context after native selection but must not select
   or start another unchecked task.
10. After implementation/final validation, publish to the same Draft PR and obtain the
    required Independent Code / Requirements Review.
11. Only after final review/fixes, run `scripts/finalize-spec` with the reviewed commit
    and PASS record. The helper validates the mechanical delivery state, archives the
    Spec, publishes the archive, transitions the Draft PR to Ready, and records delivery
    completion. It never decides review approval itself.

## Template use and validation

Feature/Quick correctness properties reference native `Requirement N.M` targets from
`requirements.md`. Bugfix properties reference numbered Expected/Unchanged items
(`2.x` / `3.x`) from `bugfix.md`. A syntactically valid reference is insufficient if the
target does not exist or does not support the property.

Use `tasks.md` as the durable task/delivery state owner. Routine delivery checkpoints
stay outside the Task Dependency Graph. Keep the implementation-authorization gate and
delivery authorization state synchronized.

For Markdown/config validation, use the repository's actual configuration and
provisioned tools; do not disable rules merely to obtain PASS. Template inspection is
not a substitute for Kiro's native Spec diagnostics when those diagnostics are
available.

## What belongs where

- **`AGENTS.md`** — repository-wide authority, safety, review, and development policy.
- **`.kiro/steering/`** — reusable Kiro-specific execution and interpretation guidance.
- **`.kiro/specs/<issue>/`** — one change's derived requirements/design/tasks and
  workspace declaration.
- **Issue / PR / progress record** — execution history, review evidence, and transient
  decisions.
- **Independent reviewer** — final gate decision; self-validation, hooks, or automated
  review do not substitute for required independent review.
