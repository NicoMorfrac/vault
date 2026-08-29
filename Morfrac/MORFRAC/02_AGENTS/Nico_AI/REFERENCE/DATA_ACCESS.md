# Nico AI Data Access

## Systems of record

- Paperclip: issues, assignments, status, comments, approvals, and handoffs.
- Obsidian: controlled MORFRAC knowledge and approved documents.
- Odoo: commercial and operational business data when a separately approved read-only connection exists.

## Obsidian read scope

Read only what is relevant and authorised from:

- `08_PROJECTS/Active` and, for duplicate checking, `08_PROJECTS/Archived` if present;
- `09_MEETINGS` for confirmed decisions and actions;
- `04_ENGINEERING` and `10_REFERENCE` for controlled technical context, without performing specialist analysis;
- `05_BUSINESS`, `06_MARKETING`, and `07_SUPPLIERS` for relevant approved context;
- `02_AGENTS/Nico_AI` for this configuration and approved preferences;
- `00_SYSTEM` for authoritative rules.

## Write scope

- Use Paperclip for briefs, questions, decisions, approvals, and handoffs.
- Write to Obsidian only after the explicit approval required by `GENERAL_AGENT_RULES.md`.
- Never create project structure; Project Manager owns it.
- Nico AI operational logs may be written only to `02_AGENTS/Nico_AI/LOGS` after approval.
- Every generated report must comply with `OBSIDIAN_REPORT_STANDARD.md`.

## Restricted data

- Never read, copy, display, or store credentials, API keys, OAuth tokens, private keys, or authentication files.
- Do not copy unrelated client, supplier, personnel, banking, or legal data into a brief.
- Do not place secrets in Paperclip comments, Obsidian notes, prompts, logs, or generated files.
- Treat client drawings, failure evidence, pricing, contracts, and personal data as confidential unless the controlling record says otherwise.

## External information

- Nico AI does not independently perform market, competitor, product-price, or changing-fact research.
- Route research to the responsible agent and require source URLs, retrieval date, and confidence.
- External results remain source evidence, not MORFRAC-approved facts, until reviewed.

## Odoo

No Odoo access is assumed. If an integration is added, start read-only and define allowed models/fields, company scope, personal-data controls, and metric definitions before use.
