---
type: seo_template_cluster_analysis
source_agent: SEO_Agent
created: 2026-06-22
related_findings: []
related_concepts: []
related_projects: []
related_reports: []
---

# SEO Template Cluster Analysis

## Generated

2026-06-22

## Input

C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC\06_MARKETING\SEO_Agent\Crawls\2026-06-22_site_crawl.csv

## Purpose

This report identifies structural SEO issues by template/page family.

It is designed to detect repeated template-level weaknesses rather than individual page defects.

---

# Template Cluster Summary

| template_cluster   |   pages |   avg_issue_count |   total_issues |   avg_commercial_seo_score |   avg_title_length |   avg_meta_length |   avg_word_count |   missing_title_count |   short_title_count |   long_title_count |   missing_meta_count |   short_meta_count |   long_meta_count |   missing_h1_count |   multiple_h1_count |   thin_content_count |   missing_alt_count |   weak_internal_linking_count |   structural_risk_score |
|:-------------------|--------:|------------------:|---------------:|---------------------------:|-------------------:|------------------:|-----------------:|----------------------:|--------------------:|-------------------:|---------------------:|-------------------:|------------------:|-------------------:|--------------------:|---------------------:|--------------------:|------------------------------:|------------------------:|
| shop_category      |      83 |                 0 |              0 |                          0 |            23.1084 |           28.1205 |          531.386 |                     0 |                   0 |                  0 |                    0 |                  0 |                 0 |                  0 |                   0 |                    0 |                   0 |                             0 |                       0 |
| product_morfblock  |      82 |                 0 |              0 |                          0 |            67.2317 |          129.134  |          455.939 |                     0 |                   0 |                  0 |                    0 |                  0 |                 0 |                  0 |                   0 |                    0 |                   0 |                             0 |                       0 |
| product_powerfurl  |      77 |                 0 |              0 |                          0 |            57.8831 |          136.922  |          366.468 |                     0 |                   0 |                  0 |                    0 |                  0 |                 0 |                  0 |                   0 |                    0 |                   0 |                             0 |                       0 |
| blog               |      59 |                 0 |              0 |                          0 |            38.2542 |          110.695  |          717.661 |                     0 |                   0 |                  0 |                    0 |                  0 |                 0 |                  0 |                   0 |                    0 |                   0 |                             0 |                       0 |
| product_dogbone    |      52 |                 0 |              0 |                          0 |            55.8077 |          153.788  |          339.077 |                     0 |                   0 |                  0 |                    0 |                  0 |                 0 |                  0 |                   0 |                    0 |                   0 |                             0 |                       0 |
| other              |      45 |                 0 |              0 |                          0 |            23.2889 |          127.711  |          541.933 |                     0 |                   0 |                  0 |                    0 |                  0 |                 0 |                  0 |                   0 |                    0 |                   0 |                             0 |                       0 |
| product_other      |      36 |                 0 |              0 |                          0 |            49.0278 |          132.389  |          396.972 |                     0 |                   0 |                  0 |                    0 |                  0 |                 0 |                  0 |                   0 |                    0 |                   0 |                             0 |                       0 |
| product_morfring   |      26 |                 0 |              0 |                          0 |            53.4615 |          146.308  |          446.346 |                     0 |                   0 |                  0 |                    0 |                  0 |                 0 |                  0 |                   0 |                    0 |                   0 |                             0 |                       0 |
| product_shackle    |      23 |                 0 |              0 |                          0 |            49.6087 |          154.087  |          542.13  |                     0 |                   0 |                  0 |                    0 |                  0 |                 0 |                  0 |                   0 |                    0 |                   0 |                             0 |                       0 |
| product_mloop      |       6 |                 0 |              0 |                          0 |            39      |          145.333  |          322     |                     0 |                   0 |                  0 |                    0 |                  0 |                 0 |                  0 |                   0 |                    0 |                   0 |                             0 |                       0 |
| landing_dogbone    |       2 |                 0 |              0 |                          0 |            19      |          134      |          775.5   |                     0 |                   0 |                  0 |                    0 |                  0 |                 0 |                  0 |                   0 |                    0 |                   0 |                             0 |                       0 |
| landing_morfblock  |       2 |                 0 |              0 |                          0 |            31      |          148      |         1373     |                     0 |                   0 |                  0 |                    0 |                  0 |                 0 |                  0 |                   0 |                    0 |                   0 |                             0 |                       0 |
| landing_padeye     |       2 |                 0 |              0 |                          0 |            18      |          133      |         1400.5   |                     0 |                   0 |                  0 |                    0 |                  0 |                 0 |                  0 |                   0 |                    0 |                   0 |                             0 |                       0 |
| landing_powerfurl  |       2 |                 0 |              0 |                          0 |            37.5    |          156      |         1589.5   |                     0 |                   0 |                  0 |                    0 |                  0 |                 0 |                  0 |                   0 |                    0 |                   0 |                             0 |                       0 |
| shop_home          |       2 |                 0 |              0 |                          0 |            55      |          152      |          628     |                     0 |                   0 |                  0 |                    0 |                  0 |                 0 |                  0 |                   0 |                    0 |                   0 |                             0 |                       0 |
| home               |       1 |                 0 |              0 |                          0 |            43      |          160      |          500     |                     0 |                   0 |                  0 |                    0 |                  0 |                 0 |                  0 |                   0 |                    0 |                   0 |                             0 |                       0 |

---

# Interpretation Notes

Higher structural risk scores indicate repeated SEO defects across a page family.

Primary template-level signals include:

- repeated short or missing titles
- repeated missing or weak meta descriptions
- repeated multiple H1 issues
- repeated missing image alt text
- repeated thin content
- weak internal linking

This report should be used to prioritize structural fixes before page-by-page edits.

## Related Links

No structured related links identified.
