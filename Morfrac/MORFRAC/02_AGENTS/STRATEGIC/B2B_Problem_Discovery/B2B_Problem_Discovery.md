---
type: agent_hub
source_agent: B2B_Problem_Discovery
created: 2026-06-03
related_findings: []
related_concepts: []
related_projects: []
related_reports: []
---

# B2B_Problem_Discovery

Hub note for B2B problem discovery outputs, raw findings, weekly strategic summaries, and pattern-convergence reports.

## Auto-Indexed Relationships

### Agent Reports

```dataview
TABLE type, created, related_findings, related_concepts
FROM ""
WHERE source_agent = this.file.name
SORT created DESC
```

### Related Findings

```dataview
TABLE related_concepts, related_projects, created
FROM ""
WHERE source_agent = this.file.name
   AND length(related_findings) > 0
SORT created DESC
```

