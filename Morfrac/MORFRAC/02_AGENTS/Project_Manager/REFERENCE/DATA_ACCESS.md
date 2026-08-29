# Project Manager Data Access

## Read

- Relevant Paperclip issue, comments, project, goal, blockers, and approved handoffs.
- `00_SYSTEM` rules relevant to the current action.
- `08_PROJECTS/Active` only to validate target existence and required structure.
- Project Manager workflows/templates in `02_AGENTS/Project_Manager`.

## Write

- Paperclip issue status, comments, approved coordination tasks, and dependencies.
- Standard project structure only through `C:\Users\nicol\tools\pm_fs.py` after exact approval.
- Project Manager logs only after the required persistent-write approval.

## Prohibited

- Credentials, tokens, authentication stores, unrelated personal/client records.
- Manual project-folder creation.
- Analysis or design files.
- Existing project-index edits after creation.
- Files outside the MORFRAC vault.
- Odoo writes, email, publication, submission, purchase, or payment.

Use `PAPERCLIP_API_URL`; never hard-code a host. Use `X-Paperclip-Run-Id` on every mutating API request.
