# Structured Handoffs

## Project Manager

Request approved scope revision, deliverables, project responsibilities, schedule/milestones, change baseline, decision records, and existing project path.

For absent proposal storage in an existing project, first check for an equivalent unresolved storage request to avoid duplicates. If authorised to create the scoped handoff, assign Project Manager `780f4096-9a8f-46d8-8249-ef018c34dda3` with:

Title: `PM_TASK prepare_proposals <Project_Name>`

```text
PM_TASK:
type: prepare_proposals
project_name: <Project_Name>
reason: <Why this proposal needs the optional storage area>
originating_issue: <actual requesting issue UUID>
```

Use exactly those four fields and the current global `ProposalWorkflow-v1` protocol. Include no confidential commercial details beyond what PM needs for storage. Creating the task is not permission to create folders; PM must get a new folder-plan `APPROVE <Project_Name>`. If scoped issue-creation access is unavailable, report the required handoff for human/PM action; do not simulate success or obtain broader access.

Until `PROPOSAL_STORAGE_READY` and independent path verification, keep drafts in this Paperclip issue with `PROPOSAL_STORAGE_REQUIRED`. Storage readiness does not approve a save/release. Missing base projects use the existing `create_project` protocol separately; do not ask the storage helper to create a project. Partial/unsafe storage stays blocked without repair.

## Engineering/technical owner

Request review of technical description, boundaries, performance/compliance statements, deliverables, acceptance tests, assumptions, exclusions, dependencies, and technical risks.

## Project Costing Analyst / commercial owner

Request only a client-safe approved price scenario with proposal-ready totals, options, currency/tax basis, validity, payment basis and approval reference. Do not request internal cost build-up unless the CEO separately authorises it.

## Legal Agent / human counsel

Request approved standard terms reference, deviation review, required clause wording, jurisdiction/language review, and explicit unresolved risks.

## CEO / authorised commercial owner

Request scope/commercial decisions, confidentiality boundary, approved client-safe price, exceptions, review ownership, and human sender.

## Other agents and employee interfaces

Accept only verified, scoped operational inputs. Return only the minimum authorised sanitised content. Do not infer role or access from an agent name, and do not disclose internal pricing strategy, cost/margin/discount information, supplier terms, legal strategy, or unrelated project/client data without explicit authority.
