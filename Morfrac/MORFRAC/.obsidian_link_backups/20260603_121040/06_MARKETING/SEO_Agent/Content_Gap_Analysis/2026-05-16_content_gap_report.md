# MORFRAC SEO Content Gap Analysis

## Generated

2026-05-16

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

- Semantic clusters: `C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC\06_MARKETING\SEO_Agent\Semantic_Clusters\2026-05-16_semantic_clusters.csv`
- Semantic pages: `C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC\06_MARKETING\SEO_Agent\Semantic_Clusters\2026-05-16_semantic_cluster_pages.csv`
- Search Console merge: `C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC\06_MARKETING\SEO_Agent\Merged_Analysis\2026-05-16_search_console_merge.csv`
- Contextual links: `C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC\06_MARKETING\SEO_Agent\Contextual_Links\2026-05-16_contextual_link_recommendations_filtered.csv`

---

# Summary

- Semantic clusters reviewed: 12
- Content gaps detected: 10
- Authority gaps detected: 9
- Missing pillar-page gaps: 7
- Orphan commercial topics: 0

---

# Highest Priority Content Gaps

|   semantic_cluster_id | dominant_label   |   page_count |   product_pages |   category_pages |   landing_pages |   authority_content_pages |   total_impressions |   total_clicks |   avg_seo_priority_score | cluster_health          | top_terms                                                                                                                                 | role_counts                                                         | label_counts                                                                                                                  | gap_type                            |   gap_score | recommended_action                                                      |
|----------------------:|:-----------------|-------------:|----------------:|-----------------:|----------------:|--------------------------:|--------------------:|---------------:|-------------------------:|:------------------------|:------------------------------------------------------------------------------------------------------------------------------------------|:--------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------|:------------------------------------|------------:|:------------------------------------------------------------------------|
|                     0 | morfblock        |           14 |              14 |                0 |               0 |                         0 |                   0 |              0 |                     0    | PRODUCT_HEAVY_NO_PILLAR | xl, morfblock xl, xl sailing, sailing block, block, morfblock, sailing, swl, sheave, handling                                             | {'product': 14}                                                     | {'morfblock': 14}                                                                                                             | Missing technical authority content |      155    | Create technical guide content supporting the morfblock product family. |
|                    11 | powerfurl        |           19 |              19 |                0 |               0 |                         0 |                   0 |              0 |                     0    | PRODUCT_HEAVY_NO_PILLAR | kit, furling, powerfurl, 5t, 5t swl, furling kit, swl, swl morfrac, powerfurl furling, powerfurl kit                                      | {'product': 19}                                                     | {'powerfurl': 16, 'shackle': 3}                                                                                               | Missing technical authority content |      155    | Create technical guide content supporting the powerfurl product family. |
|                     5 | dogbone          |           31 |              30 |                0 |               1 |                         0 |                 363 |              3 |                     2.16 | FRAGMENTED_TOPIC        | dogbone, morfrac dogbone, length, aluminium, morfrac, length morfrac, total, total length, titanium, faced                                | {'product': 30, 'landing': 1}                                       | {'dogbone': 31}                                                                                                               | Missing technical authority content |      150.16 | Create technical guide content supporting the dogbone product family.   |
|                     9 | powerfurl        |           11 |              11 |                0 |               0 |                         0 |                   0 |              0 |                     0    | PRODUCT_HEAVY_NO_PILLAR | unit, drum, powerfurl, furling, powerfurl drum, unit powerfurl, furling unit, unit morfrac, powerfurl engineered, swl                     | {'product': 11}                                                     | {'powerfurl': 11}                                                                                                             | Missing technical authority content |      148    | Create technical guide content supporting the powerfurl product family. |
|                     6 | morfblock        |           30 |              30 |                0 |               0 |                         0 |                   0 |              0 |                     0    | FRAGMENTED_TOPIC        | morfblock light, light, lightweight sailing, sailing block, block, sailing, morfblock, swl, lightweight, high                             | {'product': 30}                                                     | {'morfblock': 30}                                                                                                             | Missing technical authority content |      145    | Create technical guide content supporting the morfblock product family. |
|                     4 | shackle          |           24 |              16 |                0 |               2 |                         4 |                 358 |             21 |                     6.46 | FRAGMENTED_TOPIC        | shackle, custom, ti shackle, ti, titanium, titanium shackle, high, ultra, snatch, performance                                             | {'product': 16, 'authority_content': 4, 'general': 2, 'landing': 2} | {'shackle': 9, 'morfblock': 4, 'mloop': 4, 'powerfurl': 3, 'custom_engineering': 1, 'padeye': 1, 'dogbone': 1, 'morfring': 1} | Missing category support            |      136.46 | Create or improve category structure for shackle pages.                 |
|                    10 | morfring         |           16 |              15 |                0 |               1 |                         0 |                   0 |              0 |                     0    | OK                      | ring, friction, friction ring, morfring, aluminium friction, ptfe, aluminium, ring morfrac, morfrac morfring, groove max                  | {'product': 15, 'landing': 1}                                       | {'morfring': 13, 'padeye': 3}                                                                                                 | Missing technical authority content |       95    | Create technical guide content supporting the morfring product family.  |
|                     2 | morfblock        |            6 |               6 |                0 |               0 |                         0 |                   0 |              0 |                     0    | PRODUCT_HEAVY_NO_PILLAR | morfblock max, max, sailing, efficiency, sailing block, block, delivering low, dimensions maximum, efficiency level, reliability strength | {'product': 6}                                                      | {'morfblock': 6}                                                                                                              | Missing category support            |       68    | Create or improve category structure for morfblock pages.               |
|                     7 | powerfurl        |            6 |               6 |                0 |               0 |                         0 |                   0 |              0 |                     0    | PRODUCT_HEAVY_NO_PILLAR | fork, powerfurl fork, fitting, 10t, 10t swl, fork fitting, powerfurl, fork fork, swl, swl morfrac                                         | {'product': 6}                                                      | {'powerfurl': 6}                                                                                                              | Missing category support            |       68    | Create or improve category structure for powerfurl pages.               |
|                     8 | powerfurl        |            5 |               5 |                0 |               0 |                         0 |                   0 |              0 |                     0    | OK                      | integrator, swl integrator, powerfurl, td, powerfurl td, td integrator, designed smooth, smooth reliable, integrators, tdis               | {'product': 5}                                                      | {'powerfurl': 5}                                                                                                              | Missing category support            |       35    | Create or improve category structure for powerfurl pages.               |

---

# Authority Content Gaps

|   semantic_cluster_id | dominant_label   |   page_count |   product_pages |   category_pages |   landing_pages |   authority_content_pages |   total_impressions |   total_clicks |   avg_seo_priority_score | cluster_health          | top_terms                                                                                                                                 | role_counts                   | label_counts                    | gap_type                            |   gap_score | recommended_action                                                      |
|----------------------:|:-----------------|-------------:|----------------:|-----------------:|----------------:|--------------------------:|--------------------:|---------------:|-------------------------:|:------------------------|:------------------------------------------------------------------------------------------------------------------------------------------|:------------------------------|:--------------------------------|:------------------------------------|------------:|:------------------------------------------------------------------------|
|                    11 | powerfurl        |           19 |              19 |                0 |               0 |                         0 |                   0 |              0 |                     0    | PRODUCT_HEAVY_NO_PILLAR | kit, furling, powerfurl, 5t, 5t swl, furling kit, swl, swl morfrac, powerfurl furling, powerfurl kit                                      | {'product': 19}               | {'powerfurl': 16, 'shackle': 3} | Missing technical authority content |      155    | Create technical guide content supporting the powerfurl product family. |
|                     0 | morfblock        |           14 |              14 |                0 |               0 |                         0 |                   0 |              0 |                     0    | PRODUCT_HEAVY_NO_PILLAR | xl, morfblock xl, xl sailing, sailing block, block, morfblock, sailing, swl, sheave, handling                                             | {'product': 14}               | {'morfblock': 14}               | Missing technical authority content |      155    | Create technical guide content supporting the morfblock product family. |
|                     5 | dogbone          |           31 |              30 |                0 |               1 |                         0 |                 363 |              3 |                     2.16 | FRAGMENTED_TOPIC        | dogbone, morfrac dogbone, length, aluminium, morfrac, length morfrac, total, total length, titanium, faced                                | {'product': 30, 'landing': 1} | {'dogbone': 31}                 | Missing technical authority content |      150.16 | Create technical guide content supporting the dogbone product family.   |
|                     9 | powerfurl        |           11 |              11 |                0 |               0 |                         0 |                   0 |              0 |                     0    | PRODUCT_HEAVY_NO_PILLAR | unit, drum, powerfurl, furling, powerfurl drum, unit powerfurl, furling unit, unit morfrac, powerfurl engineered, swl                     | {'product': 11}               | {'powerfurl': 11}               | Missing technical authority content |      148    | Create technical guide content supporting the powerfurl product family. |
|                     6 | morfblock        |           30 |              30 |                0 |               0 |                         0 |                   0 |              0 |                     0    | FRAGMENTED_TOPIC        | morfblock light, light, lightweight sailing, sailing block, block, sailing, morfblock, swl, lightweight, high                             | {'product': 30}               | {'morfblock': 30}               | Missing technical authority content |      145    | Create technical guide content supporting the morfblock product family. |
|                    10 | morfring         |           16 |              15 |                0 |               1 |                         0 |                   0 |              0 |                     0    | OK                      | ring, friction, friction ring, morfring, aluminium friction, ptfe, aluminium, ring morfrac, morfrac morfring, groove max                  | {'product': 15, 'landing': 1} | {'morfring': 13, 'padeye': 3}   | Missing technical authority content |       95    | Create technical guide content supporting the morfring product family.  |
|                     2 | morfblock        |            6 |               6 |                0 |               0 |                         0 |                   0 |              0 |                     0    | PRODUCT_HEAVY_NO_PILLAR | morfblock max, max, sailing, efficiency, sailing block, block, delivering low, dimensions maximum, efficiency level, reliability strength | {'product': 6}                | {'morfblock': 6}                | Missing category support            |       68    | Create or improve category structure for morfblock pages.               |
|                     7 | powerfurl        |            6 |               6 |                0 |               0 |                         0 |                   0 |              0 |                     0    | PRODUCT_HEAVY_NO_PILLAR | fork, powerfurl fork, fitting, 10t, 10t swl, fork fitting, powerfurl, fork fork, swl, swl morfrac                                         | {'product': 6}                | {'powerfurl': 6}                | Missing category support            |       68    | Create or improve category structure for powerfurl pages.               |
|                     8 | powerfurl        |            5 |               5 |                0 |               0 |                         0 |                   0 |              0 |                     0    | OK                      | integrator, swl integrator, powerfurl, td, powerfurl td, td integrator, designed smooth, smooth reliable, integrators, tdis               | {'product': 5}                | {'powerfurl': 5}                | Missing category support            |       35    | Create or improve category structure for powerfurl pages.               |

---

# Missing Pillar / Landing Page Gaps

|   semantic_cluster_id | dominant_label   |   page_count |   product_pages |   category_pages |   landing_pages |   authority_content_pages |   total_impressions |   total_clicks |   avg_seo_priority_score | cluster_health          | top_terms                                                                                                                                 | role_counts     | label_counts                    | gap_type                            |   gap_score | recommended_action                                                      |
|----------------------:|:-----------------|-------------:|----------------:|-----------------:|----------------:|--------------------------:|--------------------:|---------------:|-------------------------:|:------------------------|:------------------------------------------------------------------------------------------------------------------------------------------|:----------------|:--------------------------------|:------------------------------------|------------:|:------------------------------------------------------------------------|
|                    11 | powerfurl        |           19 |              19 |                0 |               0 |                         0 |                   0 |              0 |                        0 | PRODUCT_HEAVY_NO_PILLAR | kit, furling, powerfurl, 5t, 5t swl, furling kit, swl, swl morfrac, powerfurl furling, powerfurl kit                                      | {'product': 19} | {'powerfurl': 16, 'shackle': 3} | Missing technical authority content |         155 | Create technical guide content supporting the powerfurl product family. |
|                     0 | morfblock        |           14 |              14 |                0 |               0 |                         0 |                   0 |              0 |                        0 | PRODUCT_HEAVY_NO_PILLAR | xl, morfblock xl, xl sailing, sailing block, block, morfblock, sailing, swl, sheave, handling                                             | {'product': 14} | {'morfblock': 14}               | Missing technical authority content |         155 | Create technical guide content supporting the morfblock product family. |
|                     9 | powerfurl        |           11 |              11 |                0 |               0 |                         0 |                   0 |              0 |                        0 | PRODUCT_HEAVY_NO_PILLAR | unit, drum, powerfurl, furling, powerfurl drum, unit powerfurl, furling unit, unit morfrac, powerfurl engineered, swl                     | {'product': 11} | {'powerfurl': 11}               | Missing technical authority content |         148 | Create technical guide content supporting the powerfurl product family. |
|                     6 | morfblock        |           30 |              30 |                0 |               0 |                         0 |                   0 |              0 |                        0 | FRAGMENTED_TOPIC        | morfblock light, light, lightweight sailing, sailing block, block, sailing, morfblock, swl, lightweight, high                             | {'product': 30} | {'morfblock': 30}               | Missing technical authority content |         145 | Create technical guide content supporting the morfblock product family. |
|                     2 | morfblock        |            6 |               6 |                0 |               0 |                         0 |                   0 |              0 |                        0 | PRODUCT_HEAVY_NO_PILLAR | morfblock max, max, sailing, efficiency, sailing block, block, delivering low, dimensions maximum, efficiency level, reliability strength | {'product': 6}  | {'morfblock': 6}                | Missing category support            |          68 | Create or improve category structure for morfblock pages.               |
|                     7 | powerfurl        |            6 |               6 |                0 |               0 |                         0 |                   0 |              0 |                        0 | PRODUCT_HEAVY_NO_PILLAR | fork, powerfurl fork, fitting, 10t, 10t swl, fork fitting, powerfurl, fork fork, swl, swl morfrac                                         | {'product': 6}  | {'powerfurl': 6}                | Missing category support            |          68 | Create or improve category structure for powerfurl pages.               |
|                     8 | powerfurl        |            5 |               5 |                0 |               0 |                         0 |                   0 |              0 |                        0 | OK                      | integrator, swl integrator, powerfurl, td, powerfurl td, td integrator, designed smooth, smooth reliable, integrators, tdis               | {'product': 5}  | {'powerfurl': 5}                | Missing category support            |          35 | Create or improve category structure for powerfurl pages.               |

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

- Content gap analysis: `C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC\06_MARKETING\SEO_Agent\Content_Gap_Analysis\2026-05-16_content_gap_analysis.csv`
- Authority gap analysis: `C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC\06_MARKETING\SEO_Agent\Content_Gap_Analysis\2026-05-16_authority_gap_analysis.csv`
- Missing pillar pages: `C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC\06_MARKETING\SEO_Agent\Content_Gap_Analysis\2026-05-16_missing_pillar_pages.csv`
- Orphan commercial topics: `C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC\06_MARKETING\SEO_Agent\Content_Gap_Analysis\2026-05-16_orphan_commercial_topics.csv`
- Page support summary: `C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC\06_MARKETING\SEO_Agent\Content_Gap_Analysis\2026-05-16_page_support_summary.csv`
