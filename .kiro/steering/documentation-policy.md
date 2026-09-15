---
inclusion: fileMatch
fileMatchPattern: "**/*.md"
description: Living-document and Spec documentation policy.
---

# Documentation Policy

Reusable documentation states current intended behavior/process directly. Do not
accumulate Issue-by-Issue chronology in living policy docs.

Preserve durable rationale where it materially helps future decisions. Use an ADR only
for a decision whose context/trade-offs need a stable historical record. Issue/PR
comments and Spec progress tables remain the right place for transient execution history
and evidence.

Specs are different: they may record review revisions, task progress, validation
evidence, and lifecycle checkpoints because those records are part of the change's
execution state.

Keep terminology and authority boundaries explicit. Do not duplicate an authoritative
requirement, policy rule, or operating procedure into multiple reusable files when a
stable reference is sufficient.

## Human-facing operational documentation

English remains authoritative for repository/GitHub artifacts.

Human-facing documents used directly for setup or recurring development operation may
have Japanese reference translations. This repository designates these maintained pairs:

- `README.md` / `README.ja.md`;
- `docs/setup.md` / `docs/setup.ja.md`;
- `docs/development-operations-runbook.md` /
  `docs/development-operations-runbook.ja.md`.

For every designated pair:

- keep the English version authoritative;
- update both languages in the same change when meaning changes;
- keep headings, procedure order, warnings, document ownership, and operational
  boundaries semantically synchronized;
- do not let the Japanese reference independently redefine policy.

AI-facing policy, steering, and Spec templates remain English unless the adopting
repository explicitly defines a different authority model.
