---
inclusion: fileMatch
fileMatchPattern: "**/*.md"
description: Living-document and Spec documentation policy.
---

# Documentation Policy

Reusable documentation states current intended behavior/process directly. Do not accumulate Issue-by-Issue chronology in living policy docs.

Preserve durable rationale where it materially helps future decisions. Remove chronology without deleting the technical reason a current invariant, fallback, ownership boundary, or constraint exists. Use an ADR only for a decision whose context/trade-offs need a stable historical record. Issue/PR comments and Spec progress records remain the right place for transient execution history and evidence.

## Reusable documentation versus Spec history

Apply the living-document rule directly to reusable policy, steering, templates, architecture, and operating documentation: describe the corrected current rule rather than leaving superseded rules beside later corrections.

Issue-specific Specs are different. Their review revisions, task progress, validation evidence, correction history, and lifecycle checkpoints are part of the change record and may remain. Even there, keep current requirements/design obvious in the main body and separate historical review/correction records so readers do not need to reconstruct current truth from chronology.

In reusable technical documentation, "when" normally describes a runtime condition/state/event, not the date or Issue sequence by which the rule evolved.

Keep terminology and authority boundaries explicit. Do not duplicate an authoritative requirement, policy rule, or operating procedure into multiple reusable files when a stable reference is sufficient.

## Human-facing operational documentation

English remains authoritative for repository/GitHub artifacts.

Human-facing documents used directly for setup or recurring development operation may have Japanese reference translations. This repository designates these maintained pairs:

- `README.md` / `README.ja.md`;
- `docs/setup.md` / `docs/setup.ja.md`;
- `docs/development-operations-runbook.md` / `docs/development-operations-runbook.ja.md`.

For every designated pair:

- keep the English version authoritative;
- update both languages in the same change when meaning changes;
- keep headings, procedure order, warnings, document ownership, and operational boundaries semantically synchronized;
- do not let the Japanese reference independently redefine policy.

AI-facing policy, steering, and Spec templates remain English unless the adopting repository explicitly defines a different authority model.