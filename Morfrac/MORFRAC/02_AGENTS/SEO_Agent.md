---
type: agent_hub
source_agent: SEO_Agent
created: 2026-06-03
related_findings: []
related_concepts: []
related_projects: []
related_reports: []
---

# SEO_Agent

Hub note for generated SEO pipeline outputs, deterministic SEO analyses, and agent-authored SEO reports.

## Auto-Indexed Relationships

### Agent Reports

```dataview
TABLE type, created, related_concepts, related_projects
FROM ""
WHERE source_agent = this.file.name
SORT created DESC
```

### Linked Concepts

```dataview
TABLE related_concepts, type, created
FROM ""
WHERE source_agent = this.file.name
   AND length(related_concepts) > 0
SORT created DESC
```

