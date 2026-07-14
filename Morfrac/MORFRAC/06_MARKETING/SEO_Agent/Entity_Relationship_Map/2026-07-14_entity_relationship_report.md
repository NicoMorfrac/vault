---
type: seo_entity_relationship_report
source_agent: SEO_Agent
created: 2026-07-14
related_findings: []
related_concepts:
  - COMMERCIAL_ENTITY_NEEDS_AUTHORITY_CONTENT
  - VERY_WEAK
  - HIGH_COMMERCIAL_LOW_AUTHORITY
  - ENTITY_HAS_CONTENT_GAP
  - COMMERCIAL_ENTITY_NEEDS_PILLAR_PAGE
  - SEARCH_VISIBLE_COMMERCIAL_ENTITY
  - ENTITY_RULES
related_projects: []
related_reports: []
---

# MORFRAC SEO Entity Relationship Map

## Generated

2026-07-14

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

- Crawl file: `C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC\06_MARKETING\SEO_Agent\Crawls\2026-07-14_site_crawl.csv`
- Semantic pages: `C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC\06_MARKETING\SEO_Agent\Semantic_Clusters\2026-07-14_semantic_cluster_pages.csv`
- Content gaps: `C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC\06_MARKETING\SEO_Agent\Content_Gap_Analysis\2026-07-14_content_gap_analysis.csv`
- Topic authority map: `C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC\06_MARKETING\SEO_Agent\Topic_Authority_Map\2026-07-14_topic_authority_map.csv`
- Contextual link recommendations loaded for future expansion: `C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC\06_MARKETING\SEO_Agent\Contextual_Links\2026-07-14_contextual_link_recommendations_filtered.csv`

---

# Summary

- Useful pages analyzed: 412
- Page-entity mappings: 3250
- Unique entities: 36
- Page relationship edges: 11966
- Entity relationship edges: 3475
- Entity opportunities: 36

---

# Highest Entity Opportunities

| entity_type | entity_name | entity_opportunity_score | entity_opportunity_type | page_count | product_pages | landing_pages | authority_content_pages | total_impressions | authority_tier | strategic_status | has_content_gap |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| product_family | dogbone | 98.56 | COMMERCIAL_ENTITY_NEEDS_AUTHORITY_CONTENT | 58 | 46 | 2 | 0 | 464 | VERY_WEAK | HIGH_COMMERCIAL_LOW_AUTHORITY | True |
| engineering_concept | marine_hardware | 84.72 | COMMERCIAL_ENTITY_NEEDS_AUTHORITY_CONTENT | 12 | 7 | 0 | 0 | 118 |  |  | False |
| application | soft_connection | 80.0 | COMMERCIAL_ENTITY_NEEDS_AUTHORITY_CONTENT | 14 | 12 | 0 | 0 | 0 |  |  | False |
| engineering_concept | cnc_machining | 80.0 | COMMERCIAL_ENTITY_NEEDS_AUTHORITY_CONTENT | 19 | 19 | 0 | 0 | 0 |  |  | False |
| product_family | shackle | 80.0 | COMMERCIAL_ENTITY_NEEDS_AUTHORITY_CONTENT | 27 | 21 | 2 | 0 | 0 | VERY_WEAK | HIGH_COMMERCIAL_LOW_AUTHORITY | True |
| product_family | morfring | 80.0 | COMMERCIAL_ENTITY_NEEDS_AUTHORITY_CONTENT | 37 | 31 | 2 | 0 | 0 | VERY_WEAK | HIGH_COMMERCIAL_LOW_AUTHORITY | True |
| material | dyneema | 80.0 | COMMERCIAL_ENTITY_NEEDS_AUTHORITY_CONTENT | 7 | 7 | 0 | 0 | 0 |  |  | False |
| product_family | padeye | 80.0 | COMMERCIAL_ENTITY_NEEDS_AUTHORITY_CONTENT | 24 | 16 | 2 | 0 | 0 | VERY_WEAK | HIGH_COMMERCIAL_LOW_AUTHORITY | True |
| material | ptfe | 80.0 | COMMERCIAL_ENTITY_NEEDS_AUTHORITY_CONTENT | 24 | 24 | 0 | 0 | 0 |  |  | False |
| product_family | mloop | 75.0 | COMMERCIAL_ENTITY_NEEDS_AUTHORITY_CONTENT | 8 | 6 | 0 | 0 | 0 |  |  | False |
| engineering_concept | low_friction | 60.0 | COMMERCIAL_ENTITY_NEEDS_AUTHORITY_CONTENT | 52 | 44 | 2 | 0 | 0 |  |  | False |
| engineering_concept | high_load | 60.0 | COMMERCIAL_ENTITY_NEEDS_AUTHORITY_CONTENT | 120 | 119 | 1 | 0 | 0 |  |  | False |
| product_family | powerfurl | 59.72 | ENTITY_HAS_CONTENT_GAP | 115 | 85 | 2 | 6 | 118 | VERY_WEAK | HIGH_COMMERCIAL_LOW_AUTHORITY | True |
| product_family | morfblock | 59.72 | ENTITY_HAS_CONTENT_GAP | 106 | 81 | 2 | 6 | 118 | VERY_WEAK | HIGH_COMMERCIAL_LOW_AUTHORITY | True |
| application | rope_management | 59.72 | COMMERCIAL_ENTITY_NEEDS_PILLAR_PAGE | 111 | 97 | 0 | 2 | 118 |  |  | False |
| application | custom_engineering | 58.28 | SEARCH_VISIBLE_COMMERCIAL_ENTITY | 66 | 33 | 6 | 9 | 582 |  |  | False |
| intent | brand | 58.28 | SEARCH_VISIBLE_COMMERCIAL_ENTITY | 400 | 262 | 14 | 31 | 582 |  |  | False |
| engineering_concept | customizable | 58.28 | SEARCH_VISIBLE_COMMERCIAL_ENTITY | 39 | 17 | 6 | 8 | 582 |  |  | False |
| intent | technical | 55.0 | COMMERCIAL_ENTITY_NEEDS_PILLAR_PAGE | 96 | 55 | 0 | 31 | 0 |  |  | False |
| material | aluminium | 53.56 | SEARCH_VISIBLE_COMMERCIAL_ENTITY | 72 | 62 | 6 | 4 | 464 |  |  | False |
| intent | commercial | 53.56 | SEARCH_VISIBLE_COMMERCIAL_ENTITY | 355 | 270 | 10 | 2 | 464 |  |  | False |
| material | titanium | 53.56 | SEARCH_VISIBLE_COMMERCIAL_ENTITY | 269 | 216 | 11 | 17 | 464 |  |  | False |
| product_family | mreel | 49.72 | COMMERCIAL_ENTITY_NEEDS_AUTHORITY_CONTENT | 7 | 4 | 0 | 0 | 118 |  |  | False |
| application | sail_handling | 39.72 | SEARCH_VISIBLE_COMMERCIAL_ENTITY | 205 | 177 | 5 | 10 | 118 |  |  | False |
| engineering_concept | breaking_load | 39.72 | SEARCH_VISIBLE_COMMERCIAL_ENTITY | 255 | 195 | 6 | 31 | 118 |  |  | False |

---

# Entity Summary

| entity_type | entity_name | page_count | product_pages | category_pages | landing_pages | authority_content_pages | total_impressions | total_clicks |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| application | sail_handling | 205 | 177 | 6 | 5 | 10 | 118.0 | 13.0 |
| application | low_friction_rigging | 147 | 126 | 6 | 2 | 1 | 0.0 | 0.0 |
| application | rope_management | 111 | 97 | 3 | 0 | 2 | 118.0 | 13.0 |
| application | sheet_handling | 111 | 84 | 14 | 2 | 6 | 118.0 | 13.0 |
| application | furling_systems | 84 | 74 | 1 | 2 | 2 | 118.0 | 13.0 |
| application | deck_attachment | 74 | 60 | 4 | 2 | 3 | 118.0 | 13.0 |
| application | custom_engineering | 66 | 33 | 2 | 6 | 9 | 582.0 | 15.0 |
| application | soft_connection | 14 | 12 | 2 | 0 | 0 | 0.0 | 0.0 |
| engineering_concept | breaking_load | 255 | 195 | 14 | 6 | 31 | 118.0 | 13.0 |
| engineering_concept | swl | 162 | 159 | 0 | 1 | 2 | 0.0 | 0.0 |
| engineering_concept | lightweight | 157 | 150 | 4 | 2 | 1 | 0.0 | 0.0 |
| engineering_concept | high_load | 120 | 119 | 0 | 1 | 0 | 0.0 | 0.0 |
| engineering_concept | low_friction | 52 | 44 | 4 | 2 | 0 | 0.0 | 0.0 |
| engineering_concept | customizable | 39 | 17 | 2 | 6 | 8 | 582.0 | 15.0 |
| engineering_concept | cnc_machining | 19 | 19 | 0 | 0 | 0 | 0.0 | 0.0 |
| engineering_concept | marine_hardware | 12 | 7 | 0 | 0 | 0 | 118.0 | 13.0 |
| intent | brand | 400 | 262 | 65 | 14 | 31 | 582.0 | 15.0 |
| intent | commercial | 355 | 270 | 65 | 10 | 2 | 464.0 | 2.0 |
| intent | technical | 96 | 55 | 0 | 0 | 31 | 0.0 | 0.0 |
| intent | support | 2 | 0 | 2 | 0 | 0 | 0.0 | 0.0 |
| material | titanium | 269 | 216 | 11 | 11 | 17 | 464.0 | 2.0 |
| material | aluminium | 72 | 62 | 0 | 6 | 4 | 464.0 | 2.0 |
| material | ptfe | 24 | 24 | 0 | 0 | 0 | 0.0 | 0.0 |
| material | dyneema | 7 | 7 | 0 | 0 | 0 | 0.0 | 0.0 |
| material | stainless_steel | 6 | 0 | 0 | 2 | 4 | 0.0 | 0.0 |
| material | carbon | 2 | 0 | 0 | 0 | 2 | 0.0 | 0.0 |
| product_family | powerfurl | 115 | 85 | 17 | 2 | 6 | 118.0 | 13.0 |
| product_family | morfblock | 106 | 81 | 14 | 2 | 6 | 118.0 | 13.0 |
| product_family | dogbone | 58 | 46 | 6 | 2 | 0 | 464.0 | 2.0 |
| product_family | morfring | 37 | 31 | 2 | 2 | 0 | 0.0 | 0.0 |
| product_family | shackle | 27 | 21 | 4 | 2 | 0 | 0.0 | 0.0 |
| product_family | padeye | 24 | 16 | 2 | 2 | 0 | 0.0 | 0.0 |
| product_family | mloop | 8 | 6 | 2 | 0 | 0 | 0.0 | 0.0 |
| product_family | mreel | 7 | 4 | 2 | 0 | 0 | 118.0 | 13.0 |
| product_family | morfwing | 6 | 0 | 0 | 2 | 4 | 0.0 | 0.0 |
| product_family | hoistlock | 1 | 1 | 0 | 0 | 0 | 0.0 | 0.0 |

---

# Strongest Entity Relationships

| source_entity_type | source_entity_name | target_entity_type | target_entity_name | relationship_type | relationship_count | total_relationship_weight |
| --- | --- | --- | --- | --- | --- | --- |
| intent | commercial | intent | brand | product_links_to_parent | 3605 | 7210 |
| intent | commercial | intent | brand | general_internal_link | 6708 | 6708 |
| intent | brand | intent | commercial | product_links_to_parent | 2969 | 5938 |
| material | titanium | intent | brand | product_links_to_parent | 2886 | 5772 |
| engineering_concept | breaking_load | intent | brand | product_links_to_parent | 2609 | 5218 |
| material | titanium | intent | commercial | product_links_to_parent | 2454 | 4908 |
| application | sail_handling | intent | brand | product_links_to_parent | 2371 | 4742 |
| engineering_concept | breaking_load | intent | commercial | product_links_to_parent | 2219 | 4438 |
| engineering_concept | swl | intent | brand | product_links_to_parent | 2125 | 4250 |
| application | sail_handling | intent | commercial | product_links_to_parent | 2017 | 4034 |
| engineering_concept | lightweight | intent | brand | product_links_to_parent | 1997 | 3994 |
| material | titanium | intent | brand | general_internal_link | 3681 | 3681 |
| engineering_concept | breaking_load | intent | brand | general_internal_link | 3674 | 3674 |
| engineering_concept | swl | intent | commercial | product_links_to_parent | 1807 | 3614 |
| intent | brand | application | custom_engineering | general_internal_link | 3514 | 3514 |
| intent | brand | intent | commercial | general_internal_link | 3507 | 3507 |
| intent | commercial | material | titanium | product_links_to_parent | 1736 | 3472 |
| intent | brand | material | titanium | general_internal_link | 3406 | 3406 |
| engineering_concept | lightweight | intent | commercial | product_links_to_parent | 1697 | 3394 |
| intent | brand | material | titanium | product_links_to_parent | 1686 | 3372 |
| application | low_friction_rigging | intent | brand | product_links_to_parent | 1680 | 3360 |
| engineering_concept | high_load | intent | brand | product_links_to_parent | 1594 | 3188 |
| intent | commercial | application | custom_engineering | general_internal_link | 3089 | 3089 |
| intent | commercial | material | titanium | general_internal_link | 3001 | 3001 |
| application | low_friction_rigging | intent | commercial | product_links_to_parent | 1428 | 2856 |
| application | sail_handling | intent | brand | general_internal_link | 2732 | 2732 |
| engineering_concept | high_load | intent | commercial | product_links_to_parent | 1356 | 2712 |
| intent | brand | engineering_concept | breaking_load | general_internal_link | 2638 | 2638 |
| intent | brand | application | low_friction_rigging | general_internal_link | 2629 | 2629 |
| application | rope_management | intent | brand | product_links_to_parent | 1288 | 2576 |
| engineering_concept | breaking_load | material | titanium | product_links_to_parent | 1250 | 2500 |
| intent | commercial | application | low_friction_rigging | general_internal_link | 2360 | 2360 |
| intent | commercial | engineering_concept | breaking_load | general_internal_link | 2280 | 2280 |
| application | sheet_handling | intent | brand | product_links_to_parent | 1137 | 2274 |
| application | sail_handling | material | titanium | product_links_to_parent | 1130 | 2260 |
| product_family | powerfurl | intent | brand | product_links_to_parent | 1128 | 2256 |
| intent | commercial | engineering_concept | breaking_load | product_links_to_parent | 1120 | 2240 |
| material | titanium | application | custom_engineering | general_internal_link | 2210 | 2210 |
| product_family | morfblock | intent | brand | product_links_to_parent | 1095 | 2190 |
| application | rope_management | intent | commercial | product_links_to_parent | 1094 | 2188 |

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

- Page entity map: `C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC\06_MARKETING\SEO_Agent\Entity_Relationship_Map\2026-07-14_page_entity_map.csv`
- Entity summary: `C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC\06_MARKETING\SEO_Agent\Entity_Relationship_Map\2026-07-14_entity_summary.csv`
- Page relationship edges: `C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC\06_MARKETING\SEO_Agent\Entity_Relationship_Map\2026-07-14_page_relationship_edges.csv`
- Stable page relationship edges: `C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC\06_MARKETING\SEO_Agent\Entity_Relationship_Map\page_relationship_edges.csv`
- Entity relationship edges: `C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC\06_MARKETING\SEO_Agent\Entity_Relationship_Map\2026-07-14_entity_relationship_edges.csv`
- Entity opportunities: `C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC\06_MARKETING\SEO_Agent\Entity_Relationship_Map\2026-07-14_entity_opportunities.csv`

## Related Links

### Concepts
- [[COMMERCIAL_ENTITY_NEEDS_AUTHORITY_CONTENT]]
- [[VERY_WEAK]]
- [[HIGH_COMMERCIAL_LOW_AUTHORITY]]
- [[ENTITY_HAS_CONTENT_GAP]]
- [[COMMERCIAL_ENTITY_NEEDS_PILLAR_PAGE]]
- [[SEARCH_VISIBLE_COMMERCIAL_ENTITY]]
- [[ENTITY_RULES]]
