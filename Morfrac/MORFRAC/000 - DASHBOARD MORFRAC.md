# MORFRAC Dashboard

## Operations and Governance

- [[005 - DASHBOARD LATEST REPORTS AND INFORMATION|Latest reports and information — live charts, review queues and accepted records]]
- [[001 - DASHBOARD AGENTS AND WORKFLOWS|Agents and workflows dashboard — live roster, routing and workflow index]]
- [[00_SYSTEM/ORGANISATION|Current organisation, reporting lines and approval boundaries]]
- [[00_SYSTEM/SCOPED_RUNTIME|Scoped runtime, save and handoff controls]]
- [[05_BUSINESS/Management/Knowledge_Base/Evidence/2026-09-01_Model_Migration_GPT-5.6|Approved and achieved GPT-5.6 model migration]]
- [[05_BUSINESS/Management/Knowledge_Base/Evidence/2026-09-02_Paperclip_Connector_Runtime_and_Attachment_Repair|Paperclip connector runtime and attachment repair — validated]]

## Company Knowledge

- [[05_BUSINESS/Management/Knowledge_Base/README|MORFRAC knowledge index — structure, decisions, reports and readiness]]
- [[05_BUSINESS/Management/Knowledge_Base/2026-08-31_Readiness_and_Next_Actions|Current recorded readiness and next actions]]
- [[05_BUSINESS/Management/Knowledge_Base/2026-09-01_Yacht_Analysis_MVP|Yacht analysis team and on-demand workflow baseline]]
- [[05_BUSINESS/Management/Knowledge_Base/Evidence/2026-09-01_Fusion_360_and_Drafting_CAD_Agent|Fusion installation and 2D/3D Drafting/CAD agent configuration]]
- [[05_BUSINESS/Management/Knowledge_Base/Evidence/2026-09-01_Nico_AI_Authentication_Repair|Nico AI authentication repair and validation]]
- [[05_BUSINESS/Management/Knowledge_Base/Evidence/2026-09-01_Company_Wide_Agent_Authentication_Repair|Company-wide agent authentication repair and validation]]
- [[05_BUSINESS/Management/Knowledge_Base/Evidence/2026-09-02_Paperclip_Connector_Runtime_and_Attachment_Repair|Scoped connector, task attachment and blocked-state repair]]

## Current Attention

- Use [[005 - DASHBOARD LATEST REPORTS AND INFORMATION#Needs human review or validation|Latest reports — review and validation queue]] before relying on draft analysis.
- Use [[001 - DASHBOARD AGENTS AND WORKFLOWS#Attention required|Agents and workflows — attention required]] for the current agent snapshot.
- The company-agent connector repair is validated: 42 approved agents use the CLI runtime and scoped task-attachment reader; 115 connector/workflow and 3 PDF tests pass.
- `MORAAAAA-141` is cleanly blocked with no active execution. It awaits complete geometry or approval for a non-production approximation, output-format confirmation and separate Drafting/Fusion runtime-routing approval.
- The last automatic validation run met the account usage limit. This is a temporary provider-capacity condition, not a connector failure. Research remains manually paused.
- Fusion is installed and the Drafting/CAD identity and instructions are configured. Scoped runtime routing still requires separate owner approval; the read-only API probe and supervised 3D/2D execution tests are also pending.
- Raffa AI remains excluded from the vault-managed company-agent rollout. The legacy `02_AGENTS/Raffa_AI` folder is not a live Paperclip instruction root.
- Heartbeats, Odoo, Fusion execution, FEA/CAM solver/toolpath/post and machine integrations remain subject to the holds in [[00_SYSTEM/ORGANISATION#Explicit readiness holds|Explicit readiness holds]].

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
