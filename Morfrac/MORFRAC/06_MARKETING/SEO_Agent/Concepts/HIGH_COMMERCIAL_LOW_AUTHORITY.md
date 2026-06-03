---
type: concept_hub
source_agent: SEO_Agent
created: 2026-06-03
related_findings: []
related_concepts: []
related_projects: []
related_reports: []
---

# HIGH_COMMERCIAL_LOW_AUTHORITY

SEO taxonomy hub for commercially important topics that have insufficient authority support or weak supporting content structure.

## Auto-Indexed Relationships

### Linked Reports

```dataview
TABLE source_agent, type, created
FROM ""
WHERE contains(related_concepts, this.file.name)
SORT created DESC
```

### Related Projects

```dataview
TABLE related_projects, source_agent, created
FROM ""
WHERE contains(related_concepts, this.file.name)
   AND length(related_projects) > 0
SORT created DESC
```

