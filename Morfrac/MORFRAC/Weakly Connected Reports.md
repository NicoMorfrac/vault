## Reports Missing Relationships

```dataview
TABLE source_agent, created
FROM ""
WHERE
length(related_findings)=0 AND
length(related_concepts)=0 AND
length(related_projects)=0 AND
length(related_reports)=0
```