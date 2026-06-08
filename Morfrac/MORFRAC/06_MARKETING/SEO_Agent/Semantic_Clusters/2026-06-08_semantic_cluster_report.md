---
type: seo_semantic_cluster_report
source_agent: SEO_Agent
created: 2026-06-08
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

    2026-06-08

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

    - Crawl file: `C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC\06_MARKETING\SEO_Agent\Crawls\2026-06-08_site_crawl.csv`
    - Search Console merge file: `C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC\06_MARKETING\SEO_Agent\Merged_Analysis\2026-06-08_search_console_merge.csv`

    ---

    # Summary

    - Pages analyzed: 258
    - Semantic clusters: 12
    - Similar page pairs above threshold: 263
    - Cannibalization/topic-overlap pairs: 253
    - Orphan topic clusters: 0

    Similarity threshold:

    `0.68`

    ---

    # Cluster Summary

    |   semantic_cluster_id | dominant_label   |   page_count |   product_pages |   category_pages |   landing_pages |   authority_content_pages |   total_impressions |   total_clicks |   avg_seo_priority_score | cluster_health          | top_terms                                                                                                          | role_counts                                                           | label_counts                                                                                                                                |
|----------------------:|:-----------------|-------------:|----------------:|-----------------:|----------------:|--------------------------:|--------------------:|---------------:|-------------------------:|:------------------------|:-------------------------------------------------------------------------------------------------------------------|:----------------------------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------|
|                     4 | morfblock        |           58 |              58 |                0 |               0 |                         0 |                   0 |              0 |                     0    | FRAGMENTED_TOPIC        | sailing block, block, sailing, morfblock, swl, morfblock light, light, high, xl, lightweight sailing               | {'product': 58}                                                       | {'morfblock': 58}                                                                                                                           |
|                     0 | morfblock        |           36 |              11 |                0 |               4 |                        11 |                 616 |              2 |                     2.79 | FRAGMENTED_TOPIC        | custom, morfrac, snatch, morfblock, solutions, high performance, loop, performance, mloop, powerfurl               | {'authority_content': 11, 'product': 11, 'general': 10, 'landing': 4} | {'morfblock': 8, 'other': 7, 'powerfurl': 6, 'custom_engineering': 5, 'mloop': 4, 'dogbone': 2, 'morfring': 2, 'padeye': 1, 'hoistlock': 1} |
|                     3 | dogbone          |           30 |              30 |                0 |               0 |                         0 |                   0 |              0 |                     0    | FRAGMENTED_TOPIC        | dogbone, morfrac dogbone, length, aluminium, morfrac, length morfrac, total length, total, titanium, faced         | {'product': 30}                                                       | {'dogbone': 30}                                                                                                                             |
|                     1 | morfblock        |           28 |               0 |               27 |               0 |                         0 |                   0 |              0 |                     0    | FRAGMENTED_TOPIC        | shop, morfrac shop, shop morfrac, morfrac, morfblock, shop morfblock, tdi, dogbone, morfblock max, single line     | {'category': 27, 'general': 1}                                        | {'morfblock': 10, 'other': 8, 'dogbone': 4, 'custom_engineering': 1, 'mloop': 1, 'morfring': 1, 'mreel': 1, 'padeye': 1, 'powerfurl': 1}    |
|                     6 | powerfurl        |           24 |              24 |                0 |               0 |                         0 |                   0 |              0 |                     0    | FRAGMENTED_TOPIC        | powerfurl, 5t swl, 5t, furling, kit, swl, morfrac powerfurl, furling kit, reliable, unit                           | {'product': 24}                                                       | {'powerfurl': 21, 'shackle': 3}                                                                                                             |
|                    10 | powerfurl        |           15 |               0 |               15 |               0 |                         0 |                   0 |              0 |                     0    | OK                      | shop, powerfurl, morfrac shop, shop powerfurl, powerfurl morfrac, shop shop, morfrac, shop morfrac, free, price    | {'category': 15}                                                      | {'powerfurl': 15}                                                                                                                           |
|                     9 | shackle          |           11 |               8 |                2 |               1 |                         0 |                   0 |              0 |                     0    | OK                      | shackle, ti shackle, ti, titanium shackle, shackle morfrac, titanium, cnc, machined, cnc machined, ultra           | {'product': 8, 'category': 2, 'landing': 1}                           | {'shackle': 11}                                                                                                                             |
|                     5 | morfwing         |           10 |               0 |                0 |               1 |                         9 |                   0 |              0 |                     0    | OK                      | morfwing, 2024, year, introducing, new, wing, sail, 372, stand 01, stand                                           | {'authority_content': 9, 'landing': 1}                                | {'morfwing': 5, 'other': 4, 'powerfurl': 1}                                                                                                 |
|                     7 | padeye           |           10 |               8 |                0 |               1 |                         1 |                   0 |              0 |                     0    | OK                      | padeye, stick, deck, morfrac padeye, stick padeye, 20, ring, deck padeye, padeye ring, ring 20                     | {'product': 8, 'landing': 1, 'authority_content': 1}                  | {'padeye': 10}                                                                                                                              |
|                    11 | mreel            |            5 |               4 |                0 |               0 |                         0 |                 126 |             27 |                    11.6  | OK                      | mreel, rope reeler, reeler, mreel rope, rope, reeler morfrac, morfrac mreel, halyards, sheets halyards, safer      | {'product': 4, 'general': 1}                                          | {'mreel': 4, 'powerfurl': 1}                                                                                                                |
|                     2 | powerfurl        |           19 |              19 |                0 |               0 |                         0 |                   0 |              0 |                     0    | PRODUCT_HEAVY_NO_PILLAR | 10t, 10t swl, powerfurl, furling, drum, fork, swl, powerfurl drum, powerfurl fork, fitting                         | {'product': 19}                                                       | {'powerfurl': 19}                                                                                                                           |
|                     8 | morfring         |           12 |              12 |                0 |               0 |                         0 |                   0 |              0 |                     0    | PRODUCT_HEAVY_NO_PILLAR | friction, ptfe, ring, friction ring, morfring, aluminium friction, aluminium, groove, groove max, morfrac morfring | {'product': 12}                                                       | {'morfring': 12}                                                                                                                            |

    ---

    # Likely Cannibalization / Duplicate Intent

    | url_a                                                                                      | role_a   | label_a   |   cluster_a | url_b                                                                                                       | role_b   | label_b   |   cluster_b |   similarity_score | same_family   | risk_type                |
|:-------------------------------------------------------------------------------------------|:---------|:----------|------------:|:------------------------------------------------------------------------------------------------------------|:---------|:----------|------------:|-------------------:|:--------------|:-------------------------|
| https://www.morfrac.com/es/shop/category/powerfurl-almacenadores-sin-fin-powerfurlthree-15 | category | powerfurl |          10 | https://www.morfrac.com/es/shop/category/powerfurl-almacenadores-sin-fin-powerfurltwelve-16                 | category | powerfurl |          10 |                  1 | False         | possible_cannibalization |
| https://www.morfrac.com/es/shop/custom-33/morfblcok-custom-runners-12664                   | product  | morfblock |           0 | https://www.morfrac.com/es/shop/morfblock-morfblockxl-21/morfblcok-custom-runners-12664                     | product  | morfblock |           0 |                  1 | False         | possible_cannibalization |
| https://www.morfrac.com/es/shop/category/powerfurl-almacenadores-sin-fin-powerfurlten-14   | category | powerfurl |          10 | https://www.morfrac.com/es/shop/category/powerfurl-almacenadores-sin-fin-powerfurltwelve-16                 | category | powerfurl |          10 |                  1 | False         | possible_cannibalization |
| https://www.morfrac.com/es/shop/category/powerfurl-almacenadores-sin-fin-powerfurlten-14   | category | powerfurl |          10 | https://www.morfrac.com/es/shop/category/powerfurl-almacenadores-sin-fin-powerfurlthree-15                  | category | powerfurl |          10 |                  1 | False         | possible_cannibalization |
| https://www.morfrac.com/es/shop/category/powerfurl-almacenadores-sin-fin-powerfurlsix-13   | category | powerfurl |          10 | https://www.morfrac.com/es/shop/category/powerfurl-almacenadores-sin-fin-powerfurlthree-15                  | category | powerfurl |          10 |                  1 | False         | possible_cannibalization |
| https://www.morfrac.com/es/shop/category/powerfurl-almacenadores-sin-fin-powerfurlsix-13   | category | powerfurl |          10 | https://www.morfrac.com/es/shop/category/powerfurl-almacenadores-sin-fin-powerfurltwelve-16                 | category | powerfurl |          10 |                  1 | False         | possible_cannibalization |
| https://www.morfrac.com/es/shop/category/powerfurl-almacenadores-sin-fin-powerfurlfour-11  | category | powerfurl |          10 | https://www.morfrac.com/es/shop/category/powerfurl-almacenadores-sin-fin-powerfurlthree-15                  | category | powerfurl |          10 |                  1 | False         | possible_cannibalization |
| https://www.morfrac.com/es/shop/category/powerfurl-almacenadores-sin-fin-powerfurlfour-11  | category | powerfurl |          10 | https://www.morfrac.com/es/shop/category/powerfurl-almacenadores-sin-fin-powerfurlten-14                    | category | powerfurl |          10 |                  1 | False         | possible_cannibalization |
| https://www.morfrac.com/es/shop/category/powerfurl-almacenadores-sin-fin-powerfurlsix-13   | category | powerfurl |          10 | https://www.morfrac.com/es/shop/category/powerfurl-almacenadores-sin-fin-powerfurlten-14                    | category | powerfurl |          10 |                  1 | False         | possible_cannibalization |
| https://www.morfrac.com/es/shop/category/powerfurl-almacenadores-sin-fin-powerfurlone-12   | category | powerfurl |          10 | https://www.morfrac.com/es/shop/category/powerfurl-almacenadores-sin-fin-powerfurltwelve-16                 | category | powerfurl |          10 |                  1 | False         | possible_cannibalization |
| https://www.morfrac.com/es/shop/category/powerfurl-almacenadores-sin-fin-powerfurlone-12   | category | powerfurl |          10 | https://www.morfrac.com/es/shop/category/powerfurl-almacenadores-sin-fin-powerfurlthree-15                  | category | powerfurl |          10 |                  1 | False         | possible_cannibalization |
| https://www.morfrac.com/es/shop/category/powerfurl-almacenadores-sin-fin-powerfurlone-12   | category | powerfurl |          10 | https://www.morfrac.com/es/shop/category/powerfurl-almacenadores-sin-fin-powerfurlten-14                    | category | powerfurl |          10 |                  1 | False         | possible_cannibalization |
| https://www.morfrac.com/es/shop/category/powerfurl-almacenadores-sin-fin-powerfurlone-12   | category | powerfurl |          10 | https://www.morfrac.com/es/shop/category/powerfurl-almacenadores-sin-fin-powerfurlsix-13                    | category | powerfurl |          10 |                  1 | False         | possible_cannibalization |
| https://www.morfrac.com/es/shop/category/powerfurl-almacenadores-sin-fin-powerfurlfour-11  | category | powerfurl |          10 | https://www.morfrac.com/es/shop/category/powerfurl-almacenadores-sin-fin-powerfurltwelve-16                 | category | powerfurl |          10 |                  1 | False         | possible_cannibalization |
| https://www.morfrac.com/shop/category/powerfurl-continuous-line-powerfurlfour-11           | category | powerfurl |          10 | https://www.morfrac.com/shop/category/powerfurl-continuous-line-powerfurlten-14                             | category | powerfurl |          10 |                  1 | False         | possible_cannibalization |
| https://www.morfrac.com/shop/category/powerfurl-continuous-line-powerfurlfour-11           | category | powerfurl |          10 | https://www.morfrac.com/shop/category/powerfurl-continuous-line-powerfurlsix-13                             | category | powerfurl |          10 |                  1 | False         | possible_cannibalization |
| https://www.morfrac.com/es/shop/category/powerfurl-almacenadores-sin-fin-powerfurlfour-11  | category | powerfurl |          10 | https://www.morfrac.com/es/shop/category/powerfurl-almacenadores-sin-fin-powerfurlsix-13                    | category | powerfurl |          10 |                  1 | False         | possible_cannibalization |
| https://www.morfrac.com/shop/category/powerfurl-continuous-line-powerfurlfour-11           | category | powerfurl |          10 | https://www.morfrac.com/shop/category/powerfurl-continuous-line-powerfurlthree-15                           | category | powerfurl |          10 |                  1 | False         | possible_cannibalization |
| https://www.morfrac.com/shop/category/powerfurl-continuous-line-powerfurlfour-11           | category | powerfurl |          10 | https://www.morfrac.com/shop/category/powerfurl-continuous-line-powerfurlone-12                             | category | powerfurl |          10 |                  1 | False         | possible_cannibalization |
| https://www.morfrac.com/shop/category/powerfurl-continuous-line-powerfurleight-10          | category | powerfurl |          10 | https://www.morfrac.com/shop/category/powerfurl-continuous-line-powerfurltwelve-16                          | category | powerfurl |          10 |                  1 | False         | possible_cannibalization |
| https://www.morfrac.com/shop/category/powerfurl-continuous-line-powerfurleight-10          | category | powerfurl |          10 | https://www.morfrac.com/shop/category/powerfurl-continuous-line-powerfurlten-14                             | category | powerfurl |          10 |                  1 | False         | possible_cannibalization |
| https://www.morfrac.com/shop/category/powerfurl-continuous-line-powerfurleight-10          | category | powerfurl |          10 | https://www.morfrac.com/shop/category/powerfurl-continuous-line-powerfurlthree-15                           | category | powerfurl |          10 |                  1 | False         | possible_cannibalization |
| https://www.morfrac.com/shop/powerfurl-1/powerfurl-one-top-down-furling-kit-12825          | product  | powerfurl |           6 | https://www.morfrac.com/es/shop/powerfurl-almacenadores-sin-fin-31/powerfurl-one-top-down-furling-kit-12825 | product  | powerfurl |           6 |                  1 | False         | possible_cannibalization |
| https://www.morfrac.com/shop/powerfurl-1/powerfurl-one-top-down-furling-kit-12825          | product  | powerfurl |           6 | https://www.morfrac.com/shop/powerfurl-one-top-down-furling-kit-12825                                       | product  | powerfurl |           6 |                  1 | False         | possible_cannibalization |
| https://www.morfrac.com/shop/category/powerfurl-continuous-line-powerfurleight-10          | category | powerfurl |          10 | https://www.morfrac.com/shop/category/powerfurl-continuous-line-powerfurlsix-13                             | category | powerfurl |          10 |                  1 | False         | possible_cannibalization |
| https://www.morfrac.com/shop/category/powerfurl-continuous-line-powerfurleight-10          | category | powerfurl |          10 | https://www.morfrac.com/shop/category/powerfurl-continuous-line-powerfurlone-12                             | category | powerfurl |          10 |                  1 | False         | possible_cannibalization |
| https://www.morfrac.com/shop/category/powerfurl-continuous-line-powerfurlone-12            | category | powerfurl |          10 | https://www.morfrac.com/shop/category/powerfurl-continuous-line-powerfurltwelve-16                          | category | powerfurl |          10 |                  1 | False         | possible_cannibalization |
| https://www.morfrac.com/shop/category/powerfurl-continuous-line-powerfurlone-12            | category | powerfurl |          10 | https://www.morfrac.com/shop/category/powerfurl-continuous-line-powerfurlthree-15                           | category | powerfurl |          10 |                  1 | False         | possible_cannibalization |
| https://www.morfrac.com/shop/category/powerfurl-continuous-line-powerfurlone-12            | category | powerfurl |          10 | https://www.morfrac.com/shop/category/powerfurl-continuous-line-powerfurlten-14                             | category | powerfurl |          10 |                  1 | False         | possible_cannibalization |
| https://www.morfrac.com/shop/category/powerfurl-continuous-line-powerfurlone-12            | category | powerfurl |          10 | https://www.morfrac.com/shop/category/powerfurl-continuous-line-powerfurlsix-13                             | category | powerfurl |          10 |                  1 | False         | possible_cannibalization |

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

    - Cluster summary: `C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC\06_MARKETING\SEO_Agent\Semantic_Clusters\2026-06-08_semantic_clusters.csv`
    - Page cluster mapping: `C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC\06_MARKETING\SEO_Agent\Semantic_Clusters\2026-06-08_semantic_cluster_pages.csv`
    - Similarity pairs: `C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC\06_MARKETING\SEO_Agent\Semantic_Clusters\2026-06-08_semantic_similarity_pairs.csv`
    - Cannibalization: `C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC\06_MARKETING\SEO_Agent\Semantic_Clusters\2026-06-08_semantic_cannibalization.csv`
    - Orphan topics: `C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC\06_MARKETING\SEO_Agent\Semantic_Clusters\2026-06-08_semantic_orphan_topics.csv`

## Related Links

### Concepts
- [[FRAGMENTED_TOPIC]]
- [[PRODUCT_HEAVY_NO_PILLAR]]
- [[ORPHAN_TOPIC]]
- [[CONTENT_WITHOUT_COMMERCIAL_TARGET]]

### Projects
- [[Search Console]]
