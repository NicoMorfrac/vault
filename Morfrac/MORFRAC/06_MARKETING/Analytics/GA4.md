---
type: project_hub
source_agent: Marketing
created: 2026-06-03
related_findings: []
related_concepts: []
related_projects: []
related_reports: []
---

# GA4

Hub note for MORFRAC GA4 traffic reporting, weekly marketing analytics, traffic quality analysis, and LLM marketing reviews.

## Auto-Indexed Relationships

### Linked Reports

```dataview
TABLE source_agent, type, created
FROM ""
WHERE contains(related_projects, this.file.name)
   OR contains(related_reports, this.file.name)
SORT created DESC
```

### Related Reports By Agent

```dataview
TABLE type, created, related_reports
FROM ""
WHERE contains(related_projects, this.file.name)
SORT source_agent ASC, created DESC
```

