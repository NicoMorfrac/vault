---
type: seo_entity_relationship_report
source_agent: SEO_Agent
created: 2026-10-05
related_findings: []
related_concepts:
  - COMMERCIAL_ENTITY_NEEDS_AUTHORITY_CONTENT
  - VERY_WEAK
  - HIGH_COMMERCIAL_LOW_AUTHORITY
  - COMMERCIAL_ENTITY_NEEDS_PILLAR_PAGE
  - ENTITY_HAS_CONTENT_GAP
  - SEARCH_VISIBLE_COMMERCIAL_ENTITY
  - ENTITY_RULES
related_projects: []
related_reports: []
---

# MORFRAC SEO Entity Relationship Map

## Generated

2026-10-05

---

# Purpose

This report creates a deterministic entity relationship layer for MORFRAC SEO intelligence.

It maps:

- product families
- applications
- materials
- engineering concepts
- search/content intent
- page-to-page relationships
- entity-to-entity relationships
- entity-level content and authority opportunities

This is the foundation for future SEO knowledge graph, content brief generation, competitor comparison, and AI-assisted planning.

---

# Source Files

- Crawl file: `C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC\06_MARKETING\SEO_Agent\Crawls\2026-10-05_site_crawl.csv`
- Semantic pages: `C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC\06_MARKETING\SEO_Agent\Semantic_Clusters\2026-10-05_semantic_cluster_pages.csv`
- Content gaps: `C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC\06_MARKETING\SEO_Agent\Content_Gap_Analysis\2026-10-05_content_gap_analysis.csv`
- Topic authority map: `C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC\06_MARKETING\SEO_Agent\Topic_Authority_Map\2026-10-05_topic_authority_map.csv`
- Contextual link recommendations loaded for future expansion: `C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC\06_MARKETING\SEO_Agent\Contextual_Links\2026-10-05_contextual_link_recommendations_filtered.csv`

---

# Summary

- Useful pages analyzed: 416
- Page-entity mappings: 3321
- Unique entities: 36
- Page relationship edges: 10546
- Entity relationship edges: 3744
- Entity opportunities: 36

---

# Highest Entity Opportunities

| entity_type | entity_name | entity_opportunity_score | entity_opportunity_type | page_count | product_pages | landing_pages | authority_content_pages | total_impressions | authority_tier | strategic_status | has_content_gap |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| product_family | dogbone | 91.28 | COMMERCIAL_ENTITY_NEEDS_AUTHORITY_CONTENT | 62 | 46 | 2 | 0 | 282 | VERY_WEAK | HIGH_COMMERCIAL_LOW_AUTHORITY | True |
| engineering_concept | marine_hardware | 80.0 | COMMERCIAL_ENTITY_NEEDS_AUTHORITY_CONTENT | 16 | 7 | 0 | 0 | 0 |  |  | False |
| application | soft_connection | 80.0 | COMMERCIAL_ENTITY_NEEDS_AUTHORITY_CONTENT | 17 | 15 | 0 | 0 | 0 |  |  | False |
| engineering_concept | cnc_machining | 80.0 | COMMERCIAL_ENTITY_NEEDS_AUTHORITY_CONTENT | 19 | 19 | 0 | 0 | 0 |  |  | False |
| material | ptfe | 80.0 | COMMERCIAL_ENTITY_NEEDS_AUTHORITY_CONTENT | 24 | 24 | 0 | 0 | 0 |  |  | False |
| product_family | morfring | 80.0 | COMMERCIAL_ENTITY_NEEDS_AUTHORITY_CONTENT | 39 | 31 | 2 | 0 | 0 | VERY_WEAK | HIGH_COMMERCIAL_LOW_AUTHORITY | True |
| material | dyneema | 80.0 | COMMERCIAL_ENTITY_NEEDS_AUTHORITY_CONTENT | 9 | 9 | 0 | 0 | 0 |  |  | False |
| product_family | mloop | 80.0 | COMMERCIAL_ENTITY_NEEDS_AUTHORITY_CONTENT | 10 | 8 | 0 | 0 | 0 |  |  | False |
| intent | technical | 63.28 | COMMERCIAL_ENTITY_NEEDS_PILLAR_PAGE | 96 | 55 | 0 | 31 | 207 |  |  | False |
| engineering_concept | low_friction | 60.0 | COMMERCIAL_ENTITY_NEEDS_AUTHORITY_CONTENT | 53 | 44 | 2 | 0 | 0 |  |  | False |
| product_family | padeye | 60.0 | COMMERCIAL_ENTITY_NEEDS_AUTHORITY_CONTENT | 28 | 16 | 2 | 0 | 0 |  |  | False |
| product_family | shackle | 60.0 | COMMERCIAL_ENTITY_NEEDS_AUTHORITY_CONTENT | 27 | 21 | 2 | 0 | 0 |  |  | False |
| engineering_concept | high_load | 60.0 | COMMERCIAL_ENTITY_NEEDS_AUTHORITY_CONTENT | 121 | 120 | 1 | 0 | 0 |  |  | False |
| product_family | powerfurl | 55.0 | ENTITY_HAS_CONTENT_GAP | 122 | 88 | 2 | 6 | 0 | VERY_WEAK | HIGH_COMMERCIAL_LOW_AUTHORITY | True |
| product_family | morfblock | 55.0 | ENTITY_HAS_CONTENT_GAP | 105 | 81 | 2 | 6 | 0 | VERY_WEAK | HIGH_COMMERCIAL_LOW_AUTHORITY | True |
| application | rope_management | 55.0 | COMMERCIAL_ENTITY_NEEDS_PILLAR_PAGE | 113 | 99 | 0 | 2 | 0 |  |  | False |
| material | aluminium | 54.56 | SEARCH_VISIBLE_COMMERCIAL_ENTITY | 76 | 66 | 6 | 4 | 489 |  |  | False |
| material | titanium | 54.56 | SEARCH_VISIBLE_COMMERCIAL_ENTITY | 271 | 221 | 9 | 17 | 489 |  |  | False |
| intent | brand | 54.56 | SEARCH_VISIBLE_COMMERCIAL_ENTITY | 404 | 270 | 12 | 31 | 489 |  |  | False |
| application | custom_engineering | 46.28 | SEARCH_VISIBLE_COMMERCIAL_ENTITY | 66 | 35 | 6 | 9 | 282 |  |  | False |
| engineering_concept | customizable | 46.28 | SEARCH_VISIBLE_COMMERCIAL_ENTITY | 41 | 19 | 6 | 8 | 282 |  |  | False |
| intent | commercial | 46.28 | SEARCH_VISIBLE_COMMERCIAL_ENTITY | 361 | 278 | 8 | 2 | 282 |  |  | False |
| product_family | mreel | 45.0 | COMMERCIAL_ENTITY_NEEDS_AUTHORITY_CONTENT | 7 | 4 | 0 | 0 | 0 |  |  | False |
| engineering_concept | breaking_load | 43.28 | SEARCH_VISIBLE_COMMERCIAL_ENTITY | 261 | 200 | 6 | 31 | 207 |  |  | False |
| application | sheet_handling | 35.0 | MONITOR | 114 | 84 | 2 | 6 | 0 |  |  | False |

---

# Entity Summary

| entity_type | entity_name | page_count | product_pages | category_pages | landing_pages | authority_content_pages | total_impressions | total_clicks |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| application | sail_handling | 209 | 180 | 5 | 3 | 10 | 0.0 | 0.0 |
| application | low_friction_rigging | 146 | 126 | 5 | 2 | 1 | 0.0 | 0.0 |
| application | sheet_handling | 114 | 84 | 13 | 2 | 6 | 0.0 | 0.0 |
| application | rope_management | 113 | 99 | 3 | 0 | 2 | 0.0 | 0.0 |
| application | furling_systems | 91 | 77 | 1 | 2 | 2 | 0.0 | 0.0 |
| application | deck_attachment | 79 | 61 | 4 | 2 | 3 | 0.0 | 0.0 |
| application | custom_engineering | 66 | 35 | 2 | 6 | 9 | 282.0 | 2.0 |
| application | soft_connection | 17 | 15 | 2 | 0 | 0 | 0.0 | 0.0 |
| engineering_concept | breaking_load | 261 | 200 | 13 | 6 | 31 | 207.0 | 2.0 |
| engineering_concept | swl | 162 | 159 | 0 | 1 | 2 | 0.0 | 0.0 |
| engineering_concept | lightweight | 157 | 151 | 3 | 2 | 1 | 0.0 | 0.0 |
| engineering_concept | high_load | 121 | 120 | 0 | 1 | 0 | 0.0 | 0.0 |
| engineering_concept | low_friction | 53 | 44 | 3 | 2 | 0 | 0.0 | 0.0 |
| engineering_concept | customizable | 41 | 19 | 2 | 6 | 8 | 282.0 | 2.0 |
| engineering_concept | cnc_machining | 19 | 19 | 0 | 0 | 0 | 0.0 | 0.0 |
| engineering_concept | marine_hardware | 16 | 7 | 0 | 0 | 0 | 0.0 | 0.0 |
| intent | brand | 404 | 270 | 63 | 12 | 31 | 489.0 | 4.0 |
| intent | commercial | 361 | 278 | 63 | 8 | 2 | 282.0 | 2.0 |
| intent | technical | 96 | 55 | 0 | 0 | 31 | 207.0 | 2.0 |
| intent | support | 2 | 0 | 2 | 0 | 0 | 0.0 | 0.0 |
| material | titanium | 271 | 221 | 10 | 9 | 17 | 489.0 | 4.0 |
| material | aluminium | 76 | 66 | 0 | 6 | 4 | 489.0 | 4.0 |
| material | ptfe | 24 | 24 | 0 | 0 | 0 | 0.0 | 0.0 |
| material | dyneema | 9 | 9 | 0 | 0 | 0 | 0.0 | 0.0 |
| material | stainless_steel | 6 | 0 | 0 | 2 | 4 | 207.0 | 2.0 |
| material | carbon | 2 | 0 | 0 | 0 | 2 | 0.0 | 0.0 |
| product_family | powerfurl | 122 | 88 | 17 | 2 | 6 | 0.0 | 0.0 |
| product_family | morfblock | 105 | 81 | 13 | 2 | 6 | 0.0 | 0.0 |
| product_family | dogbone | 62 | 46 | 6 | 2 | 0 | 282.0 | 2.0 |
| product_family | morfring | 39 | 31 | 2 | 2 | 0 | 0.0 | 0.0 |
| product_family | padeye | 28 | 16 | 2 | 2 | 0 | 0.0 | 0.0 |
| product_family | shackle | 27 | 21 | 4 | 2 | 0 | 0.0 | 0.0 |
| product_family | mloop | 10 | 8 | 2 | 0 | 0 | 0.0 | 0.0 |
| product_family | mreel | 7 | 4 | 2 | 0 | 0 | 0.0 | 0.0 |
| product_family | morfwing | 4 | 0 | 0 | 0 | 4 | 0.0 | 0.0 |
| product_family | hoistlock | 1 | 1 | 0 | 0 | 0 | 0.0 | 0.0 |

---

# Strongest Entity Relationships

| source_entity_type | source_entity_name | target_entity_type | target_entity_name | relationship_type | relationship_count | total_relationship_weight |
| --- | --- | --- | --- | --- | --- | --- |
| intent | commercial | intent | brand | general_internal_link | 6073 | 6073 |
| intent | commercial | intent | brand | product_links_to_parent | 2350 | 4700 |
| intent | brand | intent | commercial | product_links_to_parent | 2094 | 4188 |
| material | titanium | intent | brand | product_links_to_parent | 1873 | 3746 |
| intent | brand | intent | commercial | general_internal_link | 3612 | 3612 |
| material | titanium | intent | commercial | product_links_to_parent | 1719 | 3438 |
| engineering_concept | breaking_load | intent | brand | general_internal_link | 3396 | 3396 |
| engineering_concept | breaking_load | intent | brand | product_links_to_parent | 1678 | 3356 |
| material | titanium | intent | brand | general_internal_link | 3351 | 3351 |
| intent | brand | material | titanium | general_internal_link | 3179 | 3179 |
| engineering_concept | breaking_load | intent | commercial | product_links_to_parent | 1546 | 3092 |
| application | sail_handling | intent | brand | product_links_to_parent | 1496 | 2992 |
| intent | commercial | material | titanium | general_internal_link | 2808 | 2808 |
| application | sail_handling | intent | commercial | product_links_to_parent | 1382 | 2764 |
| intent | brand | application | custom_engineering | general_internal_link | 2700 | 2700 |
| engineering_concept | swl | intent | brand | product_links_to_parent | 1324 | 2648 |
| intent | brand | application | low_friction_rigging | general_internal_link | 2611 | 2611 |
| engineering_concept | lightweight | intent | brand | product_links_to_parent | 1303 | 2606 |
| intent | brand | engineering_concept | breaking_load | general_internal_link | 2601 | 2601 |
| application | sail_handling | intent | brand | general_internal_link | 2497 | 2497 |
| engineering_concept | swl | intent | commercial | product_links_to_parent | 1220 | 2440 |
| engineering_concept | lightweight | intent | commercial | product_links_to_parent | 1187 | 2374 |
| intent | commercial | application | low_friction_rigging | general_internal_link | 2356 | 2356 |
| intent | commercial | application | custom_engineering | general_internal_link | 2321 | 2321 |
| intent | commercial | engineering_concept | breaking_load | general_internal_link | 2204 | 2204 |
| intent | brand | intent | technical | general_internal_link | 2154 | 2154 |
| application | low_friction_rigging | intent | brand | product_links_to_parent | 1068 | 2136 |
| intent | brand | application | sail_handling | general_internal_link | 2127 | 2127 |
| intent | brand | product_family | powerfurl | general_internal_link | 2094 | 2094 |
| engineering_concept | high_load | intent | brand | product_links_to_parent | 1003 | 2006 |
| product_family | powerfurl | intent | brand | general_internal_link | 1981 | 1981 |
| application | low_friction_rigging | intent | commercial | product_links_to_parent | 978 | 1956 |
| intent | brand | application | sheet_handling | general_internal_link | 1905 | 1905 |
| intent | commercial | product_family | powerfurl | general_internal_link | 1873 | 1873 |
| engineering_concept | high_load | intent | commercial | product_links_to_parent | 925 | 1850 |
| intent | commercial | application | sail_handling | general_internal_link | 1849 | 1849 |
| intent | commercial | intent | technical | general_internal_link | 1849 | 1849 |
| application | low_friction_rigging | intent | brand | general_internal_link | 1832 | 1832 |
| engineering_concept | breaking_load | material | titanium | general_internal_link | 1813 | 1813 |
| application | sheet_handling | intent | brand | general_internal_link | 1761 | 1761 |

---

# Interpretation Notes

Entity opportunity types:

- `COMMERCIAL_ENTITY_NEEDS_AUTHORITY_CONTENT`: commercial footprint exists but no supporting authority content.
- `COMMERCIAL_ENTITY_NEEDS_PILLAR_PAGE`: many commercial/product pages exist but no clear landing/pillar page.
- `ENTITY_HAS_CONTENT_GAP`: entity appears in the content gap layer.
- `SEARCH_VISIBLE_COMMERCIAL_ENTITY`: entity has visibility and commercial footprint.
- `MONITOR`: no immediate structural issue detected.

Recommended actions:

1. Prioritize product entities with high opportunity scores and no authority content.
2. Build technical guides around applications and engineering concepts, not only product families.
3. Use entity relationships to design internal links and content hubs.
4. Use this layer before generating content briefs or competitor gap reports.
5. Extend `ENTITY_RULES` over time as MORFRAC adds products, applications, materials, and engineering concepts.

---

# Output Files

- Page entity map: `C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC\06_MARKETING\SEO_Agent\Entity_Relationship_Map\2026-10-05_page_entity_map.csv`
- Entity summary: `C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC\06_MARKETING\SEO_Agent\Entity_Relationship_Map\2026-10-05_entity_summary.csv`
- Page relationship edges: `C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC\06_MARKETING\SEO_Agent\Entity_Relationship_Map\2026-10-05_page_relationship_edges.csv`
- Stable page relationship edges: `C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC\06_MARKETING\SEO_Agent\Entity_Relationship_Map\page_relationship_edges.csv`
- Entity relationship edges: `C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC\06_MARKETING\SEO_Agent\Entity_Relationship_Map\2026-10-05_entity_relationship_edges.csv`
- Entity opportunities: `C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC\06_MARKETING\SEO_Agent\Entity_Relationship_Map\2026-10-05_entity_opportunities.csv`

## Related Links

### Concepts
- [[COMMERCIAL_ENTITY_NEEDS_AUTHORITY_CONTENT]]
- [[VERY_WEAK]]
- [[HIGH_COMMERCIAL_LOW_AUTHORITY]]
- [[COMMERCIAL_ENTITY_NEEDS_PILLAR_PAGE]]
- [[ENTITY_HAS_CONTENT_GAP]]
- [[SEARCH_VISIBLE_COMMERCIAL_ENTITY]]
- [[ENTITY_RULES]]
