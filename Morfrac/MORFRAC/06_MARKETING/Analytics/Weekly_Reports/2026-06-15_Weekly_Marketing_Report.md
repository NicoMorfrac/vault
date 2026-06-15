---
type: weekly_report
source_agent: Marketing
created: 2026-06-15
related_findings: []
related_concepts: []
related_projects:
  - GA4
related_reports:
  - 2026-06-15_GA4_Raw_Data
---

# Weekly Marketing Report

## Objective

Review MORFRAC website traffic performance using GA4 data and identify actionable changes.

## Executive Summary

- Current 7-day sessions: 177
- Previous 7-day sessions: 121
- 7-day sessions change: 46.3%
- Current 28-day sessions: 579
- Previous 28-day sessions: 942
- 28-day sessions change: -38.5%

## Key Metrics

| Metric | Current 7d | Previous 7d | Change | Current 28d | Previous 28d | Change |
|---|---:|---:|---:|---:|---:|---:|
| Sessions | 177 | 121 | 46.3% | 579 | 942 | -38.5% |
| Users | 147 | 98 | 50.0% | 473 | 849 | -44.3% |

## Critical Issues

- CRITICAL: Sessions dropped -38.5% over 28 days.

## Traffic Analysis

### Source / Medium

| sessionSourceMedium | sessions | totalUsers | engagedSessions |
| --- | --- | --- | --- |
| (direct) / (none) | 109 | 85 | 22 |
| google / organic | 45 | 34 | 30 |
| (not set) | 23 | 18 | 0 |
| bing / organic | 2 | 2 | 0 |
| app.inven.ai / referral | 1 | 1 | 1 |
| ecosia.org / organic | 1 | 1 | 1 |
| icexcrmglobal.lightning.force.com / referral | 1 | 1 | 1 |
| riggingmatters.gr / referral | 1 | 1 | 0 |

### Top Landing Pages

| landingPage | sessions | totalUsers | engagedSessions |
| --- | --- | --- | --- |
| / | 34 | 18 | 17 |
| (not set) | 12 | 11 | 0 |
| /shop | 11 | 10 | 3 |
| /morfblock | 9 | 9 | 3 |
|  | 7 | 7 | 0 |
| /dogbone | 7 | 6 | 3 |
| /powerfurl | 6 | 5 | 5 |
| /es | 5 | 4 | 4 |
| /shop/morfblock-light-4-hl-12823 | 5 | 1 | 4 |
| /es/my/orders/8035 | 4 | 2 | 0 |

### Device Analysis

| deviceCategory | sessions | totalUsers |
| --- | --- | --- |
| desktop | 139 | 104 |
| mobile | 38 | 26 |

### Geography

| country | sessions | totalUsers |
| --- | --- | --- |
| Spain | 34 | 15 |
| Singapore | 22 | 22 |
| Germany | 14 | 11 |
| United States | 14 | 14 |
| France | 13 | 7 |
| Netherlands | 12 | 7 |
| Australia | 10 | 4 |
| China | 9 | 8 |
| Hungary | 7 | 3 |
| Canada | 6 | 6 |

## Opportunities

Review manually:

- Pages with good sessions but low engaged sessions
- Sources bringing traffic with weak engagement
- Countries that may not match MORFRAC commercial targets
- Mobile vs desktop performance

## Recommendations

### Recommendation 1

- Action: Review top landing pages with low engagement.
- Reason: High traffic without engagement usually indicates weak intent match, weak CTA, or poor page structure.
- Expected impact: Better lead quality and improved conversion.
- Priority: Medium
- Data source: GA4

### Recommendation 2

- Action: Compare traffic sources by engagement before increasing effort in any channel.
- Reason: Session volume alone does not prove quality.
- Expected impact: Avoid wasting time on low-quality traffic.
- Priority: Medium
- Data source: GA4

## Sources

- Google Analytics 4
- Property ID: 435000386

## Traceability

- Date data pulled: 2026-06-15
- Raw GA4 file written: C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC\06_MARKETING\Analytics\Raw_Data\GA4\2026-06-15_GA4_Raw_Data.md
- Weekly report written: C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC\06_MARKETING\Analytics\Weekly_Reports\2026-06-15_Weekly_Marketing_Report.md
- Script used: weekly_ga4_report.py

## Related Links

### Projects
- [[GA4]]

### Reports
- [[2026-06-15_GA4_Raw_Data]]
