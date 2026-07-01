---
type: weekly_report
source_agent: Marketing
created: 2026-06-29
related_findings: []
related_concepts: []
related_projects:
  - GA4
related_reports:
  - 2026-06-29_GA4_Raw_Data
---

# Weekly Marketing Report

## Objective

Review MORFRAC website traffic performance using GA4 data and identify actionable changes.

## Executive Summary

- Current 7-day sessions: 537
- Previous 7-day sessions: 178
- 7-day sessions change: 201.7%
- Current 28-day sessions: 1002
- Previous 28-day sessions: 812
- 28-day sessions change: 23.4%

## Key Metrics

| Metric   | Current 7d | Previous 7d | Change | Current 28d | Previous 28d | Change |
| -------- | ---------: | ----------: | -----: | ----------: | -----------: | -----: |
| Sessions |        537 |         178 | 201.7% |        1002 |          812 |  23.4% |
| Users    |        509 |         147 | 246.3% |         890 |          723 |  23.1% |

## Critical Issues

- No critical GA4 traffic alerts detected.

## Traffic Analysis

### Source / Medium

| sessionSourceMedium        | sessions | totalUsers | engagedSessions |
| -------------------------- | -------- | ---------- | --------------- |
| (direct) / (none)          | 456      | 452        | 24              |
| (not set)                  | 42       | 29         | 14              |
| google / organic           | 31       | 21         | 20              |
| (data not available)       | 3        | 3          | 0               |
| bing / organic             | 3        | 1          | 1               |
| chatgpt.com / ai-assistant | 3        | 2          | 3               |
| woduc.com / referral       | 2        | 2          | 2               |
| m.facebook.com / referral  | 1        | 1          | 1               |

### Top Landing Pages

| landingPage                                           | sessions | totalUsers | engagedSessions |
| ----------------------------------------------------- | -------- | ---------- | --------------- |
| /                                                     | 28       | 20         | 17              |
| (not set)                                             | 15       | 14         | 0               |
| /blog/news-1/tag/news-2                               | 15       | 15         | 0               |
| /blog/tag/news-2                                      | 15       | 15         | 0               |
| /shop                                                 | 15       | 15         | 2               |
| /blog/tag/shows-exhibitions-3                         | 13       | 13         | 0               |
| /blog/stories-4/aluminium-titanium-stainless-steel-39 | 12       | 12         | 5               |
| /blog/tag/powerfurl-4                                 | 11       | 11         | 0               |
| /morfblock                                            | 11       | 9          | 5               |
| /blog/news-1/tag/partners-11                          | 9        | 9          | 0               |

### Device Analysis

| deviceCategory | sessions | totalUsers |
| --- | --- | --- |
| desktop | 520 | 486 |
| mobile | 14 | 10 |
| tablet | 1 | 1 |

### Geography

| country        | sessions | totalUsers |
| -------------- | -------- | ---------- |
| United States  | 435      | 427        |
| Spain          | 22       | 8          |
| Singapore      | 14       | 14         |
| China          | 9        | 8          |
| France         | 8        | 4          |
| Germany        | 7        | 6          |
| Australia      | 5        | 3          |
| United Kingdom | 5        | 4          |
| Brazil         | 4        | 3          |
| Argentina      | 3        | 1          |

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

- Date data pulled: 2026-06-29
- Raw GA4 file written: C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC\06_MARKETING\Analytics\Raw_Data\GA4\2026-06-29_GA4_Raw_Data.md
- Weekly report written: C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC\06_MARKETING\Analytics\Weekly_Reports\2026-06-29_Weekly_Marketing_Report.md
- Script used: weekly_ga4_report.py

## Related Links

### Projects
- [[GA4]]

### Reports
- [[2026-06-29_GA4_Raw_Data]]
