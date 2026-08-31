---
type: commercial_source_library
source_agent: Codex
created: 2026-08-31
related_findings: []
related_concepts: []
related_projects: []
related_reports: []
---

# MORFRAC price lists and supplier information

This is the user-managed, file-based source library for MORFRAC price lists, discount information, supplier catalogues, quotations and commercial terms. Copy your existing documents here. It is not yet a structured pricing database or an Odoo integration.

## Where to put files

```text
Source_Documents/
├── 00_Inbox/      Files you have not sorted yet
├── MORFRAC/       MORFRAC price lists, discounts and commercial information
├── Suppliers/     One subfolder per supplier, using its actual name
├── Archive/       Older versions deliberately retained for reference
└── README.md      This guide
```

Start by copying files into `MORFRAC`, the appropriate supplier subfolder, or `00_Inbox`. Supplier-specific folders can be added when actual supplier names are known; none have been invented.

Keep original source formats and filenames when useful (for example Excel, PDF, CSV, Word or exported records). This folder is for human-supplied originals; it does not change the global rules for agent-generated Markdown files. Do not store passwords, API credentials, bank-account details or unnecessary personal information here.

## Version and source control

- Preserve the original files. Copying a file here is not approval to edit, delete, rename or move it.
- Keep previous versions; do not silently overwrite a price list or supplier quotation. A date or revision in the filename helps distinguish versions.
- Move an older source to `Archive` only after deliberately identifying its replacement; an old quotation may still matter to a particular project.
- When known, retain the issuer, source date, currency, tax basis, validity, scope/quantity and replacement reference. Unknown details remain unknown.
- If Odoo or another system is authoritative, exported files here are dated source snapshots, not a competing live master. No synchronisation is configured.

## How agents may use the material

Uploading a document makes it available for a later explicitly assigned review. It does not automatically approve a price, discount, supplier, quote, purchase or customer commitment. No automatic scan, import, heartbeat or monitoring has been enabled.

The Project Costing Analyst is the existing owner of commercial-data interpretation and approved master-register maintenance. On a requested review, it should identify source files, dates and conflicts, propose candidate entries, and obtain the required human approval before creating or changing official registers. Preserve original source documents.

### Requesting a review

After copying your files, ask the Project Costing Analyst (or ask for a task to be assigned to it):

> Review the files I copied into the source folder. Extract MORFRAC prices, discounts and supplier terms, flag missing or conflicting information, and prepare candidates for my approval. Do not update registers.

You can name just one file or supplier folder. A general review covers `MORFRAC`, `Suppliers`, and `00_Inbox`; `Archive` is included only when you explicitly request historical comparison. You do not need a full project estimate brief to start. If the agent cannot reliably read a file, it will identify the limitation and request a readable export rather than guess.

The review is returned in the assigned Paperclip issue with source references and a short list of decisions. No review file, master register, original-file modification, or automatic process is created by default. Any later register change needs its own exact plan and approval under the existing vault rules; an unresolved global-rule conflict blocks that write, not the read-only review.

Approved costing/price/discount registers and supplier records remain separate from these originals and follow their existing locations, versioning and approval rules. Other agents receive only the authorised information needed for their task; a shared folder is not itself a technical confidentiality boundary. No employee-agent configuration is changed by this library.

## Related Links

- [Project Costing Analyst instructions](../../../../02_AGENTS/Project_Costing_Analyst/AGENTS.md)
- [Master-data workflow](../../../../02_AGENTS/Project_Costing_Analyst/WORKFLOWS/MASTER_DATA_AND_PARAMETERS.md)
- [On-request source-review workflow](../../../../02_AGENTS/Project_Costing_Analyst/WORKFLOWS/SOURCE_LIBRARY_REVIEW.md)
- [Supplier register area](../../../../07_SUPPLIERS/)
