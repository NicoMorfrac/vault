---
type: setup_knowledge
source_agent: Codex
created: 2026-09-01
audience: internal
status: achieved
approval_status: approved
approval_reference: APPROVE MORFRAC MODEL MIGRATION
as_of: 2026-09-01
related_findings:
  - Paperclip model catalogue refreshed after upgrade
  - GPT-5.6 role-based migration completed
  - Engineering secret bindings remain incomplete
  - Research remains manually paused
related_concepts:
  - Paperclip agent model governance
  - Role-based model allocation
  - Human approval boundaries
related_projects: []
related_reports:
  - 2026-08-31_Operating_Baseline
  - 2026-08-31_Readiness_and_Next_Actions
---

# MORFRAC Paperclip GPT-5.6 Model Migration

## Objective and scope

Record the owner-approved migration of the active MORFRAC Paperclip company's agent models after upgrading Paperclip to version `2026.824.1`. The scope was limited to the `adapterConfig.model` field for 42 agents. Reasoning levels, instructions, tools, permissions, runtime schedules and reporting structure were outside the approval scope.

Raffa AI was expressly excluded and remained unchanged on `gpt-5.5` with medium reasoning.

## Approval and achieved result

The human owner supplied the exact approval `APPROVE MORFRAC MODEL MIGRATION` on 2026-09-01.

The achieved live allocation is:

- `gpt-5.6-sol`: 17 agents, all retaining high reasoning.
- `gpt-5.6-terra`: 23 agents; 17 retain high reasoning and 6 retain medium reasoning.
- `gpt-5.6-luna`: 2 agents, both retaining medium reasoning.
- `gpt-5.5`: Raffa AI only, retaining medium reasoning.

## Validation evidence

- Paperclip health returned version `2026.824.1` and healthy status.
- The refreshed `codex_local` catalogue listed `gpt-5.6-sol`, `gpt-5.6-terra` and `gpt-5.6-luna`.
- All 42 approved live records matched the role-based target roster after migration.
- Reasoning effort remained unchanged for every migrated agent.
- Agent permissions remained unchanged.
- Raffa AI's adapter configuration and permissions remained unchanged.
- Minimal read-only runtime requests succeeded independently on Sol, Terra and Luna and returned the expected `MODEL_OK` response.
- Paperclip automatically added an isolated `CODEX_HOME` and explicit secret-projection metadata to 14 legacy adapter configurations when they were saved. Revision comparison found no other non-model differences. This was server-owned configuration normalisation, not an expansion of agent authority.

The guarded implementation and repeatable verifier are retained at `paperclip-config/migrate-models-gpt-5.6.ps1` in the implementation workspace.

## Limitations and unresolved items

- This migration confirms model availability and configuration integrity; it is not a domain-quality evaluation of every agent workflow.
- Engineering remains in error because its required OpenAI and Anthropic secret bindings are incomplete. The model change did not cause or repair that condition.
- Research remains manually paused.
- Heartbeats remain disabled as previously decided.
- The post-upgrade `canCreateSkills` permission state was deliberately not altered because it requires its own approval and review.

## Next actions

1. Evaluate representative tasks at the retained reasoning level before considering a one-level reduction for cost or latency.
2. Resolve Engineering secret bindings through a separate approved configuration task.
3. Review and approve the intended agent skill-creation permission baseline separately.
4. Resume Research only when the human owner decides its work should continue.

## Related Links

- [[05_BUSINESS/Management/Knowledge_Base/2026-08-31_Operating_Baseline]]
- [[05_BUSINESS/Management/Knowledge_Base/2026-08-31_Readiness_and_Next_Actions]]
- [[05_BUSINESS/Management/Knowledge_Base/README]]
