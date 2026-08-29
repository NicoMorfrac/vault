# Project Manager Configuration Package

This is the canonical Obsidian instruction package for MORFRAC's Project Operations Manager.

## Source-of-truth split

- Obsidian stores these instructions, workflows, templates, and evaluation cases.
- Paperclip stores runtime configuration, assignments, status, dependencies, comments, and approvals.
- `pm_fs.py` is the only authorised project-structure creation tool.

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
