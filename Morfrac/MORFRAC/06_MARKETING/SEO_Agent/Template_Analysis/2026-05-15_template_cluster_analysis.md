# SEO Template Cluster Analysis

## Generated

2026-05-15

## Input

C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC\06_MARKETING\SEO_Agent\Crawls\2026-05-15_site_crawl.csv

## Purpose

This report identifies structural SEO issues by template/page family.

It is designed to detect repeated template-level weaknesses rather than individual page defects.

---

# Template Cluster Summary

| template_cluster   |   pages |   avg_issue_count |   total_issues |   avg_commercial_seo_score |   avg_title_length |   avg_meta_length |   avg_word_count |   missing_title_count |   short_title_count |   long_title_count |   missing_meta_count |   short_meta_count |   long_meta_count |   missing_h1_count |   multiple_h1_count |   thin_content_count |   missing_alt_count |   weak_internal_linking_count |   structural_risk_score |
|:-------------------|--------:|------------------:|---------------:|---------------------------:|-------------------:|------------------:|-----------------:|----------------------:|--------------------:|-------------------:|---------------------:|-------------------:|------------------:|-------------------:|--------------------:|---------------------:|--------------------:|------------------------------:|------------------------:|
| shop_category      |      87 |           3.7931  |            330 |                   21.3793  |            23.4253 |           19.6092 |          532.414 |                     0 |                  81 |                  0 |                   75 |                  0 |                 0 |                  0 |                  87 |                    0 |                  87 |                             0 |                     978 |
| product_morfblock  |      82 |           2.71951 |            223 |                   17.4512  |            67.2317 |          129.366  |          449.159 |                     0 |                   1 |                 57 |                    0 |                  1 |                 0 |                  0 |                  82 |                    0 |                  82 |                             0 |                     471 |
| other              |      49 |           3.63265 |            178 |                    7.55102 |            22.5714 |          118.306  |         1685.43  |                     2 |                  38 |                  0 |                   10 |                  0 |                 4 |                  6 |                  37 |                   20 |                  45 |                             8 |                     403 |
| product_powerfurl  |      72 |           2.05556 |            148 |                   16.1111  |            57.8333 |          136.958  |          366.042 |                     0 |                   0 |                  4 |                    0 |                  0 |                 0 |                  0 |                  72 |                    0 |                  72 |                             0 |                     364 |
| blog               |      57 |           2.5614  |            146 |                    7.70175 |            40.4386 |          103.088  |          695.86  |                     0 |                  22 |                  0 |                    7 |                  8 |                 4 |                  0 |                  48 |                    0 |                  57 |                             0 |                     364 |
| product_dogbone    |      52 |           2.05769 |            107 |                   16.0577  |            55.8077 |          153.788  |          338.442 |                     0 |                   0 |                  0 |                    0 |                  0 |                 3 |                  0 |                  52 |                    0 |                  52 |                             0 |                     263 |
| product_other      |      36 |           2.16667 |             78 |                   14.8889  |            49.0278 |          132.389  |          396.583 |                     0 |                   1 |                  0 |                    2 |                  0 |                 1 |                  0 |                  36 |                    2 |                  36 |                             0 |                     194 |
| product_morfring   |      26 |           2       |             52 |                   16       |            53.4615 |          146.308  |          445.846 |                     0 |                   0 |                  0 |                    0 |                  0 |                 0 |                  0 |                  26 |                    0 |                  26 |                             0 |                     130 |
| product_shackle    |      22 |           2       |             44 |                   16       |            49.3636 |          154.182  |          524.409 |                     0 |                   0 |                  0 |                    0 |                  0 |                 0 |                  0 |                  22 |                    0 |                  22 |                             0 |                     110 |
| product_mloop      |       6 |           2.33333 |             14 |                   17       |            39      |          145.333  |          321.5   |                     0 |                   2 |                  0 |                    0 |                  0 |                 0 |                  0 |                   6 |                    0 |                   6 |                             0 |                      36 |
| landing_dogbone    |       2 |           3       |              6 |                   19       |            19      |          134      |          775     |                     0 |                   2 |                  0 |                    0 |                  0 |                 0 |                  0 |                   2 |                    0 |                   2 |                             0 |                      16 |
| landing_morfblock  |       2 |           3       |              6 |                   19       |            20      |          139      |         1379     |                     0 |                   2 |                  0 |                    0 |                  0 |                 0 |                  0 |                   2 |                    0 |                   2 |                             0 |                      16 |
| landing_padeye     |       2 |           3       |              6 |                   19       |            18      |          133      |         1400     |                     0 |                   2 |                  0 |                    0 |                  0 |                 0 |                  0 |                   2 |                    0 |                   2 |                             0 |                      16 |
| landing_powerfurl  |       2 |           3       |              6 |                   18.5     |            43      |          156      |         1589     |                     0 |                   1 |                  1 |                    0 |                  0 |                 0 |                  0 |                   2 |                    0 |                   2 |                             0 |                      14 |
| shop_home          |       2 |           2       |              4 |                   10       |            55      |          152      |          628.5   |                     0 |                   0 |                  0 |                    0 |                  0 |                 0 |                  0 |                   2 |                    0 |                   2 |                             0 |                      10 |
| home               |       1 |           2       |              2 |                   10       |            43      |          160      |          500     |                     0 |                   0 |                  0 |                    0 |                  0 |                 0 |                  0 |                   1 |                    0 |                   1 |                             0 |                       5 |

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
