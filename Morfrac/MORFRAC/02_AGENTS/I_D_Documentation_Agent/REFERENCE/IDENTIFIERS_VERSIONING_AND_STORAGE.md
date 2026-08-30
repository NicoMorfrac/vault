# Identifiers, Versioning and Storage

Use stable RDI IDs such as `RDI-YYYY-NNN`, linked to the approved MORFRAC project and Paperclip issue. Use separate IDs for work packages, experiments, datasets, configurations, decisions, failures, changes and external packs.

Proposed controlled substructure under the existing empty root, after exact save/structure approval only:

`04_ENGINEERING/R&D/`

- `00_MASTER/`
- `01_PROJECTS/<RDI-Project-ID>/00_BASELINE/`
- `01_PROJECTS/<RDI-Project-ID>/01_WORKPLAN/`
- `01_PROJECTS/<RDI-Project-ID>/02_EXPERIMENTS/`
- `01_PROJECTS/<RDI-Project-ID>/03_DATA_MANIFESTS/`
- `01_PROJECTS/<RDI-Project-ID>/04_DECISIONS_CHANGES/`
- `01_PROJECTS/<RDI-Project-ID>/05_REPORTS/`
- `02_EXTERNAL_PACKS/`
- `03_CLOSED/`

Do not create these because documented. Preserve raw data in its approved controlled location and link by immutable reference/hash rather than duplicating it unnecessarily.

Versions never overwrite baselines, raw evidence, prior reports, submitted packs or receipts. Use `DRAFT_INTERNAL`, `SAVED_INTERNAL_NOT_RELEASED`, `HUMAN_EXTERNAL_HANDOFF_READY`, `SUBMITTED_BY_HUMAN_RECEIPT_REQUIRED`, `SUPERSEDED` and `CLOSED_ARCHIVED` accurately.
