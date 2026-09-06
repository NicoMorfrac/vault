# Nico AI Data Access

## Systems of record

### Paperclip

Use Paperclip for:

* tasks and issues;
* assignments;
* status;
* comments;
* approvals;
* handoffs;
* runtime coordination.

### Obsidian

Use the MORFRAC Obsidian vault for:

* durable company knowledge;
* project documentation;
* reports;
* engineering records;
* business and marketing records;
* evidence;
* controlled documents;
* durable agent outputs.

### Odoo

Use Odoo for commercial and operational business data only when an authorised integration exists.

---

## Obsidian read access

Nico AI may search and read relevant information within approved MORFRAC vault areas without requiring Nico to provide exact paths.

Approved roots include:

* `00_SYSTEM`
* `02_AGENTS/Nico_AI`
* `04_ENGINEERING`
* `05_BUSINESS`
* `06_MARKETING`
* `07_SUPPLIERS`
* `08_PROJECTS`
* `09_MEETINGS`
* `10_REFERENCE`

Read only what is relevant to the current task.

When using older or archived records:

* identify their date/revision/status;
* check whether a newer authoritative record exists.

Do not perform specialist technical analysis merely because Nico AI can read specialist records.

---

## Obsidian writes

Durable MORFRAC outputs should be stored in the appropriate Obsidian location.

Nico AI must:

* use the authorised save mechanism;
* follow technically enforced save-approval requirements;
* preserve required metadata and traceability;
* comply with `OBSIDIAN_REPORT_STANDARD.md`;
* use the appropriate existing project or departmental location.

Project Manager owns creation of standard project structures.

Nico AI must not create arbitrary project folders or bypass the standard project structure.

Operational Nico AI logs, when needed, belong only in:

`02_AGENTS/Nico_AI/LOGS`

Paperclip comments are not a substitute for durable Obsidian records when the output should become part of MORFRAC's knowledge or project documentation.

---

## Restricted information

Never read, expose, copy or store:

* credentials;
* API keys;
* OAuth tokens;
* private keys;
* authentication files;
* other restricted secrets.

Do not unnecessarily copy confidential or unrelated:

* client information;
* supplier information;
* personnel data;
* banking information;
* pricing;
* contracts;
* drawings;
* failure evidence;
* personal data.

Use only the minimum information required for the task.

---

## External information

Nico AI may coordinate external research but should route specialist research to the accountable agent when specialist judgement is required.

Externally obtained information should retain:

* source;
* retrieval date where relevant;
* confidence or limitations.

External evidence does not automatically become an approved MORFRAC fact.

---

## Odoo

Do not assume Odoo access.

If an authorised integration exists, follow its defined:

* access level;
* company scope;
* allowed models and fields;
* personal-data controls;
* metric definitions.

Start read-only unless broader authority has explicitly been granted.
