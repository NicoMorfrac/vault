---
type: weekly_report
source_agent: Marketing
created: 2026-06-22
related_findings: []
related_concepts: []
related_projects:
  - GA4
related_reports:
  - 2026-06-22_GA4_Raw_Data
---

# Weekly Marketing Report

## Objective

Review MORFRAC website traffic performance using GA4 data and identify actionable changes.

## Executive Summary

- Current 7-day sessions: 182
- Previous 7-day sessions: 166
- 7-day sessions change: 9.6%
- Current 28-day sessions: 622
- Previous 28-day sessions: 870
- 28-day sessions change: -28.5%

## Key Metrics

| Metric | Current 7d | Previous 7d | Change | Current 28d | Previous 28d | Change |
|---|---:|---:|---:|---:|---:|---:|
| Sessions | 182 | 166 | 9.6% | 622 | 870 | -28.5% |
| Users | 151 | 136 | 11.0% | 505 | 794 | -36.4% |

## Critical Issues

- CRITICAL: Sessions dropped -28.5% over 28 days.

## Traffic Analysis

### Source / Medium

| sessionSourceMedium | sessions | totalUsers | engagedSessions |
| --- | --- | --- | --- |
| (direct) / (none) | 116 | 97 | 25 |
| google / organic | 48 | 35 | 33 |
| (not set) | 15 | 9 | 5 |
| (data not available) | 2 | 2 | 0 |
| google / cpc | 1 | 1 | 1 |
| northsails.crm.dynamics.com / referral | 1 | 1 | 0 |
| youtube.com / referral | 1 | 1 | 1 |

### Top Landing Pages

| landingPage | sessions | totalUsers | engagedSessions |
| --- | --- | --- | --- |
| /shop | 22 | 22 | 2 |
| / | 19 | 14 | 13 |
| (not set) | 6 | 6 | 0 |
| /padeye | 6 | 6 | 2 |
| /shop/cart | 6 | 2 | 0 |
| /shopcontact-us | 6 | 6 | 0 |
| /shopprivacy-policy | 6 | 6 | 1 |
| /morfwing | 5 | 5 | 2 |
| /shopproduct/dogbone-40 | 5 | 5 | 0 |
| /dogbone | 4 | 4 | 2 |

### Device Analysis

| deviceCategory | sessions | totalUsers |
| --- | --- | --- |
| desktop | 142 | 116 |
| mobile | 36 | 22 |
| tablet | 4 | 4 |

### Geography

| country | sessions | totalUsers |
| --- | --- | --- |
| Spain | 39 | 21 |
| Singapore | 35 | 35 |
| United States | 24 | 23 |
| Vietnam | 10 | 10 |
| Australia | 9 | 1 |
| France | 9 | 5 |
| United Kingdom | 7 | 6 |
| Bangladesh | 6 | 6 |
| China | 6 | 6 |
| Finland | 5 | 3 |

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

- Date data pulled: 2026-06-22
- Raw GA4 file written: C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC\06_MARKETING\Analytics\Raw_Data\GA4\2026-06-22_GA4_Raw_Data.md
- Weekly report written: C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC\06_MARKETING\Analytics\Weekly_Reports\2026-06-22_Weekly_Marketing_Report.md
- Script used: weekly_ga4_report.py

## Related Links

### Projects
- [[GA4]]

### Reports
- [[2026-06-22_GA4_Raw_Data]]
