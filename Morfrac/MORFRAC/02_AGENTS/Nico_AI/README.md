# Nico AI Configuration Package

This folder contains the canonical instructions for Nico AI.

## Role

Nico AI is Nico's executive assistant and MORFRAC's orchestration layer.

It:

* understands requests;
* recovers relevant context;
* routes work to the appropriate agents;
* coordinates dependencies;
* consolidates results;
* requests human decisions when required.

See `AGENTS.md` for the governing behaviour.

## Systems

* **Obsidian** stores this instruction package and durable MORFRAC knowledge and documents.
* **Paperclip** manages tasks, assignments, handoffs, status, comments and approvals.
* **Odoo** remains the business system of record where an authorised integration exists.

## Paperclip configuration

External instruction mode:

* Root: `C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC\02_AGENTS\Nico_AI`
* Entry: `AGENTS.md`

Do not maintain a separate active copy of `AGENTS.md` inside Paperclip.

## Maintenance

When materially changing Nico AI:

1. update the relevant file in this package;
2. preserve version history or a backup;
3. run the evaluation cases;
4. correct failures before broader use.

Keep workflow rules in their appropriate files rather than duplicating them across the package.
