# Traffic Quality Analysis

## Generated

2026-05-10

## Source

C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC\06_MARKETING\Analytics\Weekly_Reports\2026-05-09_Weekly_Marketing_Report.md

---

# Executive Interpretation

High commercial relevance traffic appears weak relative to total sessions. A significant share of traffic comes from low-tier or low-confidence territories. United States traffic is material and should be interpreted separately because it may include both commercial interest and crawler/datacenter noise. Suspicious or low-engagement landing page patterns were detected.

---

# Traffic Confidence Summary

| Segment | Sessions | Share |
|---|---:|---:|
| High commercial relevance | 60 | 32.1% |
| Medium commercial relevance | 10 | 5.3% |
| United States monitoring | 24 | 12.8% |
| Low tier / low confidence | 93 | 49.7% |
| Total analyzed | 187 | 100.0% |

---

# Territory Summary

| territory                 | tier          |   sessions |   users |
|:--------------------------|:--------------|-----------:|--------:|
| Low Tier / Low Confidence | LOW           |         93 |      92 |
| Southern Europe           | HIGH          |         50 |      31 |
| United States             | US_MONITORING |         24 |      24 |
| South America             | MEDIUM        |         10 |      10 |
| Northern Europe           | HIGH          |         10 |       9 |

---

# Country-Level Analysis

| country       | territory                 | tier          |   sessions |   users | confidence                                    | notes                                                                                                                                     |
|:--------------|:--------------------------|:--------------|-----------:|--------:|:----------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------|
| Spain         | Southern Europe           | HIGH          |         42 |      26 | High commercial relevance                     |                                                                                                                                           |
| Vietnam       | Low Tier / Low Confidence | LOW           |         31 |      31 | Low confidence or high-noise geography        | Low-tier or low-confidence geography; High session volume from low-confidence geography                                                   |
| China         | Low Tier / Low Confidence | LOW           |         27 |      26 | Low confidence or high-noise geography        | Low-tier or low-confidence geography; High session volume from low-confidence geography                                                   |
| United States | United States             | US_MONITORING |         24 |      24 | Commercially relevant but crawler/noise prone | USA requires engagement validation due to crawler/datacenter noise risk; High USA session volume should be checked for engagement quality |
| Hong Kong     | Low Tier / Low Confidence | LOW           |         14 |      14 | Low confidence or high-noise geography        | Low-tier or low-confidence geography                                                                                                      |
| Singapore     | Low Tier / Low Confidence | LOW           |         12 |      12 | Low confidence or high-noise geography        | Low-tier or low-confidence geography                                                                                                      |
| Brazil        | South America             | MEDIUM        |         10 |      10 | Medium commercial relevance                   |                                                                                                                                           |
| Germany       | Northern Europe           | HIGH          |         10 |       9 | High commercial relevance                     |                                                                                                                                           |
| India         | Low Tier / Low Confidence | LOW           |          9 |       9 | Low confidence or high-noise geography        | Low-tier or low-confidence geography                                                                                                      |
| Italy         | Southern Europe           | HIGH          |          8 |       5 | High commercial relevance                     |                                                                                                                                           |

---

# Suspicious Signals

- Suspicious landing page detected: (not set) (sessions=8)
- Low engagement traffic detected on (not set) (sessions=8, engagedSessions=0)
- Suspicious landing page detected: /web/login (sessions=7)


---

# Interpretation Rules

High commercial relevance:
- Southern Europe
- Northern Europe
- Oceania

United States monitoring:
- commercially important
- interpreted separately because of crawler and datacenter traffic risk

Medium commercial relevance:
- South America

Low tier / low confidence:
- Singapore
- Hong Kong
- UAE
- China
- India
- Vietnam
- Russia
- unknown or unclassified regions

This report is a rule-based traffic qualification layer.
It does not prove whether traffic is human, bot, commercial, or non-commercial.
It provides a confidence filter for executive interpretation.
