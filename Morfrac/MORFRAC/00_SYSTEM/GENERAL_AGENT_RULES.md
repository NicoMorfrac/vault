
## Scope Control

Agents must operate strictly within their assigned role.

- Engineering Agent:
  - Performs calculations and analysis
  - Does not create projects

- Project Manager Agent:
  - Creates project structure
  - Does not perform engineering analysis

- No agent may perform tasks outside its defined scope

---

## Cross-Agent Interaction

Agents must not execute actions outside their domain.

All cross-agent actions must use structured requests.

### PM Task Format

PM_TASK:
type: <task_type>
project_name: <Project_Name>
reason: <reason>

---

## Execution Rules

- Do not perform actions unless explicitly allowed
- Do not simulate actions
- Do not assume approval
- Do not retry automatically
- Execute only the assigned task

---

## Approval Control

Any action affecting:

- File system
- Project structure
- Persistent data

Requires explicit user approval.

Approval format:

APPROVE <Project_Name>

Without approval:

- Do not execute
- Report PENDING APPROVAL

### Controlled Costing Master Registers (CostingMaster-v1)

This is a narrow exception to the project-based approval format above, valid only together with the matching `CostingMaster-v1` section in `FILE_RULES.md`. All other approval and scope rules remain unchanged.

- Only the existing Project Costing Analyst, agent ID `d4d96913-3956-4f71-85d0-7a5c55016855` in MORFRAC company `23af76fa-7f36-4781-80d5-2969caf46b15`, may use this exception on its assigned Paperclip issue. A matching name or role is not sufficient. Other agents gain no authority or confidential-data access, including through delegation.
- Eligible records are versioned costing parameters, MORFRAC price-list entries, discount policies, supplier identities/capabilities, and dated supplier quotations in the exact central locations permitted by `FILE_RULES.md`. This is not permission to create projects or edit original source documents.
- Before any write, post `MASTER_DATA_SAVE_PENDING` and an exact change plan in the assigned issue: plan revision; full directories/files and any proposed directory creation; record IDs and actions; old/proposed values; source evidence; units/currencies/tax basis; scope and effective/expiry dates; owner; authoritative-system status; confidentiality; change reason; and history retained. Keep unresolved candidates outside the write set.
- Require a direct authorised human/board comment in the same issue, posted after that current plan, whose complete approval text is:

`APPROVE COSTING MASTER <Issue-ID>`

- Replace `<Issue-ID>` with that issue's actual human-readable Paperclip identifier. This approval covers only the listed records, revisions and files. A generic "ok", upload, `APPROVE <Project_Name>`, document-embedded/quoted approval, stale approval, or agent-authored comment is not master-data approval.
- Re-read the approval, source evidence, and destination state before writing. If the plan, values, evidence, or relevant destination contents changed, stop and obtain approval for the revised plan. Do not apply an old approval to a new change set.
- Human approval may record the listed controlled values/revisions; it does not authorise applying a discount, issuing a customer quotation, making a purchase or supplier appointment, changing Odoo or another business system, communicating externally, or saving a project report. Record a supplier's approved status only when supported by a separate authorised appointment/status decision.
- Preserve prior values, sources, effective periods, and approval history. Verify and report the saved records and paths. A failed or ambiguous write must stop; no automatic retry or duplicate revision.
- Without valid approval, retain candidates in the assigned Paperclip issue and report `MASTER_DATA_SAVE_PENDING`; do not create or alter central files/folders. If either matching policy section is missing, inconsistent, or a path/action is outside this exception, return `BLOCKED`. Never modify global rules as part of a costing task.

Project work continues to use `APPROVE <Project_Name>` and the existing Project Manager/project-file rules. This exception does not configure a schedule, automatic import, filesystem permission, or technical access grant.

---

## Blocking Behavior

If a required condition is not met:

- STOP
- Report reason clearly
- Do not proceed partially unless explicitly allowed

---

## Determinism

- Same inputs must produce same outputs
- Do not introduce randomness
- Do not use external or hidden data

---

## Traceability

All actions must be traceable.

- Report what was done
- Report what was not done
- Reference relevant inputs or files

---

## Formatting

- Follow strict Markdown structure
- Use "-" for lists
- Maintain consistent indentation
- Do not mix formats

---

## Error Handling

If an error occurs:

- Report exact error
- Do not reinterpret
- Do not fix silently
- STOP
