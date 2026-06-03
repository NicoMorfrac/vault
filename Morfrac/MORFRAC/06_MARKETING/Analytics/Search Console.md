---
type: project_hub
source_agent: Marketing
created: 2026-06-03
related_findings: []
related_concepts: []
related_projects: []
related_reports: []
---

# Search Console

Hub note for MORFRAC Search Console reporting, query analysis, SEO visibility, and search-performance workflows.

## Auto-Indexed Relationships

### Linked Reports

```dataview
TABLE source_agent, type, created
FROM ""
WHERE contains(related_projects, this.file.name)
   OR contains(related_reports, this.file.name)
SORT created DESC
```

### Related Concepts

```dataview
TABLE related_concepts, created
FROM ""
WHERE contains(related_projects, this.file.name)
   AND length(related_concepts) > 0
SORT created DESC
```

