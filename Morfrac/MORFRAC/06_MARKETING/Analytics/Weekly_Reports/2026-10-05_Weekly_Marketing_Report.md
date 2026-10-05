---
type: weekly_report
source_agent: Marketing
created: 2026-10-05
related_findings: []
related_concepts: []
related_projects:
  - GA4
related_reports:
  - 2026-10-05_GA4_Raw_Data
---

# Weekly Marketing Report

## Objective

Review MORFRAC website traffic performance using GA4 data and identify actionable changes.

## Executive Summary

- Current 7-day sessions: 184
- Previous 7-day sessions: 651
- 7-day sessions change: -71.7%
- Current 28-day sessions: 1267
- Previous 28-day sessions: 3259
- 28-day sessions change: -61.1%

## Key Metrics

| Metric | Current 7d | Previous 7d | Change | Current 28d | Previous 28d | Change |
|---|---:|---:|---:|---:|---:|---:|
| Sessions | 184 | 651 | -71.7% | 1267 | 3259 | -61.1% |
| Users | 170 | 602 | -71.8% | 1151 | 3189 | -63.9% |

## Critical Issues

- CRITICAL: Sessions dropped -71.7% over 7 days.
- CRITICAL: Sessions dropped -61.1% over 28 days.

## Traffic Analysis

### Source / Medium

| sessionSourceMedium | sessions | totalUsers | engagedSessions |
| --- | --- | --- | --- |
| (direct) / (none) | 100 | 97 | 16 |
| google / organic | 65 | 47 | 35 |
| (not set) | 16 | 15 | 1 |
| bing / organic | 2 | 2 | 1 |
| chatgpt.com / ai-assistant | 1 | 1 | 1 |

### Top Landing Pages

| landingPage | sessions | totalUsers | engagedSessions |
| --- | --- | --- | --- |
| / | 28 | 21 | 16 |
| /padeye | 10 | 10 | 3 |
| (not set) | 9 | 9 | 0 |
| /morfwing | 7 | 7 | 2 |
| /powerfurl | 7 | 6 | 3 |
| /blog/stories-4/aluminium-titanium-stainless-steel-39 | 6 | 5 | 1 |
| /dogbone | 6 | 6 | 1 |
| /es | 6 | 6 | 4 |
| /shop | 6 | 6 | 2 |
| /morfblock | 5 | 3 | 1 |

### Device Analysis

| deviceCategory | sessions | totalUsers |
| --- | --- | --- |
| desktop | 155 | 137 |
| mobile | 29 | 25 |

### Geography

| country | sessions | totalUsers |
| --- | --- | --- |
| United States | 65 | 60 |
| China | 31 | 31 |
| Spain | 27 | 14 |
| Germany | 11 | 10 |
| Singapore | 11 | 11 |
| United Kingdom | 8 | 8 |
| Italy | 6 | 4 |
| Vietnam | 5 | 5 |
| Finland | 3 | 3 |
| Australia | 2 | 2 |

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

- Date data pulled: 2026-10-05
- Raw GA4 file written: C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC\06_MARKETING\Analytics\Raw_Data\GA4\2026-10-05_GA4_Raw_Data.md
- Weekly report written: C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC\06_MARKETING\Analytics\Weekly_Reports\2026-10-05_Weekly_Marketing_Report.md
- Script used: weekly_ga4_report.py

## Related Links

### Projects
- [[GA4]]

### Reports
- [[2026-10-05_GA4_Raw_Data]]
