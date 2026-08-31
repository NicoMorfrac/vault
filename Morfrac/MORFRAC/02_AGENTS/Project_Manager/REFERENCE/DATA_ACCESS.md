# Project Manager Data Access

## Enforced connector boundary (2026-08-31)

Use only `pm_scoped` as defined in AGENTS.md. Fetch the assigned issue before any other task discovery. Guidance is allowlisted; project inspection returns structure only, never contents. General shell, environment dumps, arbitrary URLs/paths, inbox search, other-agent configuration and direct shared-helper access are unavailable.

The connector supports own-task read/checkout/verified comment/status, deterministic human-approved folder operations, and the exact verified readiness callback to the same-company originating issue. General coordination-task creation, reassignment and dependency edits below are responsibilities to request from the originating owner/human, not exposed runtime powers. State `SCOPED_HANDOFF_REQUIRED` and do not imply execution.

Do not work around missing access. On an error, read the current task and report the stable error code without exposing secrets or automatically retrying a mutation. A persisted response must be verified before completion.

## Read

- Relevant Paperclip issue, comments, project, goal, blockers, and approved handoffs.
- `00_SYSTEM` rules relevant to the current action.
- `08_PROJECTS/Active` only to validate target existence and required structure.
- Project Manager workflows/templates in `02_AGENTS/Project_Manager`.

## Write

- Paperclip issue status, comments, approved coordination tasks, and dependencies.
- Standard project structure only through `C:\Users\nicol\tools\pm_fs.py` after exact approval.
- The three optional proposal directories only through that helper's `--prepare-proposals` operation after the separate approved folder plan; no files or core/index modifications. Its `--check-proposals` operation is read-only.
- Project Manager logs only after the required persistent-write approval.

## Prohibited

- Credentials, tokens, authentication stores, unrelated personal/client records.
- Manual project-folder creation.
- Analysis or design files.
- Existing project-index edits after creation.
- Files outside the MORFRAC vault.
- Odoo writes, email, publication, submission, purchase, or payment.

Use `PAPERCLIP_API_URL`; never hard-code a host. Use `X-Paperclip-Run-Id` on every mutating API request.
