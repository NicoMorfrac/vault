---
type: seo_content_gap_report
source_agent: SEO_Agent
created: 2026-07-14
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

2026-07-14

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

- Semantic clusters: `C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC\06_MARKETING\SEO_Agent\Semantic_Clusters\2026-07-14_semantic_clusters.csv`
- Semantic pages: `C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC\06_MARKETING\SEO_Agent\Semantic_Clusters\2026-07-14_semantic_cluster_pages.csv`
- Search Console merge: `C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC\06_MARKETING\SEO_Agent\Merged_Analysis\2026-07-14_search_console_merge.csv`
- Contextual links: `C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC\06_MARKETING\SEO_Agent\Contextual_Links\2026-07-14_contextual_link_recommendations_filtered.csv`

---

# Summary

- Semantic clusters reviewed: 12
- Content gaps detected: 10
- Authority gaps detected: 10
- Missing pillar-page gaps: 8
- Orphan commercial topics: 0

---

# Highest Priority Content Gaps

|   semantic_cluster_id | dominant_label   |   page_count |   product_pages |   category_pages |   landing_pages |   authority_content_pages |   total_impressions |   total_clicks |   avg_seo_priority_score | cluster_health          | top_terms                                                                                                                     | role_counts                                                           | label_counts                                                                                                                                   | gap_type                            |   gap_score | recommended_action                                                      |
|----------------------:|:-----------------|-------------:|----------------:|-----------------:|----------------:|--------------------------:|--------------------:|---------------:|-------------------------:|:------------------------|:------------------------------------------------------------------------------------------------------------------------------|:----------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------|:------------------------------------|------------:|:------------------------------------------------------------------------|
|                     5 | dogbone          |           20 |              20 |                0 |               0 |                         0 |                   0 |              0 |                      0   | PRODUCT_HEAVY_NO_PILLAR | dogbone, length, morfrac dogbone, aluminium, 60mm, total length, total, length morfrac, morfrac, dogbone aluminium            | {'product': 20}                                                       | {'dogbone': 20}                                                                                                                                | Missing technical authority content |       155   | Create technical guide content supporting the dogbone product family.   |
|                     0 | morfring         |           12 |              12 |                0 |               0 |                         0 |                   0 |              0 |                      0   | PRODUCT_HEAVY_NO_PILLAR | friction, ptfe, ring, friction ring, morfring, aluminium friction, aluminium, groove, groove max, morfrac morfring            | {'product': 12}                                                       | {'morfring': 12}                                                                                                                               | Missing technical authority content |       151   | Create technical guide content supporting the morfring product family.  |
|                     2 | morfblock        |           30 |              30 |                0 |               0 |                         0 |                   0 |              0 |                      0   | FRAGMENTED_TOPIC        | morfblock light, light, lightweight sailing, sailing block, block, sailing, morfblock, swl, lightweight, high                 | {'product': 30}                                                       | {'morfblock': 30}                                                                                                                              | Missing technical authority content |       145   | Create technical guide content supporting the morfblock product family. |
|                     1 | powerfurl        |           44 |              44 |                0 |               0 |                         0 |                   0 |              0 |                      0   | FRAGMENTED_TOPIC        | powerfurl, furling, swl, 5t swl, 5t, kit, 10t, 10t swl, morfrac powerfurl, reliable                                           | {'product': 44}                                                       | {'powerfurl': 41, 'shackle': 3}                                                                                                                | Missing technical authority content |       145   | Create technical guide content supporting the powerfurl product family. |
|                     6 | morfblock        |           22 |              22 |                0 |               0 |                         0 |                   0 |              0 |                      0   | FRAGMENTED_TOPIC        | xl, sailing block, morfblock xl, block, xl sailing, morfblock, wood, sailing, swl, high load                                  | {'product': 22}                                                       | {'morfblock': 22}                                                                                                                              | Missing technical authority content |       145   | Create technical guide content supporting the morfblock product family. |
|                     3 | other            |           49 |              11 |                0 |               5 |                        21 |                 582 |             15 |                      3.6 | FRAGMENTED_TOPIC        | custom, morfrac, morfblock, snatch, morfwing, high performance, hardware, 2024, performance, sail                             | {'authority_content': 21, 'general': 12, 'product': 11, 'landing': 5} | {'other': 12, 'powerfurl': 8, 'morfblock': 8, 'custom_engineering': 6, 'morfwing': 5, 'mloop': 4, 'dogbone': 3, 'morfring': 2, 'hoistlock': 1} | Missing category support            |       121.6 | Create or improve category structure for other pages.                   |
|                    10 | dogbone          |            8 |               8 |                0 |               0 |                         0 |                   0 |              0 |                      0   | PRODUCT_HEAVY_NO_PILLAR | rope reeler, reeler, mreel, dogbone, mreel rope, rope, length, morfrac dogbone, reeler morfrac, morfrac mreel                 | {'product': 8}                                                        | {'dogbone': 4, 'mreel': 4}                                                                                                                     | Missing category support            |        74   | Create or improve category structure for dogbone pages.                 |
|                     7 | dogbone          |            6 |               6 |                0 |               0 |                         0 |                   0 |              0 |                      0   | PRODUCT_HEAVY_NO_PILLAR | faced, flat, flat faced, faced titanium, dogbone flat, dogbone, morfrac dogbone, titanium, titanium morfrac, titanium dogbone | {'product': 6}                                                        | {'dogbone': 6}                                                                                                                                 | Missing category support            |        68   | Create or improve category structure for dogbone pages.                 |
|                    11 | shackle          |           10 |               9 |                0 |               1 |                         0 |                   0 |              0 |                      0   | OK                      | shackle, ti shackle, ti, titanium shackle, titanium, ø6mm, machined, cnc, cnc machined, ultra                                 | {'product': 9, 'landing': 1}                                          | {'shackle': 10}                                                                                                                                | Missing category support            |        47   | Create or improve category structure for shackle pages.                 |
|                     8 | padeye           |            9 |               8 |                0 |               1 |                         0 |                   0 |              0 |                      0   | OK                      | padeye, stick, deck, morfrac padeye, stick padeye, 20, ring, deck padeye, ring 20, padeye ring                                | {'product': 8, 'landing': 1}                                          | {'padeye': 9}                                                                                                                                  | Missing category support            |        44   | Create or improve category structure for padeye pages.                  |

---

# Authority Content Gaps

|   semantic_cluster_id | dominant_label   |   page_count |   product_pages |   category_pages |   landing_pages |   authority_content_pages |   total_impressions |   total_clicks |   avg_seo_priority_score | cluster_health          | top_terms                                                                                                                          | role_counts                   | label_counts                    | gap_type                            |   gap_score | recommended_action                                                      |
|----------------------:|:-----------------|-------------:|----------------:|-----------------:|----------------:|--------------------------:|--------------------:|---------------:|-------------------------:|:------------------------|:-----------------------------------------------------------------------------------------------------------------------------------|:------------------------------|:--------------------------------|:------------------------------------|------------:|:------------------------------------------------------------------------|
|                     5 | dogbone          |           20 |              20 |                0 |               0 |                         0 |                   0 |              0 |                        0 | PRODUCT_HEAVY_NO_PILLAR | dogbone, length, morfrac dogbone, aluminium, 60mm, total length, total, length morfrac, morfrac, dogbone aluminium                 | {'product': 20}               | {'dogbone': 20}                 | Missing technical authority content |         155 | Create technical guide content supporting the dogbone product family.   |
|                     0 | morfring         |           12 |              12 |                0 |               0 |                         0 |                   0 |              0 |                        0 | PRODUCT_HEAVY_NO_PILLAR | friction, ptfe, ring, friction ring, morfring, aluminium friction, aluminium, groove, groove max, morfrac morfring                 | {'product': 12}               | {'morfring': 12}                | Missing technical authority content |         151 | Create technical guide content supporting the morfring product family.  |
|                     2 | morfblock        |           30 |              30 |                0 |               0 |                         0 |                   0 |              0 |                        0 | FRAGMENTED_TOPIC        | morfblock light, light, lightweight sailing, sailing block, block, sailing, morfblock, swl, lightweight, high                      | {'product': 30}               | {'morfblock': 30}               | Missing technical authority content |         145 | Create technical guide content supporting the morfblock product family. |
|                     1 | powerfurl        |           44 |              44 |                0 |               0 |                         0 |                   0 |              0 |                        0 | FRAGMENTED_TOPIC        | powerfurl, furling, swl, 5t swl, 5t, kit, 10t, 10t swl, morfrac powerfurl, reliable                                                | {'product': 44}               | {'powerfurl': 41, 'shackle': 3} | Missing technical authority content |         145 | Create technical guide content supporting the powerfurl product family. |
|                     6 | morfblock        |           22 |              22 |                0 |               0 |                         0 |                   0 |              0 |                        0 | FRAGMENTED_TOPIC        | xl, sailing block, morfblock xl, block, xl sailing, morfblock, wood, sailing, swl, high load                                       | {'product': 22}               | {'morfblock': 22}               | Missing technical authority content |         145 | Create technical guide content supporting the morfblock product family. |
|                    10 | dogbone          |            8 |               8 |                0 |               0 |                         0 |                   0 |              0 |                        0 | PRODUCT_HEAVY_NO_PILLAR | rope reeler, reeler, mreel, dogbone, mreel rope, rope, length, morfrac dogbone, reeler morfrac, morfrac mreel                      | {'product': 8}                | {'dogbone': 4, 'mreel': 4}      | Missing category support            |          74 | Create or improve category structure for dogbone pages.                 |
|                     7 | dogbone          |            6 |               6 |                0 |               0 |                         0 |                   0 |              0 |                        0 | PRODUCT_HEAVY_NO_PILLAR | faced, flat, flat faced, faced titanium, dogbone flat, dogbone, morfrac dogbone, titanium, titanium morfrac, titanium dogbone      | {'product': 6}                | {'dogbone': 6}                  | Missing category support            |          68 | Create or improve category structure for dogbone pages.                 |
|                    11 | shackle          |           10 |               9 |                0 |               1 |                         0 |                   0 |              0 |                        0 | OK                      | shackle, ti shackle, ti, titanium shackle, titanium, ø6mm, machined, cnc, cnc machined, ultra                                      | {'product': 9, 'landing': 1}  | {'shackle': 10}                 | Missing category support            |          47 | Create or improve category structure for shackle pages.                 |
|                     8 | padeye           |            9 |               8 |                0 |               1 |                         0 |                   0 |              0 |                        0 | OK                      | padeye, stick, deck, morfrac padeye, stick padeye, 20, ring, deck padeye, ring 20, padeye ring                                     | {'product': 8, 'landing': 1}  | {'padeye': 9}                   | Missing category support            |          44 | Create or improve category structure for padeye pages.                  |
|                     9 | morfblock        |            8 |               6 |                2 |               0 |                         0 |                   0 |              0 |                        0 | OK                      | morfblock max, max, morfblock, sailing, efficiency, sailing block, maximum reliability, block, efficiency sailing, max lightweight | {'product': 6, 'category': 2} | {'morfblock': 8}                | No major gap                        |          18 | Monitor; no immediate content gap detected.                             |

---

# Missing Pillar / Landing Page Gaps

|   semantic_cluster_id | dominant_label   |   page_count |   product_pages |   category_pages |   landing_pages |   authority_content_pages |   total_impressions |   total_clicks |   avg_seo_priority_score | cluster_health          | top_terms                                                                                                                          | role_counts                   | label_counts                    | gap_type                            |   gap_score | recommended_action                                                      |
|----------------------:|:-----------------|-------------:|----------------:|-----------------:|----------------:|--------------------------:|--------------------:|---------------:|-------------------------:|:------------------------|:-----------------------------------------------------------------------------------------------------------------------------------|:------------------------------|:--------------------------------|:------------------------------------|------------:|:------------------------------------------------------------------------|
|                     5 | dogbone          |           20 |              20 |                0 |               0 |                         0 |                   0 |              0 |                        0 | PRODUCT_HEAVY_NO_PILLAR | dogbone, length, morfrac dogbone, aluminium, 60mm, total length, total, length morfrac, morfrac, dogbone aluminium                 | {'product': 20}               | {'dogbone': 20}                 | Missing technical authority content |         155 | Create technical guide content supporting the dogbone product family.   |
|                     0 | morfring         |           12 |              12 |                0 |               0 |                         0 |                   0 |              0 |                        0 | PRODUCT_HEAVY_NO_PILLAR | friction, ptfe, ring, friction ring, morfring, aluminium friction, aluminium, groove, groove max, morfrac morfring                 | {'product': 12}               | {'morfring': 12}                | Missing technical authority content |         151 | Create technical guide content supporting the morfring product family.  |
|                     1 | powerfurl        |           44 |              44 |                0 |               0 |                         0 |                   0 |              0 |                        0 | FRAGMENTED_TOPIC        | powerfurl, furling, swl, 5t swl, 5t, kit, 10t, 10t swl, morfrac powerfurl, reliable                                                | {'product': 44}               | {'powerfurl': 41, 'shackle': 3} | Missing technical authority content |         145 | Create technical guide content supporting the powerfurl product family. |
|                     2 | morfblock        |           30 |              30 |                0 |               0 |                         0 |                   0 |              0 |                        0 | FRAGMENTED_TOPIC        | morfblock light, light, lightweight sailing, sailing block, block, sailing, morfblock, swl, lightweight, high                      | {'product': 30}               | {'morfblock': 30}               | Missing technical authority content |         145 | Create technical guide content supporting the morfblock product family. |
|                     6 | morfblock        |           22 |              22 |                0 |               0 |                         0 |                   0 |              0 |                        0 | FRAGMENTED_TOPIC        | xl, sailing block, morfblock xl, block, xl sailing, morfblock, wood, sailing, swl, high load                                       | {'product': 22}               | {'morfblock': 22}               | Missing technical authority content |         145 | Create technical guide content supporting the morfblock product family. |
|                    10 | dogbone          |            8 |               8 |                0 |               0 |                         0 |                   0 |              0 |                        0 | PRODUCT_HEAVY_NO_PILLAR | rope reeler, reeler, mreel, dogbone, mreel rope, rope, length, morfrac dogbone, reeler morfrac, morfrac mreel                      | {'product': 8}                | {'dogbone': 4, 'mreel': 4}      | Missing category support            |          74 | Create or improve category structure for dogbone pages.                 |
|                     7 | dogbone          |            6 |               6 |                0 |               0 |                         0 |                   0 |              0 |                        0 | PRODUCT_HEAVY_NO_PILLAR | faced, flat, flat faced, faced titanium, dogbone flat, dogbone, morfrac dogbone, titanium, titanium morfrac, titanium dogbone      | {'product': 6}                | {'dogbone': 6}                  | Missing category support            |          68 | Create or improve category structure for dogbone pages.                 |
|                     9 | morfblock        |            8 |               6 |                2 |               0 |                         0 |                   0 |              0 |                        0 | OK                      | morfblock max, max, morfblock, sailing, efficiency, sailing block, maximum reliability, block, efficiency sailing, max lightweight | {'product': 6, 'category': 2} | {'morfblock': 8}                | No major gap                        |          18 | Monitor; no immediate content gap detected.                             |

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

- Content gap analysis: `C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC\06_MARKETING\SEO_Agent\Content_Gap_Analysis\2026-07-14_content_gap_analysis.csv`
- Authority gap analysis: `C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC\06_MARKETING\SEO_Agent\Content_Gap_Analysis\2026-07-14_authority_gap_analysis.csv`
- Missing pillar pages: `C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC\06_MARKETING\SEO_Agent\Content_Gap_Analysis\2026-07-14_missing_pillar_pages.csv`
- Orphan commercial topics: `C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC\06_MARKETING\SEO_Agent\Content_Gap_Analysis\2026-07-14_orphan_commercial_topics.csv`
- Page support summary: `C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC\06_MARKETING\SEO_Agent\Content_Gap_Analysis\2026-07-14_page_support_summary.csv`

## Related Links

### Concepts
- [[PRODUCT_HEAVY_NO_PILLAR]]
- [[FRAGMENTED_TOPIC]]

### Projects
- [[Search Console]]
