---
type: seo_semantic_cluster_report
source_agent: SEO_Agent
created: 2026-08-10
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

    2026-08-10

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

    - Crawl file: `C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC\06_MARKETING\SEO_Agent\Crawls\2026-08-10_site_crawl.csv`
    - Search Console merge file: `C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC\06_MARKETING\SEO_Agent\Merged_Analysis\2026-08-10_search_console_merge.csv`

    ---

    # Summary

    - Pages analyzed: 258
    - Semantic clusters: 12
    - Similar page pairs above threshold: 270
    - Cannibalization/topic-overlap pairs: 259
    - Orphan topic clusters: 0

    Similarity threshold:

    `0.68`

    ---

    # Cluster Summary

    |   semantic_cluster_id | dominant_label   |   page_count |   product_pages |   category_pages |   landing_pages |   authority_content_pages |   total_impressions |   total_clicks |   avg_seo_priority_score | cluster_health          | top_terms                                                                                                                          | role_counts                                                           | label_counts                                                                                                                                           |
|----------------------:|:-----------------|-------------:|----------------:|-----------------:|----------------:|--------------------------:|--------------------:|---------------:|-------------------------:|:------------------------|:-----------------------------------------------------------------------------------------------------------------------------------|:----------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------|
|                     8 | other            |           43 |              11 |                0 |               3 |                        18 |                   0 |              0 |                     0    | FRAGMENTED_TOPIC        | custom, morfrac, morfwing, new, car, 2024, morfblock, high performance, hardware, sail                                             | {'authority_content': 18, 'general': 11, 'product': 11, 'landing': 3} | {'other': 15, 'powerfurl': 6, 'custom_engineering': 5, 'morfblock': 5, 'morfwing': 5, 'mloop': 4, 'dogbone': 2, 'hoistlock': 1}                        |
|                     4 | powerfurl        |           39 |               0 |               39 |               0 |                         0 |                   0 |              0 |                     0    | FRAGMENTED_TOPIC        | shop, morfrac shop, shop morfrac, powerfurl, morfrac, shop powerfurl, powerfurl morfrac, tdi, shop morfblock, morfblock            | {'category': 39}                                                      | {'powerfurl': 16, 'other': 9, 'morfblock': 4, 'dogbone': 3, 'shackle': 2, 'custom_engineering': 1, 'mloop': 1, 'morfring': 1, 'mreel': 1, 'padeye': 1} |
|                     0 | morfblock        |           38 |              38 |                0 |               0 |                         0 |                   0 |              0 |                     0    | FRAGMENTED_TOPIC        | morfblock light, light, sailing block, block, morfblock, sailing, swl, lightweight sailing, high, lightweight                      | {'product': 38}                                                       | {'morfblock': 38}                                                                                                                                      |
|                     6 | dogbone          |           31 |              30 |                0 |               1 |                         0 |                 347 |              4 |                     2.76 | FRAGMENTED_TOPIC        | dogbone, morfrac dogbone, length, aluminium, morfrac, total length, total, length morfrac, titanium, flat                          | {'product': 30, 'landing': 1}                                         | {'dogbone': 31}                                                                                                                                        |
|                     1 | powerfurl        |           27 |              27 |                0 |               0 |                         0 |                   0 |              0 |                     0    | FRAGMENTED_TOPIC        | powerfurl, kit, furling, 5t, 5t swl, swl, furling kit, morfrac powerfurl, swl morfrac, reliable                                    | {'product': 27}                                                       | {'powerfurl': 24, 'shackle': 3}                                                                                                                        |
|                     5 | morfring         |           22 |              20 |                0 |               2 |                         0 |                 274 |              3 |                     3.77 | FRAGMENTED_TOPIC        | padeye, ring, friction, friction ring, morfring, aluminium friction, ptfe, aluminium, stick, deck                                  | {'product': 20, 'landing': 2}                                         | {'morfring': 13, 'padeye': 9}                                                                                                                          |
|                    10 | shackle          |            9 |               8 |                0 |               1 |                         0 |                   0 |              0 |                     0    | OK                      | shackle, ti shackle, ti, titanium shackle, titanium, machined, cnc machined, cnc, ultra, grade                                     | {'product': 8, 'landing': 1}                                          | {'shackle': 9}                                                                                                                                         |
|                     2 | morfblock        |            8 |               6 |                2 |               0 |                         0 |                   0 |              0 |                     0    | OK                      | morfblock max, max, morfblock, sailing, efficiency, sailing block, maximum reliability, block, efficiency sailing, max lightweight | {'product': 6, 'category': 2}                                         | {'morfblock': 8}                                                                                                                                       |
|                     3 | morfblock        |            7 |               3 |                1 |               0 |                         3 |                   0 |              0 |                     0    | OK                      | snatch, morfblock snatch, custom, morfblock, morfring snatch, morfrac custom, cunningham, cunningham furler, solutions, precision  | {'authority_content': 3, 'product': 3, 'category': 1}                 | {'morfblock': 4, 'powerfurl': 1, 'custom_engineering': 1, 'morfring': 1}                                                                               |
|                     9 | mreel            |            5 |               4 |                0 |               0 |                         0 |                 117 |             16 |                     5.98 | OK                      | mreel, reeler, rope reeler, mreel rope, rope, morfrac mreel, reeler morfrac, safer, manoeuvres, sheets halyards                    | {'product': 4, 'general': 1}                                          | {'mreel': 4, 'powerfurl': 1}                                                                                                                           |
|                     7 | powerfurl        |           15 |              15 |                0 |               0 |                         0 |                   0 |              0 |                     0    | PRODUCT_HEAVY_NO_PILLAR | powerfurl, unit, furling, drum, 10t swl, 10t, swl, powerfurl drum, furling unit, unit powerfurl                                    | {'product': 15}                                                       | {'powerfurl': 15}                                                                                                                                      |
|                    11 | morfblock        |           14 |              14 |                0 |               0 |                         0 |                   0 |              0 |                     0    | PRODUCT_HEAVY_NO_PILLAR | xl, morfblock xl, xl sailing, sailing block, block, morfblock, sailing, swl, sheave, handling                                      | {'product': 14}                                                       | {'morfblock': 14}                                                                                                                                      |

    ---

    # Likely Cannibalization / Duplicate Intent

    | url_a                                                                                       | role_a   | label_a   |   cluster_a | url_b                                                                                        | role_b   | label_b   |   cluster_b |   similarity_score | same_family   | risk_type                |
|:--------------------------------------------------------------------------------------------|:---------|:----------|------------:|:---------------------------------------------------------------------------------------------|:---------|:----------|------------:|-------------------:|:--------------|:-------------------------|
| https://www.morfrac.com/es/shop/category/powerfurl-almacenadores-sin-fin-powerfurl-six-13   | category | powerfurl |           4 | https://www.morfrac.com/es/shop/category/powerfurl-almacenadores-sin-fin-powerfurl-ten-14    | category | powerfurl |           4 |                  1 | False         | possible_cannibalization |
| https://www.morfrac.com/es/shop/category/powerfurl-almacenadores-sin-fin-powerfurl-one-12   | category | powerfurl |           4 | https://www.morfrac.com/es/shop/category/powerfurl-almacenadores-sin-fin-powerfurl-twelve-16 | category | powerfurl |           4 |                  1 | False         | possible_cannibalization |
| https://www.morfrac.com/es/shop/category/powerfurl-almacenadores-sin-fin-powerfurl-one-12   | category | powerfurl |           4 | https://www.morfrac.com/es/shop/category/powerfurl-almacenadores-sin-fin-powerfurl-three-15  | category | powerfurl |           4 |                  1 | False         | possible_cannibalization |
| https://www.morfrac.com/es/shop/category/powerfurl-almacenadores-sin-fin-powerfurl-one-12   | category | powerfurl |           4 | https://www.morfrac.com/es/shop/category/powerfurl-almacenadores-sin-fin-powerfurl-ten-14    | category | powerfurl |           4 |                  1 | False         | possible_cannibalization |
| https://www.morfrac.com/es/shop/category/powerfurl-almacenadores-sin-fin-powerfurl-one-12   | category | powerfurl |           4 | https://www.morfrac.com/es/shop/category/powerfurl-almacenadores-sin-fin-powerfurl-six-13    | category | powerfurl |           4 |                  1 | False         | possible_cannibalization |
| https://www.morfrac.com/es/shop/category/powerfurl-almacenadores-sin-fin-powerfurl-four-11  | category | powerfurl |           4 | https://www.morfrac.com/es/shop/category/powerfurl-almacenadores-sin-fin-powerfurl-twelve-16 | category | powerfurl |           4 |                  1 | False         | possible_cannibalization |
| https://www.morfrac.com/es/shop/category/powerfurl-almacenadores-sin-fin-powerfurl-four-11  | category | powerfurl |           4 | https://www.morfrac.com/es/shop/category/powerfurl-almacenadores-sin-fin-powerfurl-three-15  | category | powerfurl |           4 |                  1 | False         | possible_cannibalization |
| https://www.morfrac.com/es/shop/category/powerfurl-almacenadores-sin-fin-powerfurl-four-11  | category | powerfurl |           4 | https://www.morfrac.com/es/shop/category/powerfurl-almacenadores-sin-fin-powerfurl-ten-14    | category | powerfurl |           4 |                  1 | False         | possible_cannibalization |
| https://www.morfrac.com/es/shop/category/powerfurl-almacenadores-sin-fin-powerfurl-four-11  | category | powerfurl |           4 | https://www.morfrac.com/es/shop/category/powerfurl-almacenadores-sin-fin-powerfurl-six-13    | category | powerfurl |           4 |                  1 | False         | possible_cannibalization |
| https://www.morfrac.com/es/shop/category/powerfurl-almacenadores-sin-fin-powerfurl-four-11  | category | powerfurl |           4 | https://www.morfrac.com/es/shop/category/powerfurl-almacenadores-sin-fin-powerfurl-one-12    | category | powerfurl |           4 |                  1 | False         | possible_cannibalization |
| https://www.morfrac.com/es/shop/category/powerfurl-almacenadores-sin-fin-powerfurl-eight-10 | category | powerfurl |           4 | https://www.morfrac.com/es/shop/category/powerfurl-almacenadores-sin-fin-powerfurl-twelve-16 | category | powerfurl |           4 |                  1 | False         | possible_cannibalization |
| https://www.morfrac.com/es/shop/category/powerfurl-almacenadores-sin-fin-powerfurl-eight-10 | category | powerfurl |           4 | https://www.morfrac.com/es/shop/category/powerfurl-almacenadores-sin-fin-powerfurl-three-15  | category | powerfurl |           4 |                  1 | False         | possible_cannibalization |
| https://www.morfrac.com/es/shop/category/powerfurl-almacenadores-sin-fin-powerfurl-eight-10 | category | powerfurl |           4 | https://www.morfrac.com/es/shop/category/powerfurl-almacenadores-sin-fin-powerfurl-ten-14    | category | powerfurl |           4 |                  1 | False         | possible_cannibalization |
| https://www.morfrac.com/es/shop/category/powerfurl-almacenadores-sin-fin-powerfurl-eight-10 | category | powerfurl |           4 | https://www.morfrac.com/es/shop/category/powerfurl-almacenadores-sin-fin-powerfurl-six-13    | category | powerfurl |           4 |                  1 | False         | possible_cannibalization |
| https://www.morfrac.com/es/shop/category/powerfurl-almacenadores-sin-fin-powerfurl-eight-10 | category | powerfurl |           4 | https://www.morfrac.com/es/shop/category/powerfurl-almacenadores-sin-fin-powerfurl-one-12    | category | powerfurl |           4 |                  1 | False         | possible_cannibalization |
| https://www.morfrac.com/es/shop/category/powerfurl-almacenadores-sin-fin-powerfurl-eight-10 | category | powerfurl |           4 | https://www.morfrac.com/es/shop/category/powerfurl-almacenadores-sin-fin-powerfurl-four-11   | category | powerfurl |           4 |                  1 | False         | possible_cannibalization |
| https://www.morfrac.com/shop/category/powerfurl-continuous-line-powerfurl-eight-10          | category | powerfurl |           4 | https://www.morfrac.com/es/shop/category/powerfurl-almacenadores-sin-fin-powerfurl-six-13    | category | powerfurl |           4 |                  1 | False         | possible_cannibalization |
| https://www.morfrac.com/shop/category/powerfurl-continuous-line-powerfurl-eight-10          | category | powerfurl |           4 | https://www.morfrac.com/es/shop/category/powerfurl-almacenadores-sin-fin-powerfurl-one-12    | category | powerfurl |           4 |                  1 | False         | possible_cannibalization |
| https://www.morfrac.com/shop/category/powerfurl-continuous-line-powerfurl-eight-10          | category | powerfurl |           4 | https://www.morfrac.com/es/shop/category/powerfurl-almacenadores-sin-fin-powerfurl-four-11   | category | powerfurl |           4 |                  1 | False         | possible_cannibalization |
| https://www.morfrac.com/shop/category/powerfurl-continuous-line-powerfurl-eight-10          | category | powerfurl |           4 | https://www.morfrac.com/es/shop/category/powerfurl-almacenadores-sin-fin-powerfurl-eight-10  | category | powerfurl |           4 |                  1 | False         | possible_cannibalization |
| https://www.morfrac.com/shop/category/powerfurl-continuous-line-powerfurl-eight-10          | category | powerfurl |           4 | https://www.morfrac.com/shop/category/powerfurl-continuous-line-powerfurl-twelve-16          | category | powerfurl |           4 |                  1 | False         | possible_cannibalization |
| https://www.morfrac.com/shop/category/powerfurl-continuous-line-powerfurl-eight-10          | category | powerfurl |           4 | https://www.morfrac.com/shop/category/powerfurl-continuous-line-powerfurl-three-15           | category | powerfurl |           4 |                  1 | False         | possible_cannibalization |
| https://www.morfrac.com/shop/category/powerfurl-continuous-line-powerfurl-eight-10          | category | powerfurl |           4 | https://www.morfrac.com/shop/category/powerfurl-continuous-line-powerfurl-ten-14             | category | powerfurl |           4 |                  1 | False         | possible_cannibalization |
| https://www.morfrac.com/shop/category/powerfurl-continuous-line-powerfurl-eight-10          | category | powerfurl |           4 | https://www.morfrac.com/shop/category/powerfurl-continuous-line-powerfurl-six-13             | category | powerfurl |           4 |                  1 | False         | possible_cannibalization |
| https://www.morfrac.com/shop/category/powerfurl-continuous-line-powerfurl-eight-10          | category | powerfurl |           4 | https://www.morfrac.com/shop/category/powerfurl-continuous-line-powerfurl-one-12             | category | powerfurl |           4 |                  1 | False         | possible_cannibalization |
| https://www.morfrac.com/shop/category/powerfurl-continuous-line-powerfurl-eight-10          | category | powerfurl |           4 | https://www.morfrac.com/shop/category/powerfurl-continuous-line-powerfurl-four-11            | category | powerfurl |           4 |                  1 | False         | possible_cannibalization |
| https://www.morfrac.com/shop/category/powerfurl-continuous-line-powerfurl-one-12            | category | powerfurl |           4 | https://www.morfrac.com/shop/category/powerfurl-continuous-line-powerfurl-six-13             | category | powerfurl |           4 |                  1 | False         | possible_cannibalization |
| https://www.morfrac.com/shop/category/powerfurl-continuous-line-powerfurl-four-11           | category | powerfurl |           4 | https://www.morfrac.com/es/shop/category/powerfurl-almacenadores-sin-fin-powerfurl-twelve-16 | category | powerfurl |           4 |                  1 | False         | possible_cannibalization |
| https://www.morfrac.com/shop/category/powerfurl-continuous-line-powerfurl-four-11           | category | powerfurl |           4 | https://www.morfrac.com/es/shop/category/powerfurl-almacenadores-sin-fin-powerfurl-three-15  | category | powerfurl |           4 |                  1 | False         | possible_cannibalization |
| https://www.morfrac.com/shop/category/powerfurl-continuous-line-powerfurl-four-11           | category | powerfurl |           4 | https://www.morfrac.com/es/shop/category/powerfurl-almacenadores-sin-fin-powerfurl-ten-14    | category | powerfurl |           4 |                  1 | False         | possible_cannibalization |

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

    - Cluster summary: `C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC\06_MARKETING\SEO_Agent\Semantic_Clusters\2026-08-10_semantic_clusters.csv`
    - Page cluster mapping: `C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC\06_MARKETING\SEO_Agent\Semantic_Clusters\2026-08-10_semantic_cluster_pages.csv`
    - Similarity pairs: `C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC\06_MARKETING\SEO_Agent\Semantic_Clusters\2026-08-10_semantic_similarity_pairs.csv`
    - Cannibalization: `C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC\06_MARKETING\SEO_Agent\Semantic_Clusters\2026-08-10_semantic_cannibalization.csv`
    - Orphan topics: `C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC\06_MARKETING\SEO_Agent\Semantic_Clusters\2026-08-10_semantic_orphan_topics.csv`

## Related Links

### Concepts
- [[FRAGMENTED_TOPIC]]
- [[PRODUCT_HEAVY_NO_PILLAR]]
- [[ORPHAN_TOPIC]]
- [[CONTENT_WITHOUT_COMMERCIAL_TARGET]]

### Projects
- [[Search Console]]
