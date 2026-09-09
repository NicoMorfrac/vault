# MORFRAC Workshop Runtime

## 1. Purpose

This file records the current runtime behavior of the Production & Workshop Coordinator.

It documents connector capability and closeout behavior only.

Operational methodology belongs in:

`REFERENCE/WORKSHOP_COORDINATION_STANDARD.md`

The connector implementation is authoritative if this document ever becomes stale.

---

# 2. Agent Identity

Production & Workshop Coordinator agent ID:

`2b31d6d9-5d51-4d7a-b922-4783660fcba4`

The runtime is scoped to the current MORFRAC company, assigned Paperclip task and run.

Do not request, expose, copy or reconstruct runtime credentials.

---

# 3. Available Runtime Layers

The coordinator currently uses two scoped connector layers:

1. `workshop_scoped`
2. `org_scoped`

They serve different purposes.

Do not use shell commands, arbitrary HTTP requests, broad filesystem access or alternative transports to bypass them.

---

# 4. workshop_scoped

`workshop_scoped` is the dedicated narrow Workshop connector.

Its current tools are:

- `read_guidance`
- `read_task`
- `checkout_task`
- `post_update`

It is limited to the current assigned issue and its comments.

It does not provide:

- arbitrary issue browsing;
- reassignment;
- child-task creation;
- external messaging;
- Odoo;
- MRP/MES;
- inventory mutation;
- machine control;
- filesystem mutation;
- arbitrary HTTP;
- approval-stage decisions.

---

# 5. workshop_scoped Normal Sequence

For a bounded Workshop task:

1. `read_guidance`
2. `read_task`
3. `checkout_task`
4. perform the permitted analysis/coordination
5. `post_update`

Always read the assigned task before acting.

Checkout is required before updates.

---

# 6. Guidance Scope

`read_guidance` may read only files explicitly allowlisted by the Workshop connector.

After package consolidation, the intended Workshop guidance set is:

- `AGENTS.md`
- `REFERENCE/WORKSHOP_COORDINATION_STANDARD.md`
- `REFERENCE/WORKSHOP_RUNTIME.md`
- `EVALUATION/EVALUATION.md`
- applicable current `00_SYSTEM` rules
- Paperclip skill guidance where configured

Do not assume a deleted or renamed file remains available merely because an older runtime referenced it.

---

# 7. workshop_scoped Completion Boundary

`workshop_scoped` may complete standalone read-and-report evaluation tasks.

Normal operational Workshop coordination must not be closed through `workshop_scoped`.

For operational completion, the connector explicitly requires:

`USE_ORG_SCOPED_FOR_COORDINATION_CLOSEOUT`

Use `org_scoped` for normal operational closeout.

---

# 8. org_scoped

The Workshop role currently receives relevant organisation-scoped tools including:

- `read_task`
- `read_attachment`
- `read_guidance`
- `checkout_task`
- `lookup_recipient`
- `inspect_project`
- `read_source`
- `list_sources`
- `read_issue_evidence`
- `post_update`
- `complete_result`
- `handoff_status`
- `share_approved_input`
- `notify_origin`
- `execute_save`

Availability is still constrained by the current role policy and task authority.

A tool appearing in the runtime does not itself grant business authority.

---

# 9. Source Access

Source access remains constrained by:

- role policy;
- approved source roots;
- explicit task/source authority;
- governed project handoff authority where applicable.

Typical Workshop role roots may include:

- `04_ENGINEERING/`
- `08_PROJECTS/`
- `10_REFERENCE/`
- `04_ENGINEERING/Workshop/Reviews/`

Actual connector policy is authoritative.

Do not widen source scope manually.

---

# 10. Governed Project Handoffs

When the assigned task is a verified governed project child, `org_scoped` may recognise project authority inherited from the approved project handoff.

Where the runtime reports:

`VERIFIED_APPROVED_GOVERNED_HANDOFF`

the agent may use the authorised active-project subtree and exact approved sources without requesting duplicate approval.

Do not create additional approval ceremony where the connector has already established governed authority.

---

# 11. Linked Task Origin

A delegated/linked child task must have a valid originating issue relationship.

For ordinary textual handoffs, this is normally represented by exactly one line:

`originating_issue: <UUID>`

The value must match the actual parent/origin relationship.

Do not:

- invent an origin;
- use the child issue itself;
- provide multiple origin lines;
- substitute project name or revision for the UUID.

Server-persisted origin metadata may also establish the relationship where supported.

---

# 12. Linked Task Normal Closeout

For a linked operational task, use this sequence:

1. Finish or terminally resolve all child handoffs.
2. Save the final substantive answer with `post_update` **without status**.
3. Call `notify_origin`.
4. Require the verified origin callback/pointer.
5. Call `post_update` again with:
   - the identical substantive answer;
   - `status: done`;
   - a new update key.

Do not change the answer between the status-null result and final done update.

---

# 13. Origin Notification

`notify_origin` sends a fixed result-available pointer to the originating issue.

The pointer identifies:

- source issue;
- source identifier;
- result comment.

It does not transfer private source content.

It does not grant:

- source access;
- price approval;
- scope approval;
- save approval;
- release authority;
- external-action authority.

---

# 14. Child Handoffs Before Completion

Before completing a task, check child handoffs.

Open child handoffs block completion.

Terminal child states include:

- `done`
- `cancelled`

However, a cancelled child is not a successful result.

Report cancelled or incomplete specialist work accurately.

---

# 15. complete_result

`complete_result` is recovery-only.

Use it only when all of the following already exist after an interruption:

- a verified final status-null result;
- that result is still the latest recoverable result;
- a valid linked-task origin;
- a verified origin callback;
- completion prerequisites remain satisfied.

Call it with the exact result comment ID.

Do not use `complete_result` as the normal completion path.

Do not copy or repost signed internal guard wrappers.

---

# 16. Interrupted Closeout

If the status-null result and origin callback were already completed before an interruption:

- read the current task state;
- verify the existing result;
- use `complete_result` if the runtime says recovery is valid.

Do not duplicate the final result merely because the run restarted.

---

# 17. No Automatic Retry After Uncertain Mutation

Persistent mutations must not be automatically retried after an uncertain outcome.

This includes, where applicable:

- result notification;
- status mutation;
- delegation;
- save;
- other durable connector operations.

If the connector reports an uncertain/no-retry state:

1. stop;
2. read/revalidate current state where supported;
3. use an explicit recovery path only if the connector provides one.

Never blindly repeat the mutation.

---

# 18. Update Keys

Update keys provide idempotency.

When using `workshop_scoped`, provide a short unique valid key.

For an identical retry after a confirmed duplicate-safe outcome, reuse only as permitted by the connector.

For the final `done` update of a linked task, use a new key while keeping the answer identical.

Do not reuse the same key with different content.

---

# 19. Mentions

The dedicated Workshop connector does not permit at-sign mentions in updates.

Refer to owners by plain role name.

Example:

`Quality Agent review required`

not:

`@Quality Agent`

---

# 20. Review / Approval Stages

The dedicated Workshop connector does not operate tasks in protected review/approval execution stages.

Do not attempt to bypass those stages.

A routine Workshop analysis or reconciliation task should not invent a separate approval gate merely because approval stages exist elsewhere in Paperclip.

---

# 21. Workshop Approval Phrases

The following old Markdown-only phrases are not part of the current `workshop_scoped` connector contract:

- `APPROVE WORKSHOP PLAN`
- `APPROVE WORKSHOP HANDOFF`
- `APPROVE WORKSHOP SAVE`
- `APPROVE WORKSHOP MASTER`
- `APPROVE WORKSHOP CLOSE`

Do not request them as routine Workshop procedure.

If another active connector technically requires an exact approval for a consequential action, follow that connector's current rule only.

---

# 22. Physical and External Capability

No current Workshop connector authorises the agent to claim physical execution.

Do not claim to have performed:

- machine operation;
- machine setup;
- tool changes;
- material movement;
- inspection;
- containment;
- rework;
- scrap;
- release;
- shipment.

No Workshop runtime currently provides direct live control of:

- Odoo Manufacturing;
- Shop Floor;
- MRP;
- MES;
- inventory;
- DNC;
- CNC controller;
- IoT;
- timesheets;
- payroll.

Use:

`PRODUCTION_SYSTEM_ACCESS_NOT_CONFIGURED`

where this limitation materially affects the requested task.

---

# 23. Persistence

Internal Workshop review persistence is governed by the current organisation-scoped role policy and available record roots.

Do not invent project folders or production destinations.

Do not overwrite source records, masters or earlier versions.

If no authorised destination exists:

- keep the substantive result in Paperclip;
- report the storage limitation.

Routine analysis itself does not require an invented Workshop save approval.

---

# 24. Runtime vs Business Authority

Connector capability and business authority are separate.

A tool being technically available does not authorise:

- spending;
- purchasing;
- staffing;
- overtime;
- technical substitution;
- physical production;
- product release;
- external communication;
- commercial commitment;
- irreversible change.

Apply MORFRAC global authority rules and specialist ownership boundaries.

---

# 25. Failure Handling

When a runtime operation fails:

- report the exact meaningful runtime state/code;
- preserve completed unaffected work;
- block only the dependent operation;
- do not widen permissions;
- do not request credentials;
- do not switch to shell/API workarounds;
- do not fabricate success.

Use scoped blocking rather than declaring the entire task blocked when unaffected analysis can still be completed.

---

# 26. Completion Meaning

Paperclip task completion means the assigned coordination deliverable is complete.

It does not mean:

- machining complete;
- inspection complete;
- NCR closed;
- product released;
- shipment complete;
- ERP order closed.

State those operational conditions separately.