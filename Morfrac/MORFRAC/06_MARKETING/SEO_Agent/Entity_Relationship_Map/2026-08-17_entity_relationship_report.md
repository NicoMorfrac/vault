---
type: seo_entity_relationship_report
source_agent: SEO_Agent
created: 2026-08-17
related_findings: []
related_concepts:
  - COMMERCIAL_ENTITY_NEEDS_AUTHORITY_CONTENT
  - VERY_WEAK
  - HIGH_COMMERCIAL_LOW_AUTHORITY
  - SEARCH_VISIBLE_COMMERCIAL_ENTITY
  - ENTITY_HAS_CONTENT_GAP
  - COMMERCIAL_ENTITY_NEEDS_PILLAR_PAGE
  - ENTITY_RULES
related_projects: []
related_reports: []
---

# MORFRAC SEO Entity Relationship Map

## Generated

2026-08-17

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

- Crawl file: `C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC\06_MARKETING\SEO_Agent\Crawls\2026-08-17_site_crawl.csv`
- Semantic pages: `C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC\06_MARKETING\SEO_Agent\Semantic_Clusters\2026-08-17_semantic_cluster_pages.csv`
- Content gaps: `C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC\06_MARKETING\SEO_Agent\Content_Gap_Analysis\2026-08-17_content_gap_analysis.csv`
- Topic authority map: `C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC\06_MARKETING\SEO_Agent\Topic_Authority_Map\2026-08-17_topic_authority_map.csv`
- Contextual link recommendations loaded for future expansion: `C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC\06_MARKETING\SEO_Agent\Contextual_Links\2026-08-17_contextual_link_recommendations_filtered.csv`

---

# Summary

- Useful pages analyzed: 412
- Page-entity mappings: 3240
- Unique entities: 36
- Page relationship edges: 12016
- Entity relationship edges: 3477
- Entity opportunities: 36

---

# Highest Entity Opportunities

| entity_type | entity_name | entity_opportunity_score | entity_opportunity_type | page_count | product_pages | landing_pages | authority_content_pages | total_impressions | authority_tier | strategic_status | has_content_gap |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| product_family | dogbone | 92.64 | COMMERCIAL_ENTITY_NEEDS_AUTHORITY_CONTENT | 58 | 46 | 2 | 0 | 316 | VERY_WEAK | HIGH_COMMERCIAL_LOW_AUTHORITY | True |
| product_family | padeye | 91.44 | COMMERCIAL_ENTITY_NEEDS_AUTHORITY_CONTENT | 24 | 16 | 2 | 0 | 286 | VERY_WEAK | HIGH_COMMERCIAL_LOW_AUTHORITY | True |
| engineering_concept | marine_hardware | 84.52 | COMMERCIAL_ENTITY_NEEDS_AUTHORITY_CONTENT | 12 | 7 | 0 | 0 | 113 |  |  | False |
| application | soft_connection | 80.0 | COMMERCIAL_ENTITY_NEEDS_AUTHORITY_CONTENT | 14 | 12 | 0 | 0 | 0 |  |  | False |
| material | ptfe | 80.0 | COMMERCIAL_ENTITY_NEEDS_AUTHORITY_CONTENT | 24 | 24 | 0 | 0 | 0 |  |  | False |
| material | dyneema | 80.0 | COMMERCIAL_ENTITY_NEEDS_AUTHORITY_CONTENT | 7 | 7 | 0 | 0 | 0 |  |  | False |
| engineering_concept | cnc_machining | 80.0 | COMMERCIAL_ENTITY_NEEDS_AUTHORITY_CONTENT | 18 | 18 | 0 | 0 | 0 |  |  | False |
| product_family | morfring | 80.0 | COMMERCIAL_ENTITY_NEEDS_AUTHORITY_CONTENT | 37 | 31 | 2 | 0 | 0 | VERY_WEAK | HIGH_COMMERCIAL_LOW_AUTHORITY | True |
| product_family | mloop | 75.0 | COMMERCIAL_ENTITY_NEEDS_AUTHORITY_CONTENT | 8 | 6 | 0 | 0 | 0 |  |  | False |
| product_family | shackle | 60.0 | COMMERCIAL_ENTITY_NEEDS_AUTHORITY_CONTENT | 26 | 20 | 2 | 0 | 0 |  |  | False |
| intent | brand | 60.0 | SEARCH_VISIBLE_COMMERCIAL_ENTITY | 400 | 264 | 14 | 31 | 715 |  |  | False |
| engineering_concept | high_load | 60.0 | COMMERCIAL_ENTITY_NEEDS_AUTHORITY_CONTENT | 120 | 119 | 1 | 0 | 0 |  |  | False |
| engineering_concept | low_friction | 60.0 | COMMERCIAL_ENTITY_NEEDS_AUTHORITY_CONTENT | 52 | 44 | 2 | 0 | 0 |  |  | False |
| product_family | powerfurl | 59.52 | ENTITY_HAS_CONTENT_GAP | 114 | 84 | 2 | 6 | 113 | VERY_WEAK | HIGH_COMMERCIAL_LOW_AUTHORITY | True |
| product_family | morfblock | 59.52 | ENTITY_HAS_CONTENT_GAP | 106 | 81 | 2 | 6 | 113 | VERY_WEAK | HIGH_COMMERCIAL_LOW_AUTHORITY | True |
| application | rope_management | 59.52 | COMMERCIAL_ENTITY_NEEDS_PILLAR_PAGE | 109 | 97 | 0 | 2 | 113 |  |  | False |
| material | aluminium | 59.08 | SEARCH_VISIBLE_COMMERCIAL_ENTITY | 75 | 65 | 6 | 4 | 602 |  |  | False |
| material | titanium | 59.08 | SEARCH_VISIBLE_COMMERCIAL_ENTITY | 267 | 216 | 11 | 17 | 602 |  |  | False |
| intent | commercial | 59.08 | SEARCH_VISIBLE_COMMERCIAL_ENTITY | 357 | 272 | 10 | 2 | 602 |  |  | False |
| intent | technical | 55.0 | COMMERCIAL_ENTITY_NEEDS_PILLAR_PAGE | 94 | 55 | 0 | 31 | 0 |  |  | False |
| application | custom_engineering | 52.16 | SEARCH_VISIBLE_COMMERCIAL_ENTITY | 63 | 32 | 6 | 9 | 429 |  |  | False |
| engineering_concept | customizable | 52.16 | SEARCH_VISIBLE_COMMERCIAL_ENTITY | 39 | 17 | 6 | 8 | 429 |  |  | False |
| application | sail_handling | 50.96 | SEARCH_VISIBLE_COMMERCIAL_ENTITY | 207 | 179 | 5 | 10 | 399 |  |  | False |
| application | deck_attachment | 50.96 | SEARCH_VISIBLE_COMMERCIAL_ENTITY | 75 | 61 | 2 | 3 | 399 |  |  | False |
| product_family | mreel | 49.52 | COMMERCIAL_ENTITY_NEEDS_AUTHORITY_CONTENT | 7 | 4 | 0 | 0 | 113 |  |  | False |

---

# Entity Summary

| entity_type | entity_name | page_count | product_pages | category_pages | landing_pages | authority_content_pages | total_impressions | total_clicks |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| application | sail_handling | 207 | 179 | 6 | 5 | 10 | 399.0 | 22.0 |
| application | low_friction_rigging | 144 | 125 | 6 | 2 | 1 | 0.0 | 0.0 |
| application | sheet_handling | 111 | 84 | 14 | 2 | 6 | 113.0 | 18.0 |
| application | rope_management | 109 | 97 | 3 | 0 | 2 | 113.0 | 18.0 |
| application | furling_systems | 84 | 74 | 1 | 2 | 2 | 113.0 | 18.0 |
| application | deck_attachment | 75 | 61 | 4 | 2 | 3 | 399.0 | 22.0 |
| application | custom_engineering | 63 | 32 | 2 | 6 | 9 | 429.0 | 22.0 |
| application | soft_connection | 14 | 12 | 2 | 0 | 0 | 0.0 | 0.0 |
| engineering_concept | breaking_load | 254 | 194 | 14 | 6 | 31 | 113.0 | 18.0 |
| engineering_concept | swl | 161 | 158 | 0 | 1 | 2 | 0.0 | 0.0 |
| engineering_concept | lightweight | 156 | 149 | 4 | 2 | 1 | 0.0 | 0.0 |
| engineering_concept | high_load | 120 | 119 | 0 | 1 | 0 | 0.0 | 0.0 |
| engineering_concept | low_friction | 52 | 44 | 4 | 2 | 0 | 0.0 | 0.0 |
| engineering_concept | customizable | 39 | 17 | 2 | 6 | 8 | 429.0 | 22.0 |
| engineering_concept | cnc_machining | 18 | 18 | 0 | 0 | 0 | 0.0 | 0.0 |
| engineering_concept | marine_hardware | 12 | 7 | 0 | 0 | 0 | 113.0 | 18.0 |
| intent | brand | 400 | 264 | 65 | 14 | 31 | 715.0 | 26.0 |
| intent | commercial | 357 | 272 | 65 | 10 | 2 | 602.0 | 8.0 |
| intent | technical | 94 | 55 | 0 | 0 | 31 | 0.0 | 0.0 |
| intent | support | 2 | 0 | 2 | 0 | 0 | 0.0 | 0.0 |
| material | titanium | 267 | 216 | 11 | 11 | 17 | 602.0 | 8.0 |
| material | aluminium | 75 | 65 | 0 | 6 | 4 | 602.0 | 8.0 |
| material | ptfe | 24 | 24 | 0 | 0 | 0 | 0.0 | 0.0 |
| material | dyneema | 7 | 7 | 0 | 0 | 0 | 0.0 | 0.0 |
| material | stainless_steel | 6 | 0 | 0 | 2 | 4 | 0.0 | 0.0 |
| material | carbon | 2 | 0 | 0 | 0 | 2 | 0.0 | 0.0 |
| product_family | powerfurl | 114 | 84 | 17 | 2 | 6 | 113.0 | 18.0 |
| product_family | morfblock | 106 | 81 | 14 | 2 | 6 | 113.0 | 18.0 |
| product_family | dogbone | 58 | 46 | 6 | 2 | 0 | 316.0 | 4.0 |
| product_family | morfring | 37 | 31 | 2 | 2 | 0 | 0.0 | 0.0 |
| product_family | shackle | 26 | 20 | 4 | 2 | 0 | 0.0 | 0.0 |
| product_family | padeye | 24 | 16 | 2 | 2 | 0 | 286.0 | 4.0 |
| product_family | mloop | 8 | 6 | 2 | 0 | 0 | 0.0 | 0.0 |
| product_family | mreel | 7 | 4 | 2 | 0 | 0 | 113.0 | 18.0 |
| product_family | morfwing | 6 | 0 | 0 | 2 | 4 | 0.0 | 0.0 |
| product_family | hoistlock | 1 | 1 | 0 | 0 | 0 | 0.0 | 0.0 |

---

# Strongest Entity Relationships

| source_entity_type | source_entity_name | target_entity_type | target_entity_name | relationship_type | relationship_count | total_relationship_weight |
| --- | --- | --- | --- | --- | --- | --- |
| intent | commercial | intent | brand | product_links_to_parent | 3633 | 7266 |
| intent | commercial | intent | brand | general_internal_link | 6373 | 6373 |
| intent | brand | intent | commercial | product_links_to_parent | 2993 | 5986 |
| material | titanium | intent | brand | product_links_to_parent | 2886 | 5772 |
| engineering_concept | breaking_load | intent | brand | product_links_to_parent | 2595 | 5190 |
| material | titanium | intent | commercial | product_links_to_parent | 2454 | 4908 |
| application | sail_handling | intent | brand | product_links_to_parent | 2399 | 4798 |
| engineering_concept | breaking_load | intent | commercial | product_links_to_parent | 2207 | 4414 |
| engineering_concept | swl | intent | brand | product_links_to_parent | 2111 | 4222 |
| application | sail_handling | intent | commercial | product_links_to_parent | 2041 | 4082 |
| engineering_concept | lightweight | intent | brand | product_links_to_parent | 1983 | 3966 |
| engineering_concept | swl | intent | commercial | product_links_to_parent | 1795 | 3590 |
| intent | brand | intent | commercial | general_internal_link | 3511 | 3511 |
| intent | commercial | material | titanium | product_links_to_parent | 1748 | 3496 |
| material | titanium | intent | brand | general_internal_link | 3414 | 3414 |
| engineering_concept | breaking_load | intent | brand | general_internal_link | 3409 | 3409 |
| intent | brand | material | titanium | product_links_to_parent | 1698 | 3396 |
| engineering_concept | lightweight | intent | commercial | product_links_to_parent | 1685 | 3370 |
| application | low_friction_rigging | intent | brand | product_links_to_parent | 1666 | 3332 |
| engineering_concept | high_load | intent | brand | product_links_to_parent | 1594 | 3188 |
| intent | brand | application | custom_engineering | general_internal_link | 3130 | 3130 |
| intent | brand | material | titanium | general_internal_link | 3020 | 3020 |
| application | low_friction_rigging | intent | commercial | product_links_to_parent | 1416 | 2832 |
| intent | commercial | application | custom_engineering | general_internal_link | 2746 | 2746 |
| engineering_concept | high_load | intent | commercial | product_links_to_parent | 1356 | 2712 |
| intent | commercial | material | titanium | general_internal_link | 2656 | 2656 |
| intent | brand | engineering_concept | breaking_load | general_internal_link | 2646 | 2646 |
| application | rope_management | intent | brand | product_links_to_parent | 1288 | 2576 |
| application | sail_handling | intent | brand | general_internal_link | 2547 | 2547 |
| engineering_concept | breaking_load | material | titanium | product_links_to_parent | 1244 | 2488 |
| intent | commercial | engineering_concept | breaking_load | general_internal_link | 2288 | 2288 |
| application | sail_handling | material | titanium | product_links_to_parent | 1142 | 2284 |
| application | sheet_handling | intent | brand | product_links_to_parent | 1137 | 2274 |
| intent | commercial | engineering_concept | breaking_load | product_links_to_parent | 1128 | 2256 |
| intent | brand | application | low_friction_rigging | general_internal_link | 2243 | 2243 |
| product_family | powerfurl | intent | brand | product_links_to_parent | 1114 | 2228 |
| intent | brand | engineering_concept | breaking_load | product_links_to_parent | 1095 | 2190 |
| product_family | morfblock | intent | brand | product_links_to_parent | 1095 | 2190 |
| application | rope_management | intent | commercial | product_links_to_parent | 1094 | 2188 |
| engineering_concept | swl | material | titanium | product_links_to_parent | 1008 | 2016 |

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

- Page entity map: `C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC\06_MARKETING\SEO_Agent\Entity_Relationship_Map\2026-08-17_page_entity_map.csv`
- Entity summary: `C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC\06_MARKETING\SEO_Agent\Entity_Relationship_Map\2026-08-17_entity_summary.csv`
- Page relationship edges: `C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC\06_MARKETING\SEO_Agent\Entity_Relationship_Map\2026-08-17_page_relationship_edges.csv`
- Stable page relationship edges: `C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC\06_MARKETING\SEO_Agent\Entity_Relationship_Map\page_relationship_edges.csv`
- Entity relationship edges: `C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC\06_MARKETING\SEO_Agent\Entity_Relationship_Map\2026-08-17_entity_relationship_edges.csv`
- Entity opportunities: `C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC\06_MARKETING\SEO_Agent\Entity_Relationship_Map\2026-08-17_entity_opportunities.csv`

## Related Links

### Concepts
- [[COMMERCIAL_ENTITY_NEEDS_AUTHORITY_CONTENT]]
- [[VERY_WEAK]]
- [[HIGH_COMMERCIAL_LOW_AUTHORITY]]
- [[SEARCH_VISIBLE_COMMERCIAL_ENTITY]]
- [[ENTITY_HAS_CONTENT_GAP]]
- [[COMMERCIAL_ENTITY_NEEDS_PILLAR_PAGE]]
- [[ENTITY_RULES]]
