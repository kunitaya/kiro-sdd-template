---
inclusion: fileMatch
fileMatchPattern: "**/*.md"
description: Living-document and Spec documentation policy.
---

# Documentation Policy

Reusable documentation states current intended behavior/process directly. Do not accumulate Issue-by-Issue chronology in living policy docs.

Preserve durable rationale where it materially helps future decisions. Use an ADR only for a decision whose context/trade-offs need a stable historical record. Issue/PR comments and Spec progress tables remain the right place for transient execution history and evidence.

Specs are different: they may record review revisions, task progress, validation evidence, and lifecycle checkpoints because those records are part of the change's execution state.

Keep terminology and authority boundaries explicit. Do not duplicate an authoritative requirement into multiple reusable files when a stable reference is sufficient.