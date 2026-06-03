---
type: generated_report
source_agent: SEO_Agent
created: 2026-05-17
related_findings: []
related_concepts:
  - FRAGMENTED_TOPIC
  - PRODUCT_HEAVY_NO_PILLAR
  - ORPHAN_TOPIC
  - CONTENT_WITHOUT_COMMERCIAL_TARGET
related_projects:
  - Search Console
related_reports: []
---

# MORFRAC SEO Semantic Cluster Analysis

## Generated

2026-05-17

---

# Purpose

This report groups MORFRAC pages by deterministic semantic similarity using TF-IDF and cosine similarity.

V2 filters out:

- paginated category pages
- blog tag/archive pages
- legal/system pages
- checkout/account/web pages
- outlet pages
- EN/ES route duplicates where equivalent

It identifies:

- semantic clusters
- likely cannibalization pairs
- SKU variant similarity
- orphan topics
- fragmented clusters
- product-heavy clusters without clear pillar support
- authority content without commercial targets

---

# Source Files

- Crawl file: `C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC\06_MARKETING\SEO_Agent\Crawls\2026-05-17_site_crawl.csv`
- Search Console merge file: `C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC\06_MARKETING\SEO_Agent\Merged_Analysis\2026-05-17_search_console_merge.csv`

---

# Summary

- Pages analyzed: 256
- Semantic clusters: 12
- Similar page pairs above threshold: 256
- Cannibalization/topic-overlap pairs: 246
- Orphan topic clusters: 0

Similarity threshold:

`0.68`

---

# Cluster Summary

|   semantic_cluster_id | dominant_label   |   page_count |   product_pages |   category_pages |   landing_pages |   authority_content_pages |   total_impressions |   total_clicks |   avg_seo_priority_score | cluster_health          | top_terms                                                                                                                                 | role_counts                                                                          | label_counts                                                                                                                                            |
|----------------------:|:-----------------|-------------:|----------------:|-----------------:|----------------:|--------------------------:|--------------------:|---------------:|-------------------------:|:------------------------|:------------------------------------------------------------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------|
|                     1 | other            |           52 |              20 |                2 |               3 |                        17 |                   0 |              0 |                     0    | FRAGMENTED_TOPIC        | padeye, morfrac, wood, deck, morfblock, wooden, wooden sailing, morfblock wood, sailing, morfwing                                         | {'product': 20, 'authority_content': 17, 'general': 10, 'landing': 3, 'category': 2} | {'other': 13, 'morfblock': 12, 'padeye': 7, 'morfwing': 5, 'powerfurl': 5, 'custom_engineering': 4, 'mreel': 4, 'dogbone': 1, 'hoistlock': 1}           |
|                     3 | powerfurl        |           42 |               0 |               42 |               0 |                         0 |                   0 |              0 |                     0    | FRAGMENTED_TOPIC        | shop, morfrac shop, shop morfrac, powerfurl, morfrac, shop powerfurl, powerfurl morfrac, shop shop, morfblock, shop morfblock             | {'category': 42}                                                                     | {'powerfurl': 16, 'morfblock': 10, 'other': 6, 'dogbone': 3, 'shackle': 2, 'custom_engineering': 1, 'mloop': 1, 'morfring': 1, 'mreel': 1, 'padeye': 1} |
|                     5 | dogbone          |           31 |              30 |                0 |               1 |                         0 |                 376 |              3 |                     2.2  | FRAGMENTED_TOPIC        | dogbone, morfrac dogbone, length, aluminium, morfrac, length morfrac, total, total length, titanium, faced                                | {'product': 30, 'landing': 1}                                                        | {'dogbone': 31}                                                                                                                                         |
|                     6 | morfblock        |           30 |              30 |                0 |               0 |                         0 |                   0 |              0 |                     0    | FRAGMENTED_TOPIC        | morfblock light, light, lightweight sailing, sailing block, block, sailing, morfblock, swl, lightweight, high                             | {'product': 30}                                                                      | {'morfblock': 30}                                                                                                                                       |
|                     4 | shackle          |           24 |              16 |                0 |               2 |                         4 |                 363 |             19 |                     6.46 | FRAGMENTED_TOPIC        | shackle, custom, ti shackle, ti, titanium, titanium shackle, high, ultra, snatch, performance                                             | {'product': 16, 'authority_content': 4, 'general': 2, 'landing': 2}                  | {'shackle': 9, 'morfblock': 4, 'mloop': 4, 'powerfurl': 3, 'custom_engineering': 1, 'padeye': 1, 'dogbone': 1, 'morfring': 1}                           |
|                    10 | morfring         |           16 |              15 |                0 |               1 |                         0 |                   0 |              0 |                     0    | OK                      | ring, friction, friction ring, morfring, aluminium friction, ptfe, aluminium, ring morfrac, morfrac morfring, groove max                  | {'product': 15, 'landing': 1}                                                        | {'morfring': 13, 'padeye': 3}                                                                                                                           |
|                     8 | powerfurl        |            5 |               5 |                0 |               0 |                         0 |                   0 |              0 |                     0    | OK                      | integrator, swl integrator, powerfurl, td, powerfurl td, td integrator, designed smooth, smooth reliable, integrators, tdis               | {'product': 5}                                                                       | {'powerfurl': 5}                                                                                                                                        |
|                    11 | powerfurl        |           19 |              19 |                0 |               0 |                         0 |                   0 |              0 |                     0    | PRODUCT_HEAVY_NO_PILLAR | kit, furling, powerfurl, 5t, 5t swl, furling kit, swl, swl morfrac, powerfurl furling, powerfurl kit                                      | {'product': 19}                                                                      | {'powerfurl': 16, 'shackle': 3}                                                                                                                         |
|                     0 | morfblock        |           14 |              14 |                0 |               0 |                         0 |                   0 |              0 |                     0    | PRODUCT_HEAVY_NO_PILLAR | xl, morfblock xl, xl sailing, sailing block, block, morfblock, sailing, swl, sheave, handling                                             | {'product': 14}                                                                      | {'morfblock': 14}                                                                                                                                       |
|                     9 | powerfurl        |           11 |              11 |                0 |               0 |                         0 |                   0 |              0 |                     0    | PRODUCT_HEAVY_NO_PILLAR | unit, drum, powerfurl, furling, powerfurl drum, unit powerfurl, furling unit, unit morfrac, powerfurl engineered, swl                     | {'product': 11}                                                                      | {'powerfurl': 11}                                                                                                                                       |
|                     2 | morfblock        |            6 |               6 |                0 |               0 |                         0 |                   0 |              0 |                     0    | PRODUCT_HEAVY_NO_PILLAR | morfblock max, max, sailing, efficiency, sailing block, block, delivering low, dimensions maximum, efficiency level, reliability strength | {'product': 6}                                                                       | {'morfblock': 6}                                                                                                                                        |
|                     7 | powerfurl        |            6 |               6 |                0 |               0 |                         0 |                   0 |              0 |                     0    | PRODUCT_HEAVY_NO_PILLAR | fork, powerfurl fork, fitting, 10t, 10t swl, fork fitting, powerfurl, fork fork, swl, swl morfrac                                         | {'product': 6}                                                                       | {'powerfurl': 6}                                                                                                                                        |

---

# Likely Cannibalization / Duplicate Intent

| url_a                                                                             | role_a            | label_a   |   cluster_a | url_b                                                                               | role_b            | label_b   |   cluster_b |   similarity_score | same_family   | risk_type                |
|:----------------------------------------------------------------------------------|:------------------|:----------|------------:|:------------------------------------------------------------------------------------|:------------------|:----------|------------:|-------------------:|:--------------|:-------------------------|
| https://www.morfrac.com/blog/news-1/morfrac-de-walle-sails-33                     | authority_content | powerfurl |           1 | https://www.morfrac.com/es/blog/blog-1/morfrac-de-walle-sails-33                    | authority_content | powerfurl |           1 |                  1 | False         | possible_cannibalization |
| https://www.morfrac.com/shop/category/morfblock-morfblock-wood-20                 | category          | morfblock |           3 | https://www.morfrac.com/shop/category/morfblock-morfblockwood-20                    | category          | morfblock |           3 |                  1 | False         | possible_cannibalization |
| https://www.morfrac.com/shop/category/morfblock-morfblock-ultra-38                | category          | morfblock |           3 | https://www.morfrac.com/shop/category/morfblock-morfblockmax-38                     | category          | morfblock |           3 |                  1 | False         | possible_cannibalization |
| https://www.morfrac.com/shop/category/morfblock-morfblock-light-18                | category          | morfblock |           3 | https://www.morfrac.com/shop/category/morfblock-morfblocklight-18                   | category          | morfblock |           3 |                  1 | False         | possible_cannibalization |
| https://www.morfrac.com/shop/category/morfblock-morfblock-xl-21                   | category          | morfblock |           3 | https://www.morfrac.com/shop/category/morfblock-morfblockxl-21                      | category          | morfblock |           3 |                  1 | False         | possible_cannibalization |
| https://www.morfrac.com/shop/category/powerfurl-continuous-line-powerfurleight-10 | category          | powerfurl |           3 | https://www.morfrac.com/shop/category/powerfurl-continuous-line-powerfurlsix-13     | category          | powerfurl |           3 |                  1 | False         | possible_cannibalization |
| https://www.morfrac.com/shop/category/powerfurl-continuous-line-powerfurleight-10 | category          | powerfurl |           3 | https://www.morfrac.com/shop/category/powerfurl-continuous-line-powerfurlone-12     | category          | powerfurl |           3 |                  1 | False         | possible_cannibalization |
| https://www.morfrac.com/shop/category/powerfurl-continuous-line-powerfurleight-10 | category          | powerfurl |           3 | https://www.morfrac.com/shop/category/powerfurl-continuous-line-powerfurlfour-11    | category          | powerfurl |           3 |                  1 | False         | possible_cannibalization |
| https://www.morfrac.com/shop/category/powerfurl-continuous-line-powerfurlfour-11  | category          | powerfurl |           3 | https://www.morfrac.com/shop/category/powerfurl-continuous-line-powerfurlone-12     | category          | powerfurl |           3 |                  1 | False         | possible_cannibalization |
| https://www.morfrac.com/shop/category/powerfurl-continuous-line-powerfurlfour-11  | category          | powerfurl |           3 | https://www.morfrac.com/shop/category/powerfurl-continuous-line-powerfurlsix-13     | category          | powerfurl |           3 |                  1 | False         | possible_cannibalization |
| https://www.morfrac.com/shop/category/powerfurl-continuous-line-powerfurleight-10 | category          | powerfurl |           3 | https://www.morfrac.com/shop/category/powerfurl-continuous-line-powerfurlthree-15   | category          | powerfurl |           3 |                  1 | False         | possible_cannibalization |
| https://www.morfrac.com/shop/category/powerfurl-continuous-line-powerfurleight-10 | category          | powerfurl |           3 | https://www.morfrac.com/shop/category/powerfurl-continuous-line-powerfurltwelve-16  | category          | powerfurl |           3 |                  1 | False         | possible_cannibalization |
| https://www.morfrac.com/shop/category/powerfurl-continuous-line-powerfurleight-10 | category          | powerfurl |           3 | https://www.morfrac.com/shop/category/powerfurl-continuous-line-powerfurlten-14     | category          | powerfurl |           3 |                  1 | False         | possible_cannibalization |
| https://www.morfrac.com/shop/category/powerfurl-continuous-line-powerfurlfour-11  | category          | powerfurl |           3 | https://www.morfrac.com/shop/category/powerfurl-continuous-line-powerfurltwelve-16  | category          | powerfurl |           3 |                  1 | False         | possible_cannibalization |
| https://www.morfrac.com/shop/category/powerfurl-continuous-line-powerfurlfour-11  | category          | powerfurl |           3 | https://www.morfrac.com/shop/category/powerfurl-continuous-line-powerfurlthree-15   | category          | powerfurl |           3 |                  1 | False         | possible_cannibalization |
| https://www.morfrac.com/shop/category/powerfurl-continuous-line-powerfurlfour-11  | category          | powerfurl |           3 | https://www.morfrac.com/shop/category/powerfurl-continuous-line-powerfurlten-14     | category          | powerfurl |           3 |                  1 | False         | possible_cannibalization |
| https://www.morfrac.com/shop/category/powerfurl-continuous-line-powerfurlsix-13   | category          | powerfurl |           3 | https://www.morfrac.com/shop/category/powerfurl-continuous-line-powerfurlthree-15   | category          | powerfurl |           3 |                  1 | False         | possible_cannibalization |
| https://www.morfrac.com/shop/category/powerfurl-continuous-line-powerfurlone-12   | category          | powerfurl |           3 | https://www.morfrac.com/shop/category/powerfurl-continuous-line-powerfurlsix-13     | category          | powerfurl |           3 |                  1 | False         | possible_cannibalization |
| https://www.morfrac.com/shop/category/powerfurl-continuous-line-powerfurlone-12   | category          | powerfurl |           3 | https://www.morfrac.com/shop/category/powerfurl-continuous-line-powerfurltwelve-16  | category          | powerfurl |           3 |                  1 | False         | possible_cannibalization |
| https://www.morfrac.com/shop/category/powerfurl-continuous-line-powerfurlone-12   | category          | powerfurl |           3 | https://www.morfrac.com/shop/category/powerfurl-continuous-line-powerfurlthree-15   | category          | powerfurl |           3 |                  1 | False         | possible_cannibalization |
| https://www.morfrac.com/shop/category/powerfurl-continuous-line-powerfurlone-12   | category          | powerfurl |           3 | https://www.morfrac.com/shop/category/powerfurl-continuous-line-powerfurlten-14     | category          | powerfurl |           3 |                  1 | False         | possible_cannibalization |
| https://www.morfrac.com/shop/category/powerfurl-continuous-line-powerfurlsix-13   | category          | powerfurl |           3 | https://www.morfrac.com/shop/category/powerfurl-continuous-line-powerfurltwelve-16  | category          | powerfurl |           3 |                  1 | False         | possible_cannibalization |
| https://www.morfrac.com/shop/category/powerfurl-continuous-line-powerfurlsix-13   | category          | powerfurl |           3 | https://www.morfrac.com/shop/category/powerfurl-continuous-line-powerfurlten-14     | category          | powerfurl |           3 |                  1 | False         | possible_cannibalization |
| https://www.morfrac.com/shop/category/powerfurl-continuous-line-powerfurlten-14   | category          | powerfurl |           3 | https://www.morfrac.com/shop/category/powerfurl-continuous-line-powerfurlthree-15   | category          | powerfurl |           3 |                  1 | False         | possible_cannibalization |
| https://www.morfrac.com/shop/dogbone-25/dogbone-50-15-titanium-12465              | product           | dogbone   |           5 | https://www.morfrac.com/es/shop/dogbone-dogbone-ti-29/dogbone-50-15-titanium-12465  | product           | dogbone   |           5 |                  1 | False         | possible_cannibalization |
| https://www.morfrac.com/shop/dogbone-25/dogbone-50-15-aluminium-12464             | product           | dogbone   |           5 | https://www.morfrac.com/es/shop/dogbone-dogbone-al-28/dogbone-50-15-aluminium-12464 | product           | dogbone   |           5 |                  1 | False         | possible_cannibalization |
| https://www.morfrac.com/shop/dogbone-25/dogbone-45-19-aluminium-12463             | product           | dogbone   |           5 | https://www.morfrac.com/es/shop/dogbone-dogbone-al-28/dogbone-45-19-aluminium-12463 | product           | dogbone   |           5 |                  1 | False         | possible_cannibalization |
| https://www.morfrac.com/shop/dogbone-25/dogbone-40-12-titanium-12462              | product           | dogbone   |           5 | https://www.morfrac.com/es/shop/dogbone-dogbone-ti-29/dogbone-40-12-titanium-12462  | product           | dogbone   |           5 |                  1 | False         | possible_cannibalization |
| https://www.morfrac.com/shop/dogbone-25/dogbone-40-12-aluminium-12461             | product           | dogbone   |           5 | https://www.morfrac.com/es/shop/dogbone-dogbone-al-28/dogbone-40-12-aluminium-12461 | product           | dogbone   |           5 |                  1 | False         | possible_cannibalization |
| https://www.morfrac.com/shop/dogbone-25/dogbone-25-7-aluminium-12460              | product           | dogbone   |           5 | https://www.morfrac.com/es/shop/dogbone-dogbone-al-28/dogbone-25-7-aluminium-12460  | product           | dogbone   |           5 |                  1 | False         | possible_cannibalization |

---

# Orphan Topic Clusters

No orphan topic clusters detected.

---

# Interpretation Notes

Cluster health meanings:

- `ORPHAN_TOPIC`: only one page in the cluster. It may lack supporting content.
- `FRAGMENTED_TOPIC`: too many pages in one cluster. This may indicate topic sprawl or cannibalization.
- `PRODUCT_HEAVY_NO_PILLAR`: many product pages but no clear category or landing page support.
- `CONTENT_WITHOUT_COMMERCIAL_TARGET`: content exists but does not clearly support product/category pages.
- `OK`: structurally acceptable cluster.

Risk type meanings:

- `sku_variant_similarity`: similar SKU pages; not automatically bad.
- `possible_cannibalization`: similar pages with same role and topic.
- `same_topic_overlap`: similar pages in same topic but different roles.
- `semantic_overlap`: related but not necessarily conflicting.

Recommended next actions:

1. Review `possible_cannibalization` before writing more content.
2. Treat `sku_variant_similarity` separately from true cannibalization.
3. Build or strengthen pillar pages for product-heavy clusters.
4. Link authority content toward commercial category/product pages.
5. Expand orphan topics only if they support commercial search demand.
6. Avoid creating new pages inside already fragmented topics unless consolidation is planned.

---

# Output Files

- Cluster summary: `C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC\06_MARKETING\SEO_Agent\Semantic_Clusters\2026-05-17_semantic_clusters.csv`
- Page cluster mapping: `C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC\06_MARKETING\SEO_Agent\Semantic_Clusters\2026-05-17_semantic_cluster_pages.csv`
- Similarity pairs: `C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC\06_MARKETING\SEO_Agent\Semantic_Clusters\2026-05-17_semantic_similarity_pairs.csv`
- Cannibalization: `C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC\06_MARKETING\SEO_Agent\Semantic_Clusters\2026-05-17_semantic_cannibalization.csv`
- Orphan topics: `C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC\06_MARKETING\SEO_Agent\Semantic_Clusters\2026-05-17_semantic_orphan_topics.csv`

## Related Links

### Concepts
- [[FRAGMENTED_TOPIC]]
- [[PRODUCT_HEAVY_NO_PILLAR]]
- [[ORPHAN_TOPIC]]
- [[CONTENT_WITHOUT_COMMERCIAL_TARGET]]

### Projects
- [[Search Console]]
