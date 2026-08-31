
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

---

## Controlled Proposal Workflow (ProposalWorkflow-v1)

This scoped exception requires matching `ProposalWorkflow-v1` sections in `FILE_RULES.md`, `PROJECT_RULES.md`, and `AGENT_COMMUNICATION.md`. If any is missing or conflicts, stop the affected proposal write. CostingMaster-v1 and ordinary project/analysis rules remain unchanged.

- Within company `23af76fa-7f36-4781-80d5-2969caf46b15`, only Project Manager `780f4096-9a8f-46d8-8249-ef018c34dda3` may prepare the optional proposal directories; only Project Proposal Agent `89219e35-ff07-4681-ac9b-f06f462e1c43` may save the approved proposal files or mark a package ready for human release. Verify actual assignment and identity, not a displayed name. Other agents gain no authority or confidential access through this exception.
- PM may inspect the requested existing project's structure read-only and use the helper's `--check-proposals` operation before approval. Creating the three planned proposal directories requires a direct authorised human/board `APPROVE <Project_Name>` in the same PM issue after the current exact folder plan. It authorises no proposal content, base-project repair, or other directories.
- Proposal drafting/review stays in the assigned Paperclip issue until a save is specifically approved. Before saving, show the exact project, one proposal ID/version, filenames and paths, complete frozen content previews/fingerprints, source revisions, confidentiality, and required prior reviews. Require a subsequent direct authorised human/board comment exactly `APPROVE PROPOSAL SAVE <Project_Name> <Version>` in that issue.
- Save approval covers only those new versioned Markdown files. It does not approve scope, price, terms, folder creation, release, sending, or signing. Reject casual agreement, quoted/embedded/stale/agent-authored approvals, mismatched projects/versions, or approvals from another issue.
- If content, source evidence, filename, path, proposal ID, version, or relevant destination state changes, stop and request approval of a new plan. Never increment a version or choose an alternative path after approval.
- Only after verified immutable saved files and all technical, schedule, price, commercial, and legal reviews, show an exact release plan with file hashes, approved references and intended human sender. Require a subsequent direct authorised human/board comment exactly `APPROVE PROPOSAL RELEASE <Proposal_ID> <Version>`.
- Release approval permits only an issue-based release manifest/checklist and `HUMAN_RELEASE_READY` handoff to that human. It permits no new vault file, saved-file edit, removal of DRAFT status, upload, email, submission, signature, negotiation, acceptance, Odoo change, purchase, or commitment. Changed evidence/files invalidate release readiness and require renewed review.
- Keep client-safe and internal material separate; share only with verified authorised audiences. Folder separation is organisational, not a technical access-control guarantee. No schedules, integrations, runtime permissions, or other agent configuration are changed by this policy.
