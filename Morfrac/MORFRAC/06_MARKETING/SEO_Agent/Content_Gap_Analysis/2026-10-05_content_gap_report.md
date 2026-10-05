---
type: seo_content_gap_report
source_agent: SEO_Agent
created: 2026-10-05
related_findings: []
related_concepts:
  - PRODUCT_HEAVY_NO_PILLAR
  - FRAGMENTED_TOPIC
related_projects:
  - Search Console
related_reports: []
---

# MORFRAC SEO Content Gap Analysis

## Generated

2026-10-05

---

# Purpose

This report identifies missing content and authority gaps across MORFRAC semantic SEO clusters.

It uses deterministic data from:

- semantic cluster analysis
- crawl data
- Search Console merge data
- contextual linking outputs

It detects:

- product-heavy clusters without technical authority content
- product-heavy clusters without pillar/landing pages
- authority content without commercial targets
- orphan commercial topics
- search-demand topics without supporting authority content

---

# Source Files

- Semantic clusters: `C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC\06_MARKETING\SEO_Agent\Semantic_Clusters\2026-10-05_semantic_clusters.csv`
- Semantic pages: `C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC\06_MARKETING\SEO_Agent\Semantic_Clusters\2026-10-05_semantic_cluster_pages.csv`
- Search Console merge: `C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC\06_MARKETING\SEO_Agent\Merged_Analysis\2026-10-05_search_console_merge.csv`
- Contextual links: `C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC\06_MARKETING\SEO_Agent\Contextual_Links\2026-10-05_contextual_link_recommendations_filtered.csv`

---

# Summary

- Semantic clusters reviewed: 12
- Content gaps detected: 10
- Authority gaps detected: 8
- Missing pillar-page gaps: 7
- Orphan commercial topics: 0

---

# Highest Priority Content Gaps

|   semantic_cluster_id | dominant_label   |   page_count |   product_pages |   category_pages |   landing_pages |   authority_content_pages |   total_impressions |   total_clicks |   avg_seo_priority_score | cluster_health          | top_terms                                                                                                                 | role_counts                                                           | label_counts                                                                                                                                | gap_type                            |   gap_score | recommended_action                                                      |
|----------------------:|:-----------------|-------------:|----------------:|-----------------:|----------------:|--------------------------:|--------------------:|---------------:|-------------------------:|:------------------------|:--------------------------------------------------------------------------------------------------------------------------|:----------------------------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------|:------------------------------------|------------:|:------------------------------------------------------------------------|
|                     3 | morfblock        |           14 |              14 |                0 |               0 |                         0 |                   0 |              0 |                     0    | PRODUCT_HEAVY_NO_PILLAR | xl, morfblock xl, xl sailing, sailing block, block, morfblock, sailing, swl, sheave, handling                             | {'product': 14}                                                       | {'morfblock': 14}                                                                                                                           | Missing technical authority content |      155    | Create technical guide content supporting the morfblock product family. |
|                     0 | morfblock        |           30 |              30 |                0 |               0 |                         0 |                   0 |              0 |                     0    | FRAGMENTED_TOPIC        | morfblock light, light, lightweight sailing, sailing block, block, sailing, morfblock, swl, lightweight, high             | {'product': 30}                                                       | {'morfblock': 30}                                                                                                                           | Missing technical authority content |      145    | Create technical guide content supporting the morfblock product family. |
|                     9 | dogbone          |           22 |              22 |                0 |               0 |                         0 |                   0 |              0 |                     0    | FRAGMENTED_TOPIC        | dogbone, morfrac dogbone, length, 60mm, morfrac, length morfrac, total, total length, titanium, attachment                | {'product': 22}                                                       | {'dogbone': 22}                                                                                                                             | Missing technical authority content |      145    | Create technical guide content supporting the dogbone product family.   |
|                     4 | powerfurl        |           23 |              23 |                0 |               0 |                         0 |                   0 |              0 |                     0    | FRAGMENTED_TOPIC        | powerfurl, furling, 10t, 10t swl, unit, fork, drum, swl, powerfurl drum, powerfurl fork                                   | {'product': 23}                                                       | {'powerfurl': 23}                                                                                                                           | Missing technical authority content |      145    | Create technical guide content supporting the powerfurl product family. |
|                    10 | morfring         |           21 |              20 |                0 |               1 |                         0 |                   0 |              0 |                     0    | FRAGMENTED_TOPIC        | padeye, ring, friction, friction ring, ptfe, aluminium friction, morfring, aluminium, stick, deck                         | {'product': 20, 'landing': 1}                                         | {'morfring': 12, 'padeye': 9}                                                                                                               | Missing technical authority content |      115    | Create technical guide content supporting the morfring product family.  |
|                     8 | powerfurl        |           28 |              27 |                0 |               1 |                         0 |                   0 |              0 |                     0    | FRAGMENTED_TOPIC        | shackle, kit, 5t, 5t swl, furling, powerfurl, furling kit, swl, ti shackle, swl morfrac                                   | {'product': 27, 'landing': 1}                                         | {'powerfurl': 15, 'shackle': 13}                                                                                                            | Missing technical authority content |      115    | Create technical guide content supporting the powerfurl product family. |
|                     6 | other            |           50 |              19 |                0 |               3 |                        15 |                 207 |              2 |                     1.62 | FRAGMENTED_TOPIC        | custom, morfrac, snatch, high performance, hardware, morfblock, mreel, reeler, rope reeler, performance                   | {'product': 19, 'authority_content': 15, 'general': 13, 'landing': 3} | {'other': 15, 'morfblock': 8, 'powerfurl': 6, 'custom_engineering': 6, 'mloop': 5, 'mreel': 4, 'dogbone': 3, 'morfring': 2, 'hoistlock': 1} | Missing category support            |      104.32 | Create or improve category structure for other pages.                   |
|                     5 | dogbone          |            9 |               8 |                0 |               1 |                         0 |                 282 |              2 |                    11.51 | OK                      | dogbone, morfrac dogbone, length, aluminium, rope, dogbone engineered, lightweight aluminium, morfrac, connections, faced | {'product': 8, 'landing': 1}                                          | {'dogbone': 9}                                                                                                                              | Missing category support            |       85.71 | Create or improve category structure for dogbone pages.                 |
|                    11 | morfblock        |           12 |               8 |                0 |               0 |                         4 |                   0 |              0 |                     0    | PRODUCT_HEAVY_NO_PILLAR | wood, wooden, wooden sailing, morfblock wood, high load, sailing block, block, morfblock, morfwing, swl wooden            | {'product': 8, 'authority_content': 4}                                | {'morfblock': 8, 'morfwing': 4}                                                                                                             | Missing category support            |       74    | Create or improve category structure for morfblock pages.               |
|                     1 | powerfurl        |            8 |               6 |                0 |               0 |                         2 |                   0 |              0 |                     0    | PRODUCT_HEAVY_NO_PILLAR | integrator, powerfurl, swl integrator, integrators, tdis, td integrator, td, powerfurl td, designed smooth, sails         | {'product': 6, 'authority_content': 2}                                | {'powerfurl': 8}                                                                                                                            | Missing category support            |       68    | Create or improve category structure for powerfurl pages.               |

---

# Authority Content Gaps

|   semantic_cluster_id | dominant_label   |   page_count |   product_pages |   category_pages |   landing_pages |   authority_content_pages |   total_impressions |   total_clicks |   avg_seo_priority_score | cluster_health          | top_terms                                                                                                                          | role_counts                   | label_counts                     | gap_type                            |   gap_score | recommended_action                                                      |
|----------------------:|:-----------------|-------------:|----------------:|-----------------:|----------------:|--------------------------:|--------------------:|---------------:|-------------------------:|:------------------------|:-----------------------------------------------------------------------------------------------------------------------------------|:------------------------------|:---------------------------------|:------------------------------------|------------:|:------------------------------------------------------------------------|
|                     3 | morfblock        |           14 |              14 |                0 |               0 |                         0 |                   0 |              0 |                     0    | PRODUCT_HEAVY_NO_PILLAR | xl, morfblock xl, xl sailing, sailing block, block, morfblock, sailing, swl, sheave, handling                                      | {'product': 14}               | {'morfblock': 14}                | Missing technical authority content |      155    | Create technical guide content supporting the morfblock product family. |
|                     0 | morfblock        |           30 |              30 |                0 |               0 |                         0 |                   0 |              0 |                     0    | FRAGMENTED_TOPIC        | morfblock light, light, lightweight sailing, sailing block, block, sailing, morfblock, swl, lightweight, high                      | {'product': 30}               | {'morfblock': 30}                | Missing technical authority content |      145    | Create technical guide content supporting the morfblock product family. |
|                     9 | dogbone          |           22 |              22 |                0 |               0 |                         0 |                   0 |              0 |                     0    | FRAGMENTED_TOPIC        | dogbone, morfrac dogbone, length, 60mm, morfrac, length morfrac, total, total length, titanium, attachment                         | {'product': 22}               | {'dogbone': 22}                  | Missing technical authority content |      145    | Create technical guide content supporting the dogbone product family.   |
|                     4 | powerfurl        |           23 |              23 |                0 |               0 |                         0 |                   0 |              0 |                     0    | FRAGMENTED_TOPIC        | powerfurl, furling, 10t, 10t swl, unit, fork, drum, swl, powerfurl drum, powerfurl fork                                            | {'product': 23}               | {'powerfurl': 23}                | Missing technical authority content |      145    | Create technical guide content supporting the powerfurl product family. |
|                     8 | powerfurl        |           28 |              27 |                0 |               1 |                         0 |                   0 |              0 |                     0    | FRAGMENTED_TOPIC        | shackle, kit, 5t, 5t swl, furling, powerfurl, furling kit, swl, ti shackle, swl morfrac                                            | {'product': 27, 'landing': 1} | {'powerfurl': 15, 'shackle': 13} | Missing technical authority content |      115    | Create technical guide content supporting the powerfurl product family. |
|                    10 | morfring         |           21 |              20 |                0 |               1 |                         0 |                   0 |              0 |                     0    | FRAGMENTED_TOPIC        | padeye, ring, friction, friction ring, ptfe, aluminium friction, morfring, aluminium, stick, deck                                  | {'product': 20, 'landing': 1} | {'morfring': 12, 'padeye': 9}    | Missing technical authority content |      115    | Create technical guide content supporting the morfring product family.  |
|                     5 | dogbone          |            9 |               8 |                0 |               1 |                         0 |                 282 |              2 |                    11.51 | OK                      | dogbone, morfrac dogbone, length, aluminium, rope, dogbone engineered, lightweight aluminium, morfrac, connections, faced          | {'product': 8, 'landing': 1}  | {'dogbone': 9}                   | Missing category support            |       85.71 | Create or improve category structure for dogbone pages.                 |
|                     2 | morfblock        |            8 |               6 |                2 |               0 |                         0 |                   0 |              0 |                     0    | OK                      | morfblock max, max, morfblock, sailing, efficiency, sailing block, maximum reliability, block, efficiency sailing, max lightweight | {'product': 6, 'category': 2} | {'morfblock': 8}                 | No major gap                        |       18    | Monitor; no immediate content gap detected.                             |

---

# Missing Pillar / Landing Page Gaps

|   semantic_cluster_id | dominant_label   |   page_count |   product_pages |   category_pages |   landing_pages |   authority_content_pages |   total_impressions |   total_clicks |   avg_seo_priority_score | cluster_health          | top_terms                                                                                                                          | role_counts                            | label_counts                    | gap_type                            |   gap_score | recommended_action                                                      |
|----------------------:|:-----------------|-------------:|----------------:|-----------------:|----------------:|--------------------------:|--------------------:|---------------:|-------------------------:|:------------------------|:-----------------------------------------------------------------------------------------------------------------------------------|:---------------------------------------|:--------------------------------|:------------------------------------|------------:|:------------------------------------------------------------------------|
|                     3 | morfblock        |           14 |              14 |                0 |               0 |                         0 |                   0 |              0 |                        0 | PRODUCT_HEAVY_NO_PILLAR | xl, morfblock xl, xl sailing, sailing block, block, morfblock, sailing, swl, sheave, handling                                      | {'product': 14}                        | {'morfblock': 14}               | Missing technical authority content |         155 | Create technical guide content supporting the morfblock product family. |
|                     4 | powerfurl        |           23 |              23 |                0 |               0 |                         0 |                   0 |              0 |                        0 | FRAGMENTED_TOPIC        | powerfurl, furling, 10t, 10t swl, unit, fork, drum, swl, powerfurl drum, powerfurl fork                                            | {'product': 23}                        | {'powerfurl': 23}               | Missing technical authority content |         145 | Create technical guide content supporting the powerfurl product family. |
|                     0 | morfblock        |           30 |              30 |                0 |               0 |                         0 |                   0 |              0 |                        0 | FRAGMENTED_TOPIC        | morfblock light, light, lightweight sailing, sailing block, block, sailing, morfblock, swl, lightweight, high                      | {'product': 30}                        | {'morfblock': 30}               | Missing technical authority content |         145 | Create technical guide content supporting the morfblock product family. |
|                     9 | dogbone          |           22 |              22 |                0 |               0 |                         0 |                   0 |              0 |                        0 | FRAGMENTED_TOPIC        | dogbone, morfrac dogbone, length, 60mm, morfrac, length morfrac, total, total length, titanium, attachment                         | {'product': 22}                        | {'dogbone': 22}                 | Missing technical authority content |         145 | Create technical guide content supporting the dogbone product family.   |
|                    11 | morfblock        |           12 |               8 |                0 |               0 |                         4 |                   0 |              0 |                        0 | PRODUCT_HEAVY_NO_PILLAR | wood, wooden, wooden sailing, morfblock wood, high load, sailing block, block, morfblock, morfwing, swl wooden                     | {'product': 8, 'authority_content': 4} | {'morfblock': 8, 'morfwing': 4} | Missing category support            |          74 | Create or improve category structure for morfblock pages.               |
|                     1 | powerfurl        |            8 |               6 |                0 |               0 |                         2 |                   0 |              0 |                        0 | PRODUCT_HEAVY_NO_PILLAR | integrator, powerfurl, swl integrator, integrators, tdis, td integrator, td, powerfurl td, designed smooth, sails                  | {'product': 6, 'authority_content': 2} | {'powerfurl': 8}                | Missing category support            |          68 | Create or improve category structure for powerfurl pages.               |
|                     2 | morfblock        |            8 |               6 |                2 |               0 |                         0 |                   0 |              0 |                        0 | OK                      | morfblock max, max, morfblock, sailing, efficiency, sailing block, maximum reliability, block, efficiency sailing, max lightweight | {'product': 6, 'category': 2}          | {'morfblock': 8}                | No major gap                        |          18 | Monitor; no immediate content gap detected.                             |

---

# Orphan Commercial Topics

No commercial orphan topics detected.

---

# Interpretation Notes

Gap type meanings:

- `Missing technical authority content`: product cluster exists, but there are no supporting technical/educational pages.
- `Missing commercial pillar page`: many pages exist, but no central commercial landing page supports the cluster.
- `Missing category support`: product pages exist without enough category-level support.
- `Authority content lacks commercial target`: educational/blog content exists but does not clearly connect to products/categories.
- `Search demand without authority support`: impressions exist, but the topic lacks supporting authority content.
- `Orphan topic`: topic has only one semantic cluster/page path and may need support if commercially useful.

Recommended actions:

1. Build technical guides for product-heavy clusters.
2. Build commercial landing pages where product families lack a central pillar.
3. Link authority content toward product/category pages.
4. Avoid creating new content in fragmented topics before consolidation.
5. Prioritize gaps with impressions, product pages, and high gap scores.

---

# Output Files

- Content gap analysis: `C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC\06_MARKETING\SEO_Agent\Content_Gap_Analysis\2026-10-05_content_gap_analysis.csv`
- Authority gap analysis: `C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC\06_MARKETING\SEO_Agent\Content_Gap_Analysis\2026-10-05_authority_gap_analysis.csv`
- Missing pillar pages: `C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC\06_MARKETING\SEO_Agent\Content_Gap_Analysis\2026-10-05_missing_pillar_pages.csv`
- Orphan commercial topics: `C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC\06_MARKETING\SEO_Agent\Content_Gap_Analysis\2026-10-05_orphan_commercial_topics.csv`
- Page support summary: `C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC\06_MARKETING\SEO_Agent\Content_Gap_Analysis\2026-10-05_page_support_summary.csv`

## Related Links

### Concepts
- [[PRODUCT_HEAVY_NO_PILLAR]]
- [[FRAGMENTED_TOPIC]]

### Projects
- [[Search Console]]
