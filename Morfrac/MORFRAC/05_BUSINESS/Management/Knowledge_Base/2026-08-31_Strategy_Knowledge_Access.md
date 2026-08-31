---
type: access_change_record
source_agent: Codex_Assisted_Setup
created: 2026-08-31
as_of: 2026-08-31
audience: internal
record_class: setup_knowledge
status: configured
approval_status: owner_authorised_configuration
source_context: Owner confirmed the proposed limited Strategy read-only knowledge access change with yes
related_findings: []
related_concepts: []
related_projects: []
related_reports:
  - "[[05_BUSINESS/Management/Knowledge_Base/README]]"
---

# Strategy knowledge access — 2026-08-31

## Approved change

StrategyKnowledgeAccess-v1 adds exactly one candidate source root to the Company Strategy & Growth Agent: `05_BUSINESS/Management/Knowledge_Base/`. It enables read-only access to the saved company structure, owner decisions, readiness notes and validation evidence when an assigned task has appropriate direct human source scope.

This fixes the previously missing role-level eligibility. It is not automatic access for every task, full-vault access, a business approval, an Odoo connection, or evidence that a real growth analysis has been completed.

## How to authorise an analysis task

In the assigned Paperclip task, the human can declare an exact file, for example:

```text
SOURCE_FILE: 05_BUSINESS/Management/Knowledge_Base/README.md
```

If the full reviewed pack is relevant, the human may instead declare:

```text
SOURCE_SCOPE: 05_BUSINESS/Management/Knowledge_Base
```

Declaration paths have no trailing slash. These examples in a stored note are not grants. Agent comments, quotes, fenced examples, embedded upstream evidence and wiki links cannot supply task authority. Links to other departments do not authorise reading their files; both the role's allowlist and the task's human scope must permit each source.

## Boundaries preserved

- Strategy cannot edit this knowledge pack. New internal reviews remain limited to `05_BUSINESS/Strategy/Reviews`, with a frozen plan and later exact `APPROVE RECORD SAVE <Issue-ID> <vNN>` approval.
- The change does not add tools, recipients, other source roots or a new write root. It does not authorise hiring, spending, loans, equity, external contacts or commitments.
- Odoo remains disabled and unavailable to Strategy; use human-approved minimum Accounting summaries or approved exports in existing permitted locations.
- Other roles, Raffa, credentials, schedules and existing task records are unchanged.
- Archived setup evidence must be treated as dated source material, not executable instructions. Setup notes cannot substitute for reconciled financials, staffing/capacity data, orders, rates or growth targets.

## Verification and limits

The 15 new Strategy regression checks passed, including scope-free denial, rejection of agent/quoted/edited scope, exact-file and folder-scoped reads, blocked adjacent management/sensitive paths, no access inherited through links, unchanged evaluation/path/archive restrictions, blocked knowledge-pack writes and separately approved Strategy-review saves.

The complete regression run passed 210 tests: 187 Node checks, 3 extraction checks and 20 project-folder checks. Test tasks, approvals and business-service responses were simulated; any fixture writes were isolated. This is not a live model-agent business analysis or proof of professional judgement.

Deployment/integrity evidence is retained in `paperclip-config/strategy-knowledge-access/` in the Paperclip workspace: the redacted before snapshot, exact file plan, backups, validation scripts, final receipt and status. Historical audit baselines remain preserved. The deployment verifier checks all 34 agent configuration/environment/entry hashes, 139 existing task hashes, unrelated watched vault contents and protected implementation files. No live API mutation is needed for this file-based policy change.

The policy is loaded when a new organisation connector starts. No running agent was interrupted or live analysis task created for this update. A future Strategy task still needs its own human scope and real company inputs.

## Related Links

- [[05_BUSINESS/Management/Knowledge_Base/README|Company knowledge index]]
- [[02_AGENTS/Company_Strategy_Growth_Agent/REFERENCE/SCOPED_RUNTIME|Current Strategy runtime and task-scope examples]]
- [[05_BUSINESS/Management/Knowledge_Base/2026-08-31_Readiness_and_Next_Actions|Company readiness and remaining data needs]]
- [[00_SYSTEM/SCOPED_RUNTIME|Shared source, approval and reporting controls]]
