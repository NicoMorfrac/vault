---
type: seo_pipeline_health_report
source_agent: SEO_Agent
created: 2026-08-17
related_findings: []
related_concepts: []
related_projects:
  - Search Console
related_reports:
  - pipeline_health_report
---

# MORFRAC SEO Pipeline Health Check

## Generated

2026-08-17

---

# Overall Status

**PASS**

| Result | Count |
|---|---:|
| PASS | 10 |
| WARN | 0 |
| FAIL | 0 |

---

# Critical Failures

No data available.

---

# Warnings

No data available.

---

# Full Pipeline Check

| check_name | status | severity | fresh_today | row_count | min_expected_rows | missing_columns | notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Crawl CSV | PASS | OK | True | 500 | 50 |  | Output looks usable. |
| Search Console Merge | PASS | OK | True | 4 | 1 |  | Output looks usable. |
| Internal Link Graph Pages | PASS | OK | True | 500 | 50 |  | Output looks usable. |
| Contextual Link Recommendations | PASS | OK | True | 908 | 10 |  | Output looks usable. |
| Semantic Cluster Summary | PASS | OK | True | 12 | 3 |  | Output looks usable. |
| Semantic Cluster Pages | PASS | OK | True | 260 | 50 |  | Output looks usable. |
| Content Gap Analysis | PASS | OK | True | 11 | 1 |  | Output looks usable. |
| Topic Authority Map | PASS | OK | True | 12 | 3 |  | Output looks usable. |
| Executive Review | PASS | OK | True | 240 | 0 |  | Output looks usable. |
| Historical Comparison | PASS | OK | True | 108 | 0 |  | Output looks usable. |

---

# Interpretation

Use this report before trusting the SEO executive review.

- `FAIL` means a required output is missing, empty, stale in structure, or missing required columns.
- `WARN` means the pipeline likely ran but has stale or optional/marginal outputs.
- `PASS` means the output exists, is fresh, and has usable structure.

If this report fails, fix the failing upstream script before relying on executive conclusions.

---

# Output Files

- Health CSV: `C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC\06_MARKETING\SEO_Agent\Pipeline_Health\2026-08-17_pipeline_health_check.csv`
- Stable health CSV: `C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC\06_MARKETING\SEO_Agent\Pipeline_Health\pipeline_health_check.csv`
- Health report: `C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC\06_MARKETING\SEO_Agent\Pipeline_Health\2026-08-17_pipeline_health_report.md`
- Stable health report: `C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC\06_MARKETING\SEO_Agent\Pipeline_Health\pipeline_health_report.md`

## Related Links

### Projects
- [[Search Console]]

### Reports
- [[pipeline_health_report]]
