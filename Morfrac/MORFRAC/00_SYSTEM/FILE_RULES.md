## General

- All files must use .md extension
- All files must be written inside:
  C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC
- Do not write outside the vault
- Do not overwrite existing files unless explicitly instructed or updating same IssueID
- If write fails, report error and STOP

---

## Naming Convention

All analysis files must follow:

<IssueID>_<Discipline>_<ShortDescription>.md

Example:
MORAAAAA-33_Bearing_IglidurX.md

Rules:

- IssueID is mandatory
- Discipline must be one of:
  - Structures
  - Bearing
  - Thermal
  - Cost
- ShortDescription:
  - must be concise
  - no spaces
  - no special characters
  - max 3 words
- Use CamelCase for materials and descriptors
- Do not use alternative suffixes (e.g. Evaluation, Analysis)
- Do not change naming structure

---

## Index Link Consistency

- Filename and Project Index link must match exactly
- Link must exclude .md extension

Example:
File:
MORAAAAA-33_Bearing_IglidurX.md

Link:
[[MORAAAAA-33_Bearing_IglidurX]]

---

## Deduplication Rule

- Files are uniquely identified by IssueID
- Same IssueID → update existing file
- Different IssueID → create new file
- Do not merge analyses across IssueIDs

---

## Write Behavior

- Confirm file path before writing
- Write file to correct project discipline folder
- Verify file exists after writing
- Report created or updated files

If file does not exist after write:

- STOP
- Report: File write failure

---

## Controlled Costing Master Registers (CostingMaster-v1)

Apply this exception only to the named Project Costing Analyst and a valid, current `APPROVE COSTING MASTER <Issue-ID>` under the matching `CostingMaster-v1` section in `GENERAL_AGENT_RULES.md`. Both sections are required. It does not grant any other agent write authority.

### Permitted central destinations

All paths below are relative to `C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC`:

- `05_BUSINESS/Costing/Parameters/`: costing-parameter registers only.
- `05_BUSINESS/Commercial/Pricing/`: MORFRAC price-list and discount-policy registers only.
- `07_SUPPLIERS/<Supplier_Code>/`: supplier master records and dated quotation registers only, using the actual supplier code in the approved plan.

The entire `05_BUSINESS/Commercial/Pricing/Source_Documents/` subtree is excluded from this write permission. Uploaded originals and their names/locations remain unchanged: no edit, rename, move, archive, delete, or generated files there.

Only the exact Markdown files and any necessary central directories listed in the approved plan may be created/updated. Directory permission is not blanket permission to modify other contents. Resolve every target to its real absolute path inside the approved location; reject path traversal, links/junctions/shortcuts that escape that scope, or paths that cannot be safely verified. No project folders, global rules, agent instructions, or non-Markdown outputs may be changed under this exception.

### Naming, history, and deduplication exception

These central registers are controlled master data, not project analysis reports. For these files only, the project-discipline destination, analysis filename pattern, project-index requirement, and IssueID-only file deduplication rule above are replaced by the following:

- Use the exact stable `.md` register filename and path declared in the approved plan. Do not invent a destination after approval or rename/move existing registers.
- Identify each record by its stable record ID and revision/effective period. Record the originating Paperclip issue and direct human approval comment/reference for every saved change.
- One register may retain approved revisions from multiple issues; one approved issue may name multiple records/files. This never permits merging project analysis reports across issues.
- Updating an existing register is authorised only for the listed changes, with all unrelated records/content preserved. Preserve previous values, sources, dates, and approval evidence. Add new revisions or traceable correction/supersedes/expiry entries; never erase history or replace an old approved value in place.
- Check for the same record/revision before writing. Do not duplicate an already verified saved revision. If the existing state differs from the approved plan or write outcome is uncertain, stop and report it; do not overwrite conflicting content or retry automatically.
- Retain source-of-truth designation and supplied external-system IDs/export dates. An authoritative Odoo record is only mirrored/referenced here; never claim synchronisation or write-back without evidence.
- Follow the existing costing master schema; store no credentials, bank details, personal IDs, or unnecessary personal data. Agent-generated reports still follow `OBSIDIAN_REPORT_STANDARD.md`.
- Re-read and verify every approved file after saving, including the new records and preservation of history/unrelated content. Report exact created/updated paths and revisions; report a failure and stop.

All remaining file rules still apply, including vault-only storage, Markdown format, explicit approval, traceability, and stop-on-error. Project reports keep their existing filename, index, deduplication, destination, and `APPROVE <Project_Name>` requirements unchanged.

