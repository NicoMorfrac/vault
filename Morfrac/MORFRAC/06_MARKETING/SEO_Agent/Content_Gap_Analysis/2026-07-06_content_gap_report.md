---
type: seo_content_gap_report
source_agent: SEO_Agent
created: 2026-07-06
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

2026-07-06

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

- Semantic clusters: `C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC\06_MARKETING\SEO_Agent\Semantic_Clusters\2026-07-06_semantic_clusters.csv`
- Semantic pages: `C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC\06_MARKETING\SEO_Agent\Semantic_Clusters\2026-07-06_semantic_cluster_pages.csv`
- Search Console merge: `C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC\06_MARKETING\SEO_Agent\Merged_Analysis\2026-07-06_search_console_merge.csv`
- Contextual links: `C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC\06_MARKETING\SEO_Agent\Contextual_Links\2026-07-06_contextual_link_recommendations_filtered.csv`

---

# Summary

- Semantic clusters reviewed: 12
- Content gaps detected: 10
- Authority gaps detected: 10
- Missing pillar-page gaps: 6
- Orphan commercial topics: 0

---

# Highest Priority Content Gaps

|   semantic_cluster_id | dominant_label   |   page_count |   product_pages |   category_pages |   landing_pages |   authority_content_pages |   total_impressions |   total_clicks |   avg_seo_priority_score | cluster_health          | top_terms                                                                                                          | role_counts                                                           | label_counts                                                                                                                                               | gap_type                            |   gap_score | recommended_action                                                      |
|----------------------:|:-----------------|-------------:|----------------:|-----------------:|----------------:|--------------------------:|--------------------:|---------------:|-------------------------:|:------------------------|:-------------------------------------------------------------------------------------------------------------------|:----------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------|:------------------------------------|------------:|:------------------------------------------------------------------------|
|                     1 | powerfurl        |           16 |              16 |                0 |               0 |                         0 |                   0 |              0 |                     0    | PRODUCT_HEAVY_NO_PILLAR | unit, powerfurl, furling, drum, 10t swl, 10t, powerfurl drum, swl, unit powerfurl, unit morfrac                    | {'product': 16}                                                       | {'powerfurl': 16}                                                                                                                                          | Missing technical authority content |      155    | Create technical guide content supporting the powerfurl product family. |
|                     3 | dogbone          |           31 |              30 |                0 |               1 |                         0 |                 470 |              3 |                     3.31 | FRAGMENTED_TOPIC        | dogbone, morfrac dogbone, length, aluminium, morfrac, total length, length morfrac, total, titanium, faced         | {'product': 30, 'landing': 1}                                         | {'dogbone': 31}                                                                                                                                            | Missing technical authority content |      151.31 | Create technical guide content supporting the dogbone product family.   |
|                     8 | powerfurl        |           24 |              24 |                0 |               0 |                         0 |                   0 |              0 |                     0    | FRAGMENTED_TOPIC        | kit, furling, powerfurl, 5t, 5t swl, furling kit, swl, swl morfrac, morfrac powerfurl, powerfurl kit               | {'product': 24}                                                       | {'powerfurl': 21, 'shackle': 3}                                                                                                                            | Missing technical authority content |      145    | Create technical guide content supporting the powerfurl product family. |
|                     0 | morfblock        |           30 |              30 |                0 |               0 |                         0 |                   0 |              0 |                     0    | FRAGMENTED_TOPIC        | morfblock light, light, lightweight sailing, sailing block, block, sailing, morfblock, swl, lightweight, high      | {'product': 30}                                                       | {'morfblock': 30}                                                                                                                                          | Missing technical authority content |      145    | Create technical guide content supporting the morfblock product family. |
|                     2 | morfblock        |           22 |              20 |                2 |               0 |                         0 |                   0 |              0 |                     0    | FRAGMENTED_TOPIC        | xl, sailing block, morfblock, block, morfblock xl, sailing, xl sailing, morfblock max, max, swl                    | {'product': 20, 'category': 2}                                        | {'morfblock': 22}                                                                                                                                          | Missing technical authority content |      125    | Create technical guide content supporting the morfblock product family. |
|                     6 | other            |           51 |              15 |                0 |               3 |                        21 |                 119 |             13 |                     1.07 | FRAGMENTED_TOPIC        | custom, morfrac, morfblock, snatch, high performance, morfwing, mreel, rope reeler, reeler, hardware               | {'authority_content': 21, 'product': 15, 'general': 12, 'landing': 3} | {'other': 12, 'powerfurl': 8, 'morfblock': 8, 'custom_engineering': 6, 'morfwing': 5, 'mloop': 4, 'mreel': 4, 'dogbone': 2, 'morfring': 1, 'hoistlock': 1} | Missing category support            |      105.97 | Create or improve category structure for other pages.                   |
|                    10 | morfring         |           13 |              12 |                0 |               1 |                         0 |                   0 |              0 |                     0    | OK                      | morfring, friction, ptfe, friction ring, ring, aluminium friction, aluminium, morfrac morfring, groove max, groove | {'product': 12, 'landing': 1}                                         | {'morfring': 13}                                                                                                                                           | Missing technical authority content |       91    | Create technical guide content supporting the morfring product family.  |
|                    11 | morfblock        |            8 |               8 |                0 |               0 |                         0 |                   0 |              0 |                     0    | PRODUCT_HEAVY_NO_PILLAR | wood, wooden sailing, wooden, morfblock wood, high load, sailing block, block, morfblock, swl wooden, sailing      | {'product': 8}                                                        | {'morfblock': 8}                                                                                                                                           | Missing category support            |       74    | Create or improve category structure for morfblock pages.               |
|                     9 | powerfurl        |            6 |               6 |                0 |               0 |                         0 |                   0 |              0 |                     0    | PRODUCT_HEAVY_NO_PILLAR | fork, powerfurl fork, fitting, 10t swl, 10t, fork fitting, powerfurl, fork fork, swl, swl morfrac                  | {'product': 6}                                                        | {'powerfurl': 6}                                                                                                                                           | Missing category support            |       68    | Create or improve category structure for powerfurl pages.               |
|                     4 | padeye           |            9 |               8 |                0 |               1 |                         0 |                   0 |              0 |                     0    | OK                      | padeye, stick, deck, morfrac padeye, stick padeye, 20, ring, deck padeye, ring 20, padeye ring                     | {'product': 8, 'landing': 1}                                          | {'padeye': 9}                                                                                                                                              | Missing category support            |       44    | Create or improve category structure for padeye pages.                  |

---

# Authority Content Gaps

|   semantic_cluster_id | dominant_label   |   page_count |   product_pages |   category_pages |   landing_pages |   authority_content_pages |   total_impressions |   total_clicks |   avg_seo_priority_score | cluster_health          | top_terms                                                                                                          | role_counts                                 | label_counts                    | gap_type                            |   gap_score | recommended_action                                                      |
|----------------------:|:-----------------|-------------:|----------------:|-----------------:|----------------:|--------------------------:|--------------------:|---------------:|-------------------------:|:------------------------|:-------------------------------------------------------------------------------------------------------------------|:--------------------------------------------|:--------------------------------|:------------------------------------|------------:|:------------------------------------------------------------------------|
|                     1 | powerfurl        |           16 |              16 |                0 |               0 |                         0 |                   0 |              0 |                     0    | PRODUCT_HEAVY_NO_PILLAR | unit, powerfurl, furling, drum, 10t swl, 10t, powerfurl drum, swl, unit powerfurl, unit morfrac                    | {'product': 16}                             | {'powerfurl': 16}               | Missing technical authority content |      155    | Create technical guide content supporting the powerfurl product family. |
|                     3 | dogbone          |           31 |              30 |                0 |               1 |                         0 |                 470 |              3 |                     3.31 | FRAGMENTED_TOPIC        | dogbone, morfrac dogbone, length, aluminium, morfrac, total length, length morfrac, total, titanium, faced         | {'product': 30, 'landing': 1}               | {'dogbone': 31}                 | Missing technical authority content |      151.31 | Create technical guide content supporting the dogbone product family.   |
|                     0 | morfblock        |           30 |              30 |                0 |               0 |                         0 |                   0 |              0 |                     0    | FRAGMENTED_TOPIC        | morfblock light, light, lightweight sailing, sailing block, block, sailing, morfblock, swl, lightweight, high      | {'product': 30}                             | {'morfblock': 30}               | Missing technical authority content |      145    | Create technical guide content supporting the morfblock product family. |
|                     8 | powerfurl        |           24 |              24 |                0 |               0 |                         0 |                   0 |              0 |                     0    | FRAGMENTED_TOPIC        | kit, furling, powerfurl, 5t, 5t swl, furling kit, swl, swl morfrac, morfrac powerfurl, powerfurl kit               | {'product': 24}                             | {'powerfurl': 21, 'shackle': 3} | Missing technical authority content |      145    | Create technical guide content supporting the powerfurl product family. |
|                     2 | morfblock        |           22 |              20 |                2 |               0 |                         0 |                   0 |              0 |                     0    | FRAGMENTED_TOPIC        | xl, sailing block, morfblock, block, morfblock xl, sailing, xl sailing, morfblock max, max, swl                    | {'product': 20, 'category': 2}              | {'morfblock': 22}               | Missing technical authority content |      125    | Create technical guide content supporting the morfblock product family. |
|                    10 | morfring         |           13 |              12 |                0 |               1 |                         0 |                   0 |              0 |                     0    | OK                      | morfring, friction, ptfe, friction ring, ring, aluminium friction, aluminium, morfrac morfring, groove max, groove | {'product': 12, 'landing': 1}               | {'morfring': 13}                | Missing technical authority content |       91    | Create technical guide content supporting the morfring product family.  |
|                    11 | morfblock        |            8 |               8 |                0 |               0 |                         0 |                   0 |              0 |                     0    | PRODUCT_HEAVY_NO_PILLAR | wood, wooden sailing, wooden, morfblock wood, high load, sailing block, block, morfblock, swl wooden, sailing      | {'product': 8}                              | {'morfblock': 8}                | Missing category support            |       74    | Create or improve category structure for morfblock pages.               |
|                     9 | powerfurl        |            6 |               6 |                0 |               0 |                         0 |                   0 |              0 |                     0    | PRODUCT_HEAVY_NO_PILLAR | fork, powerfurl fork, fitting, 10t swl, 10t, fork fitting, powerfurl, fork fork, swl, swl morfrac                  | {'product': 6}                              | {'powerfurl': 6}                | Missing category support            |       68    | Create or improve category structure for powerfurl pages.               |
|                     4 | padeye           |            9 |               8 |                0 |               1 |                         0 |                   0 |              0 |                     0    | OK                      | padeye, stick, deck, morfrac padeye, stick padeye, 20, ring, deck padeye, ring 20, padeye ring                     | {'product': 8, 'landing': 1}                | {'padeye': 9}                   | Missing category support            |       44    | Create or improve category structure for padeye pages.                  |
|                     5 | shackle          |           12 |               9 |                2 |               1 |                         0 |                   0 |              0 |                     0    | OK                      | shackle, ti shackle, ti, titanium shackle, titanium, shackle morfrac, ø6mm, machined, cnc machined, cnc            | {'product': 9, 'category': 2, 'landing': 1} | {'shackle': 12}                 | No major gap                        |       27    | Monitor; no immediate content gap detected.                             |

---

# Missing Pillar / Landing Page Gaps

|   semantic_cluster_id | dominant_label   |   page_count |   product_pages |   category_pages |   landing_pages |   authority_content_pages |   total_impressions |   total_clicks |   avg_seo_priority_score | cluster_health          | top_terms                                                                                                     | role_counts                    | label_counts                    | gap_type                            |   gap_score | recommended_action                                                      |
|----------------------:|:-----------------|-------------:|----------------:|-----------------:|----------------:|--------------------------:|--------------------:|---------------:|-------------------------:|:------------------------|:--------------------------------------------------------------------------------------------------------------|:-------------------------------|:--------------------------------|:------------------------------------|------------:|:------------------------------------------------------------------------|
|                     1 | powerfurl        |           16 |              16 |                0 |               0 |                         0 |                   0 |              0 |                        0 | PRODUCT_HEAVY_NO_PILLAR | unit, powerfurl, furling, drum, 10t swl, 10t, powerfurl drum, swl, unit powerfurl, unit morfrac               | {'product': 16}                | {'powerfurl': 16}               | Missing technical authority content |         155 | Create technical guide content supporting the powerfurl product family. |
|                     0 | morfblock        |           30 |              30 |                0 |               0 |                         0 |                   0 |              0 |                        0 | FRAGMENTED_TOPIC        | morfblock light, light, lightweight sailing, sailing block, block, sailing, morfblock, swl, lightweight, high | {'product': 30}                | {'morfblock': 30}               | Missing technical authority content |         145 | Create technical guide content supporting the morfblock product family. |
|                     8 | powerfurl        |           24 |              24 |                0 |               0 |                         0 |                   0 |              0 |                        0 | FRAGMENTED_TOPIC        | kit, furling, powerfurl, 5t, 5t swl, furling kit, swl, swl morfrac, morfrac powerfurl, powerfurl kit          | {'product': 24}                | {'powerfurl': 21, 'shackle': 3} | Missing technical authority content |         145 | Create technical guide content supporting the powerfurl product family. |
|                     2 | morfblock        |           22 |              20 |                2 |               0 |                         0 |                   0 |              0 |                        0 | FRAGMENTED_TOPIC        | xl, sailing block, morfblock, block, morfblock xl, sailing, xl sailing, morfblock max, max, swl               | {'product': 20, 'category': 2} | {'morfblock': 22}               | Missing technical authority content |         125 | Create technical guide content supporting the morfblock product family. |
|                    11 | morfblock        |            8 |               8 |                0 |               0 |                         0 |                   0 |              0 |                        0 | PRODUCT_HEAVY_NO_PILLAR | wood, wooden sailing, wooden, morfblock wood, high load, sailing block, block, morfblock, swl wooden, sailing | {'product': 8}                 | {'morfblock': 8}                | Missing category support            |          74 | Create or improve category structure for morfblock pages.               |
|                     9 | powerfurl        |            6 |               6 |                0 |               0 |                         0 |                   0 |              0 |                        0 | PRODUCT_HEAVY_NO_PILLAR | fork, powerfurl fork, fitting, 10t swl, 10t, fork fitting, powerfurl, fork fork, swl, swl morfrac             | {'product': 6}                 | {'powerfurl': 6}                | Missing category support            |          68 | Create or improve category structure for powerfurl pages.               |

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

- Content gap analysis: `C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC\06_MARKETING\SEO_Agent\Content_Gap_Analysis\2026-07-06_content_gap_analysis.csv`
- Authority gap analysis: `C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC\06_MARKETING\SEO_Agent\Content_Gap_Analysis\2026-07-06_authority_gap_analysis.csv`
- Missing pillar pages: `C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC\06_MARKETING\SEO_Agent\Content_Gap_Analysis\2026-07-06_missing_pillar_pages.csv`
- Orphan commercial topics: `C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC\06_MARKETING\SEO_Agent\Content_Gap_Analysis\2026-07-06_orphan_commercial_topics.csv`
- Page support summary: `C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC\06_MARKETING\SEO_Agent\Content_Gap_Analysis\2026-07-06_page_support_summary.csv`

## Related Links

### Concepts
- [[PRODUCT_HEAVY_NO_PILLAR]]
- [[FRAGMENTED_TOPIC]]

### Projects
- [[Search Console]]
