---
type: seo_content_gap_report
source_agent: SEO_Agent
created: 2026-06-15
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

2026-06-15

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

- Semantic clusters: `C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC\06_MARKETING\SEO_Agent\Semantic_Clusters\2026-06-15_semantic_clusters.csv`
- Semantic pages: `C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC\06_MARKETING\SEO_Agent\Semantic_Clusters\2026-06-15_semantic_cluster_pages.csv`
- Search Console merge: `C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC\06_MARKETING\SEO_Agent\Merged_Analysis\2026-06-15_search_console_merge.csv`
- Contextual links: `C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC\06_MARKETING\SEO_Agent\Contextual_Links\2026-06-15_contextual_link_recommendations_filtered.csv`

---

# Summary

- Semantic clusters reviewed: 12
- Content gaps detected: 9
- Authority gaps detected: 9
- Missing pillar-page gaps: 7
- Orphan commercial topics: 0

---

# Highest Priority Content Gaps

|   semantic_cluster_id | dominant_label   |   page_count |   product_pages |   category_pages |   landing_pages |   authority_content_pages |   total_impressions |   total_clicks |   avg_seo_priority_score | cluster_health          | top_terms                                                                                                             | role_counts                                          | label_counts                    | gap_type                            |   gap_score | recommended_action                                                      |
|----------------------:|:-----------------|-------------:|----------------:|-----------------:|----------------:|--------------------------:|--------------------:|---------------:|-------------------------:|:------------------------|:----------------------------------------------------------------------------------------------------------------------|:-----------------------------------------------------|:--------------------------------|:------------------------------------|------------:|:------------------------------------------------------------------------|
|                     0 | morfblock        |           14 |              14 |                0 |               0 |                         0 |                   0 |              0 |                        0 | PRODUCT_HEAVY_NO_PILLAR | xl, morfblock xl, xl sailing, sailing block, block, morfblock, sailing, swl, sheave, handling                         | {'product': 14}                                      | {'morfblock': 14}               | Missing technical authority content |         155 | Create technical guide content supporting the morfblock product family. |
|                     6 | powerfurl        |           12 |              12 |                0 |               0 |                         0 |                   0 |              0 |                        0 | PRODUCT_HEAVY_NO_PILLAR | unit, powerfurl, drum, furling, powerfurl drum, unit powerfurl, unit morfrac, furling unit, powerfurl engineered, swl | {'product': 12}                                      | {'powerfurl': 12}               | Missing technical authority content |         151 | Create technical guide content supporting the powerfurl product family. |
|                     3 | morfblock        |           44 |              44 |                0 |               0 |                         0 |                   0 |              0 |                        0 | FRAGMENTED_TOPIC        | sailing block, sailing, block, morfblock, morfblock light, light, swl, lightweight sailing, high, lightweight         | {'product': 44}                                      | {'morfblock': 44}               | Missing technical authority content |         145 | Create technical guide content supporting the morfblock product family. |
|                     4 | dogbone          |           24 |              24 |                0 |               0 |                         0 |                   0 |              0 |                        0 | FRAGMENTED_TOPIC        | dogbone, length, morfrac dogbone, aluminium, total length, total, length morfrac, morfrac, 60mm, aluminium dogbone    | {'product': 24}                                      | {'dogbone': 24}                 | Missing technical authority content |         145 | Create technical guide content supporting the dogbone product family.   |
|                     1 | powerfurl        |           22 |              22 |                0 |               0 |                         0 |                   0 |              0 |                        0 | FRAGMENTED_TOPIC        | kit, furling, powerfurl, 5t, 5t swl, furling kit, swl, swl morfrac, morfrac powerfurl, reliable                       | {'product': 22}                                      | {'powerfurl': 19, 'shackle': 3} | Missing technical authority content |         145 | Create technical guide content supporting the powerfurl product family. |
|                     9 | dogbone          |           10 |              10 |                0 |               0 |                         0 |                   0 |              0 |                        0 | PRODUCT_HEAVY_NO_PILLAR | flat, flat faced, faced, dogbone flat, faced titanium, dogbone, rope reeler, reeler, mreel, rope                      | {'product': 10}                                      | {'dogbone': 6, 'mreel': 4}      | Missing technical authority content |         145 | Create technical guide content supporting the dogbone product family.   |
|                     5 | morfring         |           13 |              12 |                0 |               1 |                         0 |                   0 |              0 |                        0 | OK                      | friction, morfring, ptfe, ring, friction ring, aluminium friction, aluminium, morfrac morfring, groove max, groove    | {'product': 12, 'landing': 1}                        | {'morfring': 13}                | Missing technical authority content |          91 | Create technical guide content supporting the morfring product family.  |
|                    11 | powerfurl        |            9 |               9 |                0 |               0 |                         0 |                   0 |              0 |                        0 | PRODUCT_HEAVY_NO_PILLAR | fork, 10t, 10t swl, powerfurl fork, fitting, powerfurl, fork fitting, swl, tdis, integrators                          | {'product': 9}                                       | {'powerfurl': 9}                | Missing category support            |          77 | Create or improve category structure for powerfurl pages.               |
|                    10 | padeye           |           10 |               8 |                0 |               1 |                         1 |                   0 |              0 |                        0 | OK                      | padeye, stick, deck, morfrac padeye, stick padeye, 20, ring, deck padeye, padeye ring, ring 20                        | {'product': 8, 'landing': 1, 'authority_content': 1} | {'padeye': 10}                  | Missing category support            |          44 | Create or improve category structure for padeye pages.                  |

---

# Authority Content Gaps

|   semantic_cluster_id | dominant_label   |   page_count |   product_pages |   category_pages |   landing_pages |   authority_content_pages |   total_impressions |   total_clicks |   avg_seo_priority_score | cluster_health          | top_terms                                                                                                             | role_counts                                 | label_counts                    | gap_type                            |   gap_score | recommended_action                                                      |
|----------------------:|:-----------------|-------------:|----------------:|-----------------:|----------------:|--------------------------:|--------------------:|---------------:|-------------------------:|:------------------------|:----------------------------------------------------------------------------------------------------------------------|:--------------------------------------------|:--------------------------------|:------------------------------------|------------:|:------------------------------------------------------------------------|
|                     0 | morfblock        |           14 |              14 |                0 |               0 |                         0 |                   0 |              0 |                        0 | PRODUCT_HEAVY_NO_PILLAR | xl, morfblock xl, xl sailing, sailing block, block, morfblock, sailing, swl, sheave, handling                         | {'product': 14}                             | {'morfblock': 14}               | Missing technical authority content |         155 | Create technical guide content supporting the morfblock product family. |
|                     6 | powerfurl        |           12 |              12 |                0 |               0 |                         0 |                   0 |              0 |                        0 | PRODUCT_HEAVY_NO_PILLAR | unit, powerfurl, drum, furling, powerfurl drum, unit powerfurl, unit morfrac, furling unit, powerfurl engineered, swl | {'product': 12}                             | {'powerfurl': 12}               | Missing technical authority content |         151 | Create technical guide content supporting the powerfurl product family. |
|                     3 | morfblock        |           44 |              44 |                0 |               0 |                         0 |                   0 |              0 |                        0 | FRAGMENTED_TOPIC        | sailing block, sailing, block, morfblock, morfblock light, light, swl, lightweight sailing, high, lightweight         | {'product': 44}                             | {'morfblock': 44}               | Missing technical authority content |         145 | Create technical guide content supporting the morfblock product family. |
|                     4 | dogbone          |           24 |              24 |                0 |               0 |                         0 |                   0 |              0 |                        0 | FRAGMENTED_TOPIC        | dogbone, length, morfrac dogbone, aluminium, total length, total, length morfrac, morfrac, 60mm, aluminium dogbone    | {'product': 24}                             | {'dogbone': 24}                 | Missing technical authority content |         145 | Create technical guide content supporting the dogbone product family.   |
|                     1 | powerfurl        |           22 |              22 |                0 |               0 |                         0 |                   0 |              0 |                        0 | FRAGMENTED_TOPIC        | kit, furling, powerfurl, 5t, 5t swl, furling kit, swl, swl morfrac, morfrac powerfurl, reliable                       | {'product': 22}                             | {'powerfurl': 19, 'shackle': 3} | Missing technical authority content |         145 | Create technical guide content supporting the powerfurl product family. |
|                     9 | dogbone          |           10 |              10 |                0 |               0 |                         0 |                   0 |              0 |                        0 | PRODUCT_HEAVY_NO_PILLAR | flat, flat faced, faced, dogbone flat, faced titanium, dogbone, rope reeler, reeler, mreel, rope                      | {'product': 10}                             | {'dogbone': 6, 'mreel': 4}      | Missing technical authority content |         145 | Create technical guide content supporting the dogbone product family.   |
|                     5 | morfring         |           13 |              12 |                0 |               1 |                         0 |                   0 |              0 |                        0 | OK                      | friction, morfring, ptfe, ring, friction ring, aluminium friction, aluminium, morfrac morfring, groove max, groove    | {'product': 12, 'landing': 1}               | {'morfring': 13}                | Missing technical authority content |          91 | Create technical guide content supporting the morfring product family.  |
|                    11 | powerfurl        |            9 |               9 |                0 |               0 |                         0 |                   0 |              0 |                        0 | PRODUCT_HEAVY_NO_PILLAR | fork, 10t, 10t swl, powerfurl fork, fitting, powerfurl, fork fitting, swl, tdis, integrators                          | {'product': 9}                              | {'powerfurl': 9}                | Missing category support            |          77 | Create or improve category structure for powerfurl pages.               |
|                     7 | shackle          |           11 |               8 |                2 |               1 |                         0 |                   0 |              0 |                        0 | OK                      | shackle, ti shackle, ti, titanium shackle, shackle morfrac, titanium, cnc machined, machined, cnc, grade titanium     | {'product': 8, 'category': 2, 'landing': 1} | {'shackle': 11}                 | No major gap                        |          24 | Monitor; no immediate content gap detected.                             |

---

# Missing Pillar / Landing Page Gaps

|   semantic_cluster_id | dominant_label   |   page_count |   product_pages |   category_pages |   landing_pages |   authority_content_pages |   total_impressions |   total_clicks |   avg_seo_priority_score | cluster_health          | top_terms                                                                                                             | role_counts     | label_counts                    | gap_type                            |   gap_score | recommended_action                                                      |
|----------------------:|:-----------------|-------------:|----------------:|-----------------:|----------------:|--------------------------:|--------------------:|---------------:|-------------------------:|:------------------------|:----------------------------------------------------------------------------------------------------------------------|:----------------|:--------------------------------|:------------------------------------|------------:|:------------------------------------------------------------------------|
|                     0 | morfblock        |           14 |              14 |                0 |               0 |                         0 |                   0 |              0 |                        0 | PRODUCT_HEAVY_NO_PILLAR | xl, morfblock xl, xl sailing, sailing block, block, morfblock, sailing, swl, sheave, handling                         | {'product': 14} | {'morfblock': 14}               | Missing technical authority content |         155 | Create technical guide content supporting the morfblock product family. |
|                     6 | powerfurl        |           12 |              12 |                0 |               0 |                         0 |                   0 |              0 |                        0 | PRODUCT_HEAVY_NO_PILLAR | unit, powerfurl, drum, furling, powerfurl drum, unit powerfurl, unit morfrac, furling unit, powerfurl engineered, swl | {'product': 12} | {'powerfurl': 12}               | Missing technical authority content |         151 | Create technical guide content supporting the powerfurl product family. |
|                     3 | morfblock        |           44 |              44 |                0 |               0 |                         0 |                   0 |              0 |                        0 | FRAGMENTED_TOPIC        | sailing block, sailing, block, morfblock, morfblock light, light, swl, lightweight sailing, high, lightweight         | {'product': 44} | {'morfblock': 44}               | Missing technical authority content |         145 | Create technical guide content supporting the morfblock product family. |
|                     1 | powerfurl        |           22 |              22 |                0 |               0 |                         0 |                   0 |              0 |                        0 | FRAGMENTED_TOPIC        | kit, furling, powerfurl, 5t, 5t swl, furling kit, swl, swl morfrac, morfrac powerfurl, reliable                       | {'product': 22} | {'powerfurl': 19, 'shackle': 3} | Missing technical authority content |         145 | Create technical guide content supporting the powerfurl product family. |
|                     4 | dogbone          |           24 |              24 |                0 |               0 |                         0 |                   0 |              0 |                        0 | FRAGMENTED_TOPIC        | dogbone, length, morfrac dogbone, aluminium, total length, total, length morfrac, morfrac, 60mm, aluminium dogbone    | {'product': 24} | {'dogbone': 24}                 | Missing technical authority content |         145 | Create technical guide content supporting the dogbone product family.   |
|                     9 | dogbone          |           10 |              10 |                0 |               0 |                         0 |                   0 |              0 |                        0 | PRODUCT_HEAVY_NO_PILLAR | flat, flat faced, faced, dogbone flat, faced titanium, dogbone, rope reeler, reeler, mreel, rope                      | {'product': 10} | {'dogbone': 6, 'mreel': 4}      | Missing technical authority content |         145 | Create technical guide content supporting the dogbone product family.   |
|                    11 | powerfurl        |            9 |               9 |                0 |               0 |                         0 |                   0 |              0 |                        0 | PRODUCT_HEAVY_NO_PILLAR | fork, 10t, 10t swl, powerfurl fork, fitting, powerfurl, fork fitting, swl, tdis, integrators                          | {'product': 9}  | {'powerfurl': 9}                | Missing category support            |          77 | Create or improve category structure for powerfurl pages.               |

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

- Content gap analysis: `C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC\06_MARKETING\SEO_Agent\Content_Gap_Analysis\2026-06-15_content_gap_analysis.csv`
- Authority gap analysis: `C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC\06_MARKETING\SEO_Agent\Content_Gap_Analysis\2026-06-15_authority_gap_analysis.csv`
- Missing pillar pages: `C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC\06_MARKETING\SEO_Agent\Content_Gap_Analysis\2026-06-15_missing_pillar_pages.csv`
- Orphan commercial topics: `C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC\06_MARKETING\SEO_Agent\Content_Gap_Analysis\2026-06-15_orphan_commercial_topics.csv`
- Page support summary: `C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC\06_MARKETING\SEO_Agent\Content_Gap_Analysis\2026-06-15_page_support_summary.csv`

## Related Links

### Concepts
- [[PRODUCT_HEAVY_NO_PILLAR]]
- [[FRAGMENTED_TOPIC]]

### Projects
- [[Search Console]]
