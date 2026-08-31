# Project Manager Configuration Package

This is the canonical Obsidian instruction package for MORFRAC's Project Operations Manager.

## Source-of-truth split

- Obsidian stores these instructions, workflows, templates, and evaluation cases.
- Paperclip stores runtime configuration, assignments, status, dependencies, comments, and approvals.
- `pm_fs.py` is the only authorised project-structure creation tool.

The optional `ProposalWorkflow-v1` branch uses `WORKFLOWS/PREPARE_PROPOSALS.md` and `TEMPLATES/PROPOSAL_FOLDER_APPROVAL.md`. It adds only `06_Proposals`, `Client_Drafts`, and `Internal_Review` to an existing complete project after its own exact folder plan and human approval. Ordinary project creation remains the original five folders plus index; no existing projects are migrated. Folder separation is not an access-control guarantee.

## Paperclip entry

- Root: `C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC\02_AGENTS\Project_Manager`
- Entry: `AGENTS.md`

## Safety model

- Scheduled heartbeat disabled.
- Wake on demand enabled.
- One concurrent run.
- No agent-creation permission.
- Exact direct human approval required before project creation.
- No specialist analysis or commercial commitment.

The local Codex adapter requires Paperclip runtime bypass for non-interactive use of its injected API credential. This runtime setting does not bypass MORFRAC's project approval rules.
