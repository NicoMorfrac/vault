# MORFRAC Dashboard

## Operations and Governance

- [[005 - DASHBOARD LATEST REPORTS AND INFORMATION|Latest reports and information — live charts, review queues and accepted records]]
- [[001 - DASHBOARD AGENTS AND WORKFLOWS|Agents and workflows dashboard — live roster, routing and workflow index]]
- [[00_SYSTEM/ORGANISATION|Current organisation, reporting lines and approval boundaries]]
- [[00_SYSTEM/SCOPED_RUNTIME|Scoped runtime, save and handoff controls]]
- [[05_BUSINESS/Management/Knowledge_Base/Evidence/2026-09-01_Model_Migration_GPT-5.6|Approved and achieved GPT-5.6 model migration]]

## Company Knowledge

- [[05_BUSINESS/Management/Knowledge_Base/README|MORFRAC knowledge index — structure, decisions, reports and readiness]]
- [[05_BUSINESS/Management/Knowledge_Base/2026-08-31_Readiness_and_Next_Actions|Current recorded readiness and next actions]]
- [[05_BUSINESS/Management/Knowledge_Base/2026-09-01_Yacht_Analysis_MVP|Yacht analysis team and on-demand workflow baseline]]

## Current Attention

- Use [[005 - DASHBOARD LATEST REPORTS AND INFORMATION#Needs human review or validation|Latest reports — review and validation queue]] before relying on draft analysis.
- Use [[001 - DASHBOARD AGENTS AND WORKFLOWS#Attention required|Agents and workflows — attention required]] for the current agent snapshot.
- Engineering is blocked by incomplete secret bindings; Research is manually paused.
- Raffa AI remains excluded from the vault-managed company-agent rollout. The legacy `02_AGENTS/Raffa_AI` folder is not a live Paperclip instruction root.
- Heartbeats, Odoo, Fusion/CAD and solver/machine integrations remain subject to the holds in [[00_SYSTEM/ORGANISATION#Explicit readiness holds|Explicit readiness holds]].

## Recent Generated Reports

```dataview
TABLE source_agent, type, status, approval_status, dateformat(file.mtime, "yyyy-MM-dd HH:mm") AS updated
FROM ""
WHERE source_agent
AND type != "dashboard"
SORT file.mtime DESC
LIMIT 25
```

## Reports Missing Relationships

```dataview
TABLE source_agent, type, created
FROM ""
WHERE source_agent
AND type != "dashboard"
AND length(related_findings) = 0
AND length(related_concepts) = 0
AND length(related_projects) = 0
AND length(related_reports) = 0
SORT created DESC
```

## Reports by Project

```dataview
TABLE source_agent, type, related_projects, created
FROM ""
WHERE length(related_projects) > 0
SORT created DESC
```

## Reports by Concept

```dataview
TABLE source_agent, type, related_concepts, created
FROM ""
WHERE length(related_concepts) > 0
SORT created DESC
```

## Reports by Finding

```dataview
TABLE source_agent, type, related_findings, created
FROM ""
WHERE length(related_findings) > 0
SORT created DESC
```
