---
type: dashboard
source_agent: Codex
created: 2026-09-01
as_of: 2026-09-01
audience: internal
status: current_reference
approval_status: owner_requested_update
related_projects: []
related_reports:
  - "[[005 - DASHBOARD LATEST REPORTS AND INFORMATION]]"
  - "[[000 - DASHBOARD MORFRAC]]"
  - "[[001 - DASHBOARD AGENTS AND WORKFLOWS]]"
  - "[[05_BUSINESS/Management/Knowledge_Base/README]]"
---

```dashboard
title: MORFRAC Command Center
rows:
  - height: 132
    columns:
      - width: 3
        widget:
          type: link
          target: 005 - DASHBOARD LATEST REPORTS AND INFORMATION
          description: Live report feed, review queue, accepted records and information graphics.
      - width: 3
        widget:
          type: link
          target: 000 - DASHBOARD MORFRAC
          description: Company operations, governance and durable knowledge.
      - width: 3
        widget:
          type: link
          target: 001 - DASHBOARD AGENTS AND WORKFLOWS
          description: Agent roster, authority boundaries and workflow navigation.
      - width: 3
        widget:
          type: link
          target: 05_BUSINESS/Management/Knowledge_Base/README
          description: Current reference pack and evidence map.
  - height: 300
    columns:
      - width: 8
        widget:
          type: chart
          chart:
            type: bar
            sql: SELECT COUNT(*) FROM notes GROUP BY month(file.mtime) ORDER BY label asc
            title: Vault knowledge updated by month
            dataLabels: top
            showGridlines: false
            colors:
              - "#2a9d8f"
              - "#4e79a7"
            height: 270
      - width: 4
        widget:
          type: chart
          chart:
            type: doughnut
            sql: SELECT COUNT(*) WHERE source_agent IS NOT EMPTY AS "Agent records", COUNT(*) WHERE status IS NOT EMPTY AS "Status tagged", COUNT(*) WHERE approval_status IS NOT EMPTY AS "Approval tagged", COUNT(*) WHERE related_projects IS NOT EMPTY AS "Project linked" FROM notes
            title: Vault information signals
            dataLabels: outside
            colors:
              - "#4e79a7"
              - "#59a14f"
              - "#f28e2b"
              - "#e15759"
            height: 270
  - height: 240
    columns:
      - width: 6
        widget:
          type: markdown
          content: |
            ## Current attention
            - Open [[005 - DASHBOARD LATEST REPORTS AND INFORMATION#Needs human review or validation|needs human review or validation]].
            - Check [[005 - DASHBOARD LATEST REPORTS AND INFORMATION#Approved records|approved records]] before external use.
            - Check [[005 - DASHBOARD LATEST REPORTS AND INFORMATION#Achieved and current records|achieved and current records]] before planning.
            - Repair recent records listed under [[005 - DASHBOARD LATEST REPORTS AND INFORMATION#Metadata repair queue|metadata repair queue]].
      - width: 6
        widget:
          type: markdown
          content: |
            ## Source-of-truth boundary
            - **Obsidian:** durable reports, analysis and evidence.
            - **Paperclip:** live assignments, agent state and approvals.
            - **Odoo:** accounting source of truth once connected.
            - Revalidate prices, deadlines, regulations and live system state before decisions.
```

## Latest report preview

```dataview
TABLE WITHOUT ID
file.link AS Report,
source_agent AS Agent,
type AS Type,
status AS Status,
approval_status AS Approval,
dateformat(file.mtime, "yyyy-MM-dd HH:mm") AS Updated
FROM ""
WHERE source_agent
AND type != "dashboard"
SORT file.mtime DESC
LIMIT 12
```

> [!tip] Full report view
> Open [[005 - DASHBOARD LATEST REPORTS AND INFORMATION|Latest Reports and Information]] for charts, review queues, accepted records and metadata quality.
