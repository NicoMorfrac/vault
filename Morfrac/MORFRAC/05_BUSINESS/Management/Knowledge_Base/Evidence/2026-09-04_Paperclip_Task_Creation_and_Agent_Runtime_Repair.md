---
type: setup_knowledge
source_agent: Codex_Assisted_Setup
created: 2026-09-04
as_of: 2026-09-04
audience: internal
record_class: setup_knowledge
status: repaired_and_validated
approval_status: owner_authorised
approval_reference: owner instruction "solve"
related_findings:
  - New tasks now appear immediately on the Dashboard and in the Inbox
  - Scoped company agents execute through the current ChatGPT-authenticated Codex CLI runtime
  - Agent completion updates accept safe issue identifiers and ISO-style timestamp keys
  - MORAAAAA-152 completed through the repaired interface and scoped connector
  - Raffa AI was not modified
related_concepts:
  - Paperclip task creation
  - Dashboard query invalidation
  - Agent runtime selection
  - Scoped MCP connectors
  - Idempotent completion updates
related_projects: []
related_reports:
  - "[[05_BUSINESS/Management/Knowledge_Base/Evidence/2026-09-02_Paperclip_Connector_Runtime_and_Attachment_Repair]]"
---

# Paperclip task creation and agent runtime repair

## Outcome

The Paperclip task-creation workflow is operational. Submitting the New Task form now closes the dialog, confirms success, refreshes Dashboard and agent data, shows the new task immediately, and starts the assigned agent. The live interface test `MORAAAAA-152` progressed from Todo to In Progress to Done.

## Root causes

1. The New Task dialog created the issue successfully but did not invalidate the Dashboard or agent queries and displayed no success confirmation. The task therefore looked absent until a later refresh.
2. After the Paperclip update, `engine: auto` selected the ACP execution path. That path did not load the existing scoped MCP arguments, so affected agents lacked their assigned-task connector tools.
3. The connector accepted only lowercase 64-character update keys. Agents naturally generated keys containing an uppercase Paperclip identifier and an ISO timestamp, so a successful run could not apply its final Done disposition.
4. Using the generic `codex` command was incompatible with this Paperclip process. The current versioned Codex executable path is required.

## Applied repair

- Updated `NewIssueDialog.tsx` to invalidate Dashboard and agent-list queries after creation and show a success toast with an Open action.
- Added a UI regression test covering success confirmation and both query invalidations.
- Configured all 42 scoped company agents with `engine: cli` and the current versioned Codex executable while preserving models, prompts, permissions, connector arguments and runtime settings.
- Expanded the safe completion-key grammar to 1-128 ASCII letters, digits, underscore, hyphen, period or colon. The MCP schema and runtime validation now agree.
- Added a connector regression test for a key shaped like `MORAAAAA-152-final-disposition-2026-09-04T17:50:00Z` and rejection tests for whitespace, paths, mentions and leading punctuation.
- Raffa AI remained untouched. CEO and the paused `test` agent have no scoped connector and were not included in the runtime migration.

## Verification

- New Issue dialog tests: **6 passed, 0 failed**.
- Paperclip production UI build: **completed successfully**.
- Focused completion-key and MCP-surface tests: **2 passed, 0 failed**.
- Broader connector run: **110 passed**; the 11 failures were existing sandbox filesystem checks unable to resolve `C:\\Users\\nicol`, not failures in the repaired functionality.
- Fleet readback: **45 total agents**, **42 scoped agents on CLI**, **42 scoped agents using the current executable**, Raffa AI unchanged.
- Live task `MORAAAAA-152`: created in the UI, immediately visible in Dashboard and Inbox, executed by Assistant, saved a verified scoped update and reached Done at 2026-09-04 19:50 Europe/Madrid.

## Maintenance note

The Codex desktop application uses a versioned executable directory. After a future Codex application update, verify that every scoped Paperclip agent's `adapterConfig.command` points to the new path returned by `Get-Command codex.exe`. A future Paperclip source update may also overwrite the local New Issue dialog patch; rerun its regression test after upgrades.

## Related Links

- [[000 - DASHBOARD MORFRAC|Main MORFRAC dashboard]]
- [[001 - DASHBOARD AGENTS AND WORKFLOWS|Agents and workflows dashboard]]
- [[005 - DASHBOARD LATEST REPORTS AND INFORMATION|Latest reports and information]]
- [[05_BUSINESS/Management/Knowledge_Base/Evidence/2026-09-02_Paperclip_Connector_Runtime_and_Attachment_Repair|Earlier connector and attachment repair]]

