---
type: seo_entity_relationship_report
source_agent: SEO_Agent
created: 2026-10-16
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

2026-10-16

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

- Crawl file: `C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC\06_MARKETING\SEO_Agent\Crawls\2026-10-16_site_crawl.csv`
- Semantic pages: `C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC\06_MARKETING\SEO_Agent\Semantic_Clusters\2026-10-16_semantic_cluster_pages.csv`
- Content gaps: `C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC\06_MARKETING\SEO_Agent\Content_Gap_Analysis\2026-10-16_content_gap_analysis.csv`
- Topic authority map: `C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC\06_MARKETING\SEO_Agent\Topic_Authority_Map\2026-10-16_topic_authority_map.csv`
- Contextual link recommendations loaded for future expansion: `C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC\06_MARKETING\SEO_Agent\Contextual_Links\2026-10-16_contextual_link_recommendations_filtered.csv`

---

# Summary

- Useful pages analyzed: 416
- Page-entity mappings: 3293
- Unique entities: 36
- Page relationship edges: 10507
- Entity relationship edges: 3748
- Entity opportunities: 36

---

# Highest Entity Opportunities

| entity_type | entity_name | entity_opportunity_score | entity_opportunity_type | page_count | product_pages | landing_pages | authority_content_pages | total_impressions | authority_tier | strategic_status | has_content_gap |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| product_family | dogbone | 88.16 | COMMERCIAL_ENTITY_NEEDS_AUTHORITY_CONTENT | 61 | 46 | 2 | 0 | 204 | VERY_WEAK | HIGH_COMMERCIAL_LOW_AUTHORITY | True |
| engineering_concept | marine_hardware | 80.0 | COMMERCIAL_ENTITY_NEEDS_AUTHORITY_CONTENT | 15 | 7 | 0 | 0 | 0 |  |  | False |
| application | soft_connection | 80.0 | COMMERCIAL_ENTITY_NEEDS_AUTHORITY_CONTENT | 17 | 15 | 0 | 0 | 0 |  |  | False |
| engineering_concept | cnc_machining | 80.0 | COMMERCIAL_ENTITY_NEEDS_AUTHORITY_CONTENT | 19 | 19 | 0 | 0 | 0 |  |  | False |
| product_family | padeye | 80.0 | COMMERCIAL_ENTITY_NEEDS_AUTHORITY_CONTENT | 27 | 16 | 2 | 0 | 0 | VERY_WEAK | HIGH_COMMERCIAL_LOW_AUTHORITY | True |
| product_family | morfring | 80.0 | COMMERCIAL_ENTITY_NEEDS_AUTHORITY_CONTENT | 40 | 31 | 2 | 0 | 0 | VERY_WEAK | HIGH_COMMERCIAL_LOW_AUTHORITY | True |
| material | dyneema | 80.0 | COMMERCIAL_ENTITY_NEEDS_AUTHORITY_CONTENT | 9 | 9 | 0 | 0 | 0 |  |  | False |
| product_family | mloop | 80.0 | COMMERCIAL_ENTITY_NEEDS_AUTHORITY_CONTENT | 10 | 8 | 0 | 0 | 0 |  |  | False |
| material | ptfe | 80.0 | COMMERCIAL_ENTITY_NEEDS_AUTHORITY_CONTENT | 24 | 24 | 0 | 0 | 0 |  |  | False |
| intent | technical | 62.12 | COMMERCIAL_ENTITY_NEEDS_PILLAR_PAGE | 95 | 55 | 0 | 31 | 178 |  |  | False |
| engineering_concept | low_friction | 60.0 | COMMERCIAL_ENTITY_NEEDS_AUTHORITY_CONTENT | 54 | 44 | 2 | 0 | 0 |  |  | False |
| product_family | shackle | 60.0 | COMMERCIAL_ENTITY_NEEDS_AUTHORITY_CONTENT | 28 | 21 | 2 | 0 | 0 | MODERATE | HIGH_COMMERCIAL_LOW_AUTHORITY | False |
| engineering_concept | high_load | 60.0 | COMMERCIAL_ENTITY_NEEDS_AUTHORITY_CONTENT | 120 | 119 | 1 | 0 | 0 |  |  | False |
| product_family | powerfurl | 55.0 | ENTITY_HAS_CONTENT_GAP | 119 | 86 | 2 | 6 | 0 | VERY_WEAK | HIGH_COMMERCIAL_LOW_AUTHORITY | True |
| product_family | morfblock | 55.0 | ENTITY_HAS_CONTENT_GAP | 105 | 81 | 2 | 6 | 0 | VERY_WEAK | HIGH_COMMERCIAL_LOW_AUTHORITY | True |
| application | rope_management | 55.0 | COMMERCIAL_ENTITY_NEEDS_PILLAR_PAGE | 111 | 98 | 0 | 2 | 0 |  |  | False |
| material | aluminium | 50.28 | SEARCH_VISIBLE_COMMERCIAL_ENTITY | 75 | 65 | 6 | 4 | 382 |  |  | False |
| material | titanium | 50.28 | SEARCH_VISIBLE_COMMERCIAL_ENTITY | 269 | 220 | 9 | 17 | 382 |  |  | False |
| intent | brand | 50.28 | SEARCH_VISIBLE_COMMERCIAL_ENTITY | 400 | 268 | 12 | 31 | 382 |  |  | False |
| product_family | mreel | 45.0 | COMMERCIAL_ENTITY_NEEDS_AUTHORITY_CONTENT | 7 | 4 | 0 | 0 | 0 |  |  | False |
| engineering_concept | customizable | 43.16 | SEARCH_VISIBLE_COMMERCIAL_ENTITY | 41 | 19 | 6 | 8 | 204 |  |  | False |
| intent | commercial | 43.16 | SEARCH_VISIBLE_COMMERCIAL_ENTITY | 359 | 276 | 8 | 2 | 204 |  |  | False |
| application | custom_engineering | 43.16 | SEARCH_VISIBLE_COMMERCIAL_ENTITY | 65 | 35 | 6 | 9 | 204 |  |  | False |
| engineering_concept | breaking_load | 42.12 | SEARCH_VISIBLE_COMMERCIAL_ENTITY | 258 | 198 | 6 | 31 | 178 |  |  | False |
| application | sheet_handling | 35.0 | MONITOR | 113 | 84 | 2 | 6 | 0 |  |  | False |

---

# Entity Summary

| entity_type | entity_name | page_count | product_pages | category_pages | landing_pages | authority_content_pages | total_impressions | total_clicks |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| application | sail_handling | 207 | 179 | 5 | 3 | 10 | 0.0 | 0.0 |
| application | low_friction_rigging | 146 | 126 | 5 | 2 | 1 | 0.0 | 0.0 |
| application | sheet_handling | 113 | 84 | 13 | 2 | 6 | 0.0 | 0.0 |
| application | rope_management | 111 | 98 | 3 | 0 | 2 | 0.0 | 0.0 |
| application | furling_systems | 88 | 75 | 1 | 2 | 2 | 0.0 | 0.0 |
| application | deck_attachment | 78 | 61 | 4 | 2 | 3 | 0.0 | 0.0 |
| application | custom_engineering | 65 | 35 | 2 | 6 | 9 | 204.0 | 0.0 |
| application | soft_connection | 17 | 15 | 2 | 0 | 0 | 0.0 | 0.0 |
| engineering_concept | breaking_load | 258 | 198 | 13 | 6 | 31 | 178.0 | 1.0 |
| engineering_concept | swl | 162 | 159 | 0 | 1 | 2 | 0.0 | 0.0 |
| engineering_concept | lightweight | 156 | 150 | 3 | 2 | 1 | 0.0 | 0.0 |
| engineering_concept | high_load | 120 | 119 | 0 | 1 | 0 | 0.0 | 0.0 |
| engineering_concept | low_friction | 54 | 44 | 3 | 2 | 0 | 0.0 | 0.0 |
| engineering_concept | customizable | 41 | 19 | 2 | 6 | 8 | 204.0 | 0.0 |
| engineering_concept | cnc_machining | 19 | 19 | 0 | 0 | 0 | 0.0 | 0.0 |
| engineering_concept | marine_hardware | 15 | 7 | 0 | 0 | 0 | 0.0 | 0.0 |
| intent | brand | 400 | 268 | 63 | 12 | 31 | 382.0 | 1.0 |
| intent | commercial | 359 | 276 | 63 | 8 | 2 | 204.0 | 0.0 |
| intent | technical | 95 | 55 | 0 | 0 | 31 | 178.0 | 1.0 |
| intent | support | 2 | 0 | 2 | 0 | 0 | 0.0 | 0.0 |
| material | titanium | 269 | 220 | 10 | 9 | 17 | 382.0 | 1.0 |
| material | aluminium | 75 | 65 | 0 | 6 | 4 | 382.0 | 1.0 |
| material | ptfe | 24 | 24 | 0 | 0 | 0 | 0.0 | 0.0 |
| material | dyneema | 9 | 9 | 0 | 0 | 0 | 0.0 | 0.0 |
| material | stainless_steel | 6 | 0 | 0 | 2 | 4 | 178.0 | 1.0 |
| material | carbon | 2 | 0 | 0 | 0 | 2 | 0.0 | 0.0 |
| product_family | powerfurl | 119 | 86 | 17 | 2 | 6 | 0.0 | 0.0 |
| product_family | morfblock | 105 | 81 | 13 | 2 | 6 | 0.0 | 0.0 |
| product_family | dogbone | 61 | 46 | 6 | 2 | 0 | 204.0 | 0.0 |
| product_family | morfring | 40 | 31 | 2 | 2 | 0 | 0.0 | 0.0 |
| product_family | shackle | 28 | 21 | 4 | 2 | 0 | 0.0 | 0.0 |
| product_family | padeye | 27 | 16 | 2 | 2 | 0 | 0.0 | 0.0 |
| product_family | mloop | 10 | 8 | 2 | 0 | 0 | 0.0 | 0.0 |
| product_family | mreel | 7 | 4 | 2 | 0 | 0 | 0.0 | 0.0 |
| product_family | morfwing | 4 | 0 | 0 | 0 | 4 | 0.0 | 0.0 |
| product_family | hoistlock | 1 | 1 | 0 | 0 | 0 | 0.0 | 0.0 |

---

# Strongest Entity Relationships

| source_entity_type | source_entity_name | target_entity_type | target_entity_name | relationship_type | relationship_count | total_relationship_weight |
| --- | --- | --- | --- | --- | --- | --- |
| intent | commercial | intent | brand | general_internal_link | 5613 | 5613 |
| intent | commercial | intent | brand | product_links_to_parent | 2334 | 4668 |
| intent | brand | intent | commercial | product_links_to_parent | 2078 | 4156 |
| material | titanium | intent | brand | product_links_to_parent | 1865 | 3730 |
| intent | brand | intent | commercial | general_internal_link | 3606 | 3606 |
| material | titanium | intent | commercial | product_links_to_parent | 1711 | 3422 |
| engineering_concept | breaking_load | intent | brand | product_links_to_parent | 1662 | 3324 |
| engineering_concept | breaking_load | intent | commercial | product_links_to_parent | 1530 | 3060 |
| engineering_concept | breaking_load | intent | brand | general_internal_link | 3054 | 3054 |
| material | titanium | intent | brand | general_internal_link | 3011 | 3011 |
| application | sail_handling | intent | brand | product_links_to_parent | 1488 | 2976 |
| intent | brand | material | titanium | general_internal_link | 2929 | 2929 |
| application | sail_handling | intent | commercial | product_links_to_parent | 1374 | 2748 |
| engineering_concept | swl | intent | brand | product_links_to_parent | 1324 | 2648 |
| engineering_concept | lightweight | intent | brand | product_links_to_parent | 1295 | 2590 |
| intent | commercial | material | titanium | general_internal_link | 2576 | 2576 |
| intent | brand | application | low_friction_rigging | general_internal_link | 2521 | 2521 |
| intent | brand | application | custom_engineering | general_internal_link | 2452 | 2452 |
| engineering_concept | swl | intent | commercial | product_links_to_parent | 1220 | 2440 |
| engineering_concept | lightweight | intent | commercial | product_links_to_parent | 1179 | 2358 |
| intent | brand | engineering_concept | breaking_load | general_internal_link | 2355 | 2355 |
| intent | commercial | application | low_friction_rigging | general_internal_link | 2263 | 2263 |
| application | sail_handling | intent | brand | general_internal_link | 2221 | 2221 |
| application | low_friction_rigging | intent | brand | product_links_to_parent | 1068 | 2136 |
| intent | commercial | application | custom_engineering | general_internal_link | 2091 | 2091 |
| engineering_concept | high_load | intent | brand | product_links_to_parent | 995 | 1990 |
| intent | commercial | engineering_concept | breaking_load | general_internal_link | 1976 | 1976 |
| application | low_friction_rigging | intent | commercial | product_links_to_parent | 978 | 1956 |
| intent | brand | intent | technical | general_internal_link | 1906 | 1906 |
| intent | brand | application | sail_handling | general_internal_link | 1881 | 1881 |
| intent | brand | product_family | powerfurl | general_internal_link | 1850 | 1850 |
| engineering_concept | high_load | intent | commercial | product_links_to_parent | 917 | 1834 |
| product_family | powerfurl | intent | brand | general_internal_link | 1827 | 1827 |
| application | rope_management | intent | brand | product_links_to_parent | 833 | 1666 |
| intent | brand | application | sheet_handling | general_internal_link | 1661 | 1661 |
| application | low_friction_rigging | intent | brand | general_internal_link | 1654 | 1654 |
| intent | commercial | product_family | powerfurl | general_internal_link | 1647 | 1647 |
| engineering_concept | breaking_load | material | titanium | general_internal_link | 1640 | 1640 |
| intent | commercial | application | sail_handling | general_internal_link | 1621 | 1621 |
| intent | commercial | intent | technical | general_internal_link | 1619 | 1619 |

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

- Page entity map: `C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC\06_MARKETING\SEO_Agent\Entity_Relationship_Map\2026-10-16_page_entity_map.csv`
- Entity summary: `C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC\06_MARKETING\SEO_Agent\Entity_Relationship_Map\2026-10-16_entity_summary.csv`
- Page relationship edges: `C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC\06_MARKETING\SEO_Agent\Entity_Relationship_Map\2026-10-16_page_relationship_edges.csv`
- Stable page relationship edges: `C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC\06_MARKETING\SEO_Agent\Entity_Relationship_Map\page_relationship_edges.csv`
- Entity relationship edges: `C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC\06_MARKETING\SEO_Agent\Entity_Relationship_Map\2026-10-16_entity_relationship_edges.csv`
- Entity opportunities: `C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC\06_MARKETING\SEO_Agent\Entity_Relationship_Map\2026-10-16_entity_opportunities.csv`

## Related Links

### Concepts
- [[COMMERCIAL_ENTITY_NEEDS_AUTHORITY_CONTENT]]
- [[VERY_WEAK]]
- [[HIGH_COMMERCIAL_LOW_AUTHORITY]]
- [[COMMERCIAL_ENTITY_NEEDS_PILLAR_PAGE]]
- [[ENTITY_HAS_CONTENT_GAP]]
- [[SEARCH_VISIBLE_COMMERCIAL_ENTITY]]
- [[ENTITY_RULES]]
