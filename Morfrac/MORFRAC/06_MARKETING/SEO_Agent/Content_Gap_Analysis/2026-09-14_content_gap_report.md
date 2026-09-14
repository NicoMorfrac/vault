---
type: seo_content_gap_report
source_agent: SEO_Agent
created: 2026-09-14
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

2026-09-14

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

- Semantic clusters: `C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC\06_MARKETING\SEO_Agent\Semantic_Clusters\2026-09-14_semantic_clusters.csv`
- Semantic pages: `C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC\06_MARKETING\SEO_Agent\Semantic_Clusters\2026-09-14_semantic_cluster_pages.csv`
- Search Console merge: `C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC\06_MARKETING\SEO_Agent\Merged_Analysis\2026-09-14_search_console_merge.csv`
- Contextual links: `C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC\06_MARKETING\SEO_Agent\Contextual_Links\2026-09-14_contextual_link_recommendations_filtered.csv`

---

# Summary

- Semantic clusters reviewed: 12
- Content gaps detected: 11
- Authority gaps detected: 10
- Missing pillar-page gaps: 8
- Orphan commercial topics: 0

---

# Highest Priority Content Gaps

|   semantic_cluster_id | dominant_label   |   page_count |   product_pages |   category_pages |   landing_pages |   authority_content_pages |   total_impressions |   total_clicks |   avg_seo_priority_score | cluster_health          | top_terms                                                                                                                    | role_counts                                                           | label_counts                                                                                                                                                            | gap_type                            |   gap_score | recommended_action                                                      |
|----------------------:|:-----------------|-------------:|----------------:|-----------------:|----------------:|--------------------------:|--------------------:|---------------:|-------------------------:|:------------------------|:-----------------------------------------------------------------------------------------------------------------------------|:----------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:------------------------------------|------------:|:------------------------------------------------------------------------|
|                     7 | morfblock        |           14 |              14 |                0 |               0 |                         0 |                   0 |              0 |                     0    | PRODUCT_HEAVY_NO_PILLAR | xl, morfblock xl, xl sailing, sailing block, block, morfblock, sailing, swl, sheave, handling                                | {'product': 14}                                                       | {'morfblock': 14}                                                                                                                                                       | Missing technical authority content |      155    | Create technical guide content supporting the morfblock product family. |
|                    11 | dogbone          |           16 |              16 |                0 |               0 |                         0 |                   0 |              0 |                     0    | PRODUCT_HEAVY_NO_PILLAR | dogbone, length, morfrac dogbone, aluminium, 60mm, total, length morfrac, total length, dogbone aluminium, aluminium dogbone | {'product': 16}                                                       | {'dogbone': 16}                                                                                                                                                         | Missing technical authority content |      155    | Create technical guide content supporting the dogbone product family.   |
|                     2 | powerfurl        |           15 |              15 |                0 |               0 |                         0 |                   0 |              0 |                     0    | PRODUCT_HEAVY_NO_PILLAR | unit, powerfurl, furling, drum, powerfurl drum, furling unit, unit morfrac, unit powerfurl, powerfurl engineered, swivelhead | {'product': 15}                                                       | {'powerfurl': 15}                                                                                                                                                       | Missing technical authority content |      155    | Create technical guide content supporting the powerfurl product family. |
|                     0 | dogbone          |           14 |              14 |                0 |               0 |                         0 |                   0 |              0 |                     0    | PRODUCT_HEAVY_NO_PILLAR | dogbone, morfrac dogbone, faced, flat faced, flat, titanium, length, faced titanium, dogbone flat, titanium dogbone          | {'product': 14}                                                       | {'dogbone': 14}                                                                                                                                                         | Missing technical authority content |      155    | Create technical guide content supporting the dogbone product family.   |
|                     8 | powerfurl        |           10 |              10 |                0 |               0 |                         0 |                   0 |              0 |                     0    | PRODUCT_HEAVY_NO_PILLAR | integrator, powerfurl, tdis, integrators, lashing, 5t, 5t swl, furling performance, swl, swl integrator                      | {'product': 10}                                                       | {'powerfurl': 10}                                                                                                                                                       | Missing technical authority content |      145    | Create technical guide content supporting the powerfurl product family. |
|                    10 | powerfurl        |           21 |              21 |                0 |               0 |                         0 |                   0 |              0 |                     0    | FRAGMENTED_TOPIC        | kit, furling, furling kit, powerfurl, 5t swl, 5t, powerfurl kit, swl, powerfurl furling, line furling                        | {'product': 21}                                                       | {'powerfurl': 17, 'shackle': 4}                                                                                                                                         | Missing technical authority content |      145    | Create technical guide content supporting the powerfurl product family. |
|                     3 | morfblock        |           46 |              44 |                2 |               0 |                         0 |                   0 |              0 |                     0    | FRAGMENTED_TOPIC        | sailing block, morfblock, sailing, block, morfblock light, light, swl, lightweight sailing, high, lightweight                | {'product': 44, 'category': 2}                                        | {'morfblock': 46}                                                                                                                                                       | Missing technical authority content |      125    | Create technical guide content supporting the morfblock product family. |
|                     9 | other            |           59 |              23 |                0 |               4 |                        21 |                 433 |              3 |                     3.29 | FRAGMENTED_TOPIC        | custom, padeye, morfrac, deck, morfblock, snatch, high performance, mreel, performance, hardware                             | {'product': 23, 'authority_content': 21, 'general': 11, 'landing': 4} | {'other': 14, 'powerfurl': 8, 'morfblock': 8, 'custom_engineering': 6, 'padeye': 6, 'morfwing': 4, 'mloop': 4, 'mreel': 4, 'dogbone': 3, 'morfring': 1, 'hoistlock': 1} | Missing category support            |      116.29 | Create or improve category structure for other pages.                   |
|                     5 | morfring         |           16 |              15 |                0 |               1 |                         0 |                   0 |              0 |                     0    | OK                      | ring, friction, friction ring, morfring, aluminium friction, ptfe, aluminium, ring morfrac, morfrac morfring, groove max     | {'product': 15, 'landing': 1}                                         | {'morfring': 13, 'padeye': 3}                                                                                                                                           | Missing technical authority content |       95    | Create technical guide content supporting the morfring product family.  |
|                     6 | powerfurl        |            9 |               9 |                0 |               0 |                         0 |                   0 |              0 |                     0    | PRODUCT_HEAVY_NO_PILLAR | fork, fitting, powerfurl fork, fork fitting, powerfurl, 10t, 10t swl, fork titanium, fork fork, detachable                   | {'product': 9}                                                        | {'powerfurl': 9}                                                                                                                                                        | Missing category support            |       77    | Create or improve category structure for powerfurl pages.               |
|                     4 | shackle          |           10 |               9 |                0 |               1 |                         0 |                   0 |              0 |                     0    | OK                      | shackle, ti shackle, ti, titanium shackle, titanium, ø6mm, machined, cnc machined, cnc, ultra                                | {'product': 9, 'landing': 1}                                          | {'shackle': 10}                                                                                                                                                         | Missing category support            |       47    | Create or improve category structure for shackle pages.                 |

---

# Authority Content Gaps

|   semantic_cluster_id | dominant_label   |   page_count |   product_pages |   category_pages |   landing_pages |   authority_content_pages |   total_impressions |   total_clicks |   avg_seo_priority_score | cluster_health          | top_terms                                                                                                                    | role_counts                    | label_counts                    | gap_type                            |   gap_score | recommended_action                                                      |
|----------------------:|:-----------------|-------------:|----------------:|-----------------:|----------------:|--------------------------:|--------------------:|---------------:|-------------------------:|:------------------------|:-----------------------------------------------------------------------------------------------------------------------------|:-------------------------------|:--------------------------------|:------------------------------------|------------:|:------------------------------------------------------------------------|
|                    11 | dogbone          |           16 |              16 |                0 |               0 |                         0 |                   0 |              0 |                        0 | PRODUCT_HEAVY_NO_PILLAR | dogbone, length, morfrac dogbone, aluminium, 60mm, total, length morfrac, total length, dogbone aluminium, aluminium dogbone | {'product': 16}                | {'dogbone': 16}                 | Missing technical authority content |         155 | Create technical guide content supporting the dogbone product family.   |
|                     2 | powerfurl        |           15 |              15 |                0 |               0 |                         0 |                   0 |              0 |                        0 | PRODUCT_HEAVY_NO_PILLAR | unit, powerfurl, furling, drum, powerfurl drum, furling unit, unit morfrac, unit powerfurl, powerfurl engineered, swivelhead | {'product': 15}                | {'powerfurl': 15}               | Missing technical authority content |         155 | Create technical guide content supporting the powerfurl product family. |
|                     7 | morfblock        |           14 |              14 |                0 |               0 |                         0 |                   0 |              0 |                        0 | PRODUCT_HEAVY_NO_PILLAR | xl, morfblock xl, xl sailing, sailing block, block, morfblock, sailing, swl, sheave, handling                                | {'product': 14}                | {'morfblock': 14}               | Missing technical authority content |         155 | Create technical guide content supporting the morfblock product family. |
|                     0 | dogbone          |           14 |              14 |                0 |               0 |                         0 |                   0 |              0 |                        0 | PRODUCT_HEAVY_NO_PILLAR | dogbone, morfrac dogbone, faced, flat faced, flat, titanium, length, faced titanium, dogbone flat, titanium dogbone          | {'product': 14}                | {'dogbone': 14}                 | Missing technical authority content |         155 | Create technical guide content supporting the dogbone product family.   |
|                     8 | powerfurl        |           10 |              10 |                0 |               0 |                         0 |                   0 |              0 |                        0 | PRODUCT_HEAVY_NO_PILLAR | integrator, powerfurl, tdis, integrators, lashing, 5t, 5t swl, furling performance, swl, swl integrator                      | {'product': 10}                | {'powerfurl': 10}               | Missing technical authority content |         145 | Create technical guide content supporting the powerfurl product family. |
|                    10 | powerfurl        |           21 |              21 |                0 |               0 |                         0 |                   0 |              0 |                        0 | FRAGMENTED_TOPIC        | kit, furling, furling kit, powerfurl, 5t swl, 5t, powerfurl kit, swl, powerfurl furling, line furling                        | {'product': 21}                | {'powerfurl': 17, 'shackle': 4} | Missing technical authority content |         145 | Create technical guide content supporting the powerfurl product family. |
|                     3 | morfblock        |           46 |              44 |                2 |               0 |                         0 |                   0 |              0 |                        0 | FRAGMENTED_TOPIC        | sailing block, morfblock, sailing, block, morfblock light, light, swl, lightweight sailing, high, lightweight                | {'product': 44, 'category': 2} | {'morfblock': 46}               | Missing technical authority content |         125 | Create technical guide content supporting the morfblock product family. |
|                     5 | morfring         |           16 |              15 |                0 |               1 |                         0 |                   0 |              0 |                        0 | OK                      | ring, friction, friction ring, morfring, aluminium friction, ptfe, aluminium, ring morfrac, morfrac morfring, groove max     | {'product': 15, 'landing': 1}  | {'morfring': 13, 'padeye': 3}   | Missing technical authority content |          95 | Create technical guide content supporting the morfring product family.  |
|                     6 | powerfurl        |            9 |               9 |                0 |               0 |                         0 |                   0 |              0 |                        0 | PRODUCT_HEAVY_NO_PILLAR | fork, fitting, powerfurl fork, fork fitting, powerfurl, 10t, 10t swl, fork titanium, fork fork, detachable                   | {'product': 9}                 | {'powerfurl': 9}                | Missing category support            |          77 | Create or improve category structure for powerfurl pages.               |
|                     4 | shackle          |           10 |               9 |                0 |               1 |                         0 |                   0 |              0 |                        0 | OK                      | shackle, ti shackle, ti, titanium shackle, titanium, ø6mm, machined, cnc machined, cnc, ultra                                | {'product': 9, 'landing': 1}   | {'shackle': 10}                 | Missing category support            |          47 | Create or improve category structure for shackle pages.                 |

---

# Missing Pillar / Landing Page Gaps

|   semantic_cluster_id | dominant_label   |   page_count |   product_pages |   category_pages |   landing_pages |   authority_content_pages |   total_impressions |   total_clicks |   avg_seo_priority_score | cluster_health          | top_terms                                                                                                                    | role_counts                    | label_counts                    | gap_type                            |   gap_score | recommended_action                                                      |
|----------------------:|:-----------------|-------------:|----------------:|-----------------:|----------------:|--------------------------:|--------------------:|---------------:|-------------------------:|:------------------------|:-----------------------------------------------------------------------------------------------------------------------------|:-------------------------------|:--------------------------------|:------------------------------------|------------:|:------------------------------------------------------------------------|
|                     2 | powerfurl        |           15 |              15 |                0 |               0 |                         0 |                   0 |              0 |                        0 | PRODUCT_HEAVY_NO_PILLAR | unit, powerfurl, furling, drum, powerfurl drum, furling unit, unit morfrac, unit powerfurl, powerfurl engineered, swivelhead | {'product': 15}                | {'powerfurl': 15}               | Missing technical authority content |         155 | Create technical guide content supporting the powerfurl product family. |
|                    11 | dogbone          |           16 |              16 |                0 |               0 |                         0 |                   0 |              0 |                        0 | PRODUCT_HEAVY_NO_PILLAR | dogbone, length, morfrac dogbone, aluminium, 60mm, total, length morfrac, total length, dogbone aluminium, aluminium dogbone | {'product': 16}                | {'dogbone': 16}                 | Missing technical authority content |         155 | Create technical guide content supporting the dogbone product family.   |
|                     7 | morfblock        |           14 |              14 |                0 |               0 |                         0 |                   0 |              0 |                        0 | PRODUCT_HEAVY_NO_PILLAR | xl, morfblock xl, xl sailing, sailing block, block, morfblock, sailing, swl, sheave, handling                                | {'product': 14}                | {'morfblock': 14}               | Missing technical authority content |         155 | Create technical guide content supporting the morfblock product family. |
|                     0 | dogbone          |           14 |              14 |                0 |               0 |                         0 |                   0 |              0 |                        0 | PRODUCT_HEAVY_NO_PILLAR | dogbone, morfrac dogbone, faced, flat faced, flat, titanium, length, faced titanium, dogbone flat, titanium dogbone          | {'product': 14}                | {'dogbone': 14}                 | Missing technical authority content |         155 | Create technical guide content supporting the dogbone product family.   |
|                     8 | powerfurl        |           10 |              10 |                0 |               0 |                         0 |                   0 |              0 |                        0 | PRODUCT_HEAVY_NO_PILLAR | integrator, powerfurl, tdis, integrators, lashing, 5t, 5t swl, furling performance, swl, swl integrator                      | {'product': 10}                | {'powerfurl': 10}               | Missing technical authority content |         145 | Create technical guide content supporting the powerfurl product family. |
|                    10 | powerfurl        |           21 |              21 |                0 |               0 |                         0 |                   0 |              0 |                        0 | FRAGMENTED_TOPIC        | kit, furling, furling kit, powerfurl, 5t swl, 5t, powerfurl kit, swl, powerfurl furling, line furling                        | {'product': 21}                | {'powerfurl': 17, 'shackle': 4} | Missing technical authority content |         145 | Create technical guide content supporting the powerfurl product family. |
|                     3 | morfblock        |           46 |              44 |                2 |               0 |                         0 |                   0 |              0 |                        0 | FRAGMENTED_TOPIC        | sailing block, morfblock, sailing, block, morfblock light, light, swl, lightweight sailing, high, lightweight                | {'product': 44, 'category': 2} | {'morfblock': 46}               | Missing technical authority content |         125 | Create technical guide content supporting the morfblock product family. |
|                     6 | powerfurl        |            9 |               9 |                0 |               0 |                         0 |                   0 |              0 |                        0 | PRODUCT_HEAVY_NO_PILLAR | fork, fitting, powerfurl fork, fork fitting, powerfurl, 10t, 10t swl, fork titanium, fork fork, detachable                   | {'product': 9}                 | {'powerfurl': 9}                | Missing category support            |          77 | Create or improve category structure for powerfurl pages.               |

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

- Content gap analysis: `C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC\06_MARKETING\SEO_Agent\Content_Gap_Analysis\2026-09-14_content_gap_analysis.csv`
- Authority gap analysis: `C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC\06_MARKETING\SEO_Agent\Content_Gap_Analysis\2026-09-14_authority_gap_analysis.csv`
- Missing pillar pages: `C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC\06_MARKETING\SEO_Agent\Content_Gap_Analysis\2026-09-14_missing_pillar_pages.csv`
- Orphan commercial topics: `C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC\06_MARKETING\SEO_Agent\Content_Gap_Analysis\2026-09-14_orphan_commercial_topics.csv`
- Page support summary: `C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC\06_MARKETING\SEO_Agent\Content_Gap_Analysis\2026-09-14_page_support_summary.csv`

## Related Links

### Concepts
- [[PRODUCT_HEAVY_NO_PILLAR]]
- [[FRAGMENTED_TOPIC]]

### Projects
- [[Search Console]]
