---
type: b2b_convergence_concept
source_agent: B2B_Problem_Discovery
created: YYYY-MM-DD
related_findings: []
related_concepts: []
related_projects: []
related_reports: []
---

# CONCEPT_NAME

## DESCRIPTION

Describe the recurring convergence pattern without changing the existing taxonomy structure.

---

# LINKED FINDINGS

| Finding ID | Summary | Relevance |
|---|---|---|
| MORAAAAA-XX | Short summary | LOW / MEDIUM / HIGH |

---

# RECURRING ROOT CAUSES

- Root cause.

---

# RECURRING OPERATIONAL IMPACT

- Operational impact.

---

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

---

## Related Links

No structured related links identified.
