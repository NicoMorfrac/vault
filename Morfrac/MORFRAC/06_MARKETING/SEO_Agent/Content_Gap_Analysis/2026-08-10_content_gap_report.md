---
type: seo_content_gap_report
source_agent: SEO_Agent
created: 2026-08-10
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

2026-08-10

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

- Semantic clusters: `C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC\06_MARKETING\SEO_Agent\Semantic_Clusters\2026-08-10_semantic_clusters.csv`
- Semantic pages: `C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC\06_MARKETING\SEO_Agent\Semantic_Clusters\2026-08-10_semantic_cluster_pages.csv`
- Search Console merge: `C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC\06_MARKETING\SEO_Agent\Merged_Analysis\2026-08-10_search_console_merge.csv`
- Contextual links: `C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC\06_MARKETING\SEO_Agent\Contextual_Links\2026-08-10_contextual_link_recommendations_filtered.csv`

---

# Summary

- Semantic clusters reviewed: 12
- Content gaps detected: 9
- Authority gaps detected: 9
- Missing pillar-page gaps: 5
- Orphan commercial topics: 0

---

# Highest Priority Content Gaps

|   semantic_cluster_id | dominant_label   |   page_count |   product_pages |   category_pages |   landing_pages |   authority_content_pages |   total_impressions |   total_clicks |   avg_seo_priority_score | cluster_health          | top_terms                                                                                                       | role_counts                                                           | label_counts                                                                                                                    | gap_type                                |   gap_score | recommended_action                                                         |
|----------------------:|:-----------------|-------------:|----------------:|-----------------:|----------------:|--------------------------:|--------------------:|---------------:|-------------------------:|:------------------------|:----------------------------------------------------------------------------------------------------------------|:----------------------------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------|:----------------------------------------|------------:|:---------------------------------------------------------------------------|
|                     7 | powerfurl        |           15 |              15 |                0 |               0 |                         0 |                   0 |              0 |                     0    | PRODUCT_HEAVY_NO_PILLAR | powerfurl, unit, furling, drum, 10t swl, 10t, swl, powerfurl drum, furling unit, unit powerfurl                 | {'product': 15}                                                       | {'powerfurl': 15}                                                                                                               | Missing technical authority content     |      155    | Create technical guide content supporting the powerfurl product family.    |
|                    11 | morfblock        |           14 |              14 |                0 |               0 |                         0 |                   0 |              0 |                     0    | PRODUCT_HEAVY_NO_PILLAR | xl, morfblock xl, xl sailing, sailing block, block, morfblock, sailing, swl, sheave, handling                   | {'product': 14}                                                       | {'morfblock': 14}                                                                                                               | Missing technical authority content     |      155    | Create technical guide content supporting the morfblock product family.    |
|                     6 | dogbone          |           31 |              30 |                0 |               1 |                         0 |                 347 |              4 |                     2.76 | FRAGMENTED_TOPIC        | dogbone, morfrac dogbone, length, aluminium, morfrac, total length, total, length morfrac, titanium, flat       | {'product': 30, 'landing': 1}                                         | {'dogbone': 31}                                                                                                                 | Missing technical authority content     |      151.76 | Create technical guide content supporting the dogbone product family.      |
|                     5 | morfring         |           22 |              20 |                0 |               2 |                         0 |                 274 |              3 |                     3.77 | FRAGMENTED_TOPIC        | padeye, ring, friction, friction ring, morfring, aluminium friction, ptfe, aluminium, stick, deck               | {'product': 20, 'landing': 2}                                         | {'morfring': 13, 'padeye': 9}                                                                                                   | Missing technical authority content     |      149.17 | Create technical guide content supporting the morfring product family.     |
|                     1 | powerfurl        |           27 |              27 |                0 |               0 |                         0 |                   0 |              0 |                     0    | FRAGMENTED_TOPIC        | powerfurl, kit, furling, 5t, 5t swl, swl, furling kit, morfrac powerfurl, swl morfrac, reliable                 | {'product': 27}                                                       | {'powerfurl': 24, 'shackle': 3}                                                                                                 | Missing technical authority content     |      145    | Create technical guide content supporting the powerfurl product family.    |
|                     0 | morfblock        |           38 |              38 |                0 |               0 |                         0 |                   0 |              0 |                     0    | FRAGMENTED_TOPIC        | morfblock light, light, sailing block, block, morfblock, sailing, swl, lightweight sailing, high, lightweight   | {'product': 38}                                                       | {'morfblock': 38}                                                                                                               | Missing technical authority content     |      145    | Create technical guide content supporting the morfblock product family.    |
|                     8 | other            |           43 |              11 |                0 |               3 |                        18 |                   0 |              0 |                     0    | FRAGMENTED_TOPIC        | custom, morfrac, morfwing, new, car, 2024, morfblock, high performance, hardware, sail                          | {'authority_content': 18, 'general': 11, 'product': 11, 'landing': 3} | {'other': 15, 'powerfurl': 6, 'custom_engineering': 5, 'morfblock': 5, 'morfwing': 5, 'mloop': 4, 'dogbone': 2, 'hoistlock': 1} | Missing category support                |       73    | Create or improve category structure for other pages.                      |
|                     9 | mreel            |            5 |               4 |                0 |               0 |                         0 |                 117 |             16 |                     5.98 | OK                      | mreel, reeler, rope reeler, mreel rope, rope, morfrac mreel, reeler morfrac, safer, manoeuvres, sheets halyards | {'product': 4, 'general': 1}                                          | {'mreel': 4, 'powerfurl': 1}                                                                                                    | Search demand without authority support |       45.68 | Build authority content around mreel queries and link to commercial pages. |
|                    10 | shackle          |            9 |               8 |                0 |               1 |                         0 |                   0 |              0 |                     0    | OK                      | shackle, ti shackle, ti, titanium shackle, titanium, machined, cnc machined, cnc, ultra, grade                  | {'product': 8, 'landing': 1}                                          | {'shackle': 9}                                                                                                                  | Missing category support                |       44    | Create or improve category structure for shackle pages.                    |

---

# Authority Content Gaps

|   semantic_cluster_id | dominant_label   |   page_count |   product_pages |   category_pages |   landing_pages |   authority_content_pages |   total_impressions |   total_clicks |   avg_seo_priority_score | cluster_health          | top_terms                                                                                                                          | role_counts                   | label_counts                    | gap_type                                |   gap_score | recommended_action                                                         |
|----------------------:|:-----------------|-------------:|----------------:|-----------------:|----------------:|--------------------------:|--------------------:|---------------:|-------------------------:|:------------------------|:-----------------------------------------------------------------------------------------------------------------------------------|:------------------------------|:--------------------------------|:----------------------------------------|------------:|:---------------------------------------------------------------------------|
|                     7 | powerfurl        |           15 |              15 |                0 |               0 |                         0 |                   0 |              0 |                     0    | PRODUCT_HEAVY_NO_PILLAR | powerfurl, unit, furling, drum, 10t swl, 10t, swl, powerfurl drum, furling unit, unit powerfurl                                    | {'product': 15}               | {'powerfurl': 15}               | Missing technical authority content     |      155    | Create technical guide content supporting the powerfurl product family.    |
|                    11 | morfblock        |           14 |              14 |                0 |               0 |                         0 |                   0 |              0 |                     0    | PRODUCT_HEAVY_NO_PILLAR | xl, morfblock xl, xl sailing, sailing block, block, morfblock, sailing, swl, sheave, handling                                      | {'product': 14}               | {'morfblock': 14}               | Missing technical authority content     |      155    | Create technical guide content supporting the morfblock product family.    |
|                     6 | dogbone          |           31 |              30 |                0 |               1 |                         0 |                 347 |              4 |                     2.76 | FRAGMENTED_TOPIC        | dogbone, morfrac dogbone, length, aluminium, morfrac, total length, total, length morfrac, titanium, flat                          | {'product': 30, 'landing': 1} | {'dogbone': 31}                 | Missing technical authority content     |      151.76 | Create technical guide content supporting the dogbone product family.      |
|                     5 | morfring         |           22 |              20 |                0 |               2 |                         0 |                 274 |              3 |                     3.77 | FRAGMENTED_TOPIC        | padeye, ring, friction, friction ring, morfring, aluminium friction, ptfe, aluminium, stick, deck                                  | {'product': 20, 'landing': 2} | {'morfring': 13, 'padeye': 9}   | Missing technical authority content     |      149.17 | Create technical guide content supporting the morfring product family.     |
|                     0 | morfblock        |           38 |              38 |                0 |               0 |                         0 |                   0 |              0 |                     0    | FRAGMENTED_TOPIC        | morfblock light, light, sailing block, block, morfblock, sailing, swl, lightweight sailing, high, lightweight                      | {'product': 38}               | {'morfblock': 38}               | Missing technical authority content     |      145    | Create technical guide content supporting the morfblock product family.    |
|                     1 | powerfurl        |           27 |              27 |                0 |               0 |                         0 |                   0 |              0 |                     0    | FRAGMENTED_TOPIC        | powerfurl, kit, furling, 5t, 5t swl, swl, furling kit, morfrac powerfurl, swl morfrac, reliable                                    | {'product': 27}               | {'powerfurl': 24, 'shackle': 3} | Missing technical authority content     |      145    | Create technical guide content supporting the powerfurl product family.    |
|                     9 | mreel            |            5 |               4 |                0 |               0 |                         0 |                 117 |             16 |                     5.98 | OK                      | mreel, reeler, rope reeler, mreel rope, rope, morfrac mreel, reeler morfrac, safer, manoeuvres, sheets halyards                    | {'product': 4, 'general': 1}  | {'mreel': 4, 'powerfurl': 1}    | Search demand without authority support |       45.68 | Build authority content around mreel queries and link to commercial pages. |
|                    10 | shackle          |            9 |               8 |                0 |               1 |                         0 |                   0 |              0 |                     0    | OK                      | shackle, ti shackle, ti, titanium shackle, titanium, machined, cnc machined, cnc, ultra, grade                                     | {'product': 8, 'landing': 1}  | {'shackle': 9}                  | Missing category support                |       44    | Create or improve category structure for shackle pages.                    |
|                     2 | morfblock        |            8 |               6 |                2 |               0 |                         0 |                   0 |              0 |                     0    | OK                      | morfblock max, max, morfblock, sailing, efficiency, sailing block, maximum reliability, block, efficiency sailing, max lightweight | {'product': 6, 'category': 2} | {'morfblock': 8}                | No major gap                            |       18    | Monitor; no immediate content gap detected.                                |

---

# Missing Pillar / Landing Page Gaps

|   semantic_cluster_id | dominant_label   |   page_count |   product_pages |   category_pages |   landing_pages |   authority_content_pages |   total_impressions |   total_clicks |   avg_seo_priority_score | cluster_health          | top_terms                                                                                                                          | role_counts                   | label_counts                    | gap_type                            |   gap_score | recommended_action                                                      |
|----------------------:|:-----------------|-------------:|----------------:|-----------------:|----------------:|--------------------------:|--------------------:|---------------:|-------------------------:|:------------------------|:-----------------------------------------------------------------------------------------------------------------------------------|:------------------------------|:--------------------------------|:------------------------------------|------------:|:------------------------------------------------------------------------|
|                    11 | morfblock        |           14 |              14 |                0 |               0 |                         0 |                   0 |              0 |                        0 | PRODUCT_HEAVY_NO_PILLAR | xl, morfblock xl, xl sailing, sailing block, block, morfblock, sailing, swl, sheave, handling                                      | {'product': 14}               | {'morfblock': 14}               | Missing technical authority content |         155 | Create technical guide content supporting the morfblock product family. |
|                     7 | powerfurl        |           15 |              15 |                0 |               0 |                         0 |                   0 |              0 |                        0 | PRODUCT_HEAVY_NO_PILLAR | powerfurl, unit, furling, drum, 10t swl, 10t, swl, powerfurl drum, furling unit, unit powerfurl                                    | {'product': 15}               | {'powerfurl': 15}               | Missing technical authority content |         155 | Create technical guide content supporting the powerfurl product family. |
|                     0 | morfblock        |           38 |              38 |                0 |               0 |                         0 |                   0 |              0 |                        0 | FRAGMENTED_TOPIC        | morfblock light, light, sailing block, block, morfblock, sailing, swl, lightweight sailing, high, lightweight                      | {'product': 38}               | {'morfblock': 38}               | Missing technical authority content |         145 | Create technical guide content supporting the morfblock product family. |
|                     1 | powerfurl        |           27 |              27 |                0 |               0 |                         0 |                   0 |              0 |                        0 | FRAGMENTED_TOPIC        | powerfurl, kit, furling, 5t, 5t swl, swl, furling kit, morfrac powerfurl, swl morfrac, reliable                                    | {'product': 27}               | {'powerfurl': 24, 'shackle': 3} | Missing technical authority content |         145 | Create technical guide content supporting the powerfurl product family. |
|                     2 | morfblock        |            8 |               6 |                2 |               0 |                         0 |                   0 |              0 |                        0 | OK                      | morfblock max, max, morfblock, sailing, efficiency, sailing block, maximum reliability, block, efficiency sailing, max lightweight | {'product': 6, 'category': 2} | {'morfblock': 8}                | No major gap                        |          18 | Monitor; no immediate content gap detected.                             |

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

- Content gap analysis: `C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC\06_MARKETING\SEO_Agent\Content_Gap_Analysis\2026-08-10_content_gap_analysis.csv`
- Authority gap analysis: `C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC\06_MARKETING\SEO_Agent\Content_Gap_Analysis\2026-08-10_authority_gap_analysis.csv`
- Missing pillar pages: `C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC\06_MARKETING\SEO_Agent\Content_Gap_Analysis\2026-08-10_missing_pillar_pages.csv`
- Orphan commercial topics: `C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC\06_MARKETING\SEO_Agent\Content_Gap_Analysis\2026-08-10_orphan_commercial_topics.csv`
- Page support summary: `C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC\06_MARKETING\SEO_Agent\Content_Gap_Analysis\2026-08-10_page_support_summary.csv`

## Related Links

### Concepts
- [[PRODUCT_HEAVY_NO_PILLAR]]
- [[FRAGMENTED_TOPIC]]

### Projects
- [[Search Console]]
