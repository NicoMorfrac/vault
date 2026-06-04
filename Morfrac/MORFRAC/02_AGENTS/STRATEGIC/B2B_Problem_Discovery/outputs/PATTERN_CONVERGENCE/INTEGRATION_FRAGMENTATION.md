---
type: b2b_convergence_concept
source_agent: B2B_Problem_Discovery
created: 2026-05-24
related_findings:
  - MORAAAAA-90-01_SYSTEM_INTEGRATION_proprietary_network_connector_fragmentation
  - MORAAAAA-90-02_SYSTEM_INTEGRATION_partial_mixed_brand_autopilot_interoperability
  - MORAAAAA-90-04_DOCUMENTATION_undocumented_oem_wiring_and_power_topology
related_concepts:
  - ENGINEERING_UNCERTAINTY
  - MECHANICAL_INTEGRATION_COMPLEXITY
  - RETROFIT_COMPLEXITY
related_projects: []
related_reports:
  - 2026-05-24_MORAAAAA-90_oem_vs_aftermarket_integration_friction_summary
---

# INTEGRATION_FRAGMENTATION

Business Intel taxonomy hub for fragmented integration patterns across related systems, suppliers, workflows, and retrofit contexts.

Related concept hubs:
- [[MECHANICAL_INTEGRATION_COMPLEXITY]]
- [[RETROFIT_COMPLEXITY]]
- [[ENGINEERING_UNCERTAINTY]]

---

# LINKED FINDINGS

| Finding ID | Summary | Relevance |
|---|---|---|
| MORAAAAA-90-01 | Proprietary network connector fragmentation | HIGH |
| MORAAAAA-90-02 | Mixed-brand autopilot interoperability | HIGH |
| MORAAAAA-90-04 | Undocumented OEM wiring and power topology | MEDIUM |

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

## Related Links

### Findings
- [[MORAAAAA-90-01_SYSTEM_INTEGRATION_proprietary_network_connector_fragmentation]]
- [[MORAAAAA-90-02_SYSTEM_INTEGRATION_partial_mixed_brand_autopilot_interoperability]]
- [[MORAAAAA-90-04_DOCUMENTATION_undocumented_oem_wiring_and_power_topology]]

### Concepts
- [[ENGINEERING_UNCERTAINTY]]
- [[MECHANICAL_INTEGRATION_COMPLEXITY]]
- [[RETROFIT_COMPLEXITY]]

### Reports
- [[2026-05-24_MORAAAAA-90_oem_vs_aftermarket_integration_friction_summary]]
