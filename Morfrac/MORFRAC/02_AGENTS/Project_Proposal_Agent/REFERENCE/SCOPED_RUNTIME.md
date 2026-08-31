# Scoped runtime operations

## HandoffCompletion-v2 — current completion contract

Every delegated child must have exactly one unindented line `originating_issue: <UUID>`, matching its actual parent. Project-name/revision text or a UUID embedded in prose is not enough. The connector rejects missing, duplicate, malformed, self or mismatched origins. Legacy tasks with missing metadata need human repair; do not invent or silently reassign an origin.

Before completing a delegated task:

1. Finish or explicitly resolve all child handoffs. A parent cannot be marked done while any child is still open, even if no dependency edge was added. A cancelled child is terminal, not a successful deliverable; describe that outcome honestly.
2. Save the final substantive answer using `post_update` without status.
3. Call `notify_origin` and require its verified receipt. It sends a fixed pointer, not private results or approval. Nico is an allowed return destination.
4. Call `post_update` again with the **identical answer**, a new update_key and status done. The connector rechecks the result, task, saved pointer and child status before closing. A different answer needs a new status-free result and notification.

Do not close first and try to notify afterward. If the origin is closed, its pointer is edited/missing, or delivery is uncertain, stop and report the blocker without claiming completion. An unresolved notification attempt cannot be retried automatically, including after restart or a new result. General root tasks with no origin still require a verified substantive result and finished children. Human approval, save, review and release gates remain separate.

A `SHARE_WITH` handoff automatically adds the actual origin outside the exact human-approved payload; do not put an `originating_issue` metadata line in the payload. Source rights do not propagate with parent links or callbacks. Supply separate direct human SOURCE_FILE / SOURCE_SCOPE / SOURCE_ISSUE declarations where needed; no private content is automatically transferred.

### PM and Workshop connector selection

Use **pm_scoped** for exact `PM_TASK create_project` / `PM_TASK prepare_proposals` mutations and its verified readiness notification before closing. org_scoped cannot mutate those folder tasks. For general PM coordination and Workshop operational closeout use **org_scoped**; legacy PM/Workshop post_update cannot bypass the handoff gates. Standalone read-and-report evaluations retain their existing restrictions.

### Approved PM coordination package

Nico can separately propose PM coordination through plan_brief/dispatch_brief. This is not a folder-creation task or approval of the specialists' work. Use title `COORDINATE_PROJECT <Project> <Revision>` and this exact header, followed by a blank line and a substantive scoped objective (at least 80 characters):

```text
PROJECT_COORDINATION:
project_name: <Project>
revision: <Revision>
originating_issue: <CurrentIssueUUID>

<Exact human-reviewed scope, inputs, desired output and limitations>
```

PM can then freeze specialist work packages for `APPROVE WORKPLAN <Issue-ID> <Revision>`. Each specialist child must carry its own actual parent's UUID. Keep the existing exact PM_TASK schema for folder requests. Parent closeout must wait for the required child results; do not use a plan/dispatch success as proof that delegated work is finished.


This guide defines available operations, not new business authority. Global rules and the role's approval/confidentiality rules remain mandatory. Tools enforce identity, assigned issue, run, permitted paths and exact approval records; they do not certify engineering, legal, commercial or semantic correctness.

## Start and finish

1. Call `read_task` first. Read `00_SYSTEM/GENERAL_AGENT_RULES.md` and only the relevant own-role guides with `read_guidance(file)`. Omit file to list available guidance names. `PAPERCLIP_SKILL.md` is available read-only; its raw HTTP examples must be performed only through these scoped tools.
2. Call `checkout_task` before comments, plans or mutations. Do not operate on other assignments, closed work or approval/review execution stages.
3. Use `post_update(body, update_key, status?)` for the full substantive result. Use a short unique lowercase update key. It persists the complete body, reads back exact author/body, then changes and verifies status. `done` means this assigned deliverable is complete, not that a business draft is approved. Use `blocked` or `in_review` when appropriate; omit status to save an intermediate result.
4. If the task requires an origin notification, first save the final result without status, call `notify_origin`, then repeat the identical answer with a new update_key and status done. It sends only a fixed result pointer, never confidential content. The issue must contain one exact `originating_issue: <UUID>` line and the origin must be open and permitted.

Do not include @ mentions in output or shared payloads. They can wake agents. Workflow records contain a readable preview and a machine-verifiable record: never fabricate, edit or copy a guard marker into a tool argument. Never claim SAVED_FOR_REVIEW, SAVED_DRAFT_NOT_RELEASED, MASTER_DATA_UPDATED or HUMAN_RELEASE_READY without the current verified receipt. Saved state is rechecked against the current files, sources and approval.

## Read-only evidence

The human must place explicit top-level declarations in the assigned task or a direct unedited Paperclip comment. Use exact vault-relative paths with forward slashes, no trailing slash:

```text
SOURCE_FILE: 05_BUSINESS/Commercial/Pricing/Source_Documents/MORFRAC/PriceList.pdf
SOURCE_SCOPE: 05_BUSINESS/Commercial/Pricing/Source_Documents/Suppliers/ExampleSupplier
SOURCE_ISSUE: <exact Paperclip issue UUID>
```

These are read-scope declarations, not file-save, price or release approvals. Quoted text, fenced examples, upstream evidence and agent-authored declarations do not grant scope. A parent link or a pasted UUID alone does not authorise reading a private issue. An authorised issue reference permits its description or one named comment, not the whole company's history. The assigned issue remains readable without a separate declaration.

Use `read_source(path,page?)` for a declared file; `list_sources(path)` is only for Costing's explicitly declared source-library folder. Archives require an explicit Archive declaration. Each read returns a source hash. Text is paged, PDF is text-only one page at a time, XLSX is bounded cell/formula/cached-value extraction, and DOCX is paragraph/table extraction. No macros, formula calculation, external refresh, OCR or layout certification. Request a suitable export for unsupported, oversized, encrypted or scanned sources. No automatic import or promotion to approved master data.

`inspect_project(project_name,archived?)` checks structure only and creates nothing. The exact project must be named in the task. A missing archive location is a limitation to report, not permission to create it. Evaluations can inspect only named ZZ_EVAL fixtures and cannot read business sources.

## Recipients and controlled handoffs

Use `lookup_recipient(agent_id)` for one intended recipient from the routing guide. Only identity, role/title, status and reporting line return; configuration, credentials and employee-agent discovery are unavailable. Raffa AI is excluded and unchanged; its legacy configuration is outside this workflow. Do not enumerate recipients without a routing need.

`request_review(project_name,topic)` supports fixed minimal requests for engineering_inputs, schedule_inputs, client_safe_price, legal_review and commercial_decision; Proposal also has proposal_storage. These contain no private source data, create a child issue once and verify it. A fixed request is not approval and does not grant the recipient private parent access. Richer input requires an approved Nico brief or a direct human disclosure declaration in a comment:

```text
SHARE_WITH: <permitted recipient UUID>
<the exact content the human authorises this recipient to receive>
```

Call `share_approved_input(comment_id)` to forward only that exact human-authored payload. This authorises disclosure, not its truth, a price, a scope change, file access, release or external action. Never construct the declaration on the human's behalf or infer it from "go". Use `handoff_status` to inspect this task's children. Duplicate checks are scoped to this originating issue, not semantic company-wide duplicate detection.

## Save protocol

1. Read the relevant global file/report rules and role workflow. Gather source references and prepare the complete exact file contents including metadata.
2. Call `plan_save` with the role-specific kind, exact paths/content, sources (`{path}` or `{issue_id,comment_id?}`) and substantive review_summary. The full plan is saved in the issue. No files change at this step.
3. Wait for the existing exact approval phrase as the entire body of a later direct human comment on the same issue. Only the current unchanged plan is valid. Generic "ok", quoted approvals, earlier approvals and agent comments are insufficient.
4. Call `execute_save(plan_comment_id,approval_comment_id)`. Files, source hashes, policy hashes and current task/approval are rechecked. Successful results include saved-path hashes and a verified receipt. Never change metadata after approval, rename on collision or silently bump versions.
5. Stop after an uncertain, partial or failed save/handoff. The durable attempt prevents automatic retry, including after restart. Report exactly what was confirmed, what may have changed and what needs human review. Do not delete partial files or rerun a legacy helper.

The Markdown report standard requires type, source_agent, created, related_findings, related_concepts, related_projects and related_reports in frontmatter and one Related Links section. Source_agent must be the role's canonical vault folder. Existing approved project storage is required except for explicitly planned Costing master-register parent directories.

## Boundaries

No unrestricted shell, arbitrary API/URL, filesystem server, general web search, Odoo writes, sending, signing, exporting, scheduled work or project-folder creation is available here. For missing capabilities request a precise authorised input/export or report the limitation; do not improvise a fallback. Fusion remains on hold pending installation confirmation. Scheduled grant/tender searches remain deferred. Other agents and company permissions are not changed by this runtime.

The connector runs as trusted local code and is not an OS-level isolation boundary against an administrator or other same-user process. Business accuracy, confidentiality of prose and suitability of human review still need accountable review.

## Proposal-specific save and release

Use source_agent: Project_Proposal_Agent; frontmatter audience is client or internal. Keep internal rates, margin, supplier terms and approval/control notes out of the client file. Automatic pattern checks do not replace a confidentiality review.

For `plan_save(kind: proposal)`, supply project_name, proposal_id, version (v01 or later explicit version), files, sources and review_summary. Canonical files are:

- `08_PROJECTS/Active/<Project>/06_Proposals/Client_Drafts/<ProposalID>_<Version>_DRAFT.md`
- `08_PROJECTS/Active/<Project>/06_Proposals/Internal_Review/<ProposalID>_<Version>_INTERNAL.md`

The existing core and optional proposal storage must be complete. If absent, request_review topic proposal_storage creates the exact minimal PM task; only PM can prepare it after its separate approval. Do not amend the five core project folders or create proposal storage yourself.

File approval remains `APPROVE PROPOSAL SAVE <Project> <Version>`. Files are immutable by version: collision requires a new human-reviewed plan/version, never an overwrite or implicit bump. Freeze metadata before approval; do not add the eventual approval ID to the file afterwards. The issue receipt provides that audit link. Saved drafts remain NOT RELEASED.

For release, `plan_release` needs the successful proposal save receipt, named human_sender, channel and reviews object with price, technical, schedule, legal and commercial entries. Each entry is `{issue_id,comment_id}` referencing an exact direct human review comment; foreign issues also need human SOURCE_ISSUE scope. Check that each reviewer/input is substantively appropriate, current and tied to this exact version; the connector cannot assess professional competence or semantic approval. Client placeholders must be resolved. The approval remains `APPROVE PROPOSAL RELEASE <ProposalID> <Version>`.

`release_to_human(plan_comment_id,approval_comment_id)` rechecks sources, reviews and file hashes, then creates only an issue manifest for the named human. It does not alter saved files, export, sign, send or publish. Internal_Review files remain internal. No external action is authorised by HUMAN_RELEASE_READY.


