---
type: seo_semantic_cluster_report
source_agent: SEO_Agent
created: 2026-10-05
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

    2026-10-05

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

    - Crawl file: `C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC\06_MARKETING\SEO_Agent\Crawls\2026-10-05_site_crawl.csv`
    - Search Console merge file: `C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC\06_MARKETING\SEO_Agent\Merged_Analysis\2026-10-05_search_console_merge.csv`

    ---

    # Summary

    - Pages analyzed: 265
    - Semantic clusters: 12
    - Similar page pairs above threshold: 287
    - Cannibalization/topic-overlap pairs: 276
    - Orphan topic clusters: 0

    Similarity threshold:

    `0.68`

    ---

    # Cluster Summary

    |   semantic_cluster_id | dominant_label   |   page_count |   product_pages |   category_pages |   landing_pages |   authority_content_pages |   total_impressions |   total_clicks |   avg_seo_priority_score | cluster_health          | top_terms                                                                                                                          | role_counts                                                           | label_counts                                                                                                                                           |
|----------------------:|:-----------------|-------------:|----------------:|-----------------:|----------------:|--------------------------:|--------------------:|---------------:|-------------------------:|:------------------------|:-----------------------------------------------------------------------------------------------------------------------------------|:----------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------|
|                     6 | other            |           50 |              19 |                0 |               3 |                        15 |                 207 |              2 |                     1.62 | FRAGMENTED_TOPIC        | custom, morfrac, snatch, high performance, hardware, morfblock, mreel, reeler, rope reeler, performance                            | {'product': 19, 'authority_content': 15, 'general': 13, 'landing': 3} | {'other': 15, 'morfblock': 8, 'powerfurl': 6, 'custom_engineering': 6, 'mloop': 5, 'mreel': 4, 'dogbone': 3, 'morfring': 2, 'hoistlock': 1}            |
|                     7 | powerfurl        |           40 |               0 |               40 |               0 |                         0 |                   0 |              0 |                     0    | FRAGMENTED_TOPIC        | shop, morfrac shop, shop morfrac, powerfurl, morfrac, shop powerfurl, powerfurl morfrac, tdi, shop morfblock, morfblock            | {'category': 40}                                                      | {'powerfurl': 16, 'other': 9, 'morfblock': 5, 'dogbone': 3, 'shackle': 2, 'custom_engineering': 1, 'mloop': 1, 'morfring': 1, 'mreel': 1, 'padeye': 1} |
|                     0 | morfblock        |           30 |              30 |                0 |               0 |                         0 |                   0 |              0 |                     0    | FRAGMENTED_TOPIC        | morfblock light, light, lightweight sailing, sailing block, block, sailing, morfblock, swl, lightweight, high                      | {'product': 30}                                                       | {'morfblock': 30}                                                                                                                                      |
|                     8 | powerfurl        |           28 |              27 |                0 |               1 |                         0 |                   0 |              0 |                     0    | FRAGMENTED_TOPIC        | shackle, kit, 5t, 5t swl, furling, powerfurl, furling kit, swl, ti shackle, swl morfrac                                            | {'product': 27, 'landing': 1}                                         | {'powerfurl': 15, 'shackle': 13}                                                                                                                       |
|                     4 | powerfurl        |           23 |              23 |                0 |               0 |                         0 |                   0 |              0 |                     0    | FRAGMENTED_TOPIC        | powerfurl, furling, 10t, 10t swl, unit, fork, drum, swl, powerfurl drum, powerfurl fork                                            | {'product': 23}                                                       | {'powerfurl': 23}                                                                                                                                      |
|                     9 | dogbone          |           22 |              22 |                0 |               0 |                         0 |                   0 |              0 |                     0    | FRAGMENTED_TOPIC        | dogbone, morfrac dogbone, length, 60mm, morfrac, length morfrac, total, total length, titanium, attachment                         | {'product': 22}                                                       | {'dogbone': 22}                                                                                                                                        |
|                    10 | morfring         |           21 |              20 |                0 |               1 |                         0 |                   0 |              0 |                     0    | FRAGMENTED_TOPIC        | padeye, ring, friction, friction ring, ptfe, aluminium friction, morfring, aluminium, stick, deck                                  | {'product': 20, 'landing': 1}                                         | {'morfring': 12, 'padeye': 9}                                                                                                                          |
|                     5 | dogbone          |            9 |               8 |                0 |               1 |                         0 |                 282 |              2 |                    11.51 | OK                      | dogbone, morfrac dogbone, length, aluminium, rope, dogbone engineered, lightweight aluminium, morfrac, connections, faced          | {'product': 8, 'landing': 1}                                          | {'dogbone': 9}                                                                                                                                         |
|                     2 | morfblock        |            8 |               6 |                2 |               0 |                         0 |                   0 |              0 |                     0    | OK                      | morfblock max, max, morfblock, sailing, efficiency, sailing block, maximum reliability, block, efficiency sailing, max lightweight | {'product': 6, 'category': 2}                                         | {'morfblock': 8}                                                                                                                                       |
|                     3 | morfblock        |           14 |              14 |                0 |               0 |                         0 |                   0 |              0 |                     0    | PRODUCT_HEAVY_NO_PILLAR | xl, morfblock xl, xl sailing, sailing block, block, morfblock, sailing, swl, sheave, handling                                      | {'product': 14}                                                       | {'morfblock': 14}                                                                                                                                      |
|                    11 | morfblock        |           12 |               8 |                0 |               0 |                         4 |                   0 |              0 |                     0    | PRODUCT_HEAVY_NO_PILLAR | wood, wooden, wooden sailing, morfblock wood, high load, sailing block, block, morfblock, morfwing, swl wooden                     | {'product': 8, 'authority_content': 4}                                | {'morfblock': 8, 'morfwing': 4}                                                                                                                        |
|                     1 | powerfurl        |            8 |               6 |                0 |               0 |                         2 |                   0 |              0 |                     0    | PRODUCT_HEAVY_NO_PILLAR | integrator, powerfurl, swl integrator, integrators, tdis, td integrator, td, powerfurl td, designed smooth, sails                  | {'product': 6, 'authority_content': 2}                                | {'powerfurl': 8}                                                                                                                                       |

    ---

    # Likely Cannibalization / Duplicate Intent

    | url_a                                                                                       | role_a   | label_a   |   cluster_a | url_b                                                                                        | role_b   | label_b   |   cluster_b |   similarity_score | same_family   | risk_type                |
|:--------------------------------------------------------------------------------------------|:---------|:----------|------------:|:---------------------------------------------------------------------------------------------|:---------|:----------|------------:|-------------------:|:--------------|:-------------------------|
| https://www.morfrac.com/es/shop/category/powerfurl-almacenadores-sin-fin-powerfurl-six-13   | category | powerfurl |           7 | https://www.morfrac.com/es/shop/category/powerfurl-almacenadores-sin-fin-powerfurl-twelve-16 | category | powerfurl |           7 |                  1 | False         | possible_cannibalization |
| https://www.morfrac.com/es/shop/category/powerfurl-almacenadores-sin-fin-powerfurl-six-13   | category | powerfurl |           7 | https://www.morfrac.com/es/shop/category/powerfurl-almacenadores-sin-fin-powerfurl-three-15  | category | powerfurl |           7 |                  1 | False         | possible_cannibalization |
| https://www.morfrac.com/es/shop/category/powerfurl-almacenadores-sin-fin-powerfurl-six-13   | category | powerfurl |           7 | https://www.morfrac.com/es/shop/category/powerfurl-almacenadores-sin-fin-powerfurl-ten-14    | category | powerfurl |           7 |                  1 | False         | possible_cannibalization |
| https://www.morfrac.com/es/shop/category/powerfurl-almacenadores-sin-fin-powerfurl-one-12   | category | powerfurl |           7 | https://www.morfrac.com/es/shop/category/powerfurl-almacenadores-sin-fin-powerfurl-twelve-16 | category | powerfurl |           7 |                  1 | False         | possible_cannibalization |
| https://www.morfrac.com/es/shop/category/powerfurl-almacenadores-sin-fin-powerfurl-one-12   | category | powerfurl |           7 | https://www.morfrac.com/es/shop/category/powerfurl-almacenadores-sin-fin-powerfurl-three-15  | category | powerfurl |           7 |                  1 | False         | possible_cannibalization |
| https://www.morfrac.com/es/shop/category/powerfurl-almacenadores-sin-fin-powerfurl-one-12   | category | powerfurl |           7 | https://www.morfrac.com/es/shop/category/powerfurl-almacenadores-sin-fin-powerfurl-ten-14    | category | powerfurl |           7 |                  1 | False         | possible_cannibalization |
| https://www.morfrac.com/es/shop/category/powerfurl-almacenadores-sin-fin-powerfurl-one-12   | category | powerfurl |           7 | https://www.morfrac.com/es/shop/category/powerfurl-almacenadores-sin-fin-powerfurl-six-13    | category | powerfurl |           7 |                  1 | False         | possible_cannibalization |
| https://www.morfrac.com/es/shop/category/powerfurl-almacenadores-sin-fin-powerfurl-four-11  | category | powerfurl |           7 | https://www.morfrac.com/es/shop/category/powerfurl-almacenadores-sin-fin-powerfurl-twelve-16 | category | powerfurl |           7 |                  1 | False         | possible_cannibalization |
| https://www.morfrac.com/es/shop/category/powerfurl-almacenadores-sin-fin-powerfurl-four-11  | category | powerfurl |           7 | https://www.morfrac.com/es/shop/category/powerfurl-almacenadores-sin-fin-powerfurl-three-15  | category | powerfurl |           7 |                  1 | False         | possible_cannibalization |
| https://www.morfrac.com/es/shop/category/powerfurl-almacenadores-sin-fin-powerfurl-four-11  | category | powerfurl |           7 | https://www.morfrac.com/es/shop/category/powerfurl-almacenadores-sin-fin-powerfurl-ten-14    | category | powerfurl |           7 |                  1 | False         | possible_cannibalization |
| https://www.morfrac.com/es/shop/category/powerfurl-almacenadores-sin-fin-powerfurl-four-11  | category | powerfurl |           7 | https://www.morfrac.com/es/shop/category/powerfurl-almacenadores-sin-fin-powerfurl-six-13    | category | powerfurl |           7 |                  1 | False         | possible_cannibalization |
| https://www.morfrac.com/es/shop/category/powerfurl-almacenadores-sin-fin-powerfurl-four-11  | category | powerfurl |           7 | https://www.morfrac.com/es/shop/category/powerfurl-almacenadores-sin-fin-powerfurl-one-12    | category | powerfurl |           7 |                  1 | False         | possible_cannibalization |
| https://www.morfrac.com/es/shop/category/powerfurl-almacenadores-sin-fin-powerfurl-eight-10 | category | powerfurl |           7 | https://www.morfrac.com/es/shop/category/powerfurl-almacenadores-sin-fin-powerfurl-twelve-16 | category | powerfurl |           7 |                  1 | False         | possible_cannibalization |
| https://www.morfrac.com/es/shop/category/powerfurl-almacenadores-sin-fin-powerfurl-eight-10 | category | powerfurl |           7 | https://www.morfrac.com/es/shop/category/powerfurl-almacenadores-sin-fin-powerfurl-three-15  | category | powerfurl |           7 |                  1 | False         | possible_cannibalization |
| https://www.morfrac.com/es/shop/category/powerfurl-almacenadores-sin-fin-powerfurl-eight-10 | category | powerfurl |           7 | https://www.morfrac.com/es/shop/category/powerfurl-almacenadores-sin-fin-powerfurl-ten-14    | category | powerfurl |           7 |                  1 | False         | possible_cannibalization |
| https://www.morfrac.com/es/shop/category/powerfurl-almacenadores-sin-fin-powerfurl-eight-10 | category | powerfurl |           7 | https://www.morfrac.com/es/shop/category/powerfurl-almacenadores-sin-fin-powerfurl-six-13    | category | powerfurl |           7 |                  1 | False         | possible_cannibalization |
| https://www.morfrac.com/shop/category/powerfurl-continuous-line-powerfurl-eight-10          | category | powerfurl |           7 | https://www.morfrac.com/es/shop/category/powerfurl-almacenadores-sin-fin-powerfurl-six-13    | category | powerfurl |           7 |                  1 | False         | possible_cannibalization |
| https://www.morfrac.com/shop/category/powerfurl-continuous-line-powerfurl-eight-10          | category | powerfurl |           7 | https://www.morfrac.com/es/shop/category/powerfurl-almacenadores-sin-fin-powerfurl-one-12    | category | powerfurl |           7 |                  1 | False         | possible_cannibalization |
| https://www.morfrac.com/shop/category/powerfurl-continuous-line-powerfurl-eight-10          | category | powerfurl |           7 | https://www.morfrac.com/es/shop/category/powerfurl-almacenadores-sin-fin-powerfurl-four-11   | category | powerfurl |           7 |                  1 | False         | possible_cannibalization |
| https://www.morfrac.com/shop/category/powerfurl-continuous-line-powerfurl-eight-10          | category | powerfurl |           7 | https://www.morfrac.com/es/shop/category/powerfurl-almacenadores-sin-fin-powerfurl-eight-10  | category | powerfurl |           7 |                  1 | False         | possible_cannibalization |
| https://www.morfrac.com/shop/category/powerfurl-continuous-line-powerfurl-eight-10          | category | powerfurl |           7 | https://www.morfrac.com/shop/category/powerfurl-continuous-line-powerfurl-twelve-16          | category | powerfurl |           7 |                  1 | False         | possible_cannibalization |
| https://www.morfrac.com/shop/category/powerfurl-continuous-line-powerfurl-eight-10          | category | powerfurl |           7 | https://www.morfrac.com/shop/category/powerfurl-continuous-line-powerfurl-three-15           | category | powerfurl |           7 |                  1 | False         | possible_cannibalization |
| https://www.morfrac.com/shop/category/powerfurl-continuous-line-powerfurl-eight-10          | category | powerfurl |           7 | https://www.morfrac.com/shop/category/powerfurl-continuous-line-powerfurl-ten-14             | category | powerfurl |           7 |                  1 | False         | possible_cannibalization |
| https://www.morfrac.com/shop/category/powerfurl-continuous-line-powerfurl-eight-10          | category | powerfurl |           7 | https://www.morfrac.com/shop/category/powerfurl-continuous-line-powerfurl-six-13             | category | powerfurl |           7 |                  1 | False         | possible_cannibalization |
| https://www.morfrac.com/shop/category/powerfurl-continuous-line-powerfurl-eight-10          | category | powerfurl |           7 | https://www.morfrac.com/shop/category/powerfurl-continuous-line-powerfurl-one-12             | category | powerfurl |           7 |                  1 | False         | possible_cannibalization |
| https://www.morfrac.com/shop/category/powerfurl-continuous-line-powerfurl-eight-10          | category | powerfurl |           7 | https://www.morfrac.com/shop/category/powerfurl-continuous-line-powerfurl-four-11            | category | powerfurl |           7 |                  1 | False         | possible_cannibalization |
| https://www.morfrac.com/shop/category/powerfurl-continuous-line-powerfurl-one-12            | category | powerfurl |           7 | https://www.morfrac.com/shop/category/powerfurl-continuous-line-powerfurl-six-13             | category | powerfurl |           7 |                  1 | False         | possible_cannibalization |
| https://www.morfrac.com/shop/category/powerfurl-continuous-line-powerfurl-four-11           | category | powerfurl |           7 | https://www.morfrac.com/es/shop/category/powerfurl-almacenadores-sin-fin-powerfurl-twelve-16 | category | powerfurl |           7 |                  1 | False         | possible_cannibalization |
| https://www.morfrac.com/shop/category/powerfurl-continuous-line-powerfurl-four-11           | category | powerfurl |           7 | https://www.morfrac.com/es/shop/category/powerfurl-almacenadores-sin-fin-powerfurl-three-15  | category | powerfurl |           7 |                  1 | False         | possible_cannibalization |
| https://www.morfrac.com/shop/category/powerfurl-continuous-line-powerfurl-four-11           | category | powerfurl |           7 | https://www.morfrac.com/es/shop/category/powerfurl-almacenadores-sin-fin-powerfurl-ten-14    | category | powerfurl |           7 |                  1 | False         | possible_cannibalization |

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

    - Cluster summary: `C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC\06_MARKETING\SEO_Agent\Semantic_Clusters\2026-10-05_semantic_clusters.csv`
    - Page cluster mapping: `C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC\06_MARKETING\SEO_Agent\Semantic_Clusters\2026-10-05_semantic_cluster_pages.csv`
    - Similarity pairs: `C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC\06_MARKETING\SEO_Agent\Semantic_Clusters\2026-10-05_semantic_similarity_pairs.csv`
    - Cannibalization: `C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC\06_MARKETING\SEO_Agent\Semantic_Clusters\2026-10-05_semantic_cannibalization.csv`
    - Orphan topics: `C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC\06_MARKETING\SEO_Agent\Semantic_Clusters\2026-10-05_semantic_orphan_topics.csv`

## Related Links

### Concepts
- [[FRAGMENTED_TOPIC]]
- [[PRODUCT_HEAVY_NO_PILLAR]]
- [[ORPHAN_TOPIC]]
- [[CONTENT_WITHOUT_COMMERCIAL_TARGET]]

### Projects
- [[Search Console]]
