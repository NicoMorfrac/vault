# Scoped Runtime

This file defines **connector mechanics only**.

Business authority, orchestration, approvals and blocking behaviour are defined by `AGENTS.md` and `00_SYSTEM/GENERAL_AGENT_RULES.md`.

Connector requirements that are technically enforced must still be followed exactly.

---

# 1. Start

For every Paperclip task:

1. `read_task`
2. Read only the guidance needed for the task.
3. Use the minimum connector operations necessary.
4. Do not operate on unrelated assignments.

The connector normally manages checkout automatically. Use `checkout_task` only when explicitly needed.

---

# 2. Reading internal sources

Nico may search and read relevant records within these approved roots:

* `04_ENGINEERING`
* `05_BUSINESS`
* `06_MARKETING`
* `07_SUPPLIERS`
* `08_PROJECTS`
* `09_MEETINGS`
* `10_REFERENCE`

Use:

* `search_sources` when the path is unknown;
* `read_source` for a known source;
* `list_sources` for a known folder;
* `inspect_project` to inspect an existing named project.

Prefer the newest authoritative record unless historical information is requested.

Blocked areas remain inaccessible, including credentials, authentication, secrets, banking, payroll, personnel and other restricted paths.

Reading a source does not authorise modification, release, spending or external action.

---

# 3. Internal delegation

Use:

`delegate_task(agent_id,title,objective,context?,expected_output,priority?)`

for normal specialist delegation.

Before delegating:

1. Check whether equivalent child work already exists.
2. Reuse it where appropriate.
3. Give only the context needed for the work.
4. State the objective and expected output clearly.

Routine internal delegation authorised by Nico's request does not require a separate approval step unless another governing rule explicitly requires one.

Use `handoff_status` to inspect child tasks.

When a completed direct child has returned a verified callback, use:

`read_handoff_result(issue_id)`

to retrieve its actual result.

Do not treat creation of a child task as completion of the delegated work.

---

# 4. Handoff origin

Generated handoffs must retain their real originating issue.

The runtime may use:

```text
originating_issue: <UUID>
```

or authoritative structured origin metadata.

Do not invent, rewrite or manually repair origin metadata.

For ordinary delegated work, use the connector-generated origin mechanism.

A `SHARE_WITH` handoff adds origin information automatically; do not duplicate it inside the shared payload.

---

# 5. Sensitive information sharing

Normal specialist delegation should use only the minimum necessary context.

When another role must receive sensitive/private information that is not otherwise authorised, a direct human declaration may be required:

```text
SHARE_WITH: <recipient UUID>
<exact authorised content>
```

Use `share_approved_input(comment_id)` only for that exact human-authored payload.

Do not construct a `SHARE_WITH` declaration on the human's behalf.

It authorises disclosure only. It does not approve the truth of the information, a price, scope change, release or external action.

---

# 6. Role-limited source declarations

Where another agent's policy technically requires explicit source scope, use:

```text
SOURCE_FILE: <exact vault-relative path>
SOURCE_SCOPE: <exact vault-relative folder>
SOURCE_ISSUE: <exact Paperclip issue UUID>
```

These grant read scope only.

Do not infer source access from a parent link, pasted UUID or quoted text.

Nico itself may discover sources inside its approved roots without requiring these declarations.

---

# 7. Project Manager operations

Use `pm_scoped` for technically enforced PM mutations such as:

* `PM_TASK create_project`
* `PM_TASK prepare_proposals`

Use `org_scoped` for normal PM coordination.

Project creation uses the required machine schema:

```text
Title: PM_TASK create_project <Project>

PM_TASK:
type: create_project
project_name: <Project>
reason: <reason>
originating_issue: <assigned issue UUID>
```

This schema is a connector requirement, not a conversational approval requirement.

Project creation does not need to delay unrelated specialist work.

---

# 8. CAD routing

For a direct CAD/Fusion/2D/3D request, use `route_cad_task` where applicable.

Provide a sufficiently defined instruction and preserve supported attachments.

CAD routing does not approve:

* manufacture;
* release;
* overwrite;
* production use.

---

# 9. Saving controlled files

Saving controlled vault files uses the connector's technical approval protocol.

Procedure:

1. Prepare the complete intended file content.
2. Call `plan_save`.
3. Obtain the exact human approval required by the generated save plan.
4. Call `execute_save(plan_comment_id, approval_comment_id)`.
5. Verify the returned receipt.

Where the connector requires an exact approval phrase, that exact phrase remains mandatory because it is a machine validation requirement.

Do not:

* reuse an old approval for a changed plan;
* alter approved content after approval;
* silently rename or change versions;
* automatically retry an uncertain or partial mutation.

After an uncertain mutation, report what is confirmed and what requires human review.

---

# 10. Markdown records

Where the runtime requires the MORFRAC Markdown report standard, include the required metadata:

* `type`
* `source_agent`
* `created`
* `related_findings`
* `related_concepts`
* `related_projects`
* `related_reports`

Include one `Related Links` section.

For Nico records use:

```text
source_agent: Nico_AI
```

---

# 11. Completing delegated work

Before completing a task:

1. Resolve all required direct child tasks.
2. Retrieve and incorporate required child results.
3. Post any substantive final update when useful.
4. Use `notify_origin` when a callback to an originating issue is required.
5. Use `complete_result` to complete the assigned Paperclip task.

Do not use `post_update` with `status: done` as the normal completion mechanism.

Do not mark a parent complete while required child work remains unresolved.

A cancelled child is terminal but is not a successful deliverable.

If `complete_result` fails, report the confirmed result and the exact completion failure once. Do not repeatedly retry an uncertain mutation.---

# 12. Status updates

Use:

`post_update(body, update_key, status?)`

for substantive task results.

Possible status use includes:

* `done`
* `blocked`
* `in_review`

Omit status when saving an intermediate result.

`done` means the assigned Paperclip deliverable is complete. It does not by itself mean the underlying business output has been human-approved or released.

---

# 13. Failure handling

Do not automatically retry uncertain persistent mutations.

If a connector operation fails:

1. determine what was definitely completed;
2. isolate the affected dependency;
3. continue unrelated work where safe;
4. report the failure clearly.

A connector failure does not automatically require the whole task to become `blocked`.

---

# 14. Runtime boundaries

This runtime does not provide unrestricted:

* shell execution;
* arbitrary filesystem access;
* arbitrary API access;
* external sending;
* signing;
* spending;
* production release;
* project-folder creation outside the PM operation;
* irreversible actions.

Do not improvise around missing permissions.

Use the authorised connector or report the limitation.

---

# 15. Deprecated Nico workflow mechanics

Do not use `plan_brief` / `dispatch_brief` as a mandatory approval gate for ordinary internal delegation.

Use `delegate_task` for normal authorised specialist work.

`plan_brief` / `dispatch_brief` may be used only when a specific workflow or connector operation genuinely requires an immutable reviewed package.

Do not require:

```text
APPROVE BRIEF <Project> <Revision>
```

for routine project intake or specialist dispatch unless the actual operation being executed technically validates that exact approval.

Do not require `APPROVE WORKPLAN` or additional phase approvals merely to continue normal internal project work.

Human approval remains required where defined by the governing authority rules or where a connector technically enforces it.
