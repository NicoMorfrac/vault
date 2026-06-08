---
type: seo_content_gap_report
source_agent: SEO_Agent
created: 2026-06-08
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

2026-06-08

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

- Semantic clusters: `C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC\06_MARKETING\SEO_Agent\Semantic_Clusters\2026-06-08_semantic_clusters.csv`
- Semantic pages: `C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC\06_MARKETING\SEO_Agent\Semantic_Clusters\2026-06-08_semantic_cluster_pages.csv`
- Search Console merge: `C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC\06_MARKETING\SEO_Agent\Merged_Analysis\2026-06-08_search_console_merge.csv`
- Contextual links: `C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC\06_MARKETING\SEO_Agent\Contextual_Links\2026-06-08_contextual_link_recommendations_filtered.csv`

---

# Summary

- Semantic clusters reviewed: 12
- Content gaps detected: 9
- Authority gaps detected: 7
- Missing pillar-page gaps: 5
- Orphan commercial topics: 0

---

# Highest Priority Content Gaps

|   semantic_cluster_id | dominant_label   |   page_count |   product_pages |   category_pages |   landing_pages |   authority_content_pages |   total_impressions |   total_clicks |   avg_seo_priority_score | cluster_health          | top_terms                                                                                                          | role_counts                                                           | label_counts                                                                                                                                | gap_type                                  |   gap_score | recommended_action                                                               |
|----------------------:|:-----------------|-------------:|----------------:|-----------------:|----------------:|--------------------------:|--------------------:|---------------:|-------------------------:|:------------------------|:-------------------------------------------------------------------------------------------------------------------|:----------------------------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------|:------------------------------------------|------------:|:---------------------------------------------------------------------------------|
|                     2 | powerfurl        |           19 |              19 |                0 |               0 |                         0 |                   0 |              0 |                     0    | PRODUCT_HEAVY_NO_PILLAR | 10t, 10t swl, powerfurl, furling, drum, fork, swl, powerfurl drum, powerfurl fork, fitting                         | {'product': 19}                                                       | {'powerfurl': 19}                                                                                                                           | Missing technical authority content       |      155    | Create technical guide content supporting the powerfurl product family.          |
|                     8 | morfring         |           12 |              12 |                0 |               0 |                         0 |                   0 |              0 |                     0    | PRODUCT_HEAVY_NO_PILLAR | friction, ptfe, ring, friction ring, morfring, aluminium friction, aluminium, groove, groove max, morfrac morfring | {'product': 12}                                                       | {'morfring': 12}                                                                                                                            | Missing technical authority content       |      151    | Create technical guide content supporting the morfring product family.           |
|                     4 | morfblock        |           58 |              58 |                0 |               0 |                         0 |                   0 |              0 |                     0    | FRAGMENTED_TOPIC        | sailing block, block, sailing, morfblock, swl, morfblock light, light, high, xl, lightweight sailing               | {'product': 58}                                                       | {'morfblock': 58}                                                                                                                           | Missing technical authority content       |      145    | Create technical guide content supporting the morfblock product family.          |
|                     3 | dogbone          |           30 |              30 |                0 |               0 |                         0 |                   0 |              0 |                     0    | FRAGMENTED_TOPIC        | dogbone, morfrac dogbone, length, aluminium, morfrac, length morfrac, total length, total, titanium, faced         | {'product': 30}                                                       | {'dogbone': 30}                                                                                                                             | Missing technical authority content       |      145    | Create technical guide content supporting the dogbone product family.            |
|                     6 | powerfurl        |           24 |              24 |                0 |               0 |                         0 |                   0 |              0 |                     0    | FRAGMENTED_TOPIC        | powerfurl, 5t swl, 5t, furling, kit, swl, morfrac powerfurl, furling kit, reliable, unit                           | {'product': 24}                                                       | {'powerfurl': 21, 'shackle': 3}                                                                                                             | Missing technical authority content       |      145    | Create technical guide content supporting the powerfurl product family.          |
|                     0 | morfblock        |           36 |              11 |                0 |               4 |                        11 |                 616 |              2 |                     2.79 | FRAGMENTED_TOPIC        | custom, morfrac, snatch, morfblock, solutions, high performance, loop, performance, mloop, powerfurl               | {'authority_content': 11, 'product': 11, 'general': 10, 'landing': 4} | {'morfblock': 8, 'other': 7, 'powerfurl': 6, 'custom_engineering': 5, 'mloop': 4, 'dogbone': 2, 'morfring': 2, 'padeye': 1, 'hoistlock': 1} | Missing category support                  |      107.79 | Create or improve category structure for morfblock pages.                        |
|                    11 | mreel            |            5 |               4 |                0 |               0 |                         0 |                 126 |             27 |                    11.6  | OK                      | mreel, rope reeler, reeler, mreel rope, rope, reeler morfrac, morfrac mreel, halyards, sheets halyards, safer      | {'product': 4, 'general': 1}                                          | {'mreel': 4, 'powerfurl': 1}                                                                                                                | Search demand without authority support   |       56.2  | Build authority content around mreel queries and link to commercial pages.       |
|                     7 | padeye           |           10 |               8 |                0 |               1 |                         1 |                   0 |              0 |                     0    | OK                      | padeye, stick, deck, morfrac padeye, stick padeye, 20, ring, deck padeye, padeye ring, ring 20                     | {'product': 8, 'landing': 1, 'authority_content': 1}                  | {'padeye': 10}                                                                                                                              | Missing category support                  |       44    | Create or improve category structure for padeye pages.                           |
|                     5 | morfwing         |           10 |               0 |                0 |               1 |                         9 |                   0 |              0 |                     0    | OK                      | morfwing, 2024, year, introducing, new, wing, sail, 372, stand 01, stand                                           | {'authority_content': 9, 'landing': 1}                                | {'morfwing': 5, 'other': 4, 'powerfurl': 1}                                                                                                 | Authority content lacks commercial target |       15    | Link existing authority content toward relevant morfwing product/category pages. |

---

# Authority Content Gaps

|   semantic_cluster_id | dominant_label   |   page_count |   product_pages |   category_pages |   landing_pages |   authority_content_pages |   total_impressions |   total_clicks |   avg_seo_priority_score | cluster_health          | top_terms                                                                                                          | role_counts                                 | label_counts                    | gap_type                                |   gap_score | recommended_action                                                         |
|----------------------:|:-----------------|-------------:|----------------:|-----------------:|----------------:|--------------------------:|--------------------:|---------------:|-------------------------:|:------------------------|:-------------------------------------------------------------------------------------------------------------------|:--------------------------------------------|:--------------------------------|:----------------------------------------|------------:|:---------------------------------------------------------------------------|
|                     2 | powerfurl        |           19 |              19 |                0 |               0 |                         0 |                   0 |              0 |                      0   | PRODUCT_HEAVY_NO_PILLAR | 10t, 10t swl, powerfurl, furling, drum, fork, swl, powerfurl drum, powerfurl fork, fitting                         | {'product': 19}                             | {'powerfurl': 19}               | Missing technical authority content     |       155   | Create technical guide content supporting the powerfurl product family.    |
|                     8 | morfring         |           12 |              12 |                0 |               0 |                         0 |                   0 |              0 |                      0   | PRODUCT_HEAVY_NO_PILLAR | friction, ptfe, ring, friction ring, morfring, aluminium friction, aluminium, groove, groove max, morfrac morfring | {'product': 12}                             | {'morfring': 12}                | Missing technical authority content     |       151   | Create technical guide content supporting the morfring product family.     |
|                     4 | morfblock        |           58 |              58 |                0 |               0 |                         0 |                   0 |              0 |                      0   | FRAGMENTED_TOPIC        | sailing block, block, sailing, morfblock, swl, morfblock light, light, high, xl, lightweight sailing               | {'product': 58}                             | {'morfblock': 58}               | Missing technical authority content     |       145   | Create technical guide content supporting the morfblock product family.    |
|                     6 | powerfurl        |           24 |              24 |                0 |               0 |                         0 |                   0 |              0 |                      0   | FRAGMENTED_TOPIC        | powerfurl, 5t swl, 5t, furling, kit, swl, morfrac powerfurl, furling kit, reliable, unit                           | {'product': 24}                             | {'powerfurl': 21, 'shackle': 3} | Missing technical authority content     |       145   | Create technical guide content supporting the powerfurl product family.    |
|                     3 | dogbone          |           30 |              30 |                0 |               0 |                         0 |                   0 |              0 |                      0   | FRAGMENTED_TOPIC        | dogbone, morfrac dogbone, length, aluminium, morfrac, length morfrac, total length, total, titanium, faced         | {'product': 30}                             | {'dogbone': 30}                 | Missing technical authority content     |       145   | Create technical guide content supporting the dogbone product family.      |
|                    11 | mreel            |            5 |               4 |                0 |               0 |                         0 |                 126 |             27 |                     11.6 | OK                      | mreel, rope reeler, reeler, mreel rope, rope, reeler morfrac, morfrac mreel, halyards, sheets halyards, safer      | {'product': 4, 'general': 1}                | {'mreel': 4, 'powerfurl': 1}    | Search demand without authority support |        56.2 | Build authority content around mreel queries and link to commercial pages. |
|                     9 | shackle          |           11 |               8 |                2 |               1 |                         0 |                   0 |              0 |                      0   | OK                      | shackle, ti shackle, ti, titanium shackle, shackle morfrac, titanium, cnc, machined, cnc machined, ultra           | {'product': 8, 'category': 2, 'landing': 1} | {'shackle': 11}                 | No major gap                            |        24   | Monitor; no immediate content gap detected.                                |

---

# Missing Pillar / Landing Page Gaps

|   semantic_cluster_id | dominant_label   |   page_count |   product_pages |   category_pages |   landing_pages |   authority_content_pages |   total_impressions |   total_clicks |   avg_seo_priority_score | cluster_health          | top_terms                                                                                                          | role_counts     | label_counts                    | gap_type                            |   gap_score | recommended_action                                                      |
|----------------------:|:-----------------|-------------:|----------------:|-----------------:|----------------:|--------------------------:|--------------------:|---------------:|-------------------------:|:------------------------|:-------------------------------------------------------------------------------------------------------------------|:----------------|:--------------------------------|:------------------------------------|------------:|:------------------------------------------------------------------------|
|                     2 | powerfurl        |           19 |              19 |                0 |               0 |                         0 |                   0 |              0 |                        0 | PRODUCT_HEAVY_NO_PILLAR | 10t, 10t swl, powerfurl, furling, drum, fork, swl, powerfurl drum, powerfurl fork, fitting                         | {'product': 19} | {'powerfurl': 19}               | Missing technical authority content |         155 | Create technical guide content supporting the powerfurl product family. |
|                     8 | morfring         |           12 |              12 |                0 |               0 |                         0 |                   0 |              0 |                        0 | PRODUCT_HEAVY_NO_PILLAR | friction, ptfe, ring, friction ring, morfring, aluminium friction, aluminium, groove, groove max, morfrac morfring | {'product': 12} | {'morfring': 12}                | Missing technical authority content |         151 | Create technical guide content supporting the morfring product family.  |
|                     4 | morfblock        |           58 |              58 |                0 |               0 |                         0 |                   0 |              0 |                        0 | FRAGMENTED_TOPIC        | sailing block, block, sailing, morfblock, swl, morfblock light, light, high, xl, lightweight sailing               | {'product': 58} | {'morfblock': 58}               | Missing technical authority content |         145 | Create technical guide content supporting the morfblock product family. |
|                     6 | powerfurl        |           24 |              24 |                0 |               0 |                         0 |                   0 |              0 |                        0 | FRAGMENTED_TOPIC        | powerfurl, 5t swl, 5t, furling, kit, swl, morfrac powerfurl, furling kit, reliable, unit                           | {'product': 24} | {'powerfurl': 21, 'shackle': 3} | Missing technical authority content |         145 | Create technical guide content supporting the powerfurl product family. |
|                     3 | dogbone          |           30 |              30 |                0 |               0 |                         0 |                   0 |              0 |                        0 | FRAGMENTED_TOPIC        | dogbone, morfrac dogbone, length, aluminium, morfrac, length morfrac, total length, total, titanium, faced         | {'product': 30} | {'dogbone': 30}                 | Missing technical authority content |         145 | Create technical guide content supporting the dogbone product family.   |

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

- Content gap analysis: `C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC\06_MARKETING\SEO_Agent\Content_Gap_Analysis\2026-06-08_content_gap_analysis.csv`
- Authority gap analysis: `C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC\06_MARKETING\SEO_Agent\Content_Gap_Analysis\2026-06-08_authority_gap_analysis.csv`
- Missing pillar pages: `C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC\06_MARKETING\SEO_Agent\Content_Gap_Analysis\2026-06-08_missing_pillar_pages.csv`
- Orphan commercial topics: `C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC\06_MARKETING\SEO_Agent\Content_Gap_Analysis\2026-06-08_orphan_commercial_topics.csv`
- Page support summary: `C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC\06_MARKETING\SEO_Agent\Content_Gap_Analysis\2026-06-08_page_support_summary.csv`

## Related Links

### Concepts
- [[PRODUCT_HEAVY_NO_PILLAR]]
- [[FRAGMENTED_TOPIC]]

### Projects
- [[Search Console]]
