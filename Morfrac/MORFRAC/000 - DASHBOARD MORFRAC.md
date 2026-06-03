# MORFRAC Dashboard

## Recent Generated Reports

```dataview
TABLE source_agent, type, created
FROM ""
WHERE source_agent
SORT created DESC
LIMIT 25
```

## Reports Missing Relationships

```dataview
TABLE source_agent, type, created
FROM ""
WHERE source_agent
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