# SEO Dashboard

## Recent SEO Reports

```dataview
TABLE type, created, related_projects, related_concepts
FROM "06_MARKETING"
WHERE source_agent = "SEO_Agent"
SORT created DESC
LIMIT 30
```

## SEO Action Plans

```dataview
TABLE created, related_concepts, related_projects
FROM "06_MARKETING/SEO_Agent/Action_Plans"
SORT created DESC
```

## SEO Executive Reviews

```dataview
TABLE created, related_projects, related_concepts
FROM "06_MARKETING/SEO_Agent/Executive_Reviews"
SORT created DESC
```

## Search Console Related Reports

```dataview
TABLE source_agent, type, created
FROM ""
WHERE contains(related_projects, "Search Console")
SORT created DESC
```

## GA4 Related Reports

```dataview
TABLE source_agent, type, created
FROM ""
WHERE contains(related_projects, "GA4")
SORT created DESC
```

## SEO Concept Reports

```dataview
TABLE related_concepts, type, created
FROM ""
WHERE source_agent = "SEO_Agent" AND length(related_concepts) > 0
SORT created DESC
```

## SEO Reports Missing Relationships

```dataview
TABLE type, created
FROM ""
WHERE source_agent = "SEO_Agent"
AND length(related_findings) = 0
AND length(related_concepts) = 0
AND length(related_projects) = 0
AND length(related_reports) = 0
SORT created DESC
```