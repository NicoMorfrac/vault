---
type: seo_template_cluster_analysis
source_agent: SEO_Agent
created: 2026-10-05
related_findings: []
related_concepts: []
related_projects: []
related_reports: []
---

# SEO Template Cluster Analysis

## Generated

2026-10-05

## Input

C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC\06_MARKETING\SEO_Agent\Crawls\2026-10-05_site_crawl.csv

## Purpose

This report identifies structural SEO issues by template/page family.

It is designed to detect repeated template-level weaknesses rather than individual page defects.

---

# Template Cluster Summary

| template_cluster   |   pages |   avg_issue_count |   total_issues |   avg_commercial_seo_score |   avg_title_length |   avg_meta_length |   avg_word_count |   missing_title_count |   short_title_count |   long_title_count |   missing_meta_count |   short_meta_count |   long_meta_count |   missing_h1_count |   multiple_h1_count |   thin_content_count |   missing_alt_count |   weak_internal_linking_count |   structural_risk_score |
|:-------------------|--------:|------------------:|---------------:|---------------------------:|-------------------:|------------------:|-----------------:|----------------------:|--------------------:|-------------------:|---------------------:|-------------------:|------------------:|-------------------:|--------------------:|---------------------:|--------------------:|------------------------------:|------------------------:|
| product_morfblock  |      82 |                 0 |              0 |                          0 |            67.2317 |          129.134  |          398.939 |                     0 |                   0 |                  0 |                    0 |                  0 |                 0 |                  0 |                   0 |                    0 |                   0 |                             0 |                       0 |
| shop_category      |      81 |                 0 |              0 |                          0 |            23.1605 |           26.8765 |          476.63  |                     0 |                   0 |                  0 |                    0 |                  0 |                 0 |                  0 |                   0 |                    0 |                   0 |                             0 |                       0 |
| product_powerfurl  |      78 |                 0 |              0 |                          0 |            57.8974 |          137.218  |          308.564 |                     0 |                   0 |                  0 |                    0 |                  0 |                 0 |                  0 |                   0 |                    0 |                   0 |                             0 |                       0 |
| blog               |      59 |                 0 |              0 |                          0 |            38.4915 |          112.797  |          661.203 |                     0 |                   0 |                  0 |                    0 |                  0 |                 0 |                  0 |                   0 |                    0 |                   0 |                             0 |                       0 |
| product_dogbone    |      52 |                 0 |              0 |                          0 |            55.8077 |          153.788  |          282.077 |                     0 |                   0 |                  0 |                    0 |                  0 |                 0 |                  0 |                   0 |                    0 |                   0 |                             0 |                       0 |
| other              |      41 |                 0 |              0 |                          0 |            25.2195 |           99.4878 |          404.805 |                     0 |                   0 |                  0 |                    0 |                  0 |                 0 |                  0 |                   0 |                    0 |                   0 |                             0 |                       0 |
| product_other      |      39 |                 0 |              0 |                          0 |            47.9487 |          124.923  |          333.744 |                     0 |                   0 |                  0 |                    0 |                  0 |                 0 |                  0 |                   0 |                    0 |                   0 |                             0 |                       0 |
| product_morfring   |      26 |                 0 |              0 |                          0 |            53.4615 |          146.308  |          389.346 |                     0 |                   0 |                  0 |                    0 |                  0 |                 0 |                  0 |                   0 |                    0 |                   0 |                             0 |                       0 |
| product_shackle    |      23 |                 0 |              0 |                          0 |            49.6087 |          154.087  |          485.13  |                     0 |                   0 |                  0 |                    0 |                  0 |                 0 |                  0 |                   0 |                    0 |                   0 |                             0 |                       0 |
| product_mloop      |       8 |                 0 |              0 |                          0 |            36.5    |          139      |          271.75  |                     0 |                   0 |                  0 |                    0 |                  0 |                 0 |                  0 |                   0 |                    0 |                   0 |                             0 |                       0 |
| landing_dogbone    |       2 |                 0 |              0 |                          0 |            19      |          134      |          718.5   |                     0 |                   0 |                  0 |                    0 |                  0 |                 0 |                  0 |                   0 |                    0 |                   0 |                             0 |                       0 |
| landing_morfblock  |       2 |                 0 |              0 |                          0 |            31      |          148      |         1316     |                     0 |                   0 |                  0 |                    0 |                  0 |                 0 |                  0 |                   0 |                    0 |                   0 |                             0 |                       0 |
| landing_padeye     |       2 |                 0 |              0 |                          0 |            18      |          133      |         1343.5   |                     0 |                   0 |                  0 |                    0 |                  0 |                 0 |                  0 |                   0 |                    0 |                   0 |                             0 |                       0 |
| landing_powerfurl  |       2 |                 0 |              0 |                          0 |            37.5    |          156      |         1532.5   |                     0 |                   0 |                  0 |                    0 |                  0 |                 0 |                  0 |                   0 |                    0 |                   0 |                             0 |                       0 |
| shop_home          |       2 |                 0 |              0 |                          0 |            55      |          152      |          571     |                     0 |                   0 |                  0 |                    0 |                  0 |                 0 |                  0 |                   0 |                    0 |                   0 |                             0 |                       0 |
| home               |       1 |                 0 |              0 |                          0 |            43      |          160      |          418     |                     0 |                   0 |                  0 |                    0 |                  0 |                 0 |                  0 |                   0 |                    0 |                   0 |                             0 |                       0 |

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
