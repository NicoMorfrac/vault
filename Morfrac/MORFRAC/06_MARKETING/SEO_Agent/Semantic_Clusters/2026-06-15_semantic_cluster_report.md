---
type: seo_semantic_cluster_report
source_agent: SEO_Agent
created: 2026-06-15
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

    2026-06-15

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

    - Crawl file: `C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC\06_MARKETING\SEO_Agent\Crawls\2026-06-15_site_crawl.csv`
    - Search Console merge file: `C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC\06_MARKETING\SEO_Agent\Merged_Analysis\2026-06-15_search_console_merge.csv`

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

    |   semantic_cluster_id | dominant_label   |   page_count |   product_pages |   category_pages |   landing_pages |   authority_content_pages |   total_impressions |   total_clicks |   avg_seo_priority_score | cluster_health          | top_terms                                                                                                                     | role_counts                                                                          | label_counts                                                                                                                                                |
|----------------------:|:-----------------|-------------:|----------------:|-----------------:|----------------:|--------------------------:|--------------------:|---------------:|-------------------------:|:------------------------|:------------------------------------------------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                     8 | other            |           49 |              11 |                2 |               4 |                        20 |                 794 |             26 |                     3.74 | FRAGMENTED_TOPIC        | custom, morfrac, morfblock, snatch, morfwing, high performance, hardware, 2024, performance, sail                             | {'authority_content': 20, 'general': 12, 'product': 11, 'landing': 4, 'category': 2} | {'other': 13, 'powerfurl': 8, 'morfblock': 8, 'custom_engineering': 5, 'morfwing': 5, 'mloop': 4, 'dogbone': 3, 'padeye': 1, 'morfring': 1, 'hoistlock': 1} |
|                     3 | morfblock        |           44 |              44 |                0 |               0 |                         0 |                   0 |              0 |                     0    | FRAGMENTED_TOPIC        | sailing block, sailing, block, morfblock, morfblock light, light, swl, lightweight sailing, high, lightweight                 | {'product': 44}                                                                      | {'morfblock': 44}                                                                                                                                           |
|                     2 | powerfurl        |           40 |               0 |               40 |               0 |                         0 |                   0 |              0 |                     0    | FRAGMENTED_TOPIC        | shop, morfrac shop, shop morfrac, powerfurl, shop powerfurl, morfrac, powerfurl morfrac, shop shop, morfblock, shop morfblock | {'category': 40}                                                                     | {'powerfurl': 16, 'morfblock': 10, 'other': 6, 'dogbone': 3, 'custom_engineering': 1, 'mloop': 1, 'morfring': 1, 'mreel': 1, 'padeye': 1}                   |
|                     4 | dogbone          |           24 |              24 |                0 |               0 |                         0 |                   0 |              0 |                     0    | FRAGMENTED_TOPIC        | dogbone, length, morfrac dogbone, aluminium, total length, total, length morfrac, morfrac, 60mm, aluminium dogbone            | {'product': 24}                                                                      | {'dogbone': 24}                                                                                                                                             |
|                     1 | powerfurl        |           22 |              22 |                0 |               0 |                         0 |                   0 |              0 |                     0    | FRAGMENTED_TOPIC        | kit, furling, powerfurl, 5t, 5t swl, furling kit, swl, swl morfrac, morfrac powerfurl, reliable                               | {'product': 22}                                                                      | {'powerfurl': 19, 'shackle': 3}                                                                                                                             |
|                     5 | morfring         |           13 |              12 |                0 |               1 |                         0 |                   0 |              0 |                     0    | OK                      | friction, morfring, ptfe, ring, friction ring, aluminium friction, aluminium, morfrac morfring, groove max, groove            | {'product': 12, 'landing': 1}                                                        | {'morfring': 13}                                                                                                                                            |
|                     7 | shackle          |           11 |               8 |                2 |               1 |                         0 |                   0 |              0 |                     0    | OK                      | shackle, ti shackle, ti, titanium shackle, shackle morfrac, titanium, cnc machined, machined, cnc, grade titanium             | {'product': 8, 'category': 2, 'landing': 1}                                          | {'shackle': 11}                                                                                                                                             |
|                    10 | padeye           |           10 |               8 |                0 |               1 |                         1 |                   0 |              0 |                     0    | OK                      | padeye, stick, deck, morfrac padeye, stick padeye, 20, ring, deck padeye, padeye ring, ring 20                                | {'product': 8, 'landing': 1, 'authority_content': 1}                                 | {'padeye': 10}                                                                                                                                              |
|                     0 | morfblock        |           14 |              14 |                0 |               0 |                         0 |                   0 |              0 |                     0    | PRODUCT_HEAVY_NO_PILLAR | xl, morfblock xl, xl sailing, sailing block, block, morfblock, sailing, swl, sheave, handling                                 | {'product': 14}                                                                      | {'morfblock': 14}                                                                                                                                           |
|                     6 | powerfurl        |           12 |              12 |                0 |               0 |                         0 |                   0 |              0 |                     0    | PRODUCT_HEAVY_NO_PILLAR | unit, powerfurl, drum, furling, powerfurl drum, unit powerfurl, unit morfrac, furling unit, powerfurl engineered, swl         | {'product': 12}                                                                      | {'powerfurl': 12}                                                                                                                                           |
|                     9 | dogbone          |           10 |              10 |                0 |               0 |                         0 |                   0 |              0 |                     0    | PRODUCT_HEAVY_NO_PILLAR | flat, flat faced, faced, dogbone flat, faced titanium, dogbone, rope reeler, reeler, mreel, rope                              | {'product': 10}                                                                      | {'dogbone': 6, 'mreel': 4}                                                                                                                                  |
|                    11 | powerfurl        |            9 |               9 |                0 |               0 |                         0 |                   0 |              0 |                     0    | PRODUCT_HEAVY_NO_PILLAR | fork, 10t, 10t swl, powerfurl fork, fitting, powerfurl, fork fitting, swl, tdis, integrators                                  | {'product': 9}                                                                       | {'powerfurl': 9}                                                                                                                                            |

    ---

    # Likely Cannibalization / Duplicate Intent

    | url_a                                                                                      | role_a   | label_a   |   cluster_a | url_b                                                                                                       | role_b   | label_b   |   cluster_b |   similarity_score | same_family   | risk_type                |
|:-------------------------------------------------------------------------------------------|:---------|:----------|------------:|:------------------------------------------------------------------------------------------------------------|:---------|:----------|------------:|-------------------:|:--------------|:-------------------------|
| https://www.morfrac.com/es/shop/category/powerfurl-almacenadores-sin-fin-powerfurlthree-15 | category | powerfurl |           2 | https://www.morfrac.com/es/shop/category/powerfurl-almacenadores-sin-fin-powerfurltwelve-16                 | category | powerfurl |           2 |                  1 | False         | possible_cannibalization |
| https://www.morfrac.com/es/shop/custom-33/morfblcok-custom-runners-12664                   | product  | morfblock |           8 | https://www.morfrac.com/es/shop/morfblock-morfblockxl-21/morfblcok-custom-runners-12664                     | product  | morfblock |           8 |                  1 | False         | possible_cannibalization |
| https://www.morfrac.com/es/shop/category/powerfurl-almacenadores-sin-fin-powerfurlten-14   | category | powerfurl |           2 | https://www.morfrac.com/es/shop/category/powerfurl-almacenadores-sin-fin-powerfurltwelve-16                 | category | powerfurl |           2 |                  1 | False         | possible_cannibalization |
| https://www.morfrac.com/es/shop/category/powerfurl-almacenadores-sin-fin-powerfurlten-14   | category | powerfurl |           2 | https://www.morfrac.com/es/shop/category/powerfurl-almacenadores-sin-fin-powerfurlthree-15                  | category | powerfurl |           2 |                  1 | False         | possible_cannibalization |
| https://www.morfrac.com/es/shop/category/powerfurl-almacenadores-sin-fin-powerfurlsix-13   | category | powerfurl |           2 | https://www.morfrac.com/es/shop/category/powerfurl-almacenadores-sin-fin-powerfurlthree-15                  | category | powerfurl |           2 |                  1 | False         | possible_cannibalization |
| https://www.morfrac.com/es/shop/category/powerfurl-almacenadores-sin-fin-powerfurlsix-13   | category | powerfurl |           2 | https://www.morfrac.com/es/shop/category/powerfurl-almacenadores-sin-fin-powerfurltwelve-16                 | category | powerfurl |           2 |                  1 | False         | possible_cannibalization |
| https://www.morfrac.com/es/shop/category/powerfurl-almacenadores-sin-fin-powerfurlfour-11  | category | powerfurl |           2 | https://www.morfrac.com/es/shop/category/powerfurl-almacenadores-sin-fin-powerfurlthree-15                  | category | powerfurl |           2 |                  1 | False         | possible_cannibalization |
| https://www.morfrac.com/es/shop/category/powerfurl-almacenadores-sin-fin-powerfurlfour-11  | category | powerfurl |           2 | https://www.morfrac.com/es/shop/category/powerfurl-almacenadores-sin-fin-powerfurlten-14                    | category | powerfurl |           2 |                  1 | False         | possible_cannibalization |
| https://www.morfrac.com/es/shop/category/powerfurl-almacenadores-sin-fin-powerfurlsix-13   | category | powerfurl |           2 | https://www.morfrac.com/es/shop/category/powerfurl-almacenadores-sin-fin-powerfurlten-14                    | category | powerfurl |           2 |                  1 | False         | possible_cannibalization |
| https://www.morfrac.com/es/shop/category/powerfurl-almacenadores-sin-fin-powerfurlone-12   | category | powerfurl |           2 | https://www.morfrac.com/es/shop/category/powerfurl-almacenadores-sin-fin-powerfurltwelve-16                 | category | powerfurl |           2 |                  1 | False         | possible_cannibalization |
| https://www.morfrac.com/es/shop/category/powerfurl-almacenadores-sin-fin-powerfurlone-12   | category | powerfurl |           2 | https://www.morfrac.com/es/shop/category/powerfurl-almacenadores-sin-fin-powerfurlthree-15                  | category | powerfurl |           2 |                  1 | False         | possible_cannibalization |
| https://www.morfrac.com/es/shop/category/powerfurl-almacenadores-sin-fin-powerfurlone-12   | category | powerfurl |           2 | https://www.morfrac.com/es/shop/category/powerfurl-almacenadores-sin-fin-powerfurlten-14                    | category | powerfurl |           2 |                  1 | False         | possible_cannibalization |
| https://www.morfrac.com/es/shop/category/powerfurl-almacenadores-sin-fin-powerfurlone-12   | category | powerfurl |           2 | https://www.morfrac.com/es/shop/category/powerfurl-almacenadores-sin-fin-powerfurlsix-13                    | category | powerfurl |           2 |                  1 | False         | possible_cannibalization |
| https://www.morfrac.com/es/shop/category/powerfurl-almacenadores-sin-fin-powerfurlfour-11  | category | powerfurl |           2 | https://www.morfrac.com/es/shop/category/powerfurl-almacenadores-sin-fin-powerfurltwelve-16                 | category | powerfurl |           2 |                  1 | False         | possible_cannibalization |
| https://www.morfrac.com/shop/category/powerfurl-continuous-line-powerfurlfour-11           | category | powerfurl |           2 | https://www.morfrac.com/shop/category/powerfurl-continuous-line-powerfurlten-14                             | category | powerfurl |           2 |                  1 | False         | possible_cannibalization |
| https://www.morfrac.com/shop/category/powerfurl-continuous-line-powerfurlfour-11           | category | powerfurl |           2 | https://www.morfrac.com/shop/category/powerfurl-continuous-line-powerfurlsix-13                             | category | powerfurl |           2 |                  1 | False         | possible_cannibalization |
| https://www.morfrac.com/es/shop/category/powerfurl-almacenadores-sin-fin-powerfurlfour-11  | category | powerfurl |           2 | https://www.morfrac.com/es/shop/category/powerfurl-almacenadores-sin-fin-powerfurlsix-13                    | category | powerfurl |           2 |                  1 | False         | possible_cannibalization |
| https://www.morfrac.com/shop/category/powerfurl-continuous-line-powerfurlfour-11           | category | powerfurl |           2 | https://www.morfrac.com/shop/category/powerfurl-continuous-line-powerfurlthree-15                           | category | powerfurl |           2 |                  1 | False         | possible_cannibalization |
| https://www.morfrac.com/shop/category/powerfurl-continuous-line-powerfurlfour-11           | category | powerfurl |           2 | https://www.morfrac.com/shop/category/powerfurl-continuous-line-powerfurlone-12                             | category | powerfurl |           2 |                  1 | False         | possible_cannibalization |
| https://www.morfrac.com/shop/category/powerfurl-continuous-line-powerfurleight-10          | category | powerfurl |           2 | https://www.morfrac.com/shop/category/powerfurl-continuous-line-powerfurltwelve-16                          | category | powerfurl |           2 |                  1 | False         | possible_cannibalization |
| https://www.morfrac.com/shop/category/powerfurl-continuous-line-powerfurleight-10          | category | powerfurl |           2 | https://www.morfrac.com/shop/category/powerfurl-continuous-line-powerfurlten-14                             | category | powerfurl |           2 |                  1 | False         | possible_cannibalization |
| https://www.morfrac.com/shop/category/powerfurl-continuous-line-powerfurleight-10          | category | powerfurl |           2 | https://www.morfrac.com/shop/category/powerfurl-continuous-line-powerfurlthree-15                           | category | powerfurl |           2 |                  1 | False         | possible_cannibalization |
| https://www.morfrac.com/shop/powerfurl-1/powerfurl-one-top-down-furling-kit-12825          | product  | powerfurl |           1 | https://www.morfrac.com/es/shop/powerfurl-almacenadores-sin-fin-31/powerfurl-one-top-down-furling-kit-12825 | product  | powerfurl |           1 |                  1 | False         | possible_cannibalization |
| https://www.morfrac.com/shop/powerfurl-1/powerfurl-one-top-down-furling-kit-12825          | product  | powerfurl |           1 | https://www.morfrac.com/shop/powerfurl-one-top-down-furling-kit-12825                                       | product  | powerfurl |           1 |                  1 | False         | possible_cannibalization |
| https://www.morfrac.com/shop/category/powerfurl-continuous-line-powerfurleight-10          | category | powerfurl |           2 | https://www.morfrac.com/shop/category/powerfurl-continuous-line-powerfurlsix-13                             | category | powerfurl |           2 |                  1 | False         | possible_cannibalization |
| https://www.morfrac.com/shop/category/powerfurl-continuous-line-powerfurleight-10          | category | powerfurl |           2 | https://www.morfrac.com/shop/category/powerfurl-continuous-line-powerfurlone-12                             | category | powerfurl |           2 |                  1 | False         | possible_cannibalization |
| https://www.morfrac.com/shop/category/powerfurl-continuous-line-powerfurlone-12            | category | powerfurl |           2 | https://www.morfrac.com/shop/category/powerfurl-continuous-line-powerfurltwelve-16                          | category | powerfurl |           2 |                  1 | False         | possible_cannibalization |
| https://www.morfrac.com/shop/category/powerfurl-continuous-line-powerfurlone-12            | category | powerfurl |           2 | https://www.morfrac.com/shop/category/powerfurl-continuous-line-powerfurlthree-15                           | category | powerfurl |           2 |                  1 | False         | possible_cannibalization |
| https://www.morfrac.com/shop/category/powerfurl-continuous-line-powerfurlone-12            | category | powerfurl |           2 | https://www.morfrac.com/shop/category/powerfurl-continuous-line-powerfurlten-14                             | category | powerfurl |           2 |                  1 | False         | possible_cannibalization |
| https://www.morfrac.com/shop/category/powerfurl-continuous-line-powerfurlone-12            | category | powerfurl |           2 | https://www.morfrac.com/shop/category/powerfurl-continuous-line-powerfurlsix-13                             | category | powerfurl |           2 |                  1 | False         | possible_cannibalization |

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

    - Cluster summary: `C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC\06_MARKETING\SEO_Agent\Semantic_Clusters\2026-06-15_semantic_clusters.csv`
    - Page cluster mapping: `C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC\06_MARKETING\SEO_Agent\Semantic_Clusters\2026-06-15_semantic_cluster_pages.csv`
    - Similarity pairs: `C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC\06_MARKETING\SEO_Agent\Semantic_Clusters\2026-06-15_semantic_similarity_pairs.csv`
    - Cannibalization: `C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC\06_MARKETING\SEO_Agent\Semantic_Clusters\2026-06-15_semantic_cannibalization.csv`
    - Orphan topics: `C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC\06_MARKETING\SEO_Agent\Semantic_Clusters\2026-06-15_semantic_orphan_topics.csv`

## Related Links

### Concepts
- [[FRAGMENTED_TOPIC]]
- [[PRODUCT_HEAVY_NO_PILLAR]]
- [[ORPHAN_TOPIC]]
- [[CONTENT_WITHOUT_COMMERCIAL_TARGET]]

### Projects
- [[Search Console]]
