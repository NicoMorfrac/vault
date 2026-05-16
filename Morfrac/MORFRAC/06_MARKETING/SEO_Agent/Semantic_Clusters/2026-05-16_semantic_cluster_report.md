# MORFRAC SEO Semantic Cluster Analysis

## Generated

2026-05-16

---

# Purpose

This report groups MORFRAC pages by deterministic semantic similarity using TF-IDF and cosine similarity.

It identifies:

- semantic clusters
- likely cannibalization pairs
- orphan topics
- fragmented clusters
- product-heavy clusters without clear pillar support
- authority content without commercial targets

---

# Source Files

- Crawl file: `C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC\06_MARKETING\SEO_Agent\Crawls\2026-05-16_site_crawl.csv`
- Search Console merge file: `C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC\06_MARKETING\SEO_Agent\Merged_Analysis\2026-05-16_search_console_merge.csv`

---

# Summary

- Pages analyzed: 487
- Semantic clusters: 12
- Similar page pairs above threshold: 1330
- Likely cannibalization pairs: 1327
- Orphan topic clusters: 0

Similarity threshold:

`0.65`

---

# Cluster Summary

|   semantic_cluster_id | dominant_label     |   page_count |   product_pages |   category_pages |   landing_pages |   authority_content_pages |   total_impressions |   total_clicks |   avg_seo_priority_score | cluster_health   | top_terms                                                                                                                                               | role_counts                                                           | label_counts                                                                                                                                                              |
|----------------------:|:-------------------|-------------:|----------------:|-----------------:|----------------:|--------------------------:|--------------------:|---------------:|-------------------------:|:-----------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------|:----------------------------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                     3 | powerfurl          |           93 |               9 |               82 |               0 |                         0 |                   0 |              0 |                     0    | FRAGMENTED_TOPIC | shop, morfrac shop, shop shop, morfrac, shop morfrac, shop powerfurl, powerfurl, morfblock, shop morfblock, powerfurl morfrac                           | {'category': 82, 'product': 9, 'general': 2}                          | {'powerfurl': 25, 'morfblock': 24, 'other': 19, 'dogbone': 16, 'mloop': 2, 'morfring': 2, 'custom_engineering': 2, 'mreel': 2, 'padeye': 1}                               |
|                     1 | morfblock          |           79 |              79 |                0 |               0 |                         0 |                   0 |              0 |                     0    | FRAGMENTED_TOPIC | sailing block, block, morfblock, sailing, swl, morfblock light, light, lightweight sailing, high, high load                                             | {'product': 79}                                                       | {'morfblock': 79}                                                                                                                                                         |
|                     2 | powerfurl          |           76 |              76 |                0 |               0 |                         0 |                   0 |              0 |                     0    | FRAGMENTED_TOPIC | powerfurl, furling, swl, kit, 5t swl, 5t, 10t swl, 10t, morfrac powerfurl, reliable                                                                     | {'product': 76}                                                       | {'powerfurl': 71, 'shackle': 5}                                                                                                                                           |
|                    10 | other              |           63 |              17 |                0 |               6 |                        23 |                 172 |             21 |                     0.97 | FRAGMENTED_TOPIC | custom, morfrac, morfblock, morfwing, solutions, products, snatch, en, 2024, sail                                                                       | {'authority_content': 23, 'general': 17, 'product': 17, 'landing': 6} | {'other': 18, 'powerfurl': 10, 'morfblock': 10, 'custom_engineering': 7, 'morfwing': 6, 'mreel': 4, 'mloop': 3, 'dogbone': 2, 'padeye': 1, 'morfring': 1, 'hoistlock': 1} |
|                     6 | dogbone            |           39 |              37 |                0 |               2 |                         0 |                 467 |              3 |                     3.91 | FRAGMENTED_TOPIC | dogbone, length, morfrac dogbone, aluminium, total, length morfrac, total length, 60mm, morfrac, aluminium dogbone                                      | {'product': 37, 'landing': 2}                                         | {'dogbone': 39}                                                                                                                                                           |
|                     4 | custom_engineering |           28 |               0 |                0 |               0 |                        26 |                   0 |              0 |                     0    | FRAGMENTED_TOPIC | yacht engineering, projects, engineering, stories, yacht, sailing, stories product, blog sailing, product launches, product                             | {'authority_content': 26, 'general': 2}                               | {'custom_engineering': 28}                                                                                                                                                |
|                     9 | morfring           |           28 |              26 |                0 |               2 |                         0 |                   0 |              0 |                     0    | FRAGMENTED_TOPIC | friction, morfring, ptfe, ring, friction ring, aluminium friction, aluminium, morfrac morfring, groove, groove max                                      | {'product': 26, 'landing': 2}                                         | {'morfring': 28}                                                                                                                                                          |
|                     8 | padeye             |           24 |              20 |                1 |               2 |                         1 |                 307 |              0 |                     7.53 | FRAGMENTED_TOPIC | padeye, deck, stick, morfrac padeye, stick padeye, 20, deck padeye, ring, padeye morfrac, padeye ring                                                   | {'product': 20, 'landing': 2, 'category': 1, 'authority_content': 1}  | {'padeye': 20, 'mloop': 4}                                                                                                                                                |
|                     0 | shackle            |           23 |              17 |                4 |               2 |                         0 |                   0 |              0 |                     0    | FRAGMENTED_TOPIC | shackle, ti shackle, ti, titanium shackle, shackle morfrac, titanium, cnc machined, cnc, machined, ultra                                                | {'product': 17, 'category': 4, 'landing': 2}                          | {'shackle': 23}                                                                                                                                                           |
|                     7 | dogbone            |           15 |              15 |                0 |               0 |                         0 |                   0 |              0 |                     0    | FRAGMENTED_TOPIC | faced, flat, flat faced, dogbone, dogbone flat, faced titanium, morfrac dogbone, titanium, titanium morfrac, titanium dogbone                           | {'product': 15}                                                       | {'dogbone': 15}                                                                                                                                                           |
|                     5 | custom_engineering |           13 |               0 |                0 |               0 |                         0 |                   0 |              0 |                     0    | FRAGMENTED_TOPIC | yachting industry, yachting, smart reliable, smart, morfrac comes, morfrac innovating, reliable customizable, learn morfrac, learn, innovating yachting | {'general': 13}                                                       | {'custom_engineering': 13}                                                                                                                                                |
|                    11 | other              |            6 |               0 |                0 |               0 |                         0 |                   0 |              0 |                     0    | OK               | error, page, morfrac error, page morfrac, error 404, 404, ya, morfrac                                                                                   | {'general': 6}                                                        | {'other': 6}                                                                                                                                                              |

---

# Likely Cannibalization / Duplicate Intent

| url_a                                                                                          | role_a            | label_a            |   cluster_a | url_b                                                                                          | role_b            | label_b            |   cluster_b |   similarity_score | risk_type              |
|:-----------------------------------------------------------------------------------------------|:------------------|:-------------------|------------:|:-----------------------------------------------------------------------------------------------|:------------------|:-------------------|------------:|-------------------:|:-----------------------|
| https://www.morfrac.com/shop/mloop-dyneema-loop-12675                                          | product           | mloop              |           8 | https://www.morfrac.com/es/shop/mloop-dyneema-loop-12675                                       | product           | mloop              |           8 |                  1 | likely_cannibalization |
| https://www.morfrac.com/shop/mloop-dyneema-loop-12675                                          | product           | mloop              |           8 | https://www.morfrac.com/es/shop/mloop-34/mloop-dyneema-loop-12675                              | product           | mloop              |           8 |                  1 | likely_cannibalization |
| https://www.morfrac.com/es/shop/morfblock-morfblockmax-38/morfblock-max-3t-sailing-block-12859 | product           | morfblock          |           1 | https://www.morfrac.com/es/shop/morfblock-morfblockmax-38/morfblock-max-9t-sailing-block-12885 | product           | morfblock          |           1 |                  1 | likely_cannibalization |
| https://www.morfrac.com/es/shop/morfblock-morfblockmax-38/morfblock-max-3t-sailing-block-12859 | product           | morfblock          |           1 | https://www.morfrac.com/es/shop/morfblock-morfblockmax-38/morfblock-max-7t-sailing-block-12884 | product           | morfblock          |           1 |                  1 | likely_cannibalization |
| https://www.morfrac.com/es/shop/category/powerfurl-almacenadores-sin-fin-31/page/2             | category          | other              |           3 | https://www.morfrac.com/es/shop/category/powerfurl-almacenadores-sin-fin-31/page/3             | category          | other              |           3 |                  1 | likely_cannibalization |
| https://www.morfrac.com/es/shop/category/powerfurl-almacenadores-sin-fin-31/page/2             | category          | other              |           3 | https://www.morfrac.com/es/shop/category/powerfurl-almacenadores-sin-fin-31/page/4             | category          | other              |           3 |                  1 | likely_cannibalization |
| https://www.morfrac.com/es/shop/category/powerfurl-almacenadores-sin-fin-31/page/2             | category          | other              |           3 | https://www.morfrac.com/es/shop/category/powerfurl-almacenadores-sin-fin-31/page/5             | category          | other              |           3 |                  1 | likely_cannibalization |
| https://www.morfrac.com/es/shop/category/powerfurl-almacenadores-sin-fin-31/page/3             | category          | other              |           3 | https://www.morfrac.com/es/shop/category/powerfurl-almacenadores-sin-fin-31/page/4             | category          | other              |           3 |                  1 | likely_cannibalization |
| https://www.morfrac.com/es/shop/category/powerfurl-almacenadores-sin-fin-31/page/3             | category          | other              |           3 | https://www.morfrac.com/es/shop/category/powerfurl-almacenadores-sin-fin-31/page/5             | category          | other              |           3 |                  1 | likely_cannibalization |
| https://www.morfrac.com/es/shop/category/powerfurl-almacenadores-sin-fin-31/page/4             | category          | other              |           3 | https://www.morfrac.com/es/shop/category/powerfurl-almacenadores-sin-fin-31/page/5             | category          | other              |           3 |                  1 | likely_cannibalization |
| https://www.morfrac.com/es/blog/tag/custom-9                                                   | authority_content | custom_engineering |           4 | https://www.morfrac.com/es/blog/tag/media-5                                                    | authority_content | custom_engineering |           4 |                  1 | likely_cannibalization |
| https://www.morfrac.com/es/blog/tag/custom-9                                                   | authority_content | custom_engineering |           4 | https://www.morfrac.com/es/blog/tag/morfblock-1                                                | authority_content | custom_engineering |           4 |                  1 | likely_cannibalization |
| https://www.morfrac.com/es/blog/tag/custom-9                                                   | authority_content | custom_engineering |           4 | https://www.morfrac.com/es/blog/tag/morfrac-network-10                                         | authority_content | custom_engineering |           4 |                  1 | likely_cannibalization |
| https://www.morfrac.com/es/blog/tag/custom-9                                                   | authority_content | custom_engineering |           4 | https://www.morfrac.com/es/blog/tag/morfwing-13                                                | authority_content | custom_engineering |           4 |                  1 | likely_cannibalization |
| https://www.morfrac.com/es/blog/tag/custom-9                                                   | authority_content | custom_engineering |           4 | https://www.morfrac.com/es/blog/tag/news-2                                                     | authority_content | custom_engineering |           4 |                  1 | likely_cannibalization |
| https://www.morfrac.com/es/blog/tag/custom-9                                                   | authority_content | custom_engineering |           4 | https://www.morfrac.com/es/blog/tag/on-board-6                                                 | authority_content | custom_engineering |           4 |                  1 | likely_cannibalization |
| https://www.morfrac.com/es/blog/tag/custom-9                                                   | authority_content | custom_engineering |           4 | https://www.morfrac.com/es/blog/tag/partners-11                                                | authority_content | custom_engineering |           4 |                  1 | likely_cannibalization |
| https://www.morfrac.com/about                                                                  | general           | custom_engineering |           5 | https://www.morfrac.com/returns                                                                | general           | custom_engineering |           5 |                  1 | likely_cannibalization |
| https://www.morfrac.com/about                                                                  | general           | custom_engineering |           5 | https://www.morfrac.com/shipping                                                               | general           | custom_engineering |           5 |                  1 | likely_cannibalization |
| https://www.morfrac.com/about                                                                  | general           | custom_engineering |           5 | https://www.morfrac.com/terms-conditions                                                       | general           | custom_engineering |           5 |                  1 | likely_cannibalization |
| https://www.morfrac.com/about                                                                  | general           | custom_engineering |           5 | https://www.morfrac.com/use                                                                    | general           | custom_engineering |           5 |                  1 | likely_cannibalization |
| https://www.morfrac.com/about                                                                  | general           | custom_engineering |           5 | https://www.morfrac.com/es/disclaimer                                                          | general           | custom_engineering |           5 |                  1 | likely_cannibalization |
| https://www.morfrac.com/about                                                                  | general           | custom_engineering |           5 | https://www.morfrac.com/es/privacy                                                             | general           | custom_engineering |           5 |                  1 | likely_cannibalization |
| https://www.morfrac.com/about                                                                  | general           | custom_engineering |           5 | https://www.morfrac.com/es/returns                                                             | general           | custom_engineering |           5 |                  1 | likely_cannibalization |
| https://www.morfrac.com/about                                                                  | general           | custom_engineering |           5 | https://www.morfrac.com/es/shipping                                                            | general           | custom_engineering |           5 |                  1 | likely_cannibalization |
| https://www.morfrac.com/about                                                                  | general           | custom_engineering |           5 | https://www.morfrac.com/es/terms-conditions                                                    | general           | custom_engineering |           5 |                  1 | likely_cannibalization |
| https://www.morfrac.com/about                                                                  | general           | custom_engineering |           5 | https://www.morfrac.com/es/use                                                                 | general           | custom_engineering |           5 |                  1 | likely_cannibalization |
| https://www.morfrac.com/es/shop/shackle-17-4ph-12827                                           | product           | shackle            |           0 | https://www.morfrac.com/shop/shackle-17-4ph-12827                                              | product           | shackle            |           0 |                  1 | likely_cannibalization |
| https://www.morfrac.com/es/shop/shackle-17-4ph-12827                                           | product           | shackle            |           0 | https://www.morfrac.com/es/shop/outlet-36/shackle-17-4ph-12827                                 | product           | shackle            |           0 |                  1 | likely_cannibalization |
| https://www.morfrac.com/es/shop/shackle-17-4ph-12827                                           | product           | shackle            |           0 | https://www.morfrac.com/shop/outlet-36/shackle-17-4ph-12827                                    | product           | shackle            |           0 |                  1 | likely_cannibalization |

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

Recommended next actions:

1. Review cannibalization pairs before writing more content.
2. Build or strengthen pillar pages for product-heavy clusters.
3. Link authority content toward commercial category/product pages.
4. Expand orphan topics only if they support commercial search demand.
5. Avoid creating new pages inside already fragmented topics unless consolidation is planned.

---

# Output Files

- Cluster summary: `C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC\06_MARKETING\SEO_Agent\Semantic_Clusters\2026-05-16_semantic_clusters.csv`
- Page cluster mapping: `C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC\06_MARKETING\SEO_Agent\Semantic_Clusters\2026-05-16_semantic_cluster_pages.csv`
- Similarity pairs: `C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC\06_MARKETING\SEO_Agent\Semantic_Clusters\2026-05-16_semantic_similarity_pairs.csv`
- Cannibalization: `C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC\06_MARKETING\SEO_Agent\Semantic_Clusters\2026-05-16_semantic_cannibalization.csv`
- Orphan topics: `C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC\06_MARKETING\SEO_Agent\Semantic_Clusters\2026-05-16_semantic_orphan_topics.csv`
