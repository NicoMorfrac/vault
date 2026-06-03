# Engineering Dashboard

## Recent Engineering Reports

```dataview
TABLE type, created, related_projects
FROM ""
WHERE source_agent = "Engineering"
SORT created DESC
LIMIT 30
```

## Active Projects

```dataview
TABLE created
FROM "08_PROJECTS"
SORT file.name ASC
```

## Engineering Reports Linked to Projects

```dataview
TABLE related_projects, created
FROM ""
WHERE source_agent = "Engineering"
AND length(related_projects) > 0
SORT created DESC
```

## Engineering Reports Linked to Findings

```dataview
TABLE related_findings, created
FROM ""
WHERE source_agent = "Engineering"
AND length(related_findings) > 0
SORT created DESC
```

## Reports Referencing K8

```dataview
TABLE source_agent, type, created
FROM ""
WHERE contains(related_projects, "K8")
SORT created DESC
```

## Reports Referencing SRW

```dataview
TABLE source_agent, type, created
FROM ""
WHERE contains(related_projects, "SRW")
SORT created DESC
```

## Reports Influenced by B2B Discoveries

```dataview
TABLE source_agent, type, created
FROM ""
WHERE length(related_findings) > 0
SORT created DESC
```

## Engineering Reports Missing Relationships

```dataview
TABLE created
FROM ""
WHERE source_agent = "Engineering"
AND length(related_findings) = 0
AND length(related_concepts) = 0
AND length(related_projects) = 0
AND length(related_reports) = 0
```