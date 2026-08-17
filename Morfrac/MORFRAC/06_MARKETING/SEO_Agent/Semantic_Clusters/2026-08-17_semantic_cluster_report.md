---
type: seo_semantic_cluster_report
source_agent: SEO_Agent
created: 2026-08-17
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

    2026-08-17

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

    - Crawl file: `C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC\06_MARKETING\SEO_Agent\Crawls\2026-08-17_site_crawl.csv`
    - Search Console merge file: `C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC\06_MARKETING\SEO_Agent\Merged_Analysis\2026-08-17_search_console_merge.csv`

    ---

    # Summary

    - Pages analyzed: 260
    - Semantic clusters: 12
    - Similar page pairs above threshold: 276
    - Cannibalization/topic-overlap pairs: 265
    - Orphan topic clusters: 0

    Similarity threshold:

    `0.68`

    ---

    # Cluster Summary

    |   semantic_cluster_id | dominant_label   |   page_count |   product_pages |   category_pages |   landing_pages |   authority_content_pages |   total_impressions |   total_clicks |   avg_seo_priority_score | cluster_health          | top_terms                                                                                                                          | role_counts                                                           | label_counts                                                                                                                                                             |
|----------------------:|:-----------------|-------------:|----------------:|-----------------:|----------------:|--------------------------:|--------------------:|---------------:|-------------------------:|:------------------------|:-----------------------------------------------------------------------------------------------------------------------------------|:----------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                    11 | other            |           61 |              23 |                0 |               5 |                        21 |                 429 |             22 |                     1.51 | FRAGMENTED_TOPIC        | custom, morfrac, shackle, morfblock, snatch, high performance, high, morfwing, titanium, mreel                                     | {'product': 23, 'authority_content': 21, 'general': 12, 'landing': 5} | {'other': 15, 'powerfurl': 8, 'morfblock': 8, 'custom_engineering': 6, 'shackle': 6, 'morfwing': 5, 'mloop': 4, 'mreel': 4, 'dogbone': 3, 'morfring': 1, 'hoistlock': 1} |
|                     8 | powerfurl        |           40 |               0 |               40 |               0 |                         0 |                   0 |              0 |                     0    | FRAGMENTED_TOPIC        | shop, morfrac shop, shop morfrac, powerfurl, morfrac, shop powerfurl, powerfurl morfrac, tdi, shop morfblock, morfblock            | {'category': 40}                                                      | {'powerfurl': 16, 'other': 9, 'morfblock': 5, 'dogbone': 3, 'shackle': 2, 'custom_engineering': 1, 'mloop': 1, 'morfring': 1, 'mreel': 1, 'padeye': 1}                   |
|                     2 | morfblock        |           38 |              36 |                2 |               0 |                         0 |                   0 |              0 |                     0    | FRAGMENTED_TOPIC        | morfblock light, sailing block, light, morfblock, sailing, block, lightweight sailing, swl, lightweight, high                      | {'product': 36, 'category': 2}                                        | {'morfblock': 38}                                                                                                                                                        |
|                     0 | dogbone          |           24 |              24 |                0 |               0 |                         0 |                   0 |              0 |                     0    | FRAGMENTED_TOPIC        | dogbone, length, morfrac dogbone, aluminium, total length, total, length morfrac, morfrac, 60mm, aluminium dogbone                 | {'product': 24}                                                       | {'dogbone': 24}                                                                                                                                                          |
|                     4 | powerfurl        |           21 |              21 |                0 |               0 |                         0 |                   0 |              0 |                     0    | FRAGMENTED_TOPIC        | 5t swl, 5t, powerfurl, kit, furling, swl, furling kit, swl morfrac, morfrac powerfurl, shackle                                     | {'product': 21}                                                       | {'powerfurl': 15, 'shackle': 6}                                                                                                                                          |
|                     9 | powerfurl        |           21 |              21 |                0 |               0 |                         0 |                   0 |              0 |                     0    | FRAGMENTED_TOPIC        | powerfurl, 10t swl, 10t, furling, unit, drum, fork, swl, swl furling, powerfurl drum                                               | {'product': 21}                                                       | {'powerfurl': 21}                                                                                                                                                        |
|                     6 | morfring         |           13 |              12 |                0 |               1 |                         0 |                   0 |              0 |                     0    | OK                      | morfring, friction, ptfe, friction ring, ring, aluminium friction, aluminium, morfrac morfring, groove, groove max                 | {'product': 12, 'landing': 1}                                         | {'morfring': 13}                                                                                                                                                         |
|                     3 | padeye           |            9 |               8 |                0 |               1 |                         0 |                 286 |              4 |                     9.38 | OK                      | padeye, stick, deck, morfrac padeye, stick padeye, 20, deck padeye, ring, padeye ring, ring 20                                     | {'product': 8, 'landing': 1}                                          | {'padeye': 9}                                                                                                                                                            |
|                     1 | powerfurl        |            5 |               5 |                0 |               0 |                         0 |                   0 |              0 |                     0    | OK                      | kit, furling, furling kit, line furling, continuous, continuous line, line, swl continuous, offshore durability, handling offshore | {'product': 5}                                                        | {'powerfurl': 5}                                                                                                                                                         |
|                     5 | morfblock        |           14 |              14 |                0 |               0 |                         0 |                   0 |              0 |                     0    | PRODUCT_HEAVY_NO_PILLAR | xl, morfblock xl, xl sailing, sailing block, block, morfblock, sailing, swl, sheave, handling                                      | {'product': 14}                                                       | {'morfblock': 14}                                                                                                                                                        |
|                    10 | morfblock        |            8 |               8 |                0 |               0 |                         0 |                   0 |              0 |                     0    | PRODUCT_HEAVY_NO_PILLAR | wood, wooden sailing, wooden, morfblock wood, high load, sailing block, block, morfblock, swl wooden, sailing                      | {'product': 8}                                                        | {'morfblock': 8}                                                                                                                                                         |
|                     7 | dogbone          |            6 |               6 |                0 |               0 |                         0 |                   0 |              0 |                     0    | PRODUCT_HEAVY_NO_PILLAR | faced, flat faced, flat, dogbone flat, faced titanium, dogbone, morfrac dogbone, titanium, titanium morfrac, titanium dogbone      | {'product': 6}                                                        | {'dogbone': 6}                                                                                                                                                           |

    ---

    # Likely Cannibalization / Duplicate Intent

    | url_a                                                                                       | role_a   | label_a   |   cluster_a | url_b                                                                                        | role_b   | label_b   |   cluster_b |   similarity_score | same_family   | risk_type                |
|:--------------------------------------------------------------------------------------------|:---------|:----------|------------:|:---------------------------------------------------------------------------------------------|:---------|:----------|------------:|-------------------:|:--------------|:-------------------------|
| https://www.morfrac.com/es/shop/custom-33/morfblcok-custom-runners-12664                    | product  | morfblock |          11 | https://www.morfrac.com/es/shop/morfblock-morfblock-xl-21/morfblcok-custom-runners-12664     | product  | morfblock |          11 |                  1 | False         | possible_cannibalization |
| https://www.morfrac.com/es/shop/category/powerfurl-almacenadores-sin-fin-powerfurl-three-15 | category | powerfurl |           8 | https://www.morfrac.com/es/shop/category/powerfurl-almacenadores-sin-fin-powerfurl-twelve-16 | category | powerfurl |           8 |                  1 | False         | possible_cannibalization |
| https://www.morfrac.com/es/shop/category/powerfurl-almacenadores-sin-fin-powerfurl-ten-14   | category | powerfurl |           8 | https://www.morfrac.com/es/shop/category/powerfurl-almacenadores-sin-fin-powerfurl-twelve-16 | category | powerfurl |           8 |                  1 | False         | possible_cannibalization |
| https://www.morfrac.com/es/shop/category/powerfurl-almacenadores-sin-fin-powerfurl-ten-14   | category | powerfurl |           8 | https://www.morfrac.com/es/shop/category/powerfurl-almacenadores-sin-fin-powerfurl-three-15  | category | powerfurl |           8 |                  1 | False         | possible_cannibalization |
| https://www.morfrac.com/es/shop/category/powerfurl-almacenadores-sin-fin-powerfurl-six-13   | category | powerfurl |           8 | https://www.morfrac.com/es/shop/category/powerfurl-almacenadores-sin-fin-powerfurl-twelve-16 | category | powerfurl |           8 |                  1 | False         | possible_cannibalization |
| https://www.morfrac.com/es/shop/category/powerfurl-almacenadores-sin-fin-powerfurl-six-13   | category | powerfurl |           8 | https://www.morfrac.com/es/shop/category/powerfurl-almacenadores-sin-fin-powerfurl-three-15  | category | powerfurl |           8 |                  1 | False         | possible_cannibalization |
| https://www.morfrac.com/es/shop/category/powerfurl-almacenadores-sin-fin-powerfurl-six-13   | category | powerfurl |           8 | https://www.morfrac.com/es/shop/category/powerfurl-almacenadores-sin-fin-powerfurl-ten-14    | category | powerfurl |           8 |                  1 | False         | possible_cannibalization |
| https://www.morfrac.com/es/shop/category/powerfurl-almacenadores-sin-fin-powerfurl-one-12   | category | powerfurl |           8 | https://www.morfrac.com/es/shop/category/powerfurl-almacenadores-sin-fin-powerfurl-twelve-16 | category | powerfurl |           8 |                  1 | False         | possible_cannibalization |
| https://www.morfrac.com/es/shop/category/powerfurl-almacenadores-sin-fin-powerfurl-one-12   | category | powerfurl |           8 | https://www.morfrac.com/es/shop/category/powerfurl-almacenadores-sin-fin-powerfurl-three-15  | category | powerfurl |           8 |                  1 | False         | possible_cannibalization |
| https://www.morfrac.com/es/shop/category/powerfurl-almacenadores-sin-fin-powerfurl-one-12   | category | powerfurl |           8 | https://www.morfrac.com/es/shop/category/powerfurl-almacenadores-sin-fin-powerfurl-ten-14    | category | powerfurl |           8 |                  1 | False         | possible_cannibalization |
| https://www.morfrac.com/es/shop/category/powerfurl-almacenadores-sin-fin-powerfurl-one-12   | category | powerfurl |           8 | https://www.morfrac.com/es/shop/category/powerfurl-almacenadores-sin-fin-powerfurl-six-13    | category | powerfurl |           8 |                  1 | False         | possible_cannibalization |
| https://www.morfrac.com/shop/category/powerfurl-continuous-line-powerfurl-eight-10          | category | powerfurl |           8 | https://www.morfrac.com/es/shop/category/powerfurl-almacenadores-sin-fin-powerfurl-six-13    | category | powerfurl |           8 |                  1 | False         | possible_cannibalization |
| https://www.morfrac.com/shop/category/powerfurl-continuous-line-powerfurl-eight-10          | category | powerfurl |           8 | https://www.morfrac.com/es/shop/category/powerfurl-almacenadores-sin-fin-powerfurl-one-12    | category | powerfurl |           8 |                  1 | False         | possible_cannibalization |
| https://www.morfrac.com/shop/category/powerfurl-continuous-line-powerfurl-eight-10          | category | powerfurl |           8 | https://www.morfrac.com/es/shop/category/powerfurl-almacenadores-sin-fin-powerfurl-four-11   | category | powerfurl |           8 |                  1 | False         | possible_cannibalization |
| https://www.morfrac.com/shop/category/powerfurl-continuous-line-powerfurl-eight-10          | category | powerfurl |           8 | https://www.morfrac.com/es/shop/category/powerfurl-almacenadores-sin-fin-powerfurl-eight-10  | category | powerfurl |           8 |                  1 | False         | possible_cannibalization |
| https://www.morfrac.com/shop/category/powerfurl-continuous-line-powerfurl-eight-10          | category | powerfurl |           8 | https://www.morfrac.com/shop/category/powerfurl-continuous-line-powerfurl-twelve-16          | category | powerfurl |           8 |                  1 | False         | possible_cannibalization |
| https://www.morfrac.com/shop/category/powerfurl-continuous-line-powerfurl-eight-10          | category | powerfurl |           8 | https://www.morfrac.com/shop/category/powerfurl-continuous-line-powerfurl-three-15           | category | powerfurl |           8 |                  1 | False         | possible_cannibalization |
| https://www.morfrac.com/shop/category/powerfurl-continuous-line-powerfurl-eight-10          | category | powerfurl |           8 | https://www.morfrac.com/shop/category/powerfurl-continuous-line-powerfurl-ten-14             | category | powerfurl |           8 |                  1 | False         | possible_cannibalization |
| https://www.morfrac.com/shop/category/powerfurl-continuous-line-powerfurl-eight-10          | category | powerfurl |           8 | https://www.morfrac.com/shop/category/powerfurl-continuous-line-powerfurl-six-13             | category | powerfurl |           8 |                  1 | False         | possible_cannibalization |
| https://www.morfrac.com/shop/category/powerfurl-continuous-line-powerfurl-eight-10          | category | powerfurl |           8 | https://www.morfrac.com/shop/category/powerfurl-continuous-line-powerfurl-one-12             | category | powerfurl |           8 |                  1 | False         | possible_cannibalization |
| https://www.morfrac.com/shop/category/powerfurl-continuous-line-powerfurl-eight-10          | category | powerfurl |           8 | https://www.morfrac.com/shop/category/powerfurl-continuous-line-powerfurl-four-11            | category | powerfurl |           8 |                  1 | False         | possible_cannibalization |
| https://www.morfrac.com/shop/category/powerfurl-continuous-line-powerfurl-one-12            | category | powerfurl |           8 | https://www.morfrac.com/shop/category/powerfurl-continuous-line-powerfurl-six-13             | category | powerfurl |           8 |                  1 | False         | possible_cannibalization |
| https://www.morfrac.com/shop/category/powerfurl-continuous-line-powerfurl-four-11           | category | powerfurl |           8 | https://www.morfrac.com/es/shop/category/powerfurl-almacenadores-sin-fin-powerfurl-twelve-16 | category | powerfurl |           8 |                  1 | False         | possible_cannibalization |
| https://www.morfrac.com/shop/category/powerfurl-continuous-line-powerfurl-four-11           | category | powerfurl |           8 | https://www.morfrac.com/es/shop/category/powerfurl-almacenadores-sin-fin-powerfurl-three-15  | category | powerfurl |           8 |                  1 | False         | possible_cannibalization |
| https://www.morfrac.com/shop/category/powerfurl-continuous-line-powerfurl-four-11           | category | powerfurl |           8 | https://www.morfrac.com/es/shop/category/powerfurl-almacenadores-sin-fin-powerfurl-ten-14    | category | powerfurl |           8 |                  1 | False         | possible_cannibalization |
| https://www.morfrac.com/shop/category/powerfurl-continuous-line-powerfurl-four-11           | category | powerfurl |           8 | https://www.morfrac.com/es/shop/category/powerfurl-almacenadores-sin-fin-powerfurl-six-13    | category | powerfurl |           8 |                  1 | False         | possible_cannibalization |
| https://www.morfrac.com/shop/category/powerfurl-continuous-line-powerfurl-four-11           | category | powerfurl |           8 | https://www.morfrac.com/es/shop/category/powerfurl-almacenadores-sin-fin-powerfurl-one-12    | category | powerfurl |           8 |                  1 | False         | possible_cannibalization |
| https://www.morfrac.com/shop/category/powerfurl-continuous-line-powerfurl-four-11           | category | powerfurl |           8 | https://www.morfrac.com/es/shop/category/powerfurl-almacenadores-sin-fin-powerfurl-four-11   | category | powerfurl |           8 |                  1 | False         | possible_cannibalization |
| https://www.morfrac.com/shop/category/powerfurl-continuous-line-powerfurl-four-11           | category | powerfurl |           8 | https://www.morfrac.com/es/shop/category/powerfurl-almacenadores-sin-fin-powerfurl-eight-10  | category | powerfurl |           8 |                  1 | False         | possible_cannibalization |
| https://www.morfrac.com/shop/category/powerfurl-continuous-line-powerfurl-four-11           | category | powerfurl |           8 | https://www.morfrac.com/shop/category/powerfurl-continuous-line-powerfurl-twelve-16          | category | powerfurl |           8 |                  1 | False         | possible_cannibalization |

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

    - Cluster summary: `C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC\06_MARKETING\SEO_Agent\Semantic_Clusters\2026-08-17_semantic_clusters.csv`
    - Page cluster mapping: `C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC\06_MARKETING\SEO_Agent\Semantic_Clusters\2026-08-17_semantic_cluster_pages.csv`
    - Similarity pairs: `C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC\06_MARKETING\SEO_Agent\Semantic_Clusters\2026-08-17_semantic_similarity_pairs.csv`
    - Cannibalization: `C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC\06_MARKETING\SEO_Agent\Semantic_Clusters\2026-08-17_semantic_cannibalization.csv`
    - Orphan topics: `C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC\06_MARKETING\SEO_Agent\Semantic_Clusters\2026-08-17_semantic_orphan_topics.csv`

## Related Links

### Concepts
- [[FRAGMENTED_TOPIC]]
- [[PRODUCT_HEAVY_NO_PILLAR]]
- [[ORPHAN_TOPIC]]
- [[CONTENT_WITHOUT_COMMERCIAL_TARGET]]

### Projects
- [[Search Console]]
