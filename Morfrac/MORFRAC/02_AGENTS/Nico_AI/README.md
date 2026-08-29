# Nico AI Configuration Package

This folder is the canonical instruction package for Nico AI.

## Purpose

Nico AI is Nico's personal work assistant and MORFRAC's intake layer. It converts informal requests into approved briefs and structured Paperclip handoffs while preserving MORFRAC's existing separation of responsibilities.

## Source-of-truth split

- Obsidian stores this package, approved knowledge, and controlled documents.
- Paperclip stores runtime configuration, reporting line, permissions, budget, tasks, comments, and approvals.
- Odoo remains the business system of record when connected.

## Runtime entry

Paperclip must use external instruction mode with:

- Root: `C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC\02_AGENTS\Nico_AI`
- Entry: `AGENTS.md`

## Change control

- Review instruction changes before applying them to Paperclip.
- Do not maintain a second active copy of `AGENTS.md` inside Paperclip.
- Preserve backups or version history for this folder.
- Run the evaluation cases after material instruction or routing changes.

## Activation standard

Nico AI should remain wake-on-demand with scheduled heartbeat disabled until the evaluation set passes and its external integrations are separately approved.
