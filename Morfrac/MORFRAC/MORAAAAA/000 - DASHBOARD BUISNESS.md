# Business Dashboard

## Recent Business Reports

```dataview
TABLE source_agent, type, created
FROM "05_BUSINESS"
SORT created DESC
LIMIT 25
```

## Recent B2B Findings

```dataview
TABLE created, related_concepts
FROM ""
WHERE regexmatch("^MORAAAAAA-", file.name)
SORT file.name DESC
```

## Findings by Concept

```dataview
TABLE related_concepts, created
FROM ""
WHERE length(related_concepts) > 0
SORT created DESC
```

## Retrofit Complexity

```dataview
TABLE source_agent, type, created
FROM ""
WHERE contains(related_concepts, "RETROFIT_COMPLEXITY")
SORT created DESC
```

## Mechanical Integration Complexity

```dataview
TABLE source_agent, type, created
FROM ""
WHERE contains(related_concepts, "MECHANICAL_INTEGRATION_COMPLEXITY")
SORT created DESC
```

## Serviceability Complexity

```dataview
TABLE source_agent, type, created
FROM ""
WHERE contains(related_concepts, "SERVICEABILITY_COMPLEXITY")
SORT created DESC
```

## Strategic Opportunities

```dataview
TABLE created
FROM "05_BUSINESS/Strategic_Opportunities"
SORT created DESC
```

## B2B Discovery Outputs

```dataview
TABLE type, created, related_concepts
FROM ""
WHERE source_agent = "B2B_Problem_Discovery"
SORT created DESC
```

## Reports Missing Relationships

```dataview
TABLE source_agent, created
FROM ""
WHERE source_agent = "B2B_Problem_Discovery"
AND length(related_findings) = 0
AND length(related_concepts) = 0
AND length(related_projects) = 0
AND length(related_reports) = 0
```