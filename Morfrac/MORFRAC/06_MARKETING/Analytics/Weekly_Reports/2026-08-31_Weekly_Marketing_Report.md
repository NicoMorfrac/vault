---
type: weekly_report
source_agent: Marketing
created: 2026-08-31
related_findings: []
related_concepts: []
related_projects:
  - GA4
related_reports:
  - 2026-08-31_GA4_Raw_Data
---

# Weekly Marketing Report

## Objective

Review MORFRAC website traffic performance using GA4 data and identify actionable changes.

## Executive Summary

- Current 7-day sessions: 232
- Previous 7-day sessions: 2280
- 7-day sessions change: -89.8%
- Current 28-day sessions: 2808
- Previous 28-day sessions: 1248
- 28-day sessions change: 125.0%

## Key Metrics

| Metric | Current 7d | Previous 7d | Change | Current 28d | Previous 28d | Change |
|---|---:|---:|---:|---:|---:|---:|
| Sessions | 232 | 2280 | -89.8% | 2808 | 1248 | 125.0% |
| Users | 208 | 2258 | -90.8% | 2740 | 1149 | 138.5% |

## Critical Issues

- CRITICAL: Sessions dropped -89.8% over 7 days.

## Traffic Analysis

### Source / Medium

| sessionSourceMedium | sessions | totalUsers | engagedSessions |
| --- | --- | --- | --- |
| (direct) / (none) | 152 | 142 | 17 |
| google / organic | 36 | 23 | 22 |
| (not set) | 33 | 24 | 10 |
| (data not available) | 7 | 7 | 0 |
| bing / organic | 4 | 2 | 3 |
| scrub.sourcescrub.com / referral | 4 | 4 | 3 |
| sunblog.asia / referral | 2 | 2 | 0 |
| IGShopping / Social | 1 | 1 | 1 |
| duckduckgo / organic | 1 | 1 | 1 |
| ig / social | 1 | 1 | 0 |

### Top Landing Pages

| landingPage | sessions | totalUsers | engagedSessions |
| --- | --- | --- | --- |
| / | 27 | 18 | 20 |
| /shop | 17 | 17 | 4 |
| (not set) | 15 | 15 | 0 |
|  | 14 | 13 | 0 |
| /es/shop/padeye-through-6t-through-deck-padeye-12655 | 12 | 8 | 1 |
| /shopproduct-category/morf-block-xl | 10 | 10 | 1 |
| /shopour-office | 6 | 6 | 0 |
| /shopreferral-program | 6 | 6 | 0 |
| /dogbone | 5 | 5 | 1 |
| /shopmb04-bearing/wichard | 5 | 5 | 0 |

### Device Analysis

| deviceCategory | sessions | totalUsers |
| --- | --- | --- |
| desktop | 196 | 167 |
| mobile | 35 | 27 |
| tablet | 1 | 1 |

### Geography

| country | sessions | totalUsers |
| --- | --- | --- |
| Singapore | 63 | 57 |
| United States | 34 | 31 |
| Vietnam | 31 | 31 |
| Spain | 25 | 14 |
| China | 11 | 11 |
| United Kingdom | 8 | 5 |
| Poland | 7 | 4 |
| Germany | 6 | 3 |
| Netherlands | 6 | 3 |
| Philippines | 6 | 5 |

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

- Date data pulled: 2026-08-31
- Raw GA4 file written: C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC\06_MARKETING\Analytics\Raw_Data\GA4\2026-08-31_GA4_Raw_Data.md
- Weekly report written: C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC\06_MARKETING\Analytics\Weekly_Reports\2026-08-31_Weekly_Marketing_Report.md
- Script used: weekly_ga4_report.py

## Related Links

### Projects
- [[GA4]]

### Reports
- [[2026-08-31_GA4_Raw_Data]]
