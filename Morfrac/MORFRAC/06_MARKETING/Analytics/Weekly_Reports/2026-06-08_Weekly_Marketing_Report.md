---
type: weekly_report
source_agent: Marketing
created: 2026-06-08
related_findings: []
related_concepts: []
related_projects:
  - GA4
related_reports:
  - 2026-06-08_GA4_Raw_Data
---

# Weekly Marketing Report

## Objective

Review MORFRAC website traffic performance using GA4 data and identify actionable changes.

## Executive Summary

- Current 7-day sessions: 121
- Previous 7-day sessions: 153
- 7-day sessions change: -20.9%
- Current 28-day sessions: 688
- Previous 28-day sessions: 800
- 28-day sessions change: -14.0%

## Key Metrics

| Metric | Current 7d | Previous 7d | Change | Current 28d | Previous 28d | Change |
|---|---:|---:|---:|---:|---:|---:|
| Sessions | 121 | 153 | -20.9% | 688 | 800 | -14.0% |
| Users | 98 | 120 | -18.3% | 590 | 715 | -17.5% |

## Critical Issues

- CRITICAL: Sessions dropped -20.9% over 7 days.

## Traffic Analysis

### Source / Medium

| sessionSourceMedium | sessions | totalUsers | engagedSessions |
| --- | --- | --- | --- |
| google / organic | 56 | 42 | 33 |
| (direct) / (none) | 48 | 33 | 15 |
| (not set) | 5 | 5 | 1 |
| duckduckgo / organic | 3 | 2 | 1 |
| riggingmatters.gr / referral | 3 | 1 | 2 |
| bing / organic | 2 | 1 | 1 |
| m.facebook.com / referral | 2 | 2 | 2 |
| cn.bing.com / referral | 1 | 1 | 1 |
| facebook.com / referral | 1 | 1 | 0 |

### Top Landing Pages

| landingPage | sessions | totalUsers | engagedSessions |
| --- | --- | --- | --- |
| / | 29 | 17 | 20 |
| /dogbone | 9 | 9 | 7 |
| (not set) | 8 | 8 | 0 |
| /es | 7 | 6 | 5 |
| /shop | 7 | 7 | 4 |
| /morfblock | 5 | 5 | 3 |
| /shop/morfblock-light-4-hl-12823 | 5 | 1 | 3 |
| /blog/news-1/farr-x2-5 | 3 | 3 | 2 |
| /morfwing | 3 | 3 | 1 |
| /padeye | 2 | 2 | 2 |

### Device Analysis

| deviceCategory | sessions | totalUsers |
| --- | --- | --- |
| desktop | 76 | 50 |
| mobile | 44 | 35 |
| tablet | 1 | 1 |

### Geography

| country | sessions | totalUsers |
| --- | --- | --- |
| Spain | 24 | 10 |
| United States | 22 | 21 |
| Netherlands | 20 | 17 |
| France | 10 | 5 |
| United Kingdom | 8 | 6 |
| Hungary | 6 | 4 |
| Germany | 5 | 4 |
| New Zealand | 4 | 2 |
| Australia | 3 | 2 |
| China | 3 | 3 |

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

- Date data pulled: 2026-06-08
- Raw GA4 file written: C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC\06_MARKETING\Analytics\Raw_Data\GA4\2026-06-08_GA4_Raw_Data.md
- Weekly report written: C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC\06_MARKETING\Analytics\Weekly_Reports\2026-06-08_Weekly_Marketing_Report.md
- Script used: weekly_ga4_report.py

## Related Links

### Projects
- [[GA4]]

### Reports
- [[2026-06-08_GA4_Raw_Data]]
