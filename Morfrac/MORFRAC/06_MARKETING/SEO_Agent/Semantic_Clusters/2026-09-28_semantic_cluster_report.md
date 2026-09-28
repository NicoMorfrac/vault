---
type: seo_semantic_cluster_report
source_agent: SEO_Agent
created: 2026-09-28
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

    2026-09-28

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

    - Crawl file: `C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC\06_MARKETING\SEO_Agent\Crawls\2026-09-28_site_crawl.csv`
    - Search Console merge file: `C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC\06_MARKETING\SEO_Agent\Merged_Analysis\2026-09-28_search_console_merge.csv`

    ---

    # Summary

    - Pages analyzed: 263
    - Semantic clusters: 12
    - Similar page pairs above threshold: 279
    - Cannibalization/topic-overlap pairs: 269
    - Orphan topic clusters: 0

    Similarity threshold:

    `0.68`

    ---

    # Cluster Summary

    |   semantic_cluster_id | dominant_label   |   page_count |   product_pages |   category_pages |   landing_pages |   authority_content_pages |   total_impressions |   total_clicks |   avg_seo_priority_score | cluster_health          | top_terms                                                                                                                   | role_counts                                                           | label_counts                                                                                                                                               |
|----------------------:|:-----------------|-------------:|----------------:|-----------------:|----------------:|--------------------------:|--------------------:|---------------:|-------------------------:|:------------------------|:----------------------------------------------------------------------------------------------------------------------------|:----------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------|
|                     3 | other            |           56 |              19 |                0 |               3 |                        21 |                 568 |             19 |                     4.21 | FRAGMENTED_TOPIC        | custom, morfrac, morfblock, snatch, high performance, hardware, mreel, performance, rope reeler, reeler                     | {'authority_content': 21, 'product': 19, 'general': 13, 'landing': 3} | {'other': 15, 'powerfurl': 8, 'morfblock': 8, 'custom_engineering': 6, 'mloop': 5, 'morfwing': 4, 'dogbone': 4, 'mreel': 4, 'morfring': 1, 'hoistlock': 1} |
|                    11 | powerfurl        |           35 |               0 |               35 |               0 |                         0 |                   0 |              0 |                     0    | FRAGMENTED_TOPIC        | shop, morfrac shop, shop morfrac, powerfurl, shop powerfurl, morfrac, powerfurl morfrac, shop morfblock, morfblock, dogbone | {'category': 35}                                                      | {'powerfurl': 16, 'other': 6, 'morfblock': 5, 'dogbone': 3, 'custom_engineering': 1, 'mloop': 1, 'morfring': 1, 'mreel': 1, 'padeye': 1}                   |
|                     2 | powerfurl        |           33 |              33 |                0 |               0 |                         0 |                   0 |              0 |                     0    | FRAGMENTED_TOPIC        | furling, powerfurl, kit, 5t, 5t swl, swl, furling kit, drum, morfrac powerfurl, reliable                                    | {'product': 33}                                                       | {'powerfurl': 30, 'shackle': 3}                                                                                                                            |
|                     4 | dogbone          |           30 |              30 |                0 |               0 |                         0 |                   0 |              0 |                     0    | FRAGMENTED_TOPIC        | dogbone, morfrac dogbone, length, aluminium, morfrac, total length, total, length morfrac, flat faced, faced                | {'product': 30}                                                       | {'dogbone': 30}                                                                                                                                            |
|                     6 | morfblock        |           30 |              30 |                0 |               0 |                         0 |                   0 |              0 |                     0    | FRAGMENTED_TOPIC        | morfblock light, light, lightweight sailing, sailing block, block, sailing, morfblock, swl, lightweight, high               | {'product': 30}                                                       | {'morfblock': 30}                                                                                                                                          |
|                     1 | morfblock        |           22 |              20 |                2 |               0 |                         0 |                   0 |              0 |                     0    | FRAGMENTED_TOPIC        | xl, sailing block, morfblock, block, morfblock xl, sailing, xl sailing, morfblock max, max, swl                             | {'product': 20, 'category': 2}                                        | {'morfblock': 22}                                                                                                                                          |
|                     9 | morfring         |           13 |              12 |                0 |               1 |                         0 |                   0 |              0 |                     0    | OK                      | morfring, friction, ptfe, friction ring, ring, aluminium friction, aluminium, morfrac morfring, groove max, groove          | {'product': 12, 'landing': 1}                                         | {'morfring': 13}                                                                                                                                           |
|                     0 | shackle          |           12 |               9 |                2 |               1 |                         0 |                   0 |              0 |                     0    | OK                      | shackle, ti shackle, ti, titanium shackle, titanium, shackle morfrac, ø6mm, cnc machined, machined, cnc                     | {'product': 9, 'category': 2, 'landing': 1}                           | {'shackle': 12}                                                                                                                                            |
|                     7 | padeye           |            9 |               8 |                0 |               1 |                         0 |                   0 |              0 |                     0    | OK                      | padeye, stick, deck, morfrac padeye, stick padeye, 20, ring, deck padeye, ring 20, padeye ring                              | {'product': 8, 'landing': 1}                                          | {'padeye': 9}                                                                                                                                              |
|                     5 | other            |            3 |               0 |                3 |               0 |                         0 |                   0 |              0 |                     0    | OK                      | tdi, shop, morfrac shop, shop tdi, tdi morfrac, shop morfrac, morfrac                                                       | {'category': 3}                                                       | {'other': 3}                                                                                                                                               |
|                     8 | powerfurl        |           12 |              12 |                0 |               0 |                         0 |                   0 |              0 |                     0    | PRODUCT_HEAVY_NO_PILLAR | 10t, 10t swl, fork, powerfurl, powerfurl fork, fitting, swl, furling, fork fitting, reliable 10t                            | {'product': 12}                                                       | {'powerfurl': 12}                                                                                                                                          |
|                    10 | morfblock        |            8 |               8 |                0 |               0 |                         0 |                   0 |              0 |                     0    | PRODUCT_HEAVY_NO_PILLAR | wood, wooden, wooden sailing, morfblock wood, high load, sailing block, block, morfblock, swl wooden, sailing               | {'product': 8}                                                        | {'morfblock': 8}                                                                                                                                           |

    ---

    # Likely Cannibalization / Duplicate Intent

    | url_a                                                                                       | role_a   | label_a   |   cluster_a | url_b                                                                                        | role_b   | label_b   |   cluster_b |   similarity_score | same_family   | risk_type                |
|:--------------------------------------------------------------------------------------------|:---------|:----------|------------:|:---------------------------------------------------------------------------------------------|:---------|:----------|------------:|-------------------:|:--------------|:-------------------------|
| https://www.morfrac.com/es/shop/custom-33/morfblcok-custom-runners-12664                    | product  | morfblock |           3 | https://www.morfrac.com/es/shop/morfblock-morfblock-xl-21/morfblcok-custom-runners-12664     | product  | morfblock |           3 |                  1 | False         | possible_cannibalization |
| https://www.morfrac.com/es/shop/category/powerfurl-almacenadores-sin-fin-powerfurl-three-15 | category | powerfurl |          11 | https://www.morfrac.com/es/shop/category/powerfurl-almacenadores-sin-fin-powerfurl-twelve-16 | category | powerfurl |          11 |                  1 | False         | possible_cannibalization |
| https://www.morfrac.com/es/shop/category/powerfurl-almacenadores-sin-fin-powerfurl-ten-14   | category | powerfurl |          11 | https://www.morfrac.com/es/shop/category/powerfurl-almacenadores-sin-fin-powerfurl-twelve-16 | category | powerfurl |          11 |                  1 | False         | possible_cannibalization |
| https://www.morfrac.com/es/shop/category/powerfurl-almacenadores-sin-fin-powerfurl-ten-14   | category | powerfurl |          11 | https://www.morfrac.com/es/shop/category/powerfurl-almacenadores-sin-fin-powerfurl-three-15  | category | powerfurl |          11 |                  1 | False         | possible_cannibalization |
| https://www.morfrac.com/es/shop/category/powerfurl-almacenadores-sin-fin-powerfurl-six-13   | category | powerfurl |          11 | https://www.morfrac.com/es/shop/category/powerfurl-almacenadores-sin-fin-powerfurl-twelve-16 | category | powerfurl |          11 |                  1 | False         | possible_cannibalization |
| https://www.morfrac.com/es/shop/category/powerfurl-almacenadores-sin-fin-powerfurl-six-13   | category | powerfurl |          11 | https://www.morfrac.com/es/shop/category/powerfurl-almacenadores-sin-fin-powerfurl-three-15  | category | powerfurl |          11 |                  1 | False         | possible_cannibalization |
| https://www.morfrac.com/es/shop/category/powerfurl-almacenadores-sin-fin-powerfurl-six-13   | category | powerfurl |          11 | https://www.morfrac.com/es/shop/category/powerfurl-almacenadores-sin-fin-powerfurl-ten-14    | category | powerfurl |          11 |                  1 | False         | possible_cannibalization |
| https://www.morfrac.com/es/shop/category/powerfurl-almacenadores-sin-fin-powerfurl-one-12   | category | powerfurl |          11 | https://www.morfrac.com/es/shop/category/powerfurl-almacenadores-sin-fin-powerfurl-twelve-16 | category | powerfurl |          11 |                  1 | False         | possible_cannibalization |
| https://www.morfrac.com/es/shop/category/powerfurl-almacenadores-sin-fin-powerfurl-one-12   | category | powerfurl |          11 | https://www.morfrac.com/es/shop/category/powerfurl-almacenadores-sin-fin-powerfurl-three-15  | category | powerfurl |          11 |                  1 | False         | possible_cannibalization |
| https://www.morfrac.com/es/shop/category/powerfurl-almacenadores-sin-fin-powerfurl-one-12   | category | powerfurl |          11 | https://www.morfrac.com/es/shop/category/powerfurl-almacenadores-sin-fin-powerfurl-ten-14    | category | powerfurl |          11 |                  1 | False         | possible_cannibalization |
| https://www.morfrac.com/es/shop/category/powerfurl-almacenadores-sin-fin-powerfurl-one-12   | category | powerfurl |          11 | https://www.morfrac.com/es/shop/category/powerfurl-almacenadores-sin-fin-powerfurl-six-13    | category | powerfurl |          11 |                  1 | False         | possible_cannibalization |
| https://www.morfrac.com/es/shop/category/powerfurl-almacenadores-sin-fin-powerfurl-four-11  | category | powerfurl |          11 | https://www.morfrac.com/es/shop/category/powerfurl-almacenadores-sin-fin-powerfurl-twelve-16 | category | powerfurl |          11 |                  1 | False         | possible_cannibalization |
| https://www.morfrac.com/es/shop/category/powerfurl-almacenadores-sin-fin-powerfurl-four-11  | category | powerfurl |          11 | https://www.morfrac.com/es/shop/category/powerfurl-almacenadores-sin-fin-powerfurl-three-15  | category | powerfurl |          11 |                  1 | False         | possible_cannibalization |
| https://www.morfrac.com/es/shop/category/powerfurl-almacenadores-sin-fin-powerfurl-four-11  | category | powerfurl |          11 | https://www.morfrac.com/es/shop/category/powerfurl-almacenadores-sin-fin-powerfurl-ten-14    | category | powerfurl |          11 |                  1 | False         | possible_cannibalization |
| https://www.morfrac.com/shop/category/powerfurl-continuous-line-powerfurl-eight-10          | category | powerfurl |          11 | https://www.morfrac.com/es/shop/category/powerfurl-almacenadores-sin-fin-powerfurl-ten-14    | category | powerfurl |          11 |                  1 | False         | possible_cannibalization |
| https://www.morfrac.com/shop/category/powerfurl-continuous-line-powerfurl-eight-10          | category | powerfurl |          11 | https://www.morfrac.com/es/shop/category/powerfurl-almacenadores-sin-fin-powerfurl-six-13    | category | powerfurl |          11 |                  1 | False         | possible_cannibalization |
| https://www.morfrac.com/shop/category/powerfurl-continuous-line-powerfurl-eight-10          | category | powerfurl |          11 | https://www.morfrac.com/es/shop/category/powerfurl-almacenadores-sin-fin-powerfurl-one-12    | category | powerfurl |          11 |                  1 | False         | possible_cannibalization |
| https://www.morfrac.com/shop/category/powerfurl-continuous-line-powerfurl-eight-10          | category | powerfurl |          11 | https://www.morfrac.com/es/shop/category/powerfurl-almacenadores-sin-fin-powerfurl-four-11   | category | powerfurl |          11 |                  1 | False         | possible_cannibalization |
| https://www.morfrac.com/shop/category/powerfurl-continuous-line-powerfurl-eight-10          | category | powerfurl |          11 | https://www.morfrac.com/es/shop/category/powerfurl-almacenadores-sin-fin-powerfurl-eight-10  | category | powerfurl |          11 |                  1 | False         | possible_cannibalization |
| https://www.morfrac.com/shop/category/powerfurl-continuous-line-powerfurl-eight-10          | category | powerfurl |          11 | https://www.morfrac.com/shop/category/powerfurl-continuous-line-powerfurl-twelve-16          | category | powerfurl |          11 |                  1 | False         | possible_cannibalization |
| https://www.morfrac.com/shop/category/powerfurl-continuous-line-powerfurl-eight-10          | category | powerfurl |          11 | https://www.morfrac.com/shop/category/powerfurl-continuous-line-powerfurl-three-15           | category | powerfurl |          11 |                  1 | False         | possible_cannibalization |
| https://www.morfrac.com/shop/category/powerfurl-continuous-line-powerfurl-eight-10          | category | powerfurl |          11 | https://www.morfrac.com/shop/category/powerfurl-continuous-line-powerfurl-ten-14             | category | powerfurl |          11 |                  1 | False         | possible_cannibalization |
| https://www.morfrac.com/shop/category/powerfurl-continuous-line-powerfurl-eight-10          | category | powerfurl |          11 | https://www.morfrac.com/shop/category/powerfurl-continuous-line-powerfurl-six-13             | category | powerfurl |          11 |                  1 | False         | possible_cannibalization |
| https://www.morfrac.com/shop/category/powerfurl-continuous-line-powerfurl-eight-10          | category | powerfurl |          11 | https://www.morfrac.com/shop/category/powerfurl-continuous-line-powerfurl-one-12             | category | powerfurl |          11 |                  1 | False         | possible_cannibalization |
| https://www.morfrac.com/shop/category/powerfurl-continuous-line-powerfurl-eight-10          | category | powerfurl |          11 | https://www.morfrac.com/shop/category/powerfurl-continuous-line-powerfurl-four-11            | category | powerfurl |          11 |                  1 | False         | possible_cannibalization |
| https://www.morfrac.com/shop/category/powerfurl-continuous-line-powerfurl-one-12            | category | powerfurl |          11 | https://www.morfrac.com/shop/category/powerfurl-continuous-line-powerfurl-ten-14             | category | powerfurl |          11 |                  1 | False         | possible_cannibalization |
| https://www.morfrac.com/shop/category/powerfurl-continuous-line-powerfurl-one-12            | category | powerfurl |          11 | https://www.morfrac.com/shop/category/powerfurl-continuous-line-powerfurl-six-13             | category | powerfurl |          11 |                  1 | False         | possible_cannibalization |
| https://www.morfrac.com/shop/category/powerfurl-continuous-line-powerfurl-four-11           | category | powerfurl |          11 | https://www.morfrac.com/es/shop/category/powerfurl-almacenadores-sin-fin-powerfurl-twelve-16 | category | powerfurl |          11 |                  1 | False         | possible_cannibalization |
| https://www.morfrac.com/shop/category/powerfurl-continuous-line-powerfurl-four-11           | category | powerfurl |          11 | https://www.morfrac.com/es/shop/category/powerfurl-almacenadores-sin-fin-powerfurl-three-15  | category | powerfurl |          11 |                  1 | False         | possible_cannibalization |
| https://www.morfrac.com/shop/category/powerfurl-continuous-line-powerfurl-four-11           | category | powerfurl |          11 | https://www.morfrac.com/es/shop/category/powerfurl-almacenadores-sin-fin-powerfurl-ten-14    | category | powerfurl |          11 |                  1 | False         | possible_cannibalization |

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

    - Cluster summary: `C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC\06_MARKETING\SEO_Agent\Semantic_Clusters\2026-09-28_semantic_clusters.csv`
    - Page cluster mapping: `C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC\06_MARKETING\SEO_Agent\Semantic_Clusters\2026-09-28_semantic_cluster_pages.csv`
    - Similarity pairs: `C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC\06_MARKETING\SEO_Agent\Semantic_Clusters\2026-09-28_semantic_similarity_pairs.csv`
    - Cannibalization: `C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC\06_MARKETING\SEO_Agent\Semantic_Clusters\2026-09-28_semantic_cannibalization.csv`
    - Orphan topics: `C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC\06_MARKETING\SEO_Agent\Semantic_Clusters\2026-09-28_semantic_orphan_topics.csv`

## Related Links

### Concepts
- [[FRAGMENTED_TOPIC]]
- [[PRODUCT_HEAVY_NO_PILLAR]]
- [[ORPHAN_TOPIC]]
- [[CONTENT_WITHOUT_COMMERCIAL_TARGET]]

### Projects
- [[Search Console]]
