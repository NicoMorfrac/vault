---
type: generated_report
source_agent: SEO_Agent
created: 2026-05-14
related_findings: []
related_concepts: []
related_projects:
  - Search Console
related_reports: []
---

# SEO Query Leverage Opportunity Report

## Generated

2026-05-14

## Summary

This report identifies filtered Search Console query opportunities.

Current filters applied:

- non-branded queries only
- duplicate query removal
- obvious junk-query filtering
- minimum impression threshold
- deterministic intent classification
- expected CTR and CTR gap scoring

It is query-level only.

It does not yet correlate queries with crawl/page metadata.

---

# Highest Leverage Query Opportunities

| query           |   clicks |   impressions |   ctr_percent |   expected_ctr |   ctr_gap |   position | query_type   | intent       |   opportunity_score | opportunity_level   |
|:----------------|---------:|--------------:|--------------:|---------------:|----------:|-----------:|:-------------|:-------------|--------------------:|:--------------------|
| dogbones        |        1 |           134 |          0.75 |            0.8 |      0.05 |      16.77 | Non-branded  | commercial   |                  75 | HIGH                |
| 60-23           |        0 |             5 |          0    |            3   |      3    |       7.6  | Non-branded  | product_code |                  75 | HIGH                |
| cancamo pasante |        0 |             7 |          0    |            2.5 |      2.5  |       8.86 | Non-branded  | commercial   |                  75 | HIGH                |
| farr x2         |        2 |            38 |          5.26 |            3.5 |     -1.76 |       6.68 | Non-branded  | commercial   |                  65 | HIGH                |
| d shackle       |        0 |            11 |          0    |            1   |      1    |      10.91 | Non-branded  | commercial   |                  65 | HIGH                |
| soft pad eye    |        1 |             5 |         20    |            4   |    -16    |       5.8  | Non-branded  | commercial   |                  55 | MEDIUM              |

---

# Interpretation Notes

Higher opportunity scores indicate:

- existing search visibility
- CTR below expected for current ranking position
- near-page-one ranking potential
- commercial/product intent
- non-branded discovery potential

CTR gap means:

expected CTR minus actual CTR.

Intent categories:

- commercial = generic high-intent product/service discovery
- product_code = MORFRAC/product-size code discovery
- product_brand = MORFRAC product-brand discovery
- unknown = insufficient deterministic intent signal

This is a filtered query-level SEO leverage report.

## Related Links

### Projects
- [[Search Console]]
