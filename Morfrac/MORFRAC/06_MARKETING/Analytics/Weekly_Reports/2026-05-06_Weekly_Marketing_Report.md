---
type: weekly_report
source_agent: Marketing
created: 2026-05-06
related_findings: []
related_concepts: []
related_projects:
  - GA4
related_reports:
  - 2026-05-06_GA4_Raw_Data
---

# Weekly Marketing Report

## Objective

Review MORFRAC website traffic performance using GA4 data and identify actionable changes.

## Executive Summary

- Current 7-day sessions: 198
- Previous 7-day sessions: 195
- 7-day sessions change: 1.5%
- Current 28-day sessions: 752
- Previous 28-day sessions: 1180
- 28-day sessions change: -36.3%

## Key Metrics

| Metric | Current 7d | Previous 7d | Change | Current 28d | Previous 28d | Change |
|---|---:|---:|---:|---:|---:|---:|
| Sessions | 198 | 195 | 1.5% | 752 | 1180 | -36.3% |
| Users | 184 | 166 | 10.8% | 667 | 1092 | -38.9% |

## Critical Issues

- CRITICAL: Sessions dropped -36.3% over 28 days.

## Traffic Analysis

### Source / Medium

| sessionSourceMedium | sessions | totalUsers | engagedSessions |
| --- | --- | --- | --- |
| (direct) / (none) | 149 | 135 | 31 |
| google / organic | 36 | 32 | 22 |
| (not set) | 22 | 22 | 0 |
| balatonrigging.hu / referral | 1 | 1 | 0 |
| duckduckgo / organic | 1 | 1 | 1 |
| es.search.yahoo.com / referral | 1 | 1 | 1 |
| riggingmatters.gr / referral | 1 | 1 | 0 |

### Top Landing Pages

| landingPage | sessions | totalUsers | engagedSessions |
| --- | --- | --- | --- |
| / | 22 | 18 | 12 |
|  | 16 | 15 | 0 |
| /dogbone | 7 | 6 | 3 |
| (not set) | 6 | 6 | 0 |
| /morfblock | 6 | 6 | 3 |
| /shop | 5 | 5 | 0 |
| /shop/dogbone-dogbone-ti-29/dogbone40-12-ti-12462 | 5 | 1 | 3 |
| /web/login | 5 | 4 | 2 |
| /es | 4 | 3 | 4 |
| /morfwing | 4 | 3 | 1 |

### Device Analysis

| deviceCategory | sessions | totalUsers |
| --- | --- | --- |
| desktop | 162 | 152 |
| mobile | 34 | 24 |
| tablet | 1 | 1 |

### Geography

| country | sessions | totalUsers |
| --- | --- | --- |
| United States | 31 | 24 |
| Vietnam | 28 | 28 |
| Spain | 21 | 13 |
| China | 19 | 19 |
| Hong Kong | 17 | 17 |
| Singapore | 15 | 15 |
| Brazil | 11 | 11 |
| Indonesia | 10 | 10 |
| Germany | 7 | 6 |
| Italy | 7 | 6 |

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

- Date data pulled: 2026-05-06
- Raw GA4 file written: C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC\06_MARKETING\Analytics\Raw_Data\GA4\2026-05-06_GA4_Raw_Data.md
- Weekly report written: C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC\06_MARKETING\Analytics\Weekly_Reports\2026-05-06_Weekly_Marketing_Report.md
- Script used: weekly_ga4_report.py

## Related Links

### Projects
- [[GA4]]

### Reports
- [[2026-05-06_GA4_Raw_Data]]
