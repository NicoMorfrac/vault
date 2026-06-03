# SEO Indexation Audit

## Generated

2026-05-14

## Purpose

This report identifies likely indexation inefficiencies and crawl waste.

It detects:

- likely low-value indexable URLs
- canonical inconsistencies
- pagination indexation
- document URL indexation
- multilingual duplicate candidates
- category/product overlap
- missing canonical signals

---

# Input Crawl

C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC\06_MARKETING\SEO_Agent\Crawls\2026-05-14_site_crawl.csv

---

# Risk Summary

| priority   |   affected_urls |
|:-----------|----------------:|
| CRITICAL   |             339 |
| MEDIUM     |             114 |
| HIGH       |              47 |

---

# Highest Priority Indexation Risks

| priority   | url                                                                                         | page_type      | business_priority   | indexable   |   status_code | canonical                                                                                   | robots                             | indexation_risks                                                                 |
|:-----------|:--------------------------------------------------------------------------------------------|:---------------|:--------------------|:------------|--------------:|:--------------------------------------------------------------------------------------------|:-----------------------------------|:---------------------------------------------------------------------------------|
| CRITICAL   | https://www.morfrac.com/document/share/12/d301f2c6-5349-4ff4-b4b7-25a78f83e1e7              | general        | medium              | True        |           200 | nan                                                                                         | nan                                | document_indexation; likely_low_value_indexable; missing_canonical               |
| CRITICAL   | https://www.morfrac.com/document/share/13/2b506fa7-1216-484f-900f-d0fe8d85ffdd              | general        | medium              | True        |           200 | nan                                                                                         | nan                                | document_indexation; likely_low_value_indexable; missing_canonical               |
| CRITICAL   | https://www.morfrac.com/es/blog/stories-4                                                   | technical_blog | medium              | True        |           200 | https://www.morfrac.com/es/blog/historias-4                                                 | nan                                | canonical_mismatch; multilingual_duplicate_candidate                             |
| CRITICAL   | https://www.morfrac.com/documents/content/DJfhNPEwQOWKgG4br81f3Qo24                         | general        | medium              | True        |           200 | nan                                                                                         | nan                                | document_indexation; missing_canonical                                           |
| CRITICAL   | https://www.morfrac.com/documents/content/PlGfSxqcRQqanrFuPh90wwo26                         | general        | medium              | True        |           200 | nan                                                                                         | nan                                | document_indexation; missing_canonical                                           |
| CRITICAL   | https://www.morfrac.com/website/social/instagram                                            | system         | ignore              | True        |           200 | https://www.instagram.com/morfracsystems/                                                   | noarchive, noimageindex            | canonical_mismatch; likely_low_value_indexable                                   |
| CRITICAL   | https://www.morfrac.com/website/social/linkedin                                             | system         | ignore              | True        |           200 | https://es.linkedin.com/company/morfrac                                                     | max-image-preview:large, noarchive | canonical_mismatch; likely_low_value_indexable                                   |
| CRITICAL   | https://www.morfrac.com/es/website/social/instagram                                         | system         | ignore              | True        |           200 | https://www.instagram.com/morfracsystems/                                                   | noarchive, noimageindex            | canonical_mismatch; likely_low_value_indexable; multilingual_duplicate_candidate |
| CRITICAL   | https://www.morfrac.com/es/website/social/linkedin                                          | system         | ignore              | True        |           200 | https://es.linkedin.com/company/morfrac                                                     | max-image-preview:large, noarchive | canonical_mismatch; likely_low_value_indexable; multilingual_duplicate_candidate |
| CRITICAL   | https://www.morfrac.com/shop/dogbone60-23-12467                                             | product        | high                | True        |           200 | https://www.morfrac.com/shop/dogbone-60-23-aluminium-12467                                  | nan                                | canonical_mismatch                                                               |
| CRITICAL   | https://www.morfrac.com/es/shop/dogbone60-23-12467                                          | product        | high                | True        |           200 | https://www.morfrac.com/es/shop/dogbone-60-23-aluminium-12467                               | nan                                | canonical_mismatch; multilingual_duplicate_candidate                             |
| CRITICAL   | https://www.morfrac.com/shop/morfblock-light-4-p-12338                                      | product        | high                | True        |           200 | https://www.morfrac.com/shop/morfblock-light-04-performance-sailing-block-12338             | nan                                | canonical_mismatch                                                               |
| CRITICAL   | https://www.morfrac.com/es/shop/category/mloop-34                                           | product        | high                | True        |           200 | https://www.morfrac.com/es/shop/category/mloop-34                                           | nan                                | category_product_overlap; multilingual_duplicate_candidate; self_canonical       |
| CRITICAL   | https://www.morfrac.com/es/shop/category/morfblock-17                                       | product        | high                | True        |           200 | https://www.morfrac.com/es/shop/category/morfblock-17                                       | nan                                | category_product_overlap; multilingual_duplicate_candidate; self_canonical       |
| CRITICAL   | https://www.morfrac.com/shop/category/powerfurl-1                                           | product        | high                | True        |           200 | https://www.morfrac.com/shop/category/powerfurl-1                                           | nan                                | category_product_overlap; self_canonical                                         |
| CRITICAL   | https://www.morfrac.com/shop/category/dogbone-25                                            | product        | high                | True        |           200 | https://www.morfrac.com/shop/category/dogbone-25                                            | nan                                | category_product_overlap; self_canonical                                         |
| CRITICAL   | https://www.morfrac.com/shop/category/mloop-34                                              | product        | high                | True        |           200 | https://www.morfrac.com/shop/category/mloop-34                                              | nan                                | category_product_overlap; self_canonical                                         |
| CRITICAL   | https://www.morfrac.com/shop/category/morfblock-17                                          | product        | high                | True        |           200 | https://www.morfrac.com/shop/category/morfblock-17                                          | nan                                | category_product_overlap; self_canonical                                         |
| CRITICAL   | https://www.morfrac.com/shop/category/morfring-26                                           | product        | high                | True        |           200 | https://www.morfrac.com/shop/category/morfring-26                                           | nan                                | category_product_overlap; self_canonical                                         |
| CRITICAL   | https://www.morfrac.com/shop/category/padeye-27                                             | product        | high                | True        |           200 | https://www.morfrac.com/shop/category/padeye-27                                             | nan                                | category_product_overlap; self_canonical                                         |
| CRITICAL   | https://www.morfrac.com/shop/category/shackle-24                                            | product        | high                | True        |           200 | https://www.morfrac.com/shop/category/ti-shackle-24                                         | nan                                | canonical_mismatch; category_product_overlap                                     |
| CRITICAL   | https://www.morfrac.com/es/shop/category/dogbone-25                                         | product        | high                | True        |           200 | https://www.morfrac.com/es/shop/category/dogbone-25                                         | nan                                | category_product_overlap; multilingual_duplicate_candidate; self_canonical       |
| CRITICAL   | https://www.morfrac.com/es/shop/category/morfring-26                                        | product        | high                | True        |           200 | https://www.morfrac.com/es/shop/category/morfring-26                                        | nan                                | category_product_overlap; multilingual_duplicate_candidate; self_canonical       |
| CRITICAL   | https://www.morfrac.com/es/shop/category/padeye-27                                          | product        | high                | True        |           200 | https://www.morfrac.com/es/shop/category/padeye-27                                          | nan                                | category_product_overlap; multilingual_duplicate_candidate; self_canonical       |
| CRITICAL   | https://www.morfrac.com/es/shop/category/powerfurl-1                                        | product        | high                | True        |           200 | https://www.morfrac.com/es/shop/category/powerfurl-1                                        | nan                                | category_product_overlap; multilingual_duplicate_candidate; self_canonical       |
| CRITICAL   | https://www.morfrac.com/es/shop/category/shackle-24                                         | product        | high                | True        |           200 | https://www.morfrac.com/es/shop/category/ti-shackle-24                                      | nan                                | canonical_mismatch; category_product_overlap; multilingual_duplicate_candidate   |
| CRITICAL   | https://www.morfrac.com/es/shop/category/outlet-36                                          | product        | high                | True        |           200 | https://www.morfrac.com/es/shop/category/outlet-36                                          | nan                                | category_product_overlap; multilingual_duplicate_candidate; self_canonical       |
| CRITICAL   | https://www.morfrac.com/shop/category/outlet-36                                             | product        | high                | True        |           200 | https://www.morfrac.com/shop/category/outlet-36                                             | nan                                | category_product_overlap; self_canonical                                         |
| CRITICAL   | https://www.morfrac.com/es/shop/category/custom-33                                          | product        | high                | True        |           200 | https://www.morfrac.com/es/shop/category/custom-33                                          | nan                                | category_product_overlap; multilingual_duplicate_candidate; self_canonical       |
| CRITICAL   | https://www.morfrac.com/es/shop/category/dogbone-dogbone-al-28                              | product        | high                | True        |           200 | https://www.morfrac.com/es/shop/category/dogbone-dogbone-al-28                              | nan                                | category_product_overlap; multilingual_duplicate_candidate; self_canonical       |
| CRITICAL   | https://www.morfrac.com/es/shop/category/dogbone-dogbone-ti-29                              | product        | high                | True        |           200 | https://www.morfrac.com/es/shop/category/dogbone-dogbone-ti-29                              | nan                                | category_product_overlap; multilingual_duplicate_candidate; self_canonical       |
| CRITICAL   | https://www.morfrac.com/es/shop/category/mainsail-systems-39                                | product        | high                | True        |           200 | https://www.morfrac.com/es/shop/category/mainsail-systems-39                                | nan                                | category_product_overlap; multilingual_duplicate_candidate; self_canonical       |
| CRITICAL   | https://www.morfrac.com/es/shop/category/morfblock-morfblocklight-18                        | product        | high                | True        |           200 | https://www.morfrac.com/es/shop/category/morfblock-morfblocklight-18                        | nan                                | category_product_overlap; multilingual_duplicate_candidate; self_canonical       |
| CRITICAL   | https://www.morfrac.com/es/shop/category/morfblock-morfblockmax-38                          | product        | high                | True        |           200 | https://www.morfrac.com/es/shop/category/morfblock-morfblockmax-38                          | nan                                | category_product_overlap; multilingual_duplicate_candidate; self_canonical       |
| CRITICAL   | https://www.morfrac.com/es/shop/category/morfblock-morfblocksnatch-19                       | product        | high                | True        |           200 | https://www.morfrac.com/es/shop/category/morfblock-morfblocksnatch-19                       | nan                                | category_product_overlap; multilingual_duplicate_candidate; self_canonical       |
| CRITICAL   | https://www.morfrac.com/es/shop/category/morfblock-morfblockwood-20                         | product        | high                | True        |           200 | https://www.morfrac.com/es/shop/category/morfblock-morfblockwood-20                         | nan                                | category_product_overlap; multilingual_duplicate_candidate; self_canonical       |
| CRITICAL   | https://www.morfrac.com/es/shop/category/morfblock-morfblockxl-21                           | product        | high                | True        |           200 | https://www.morfrac.com/es/shop/category/morfblock-morfblockxl-21                           | nan                                | category_product_overlap; multilingual_duplicate_candidate; self_canonical       |
| CRITICAL   | https://www.morfrac.com/es/shop/category/mreel-35                                           | product        | high                | True        |           200 | https://www.morfrac.com/es/shop/category/mreel-35                                           | nan                                | category_product_overlap; multilingual_duplicate_candidate; self_canonical       |
| CRITICAL   | https://www.morfrac.com/es/shop/category/powerfurl-almacenadores-sin-fin-31                 | product        | high                | True        |           200 | https://www.morfrac.com/es/shop/category/powerfurl-almacenadores-sin-fin-31                 | nan                                | category_product_overlap; multilingual_duplicate_candidate; self_canonical       |
| CRITICAL   | https://www.morfrac.com/es/shop/category/powerfurl-almacenadores-sin-fin-powerfurleight-10  | product        | high                | True        |           200 | https://www.morfrac.com/es/shop/category/powerfurl-almacenadores-sin-fin-powerfurleight-10  | nan                                | category_product_overlap; multilingual_duplicate_candidate; self_canonical       |
| CRITICAL   | https://www.morfrac.com/es/shop/category/powerfurl-almacenadores-sin-fin-powerfurlfour-11   | product        | high                | True        |           200 | https://www.morfrac.com/es/shop/category/powerfurl-almacenadores-sin-fin-powerfurlfour-11   | nan                                | category_product_overlap; multilingual_duplicate_candidate; self_canonical       |
| CRITICAL   | https://www.morfrac.com/es/shop/category/powerfurl-almacenadores-sin-fin-powerfurlone-12    | product        | high                | True        |           200 | https://www.morfrac.com/es/shop/category/powerfurl-almacenadores-sin-fin-powerfurlone-12    | nan                                | category_product_overlap; multilingual_duplicate_candidate; self_canonical       |
| CRITICAL   | https://www.morfrac.com/es/shop/category/powerfurl-almacenadores-sin-fin-powerfurlsix-13    | product        | high                | True        |           200 | https://www.morfrac.com/es/shop/category/powerfurl-almacenadores-sin-fin-powerfurlsix-13    | nan                                | category_product_overlap; multilingual_duplicate_candidate; self_canonical       |
| CRITICAL   | https://www.morfrac.com/es/shop/category/powerfurl-almacenadores-sin-fin-powerfurlten-14    | product        | high                | True        |           200 | https://www.morfrac.com/es/shop/category/powerfurl-almacenadores-sin-fin-powerfurlten-14    | nan                                | category_product_overlap; multilingual_duplicate_candidate; self_canonical       |
| CRITICAL   | https://www.morfrac.com/es/shop/category/powerfurl-almacenadores-sin-fin-powerfurlthree-15  | product        | high                | True        |           200 | https://www.morfrac.com/es/shop/category/powerfurl-almacenadores-sin-fin-powerfurlthree-15  | nan                                | category_product_overlap; multilingual_duplicate_candidate; self_canonical       |
| CRITICAL   | https://www.morfrac.com/es/shop/category/powerfurl-almacenadores-sin-fin-powerfurltwelve-16 | product        | high                | True        |           200 | https://www.morfrac.com/es/shop/category/powerfurl-almacenadores-sin-fin-powerfurltwelve-16 | nan                                | category_product_overlap; multilingual_duplicate_candidate; self_canonical       |
| CRITICAL   | https://www.morfrac.com/es/shop/category/powerfurl-almacenadores-tambor-30                  | product        | high                | True        |           200 | https://www.morfrac.com/es/shop/category/powerfurl-almacenadores-tambor-30                  | nan                                | category_product_overlap; multilingual_duplicate_candidate; self_canonical       |
| CRITICAL   | https://www.morfrac.com/es/shop/category/powerfurl-tdi-22                                   | product        | high                | True        |           200 | https://www.morfrac.com/es/shop/category/powerfurl-tdi-22                                   | nan                                | category_product_overlap; multilingual_duplicate_candidate; self_canonical       |
| CRITICAL   | https://www.morfrac.com/es/shop/category/powerfurl-tdis-23                                  | product        | high                | True        |           200 | https://www.morfrac.com/es/shop/category/powerfurl-tdis-23                                  | nan                                | category_product_overlap; multilingual_duplicate_candidate; self_canonical       |
| CRITICAL   | https://www.morfrac.com/es/shop/category/powerfurl-underdeck-32                             | product        | high                | True        |           200 | https://www.morfrac.com/es/shop/category/powerfurl-underdeck-32                             | nan                                | category_product_overlap; multilingual_duplicate_candidate; self_canonical       |

---

# Interpretation Notes

This report does not automatically mean URLs should be deindexed.

Priority should focus on URLs that:

- dilute authority
- compete with stronger canonical targets
- create crawl waste
- expose duplicate paths
- reduce query clarity
- create unnecessary index bloat

Common Odoo SEO risks include:

- category/product duplicate routing
- paginated archives
- tag archives
- document share URLs
- duplicated multilingual structures
- weak canonical consistency

---

# Output Files

- CSV: C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC\06_MARKETING\SEO_Agent\Indexation_Audit\2026-05-14_indexation_audit.csv
- Markdown: C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC\06_MARKETING\SEO_Agent\Indexation_Audit\2026-05-14_indexation_audit.md
