# INTEGRATION_FRAGMENTATION

Business Intel taxonomy hub for fragmented integration patterns across related systems, suppliers, workflows, and retrofit contexts.

Related concept hubs:
- [[MECHANICAL_INTEGRATION_COMPLEXITY]]
- [[RETROFIT_COMPLEXITY]]
- [[ENGINEERING_UNCERTAINTY]]

## Auto-Indexed Relationships

### Related Findings

```dataview
TABLE source_agent, type, created, related_concepts
FROM ""
WHERE contains(related_concepts, this.file.name)
AND length(related_findings) > 0
SORT created DESC
```

### Related Reports

```dataview
TABLE source_agent, type, created
FROM ""
WHERE contains(related_concepts, this.file.name)
SORT created DESC
```

### Related Strategic Opportunities

```dataview
TABLE source_agent, type, created
FROM "05_BUSINESS/Strategic_Opportunities"
WHERE contains(related_concepts, this.file.name)
SORT created DESC
```

### Related Projects

```dataview
TABLE source_agent, type, created, related_projects
FROM ""
WHERE contains(related_concepts, this.file.name)
AND length(related_projects) > 0
SORT created DESC
```

### Related Agents / Sources

```dataview
TABLE source_agent, type, created
FROM ""
WHERE contains(related_concepts, this.file.name)
SORT source_agent ASC, created DESC
```
