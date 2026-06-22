---
type: seo_content_gap_report
source_agent: SEO_Agent
created: 2026-06-22
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

2026-06-22

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

- Semantic clusters: `C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC\06_MARKETING\SEO_Agent\Semantic_Clusters\2026-06-22_semantic_clusters.csv`
- Semantic pages: `C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC\06_MARKETING\SEO_Agent\Semantic_Clusters\2026-06-22_semantic_cluster_pages.csv`
- Search Console merge: `C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC\06_MARKETING\SEO_Agent\Merged_Analysis\2026-06-22_search_console_merge.csv`
- Contextual links: `C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC\06_MARKETING\SEO_Agent\Contextual_Links\2026-06-22_contextual_link_recommendations_filtered.csv`

---

# Summary

- Semantic clusters reviewed: 12
- Content gaps detected: 9
- Authority gaps detected: 9
- Missing pillar-page gaps: 5
- Orphan commercial topics: 0

---

# Highest Priority Content Gaps

|   semantic_cluster_id | dominant_label   |   page_count |   product_pages |   category_pages |   landing_pages |   authority_content_pages |   total_impressions |   total_clicks |   avg_seo_priority_score | cluster_health          | top_terms                                                                                                             | role_counts                                          | label_counts                    | gap_type                            |   gap_score | recommended_action                                                      |
|----------------------:|:-----------------|-------------:|----------------:|-----------------:|----------------:|--------------------------:|--------------------:|---------------:|-------------------------:|:------------------------|:----------------------------------------------------------------------------------------------------------------------|:-----------------------------------------------------|:--------------------------------|:------------------------------------|------------:|:------------------------------------------------------------------------|
|                     3 | morfblock        |           14 |              14 |                0 |               0 |                         0 |                   0 |              0 |                     0    | PRODUCT_HEAVY_NO_PILLAR | xl, morfblock xl, xl sailing, sailing block, block, morfblock, sailing, swl, sheave, handling                         | {'product': 14}                                      | {'morfblock': 14}               | Missing technical authority content |      155    | Create technical guide content supporting the morfblock product family. |
|                     8 | powerfurl        |           13 |              13 |                0 |               0 |                         0 |                   0 |              0 |                     0    | PRODUCT_HEAVY_NO_PILLAR | unit, drum, powerfurl, furling, powerfurl drum, unit powerfurl, unit morfrac, furling unit, powerfurl engineered, swl | {'product': 13}                                      | {'powerfurl': 13}               | Missing technical authority content |      154    | Create technical guide content supporting the powerfurl product family. |
|                     9 | dogbone          |           31 |              30 |                0 |               1 |                         0 |                 537 |              2 |                     4.05 | FRAGMENTED_TOPIC        | dogbone, morfrac dogbone, length, aluminium, morfrac, length morfrac, total length, total, titanium, faced            | {'product': 30, 'landing': 1}                        | {'dogbone': 31}                 | Missing technical authority content |      151.05 | Create technical guide content supporting the dogbone product family.   |
|                     0 | morfblock        |           30 |              30 |                0 |               0 |                         0 |                   0 |              0 |                     0    | FRAGMENTED_TOPIC        | morfblock light, light, lightweight sailing, sailing block, block, sailing, morfblock, swl, lightweight, high         | {'product': 30}                                      | {'morfblock': 30}               | Missing technical authority content |      145    | Create technical guide content supporting the morfblock product family. |
|                     5 | powerfurl        |           24 |              24 |                0 |               0 |                         0 |                   0 |              0 |                     0    | FRAGMENTED_TOPIC        | kit, furling, powerfurl, 5t, 5t swl, furling kit, swl, swl morfrac, morfrac powerfurl, powerfurl kit                  | {'product': 24}                                      | {'powerfurl': 21, 'shackle': 3} | Missing technical authority content |      145    | Create technical guide content supporting the powerfurl product family. |
|                    10 | morfring         |           13 |              12 |                0 |               1 |                         0 |                   0 |              0 |                     0    | OK                      | morfring, friction, ptfe, friction ring, ring, aluminium friction, aluminium, morfrac morfring, groove, groove max    | {'product': 12, 'landing': 1}                        | {'morfring': 13}                | Missing technical authority content |       91    | Create technical guide content supporting the morfring product family.  |
|                     1 | powerfurl        |            9 |               9 |                0 |               0 |                         0 |                   0 |              0 |                     0    | PRODUCT_HEAVY_NO_PILLAR | fork, 10t swl, 10t, powerfurl fork, fitting, powerfurl, fork fitting, swl, integrators, tdis                          | {'product': 9}                                       | {'powerfurl': 9}                | Missing category support            |       77    | Create or improve category structure for powerfurl pages.               |
|                    11 | morfblock        |           13 |               8 |                0 |               1 |                         4 |                   0 |              0 |                     0    | OK                      | wood, wooden, wooden sailing, morfblock wood, morfwing, high load, sailing block, block, sailing, morfblock           | {'product': 8, 'authority_content': 4, 'landing': 1} | {'morfblock': 8, 'morfwing': 5} | Missing category support            |       44    | Create or improve category structure for morfblock pages.               |
|                     4 | padeye           |            9 |               8 |                0 |               1 |                         0 |                   0 |              0 |                     0    | OK                      | padeye, stick, deck, morfrac padeye, stick padeye, 20, ring, deck padeye, padeye ring, ring 20                        | {'product': 8, 'landing': 1}                         | {'padeye': 9}                   | Missing category support            |       44    | Create or improve category structure for padeye pages.                  |

---

# Authority Content Gaps

|   semantic_cluster_id | dominant_label   |   page_count |   product_pages |   category_pages |   landing_pages |   authority_content_pages |   total_impressions |   total_clicks |   avg_seo_priority_score | cluster_health          | top_terms                                                                                                             | role_counts                                 | label_counts                    | gap_type                            |   gap_score | recommended_action                                                      |
|----------------------:|:-----------------|-------------:|----------------:|-----------------:|----------------:|--------------------------:|--------------------:|---------------:|-------------------------:|:------------------------|:----------------------------------------------------------------------------------------------------------------------|:--------------------------------------------|:--------------------------------|:------------------------------------|------------:|:------------------------------------------------------------------------|
|                     3 | morfblock        |           14 |              14 |                0 |               0 |                         0 |                   0 |              0 |                     0    | PRODUCT_HEAVY_NO_PILLAR | xl, morfblock xl, xl sailing, sailing block, block, morfblock, sailing, swl, sheave, handling                         | {'product': 14}                             | {'morfblock': 14}               | Missing technical authority content |      155    | Create technical guide content supporting the morfblock product family. |
|                     8 | powerfurl        |           13 |              13 |                0 |               0 |                         0 |                   0 |              0 |                     0    | PRODUCT_HEAVY_NO_PILLAR | unit, drum, powerfurl, furling, powerfurl drum, unit powerfurl, unit morfrac, furling unit, powerfurl engineered, swl | {'product': 13}                             | {'powerfurl': 13}               | Missing technical authority content |      154    | Create technical guide content supporting the powerfurl product family. |
|                     9 | dogbone          |           31 |              30 |                0 |               1 |                         0 |                 537 |              2 |                     4.05 | FRAGMENTED_TOPIC        | dogbone, morfrac dogbone, length, aluminium, morfrac, length morfrac, total length, total, titanium, faced            | {'product': 30, 'landing': 1}               | {'dogbone': 31}                 | Missing technical authority content |      151.05 | Create technical guide content supporting the dogbone product family.   |
|                     0 | morfblock        |           30 |              30 |                0 |               0 |                         0 |                   0 |              0 |                     0    | FRAGMENTED_TOPIC        | morfblock light, light, lightweight sailing, sailing block, block, sailing, morfblock, swl, lightweight, high         | {'product': 30}                             | {'morfblock': 30}               | Missing technical authority content |      145    | Create technical guide content supporting the morfblock product family. |
|                     5 | powerfurl        |           24 |              24 |                0 |               0 |                         0 |                   0 |              0 |                     0    | FRAGMENTED_TOPIC        | kit, furling, powerfurl, 5t, 5t swl, furling kit, swl, swl morfrac, morfrac powerfurl, powerfurl kit                  | {'product': 24}                             | {'powerfurl': 21, 'shackle': 3} | Missing technical authority content |      145    | Create technical guide content supporting the powerfurl product family. |
|                    10 | morfring         |           13 |              12 |                0 |               1 |                         0 |                   0 |              0 |                     0    | OK                      | morfring, friction, ptfe, friction ring, ring, aluminium friction, aluminium, morfrac morfring, groove, groove max    | {'product': 12, 'landing': 1}               | {'morfring': 13}                | Missing technical authority content |       91    | Create technical guide content supporting the morfring product family.  |
|                     1 | powerfurl        |            9 |               9 |                0 |               0 |                         0 |                   0 |              0 |                     0    | PRODUCT_HEAVY_NO_PILLAR | fork, 10t swl, 10t, powerfurl fork, fitting, powerfurl, fork fitting, swl, integrators, tdis                          | {'product': 9}                              | {'powerfurl': 9}                | Missing category support            |       77    | Create or improve category structure for powerfurl pages.               |
|                     4 | padeye           |            9 |               8 |                0 |               1 |                         0 |                   0 |              0 |                     0    | OK                      | padeye, stick, deck, morfrac padeye, stick padeye, 20, ring, deck padeye, padeye ring, ring 20                        | {'product': 8, 'landing': 1}                | {'padeye': 9}                   | Missing category support            |       44    | Create or improve category structure for padeye pages.                  |
|                     6 | shackle          |           12 |               9 |                2 |               1 |                         0 |                   0 |              0 |                     0    | OK                      | shackle, ti shackle, ti, titanium shackle, titanium, shackle morfrac, ø6mm, machined, cnc machined, cnc               | {'product': 9, 'category': 2, 'landing': 1} | {'shackle': 12}                 | No major gap                        |       27    | Monitor; no immediate content gap detected.                             |

---

# Missing Pillar / Landing Page Gaps

|   semantic_cluster_id | dominant_label   |   page_count |   product_pages |   category_pages |   landing_pages |   authority_content_pages |   total_impressions |   total_clicks |   avg_seo_priority_score | cluster_health          | top_terms                                                                                                             | role_counts     | label_counts                    | gap_type                            |   gap_score | recommended_action                                                      |
|----------------------:|:-----------------|-------------:|----------------:|-----------------:|----------------:|--------------------------:|--------------------:|---------------:|-------------------------:|:------------------------|:----------------------------------------------------------------------------------------------------------------------|:----------------|:--------------------------------|:------------------------------------|------------:|:------------------------------------------------------------------------|
|                     3 | morfblock        |           14 |              14 |                0 |               0 |                         0 |                   0 |              0 |                        0 | PRODUCT_HEAVY_NO_PILLAR | xl, morfblock xl, xl sailing, sailing block, block, morfblock, sailing, swl, sheave, handling                         | {'product': 14} | {'morfblock': 14}               | Missing technical authority content |         155 | Create technical guide content supporting the morfblock product family. |
|                     8 | powerfurl        |           13 |              13 |                0 |               0 |                         0 |                   0 |              0 |                        0 | PRODUCT_HEAVY_NO_PILLAR | unit, drum, powerfurl, furling, powerfurl drum, unit powerfurl, unit morfrac, furling unit, powerfurl engineered, swl | {'product': 13} | {'powerfurl': 13}               | Missing technical authority content |         154 | Create technical guide content supporting the powerfurl product family. |
|                     0 | morfblock        |           30 |              30 |                0 |               0 |                         0 |                   0 |              0 |                        0 | FRAGMENTED_TOPIC        | morfblock light, light, lightweight sailing, sailing block, block, sailing, morfblock, swl, lightweight, high         | {'product': 30} | {'morfblock': 30}               | Missing technical authority content |         145 | Create technical guide content supporting the morfblock product family. |
|                     5 | powerfurl        |           24 |              24 |                0 |               0 |                         0 |                   0 |              0 |                        0 | FRAGMENTED_TOPIC        | kit, furling, powerfurl, 5t, 5t swl, furling kit, swl, swl morfrac, morfrac powerfurl, powerfurl kit                  | {'product': 24} | {'powerfurl': 21, 'shackle': 3} | Missing technical authority content |         145 | Create technical guide content supporting the powerfurl product family. |
|                     1 | powerfurl        |            9 |               9 |                0 |               0 |                         0 |                   0 |              0 |                        0 | PRODUCT_HEAVY_NO_PILLAR | fork, 10t swl, 10t, powerfurl fork, fitting, powerfurl, fork fitting, swl, integrators, tdis                          | {'product': 9}  | {'powerfurl': 9}                | Missing category support            |          77 | Create or improve category structure for powerfurl pages.               |

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

- Content gap analysis: `C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC\06_MARKETING\SEO_Agent\Content_Gap_Analysis\2026-06-22_content_gap_analysis.csv`
- Authority gap analysis: `C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC\06_MARKETING\SEO_Agent\Content_Gap_Analysis\2026-06-22_authority_gap_analysis.csv`
- Missing pillar pages: `C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC\06_MARKETING\SEO_Agent\Content_Gap_Analysis\2026-06-22_missing_pillar_pages.csv`
- Orphan commercial topics: `C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC\06_MARKETING\SEO_Agent\Content_Gap_Analysis\2026-06-22_orphan_commercial_topics.csv`
- Page support summary: `C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC\06_MARKETING\SEO_Agent\Content_Gap_Analysis\2026-06-22_page_support_summary.csv`

## Related Links

### Concepts
- [[PRODUCT_HEAVY_NO_PILLAR]]
- [[FRAGMENTED_TOPIC]]

### Projects
- [[Search Console]]
