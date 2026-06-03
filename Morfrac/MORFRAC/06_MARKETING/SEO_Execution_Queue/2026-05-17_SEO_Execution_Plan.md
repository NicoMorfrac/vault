---
type: plan
source_agent: Marketing
created: 2026-05-17
related_findings: []
related_concepts:
  - PRODUCT_HEAVY_NO_PILLAR
related_projects: []
related_reports: []
---

# MORFRAC SEO Execution Plan

## Date

2026-05-17

## Source Validation

- Pipeline health: `PASS`
- Fresh source sets used: `Executive_Reviews`, `Topic_Authority_Map`, `Content_Gap_Analysis`, `Entity_Relationship_Map`, `Contextual_Links`, `Pipeline_Health`, `Semantic_Clusters`, `Merged_Analysis`

## Execution Queue

| Priority | Workstream | Task | Why now | Source signals |
| --- | --- | --- | --- | --- |
| 1 | Metadata | Rewrite title and meta for `https://www.morfrac.com/shop/mloop-dyneema-loop-12675` and `https://www.morfrac.com/es/shop/mloop-dyneema-loop-12675` | Both pages rank on page 1 with `0` clicks and the highest priority scores in merged analysis. | `Merged_Analysis`, `Executive_Reviews` |
| 2 | Metadata + landing-page copy | Rewrite title and meta for `https://www.morfrac.com/dogbone` and `https://www.morfrac.com/es/dogbone`, then expand above-the-fold copy around the dogbone query cluster | `dogbone` is the strongest search-visible commercial topic with very weak authority and clear CTR/headline weakness. | `Executive_Reviews`, `Topic_Authority_Map`, `Merged_Analysis` |
| 3 | Internal linking | Add contextual links from `mloop custom` pages into the main `mloop dyneema loop` pages in EN and ES | `mloop` has high commercial relevance, zero clicks, and direct filtered link recommendations. | `Contextual_Links`, `Entity_Relationship_Map`, `Merged_Analysis` |
| 4 | Pillar planning | Create a `powerfurl` pillar/category hub that consolidates continuous-line, single-line, kit, drum, and fork-fitting product families | `powerfurl` is the weakest authority topic, has multiple `PRODUCT_HEAVY_NO_PILLAR` clusters, and is flagged for category support. | `Topic_Authority_Map`, `Content_Gap_Analysis`, `Semantic_Clusters` |
| 5 | Content brief | Publish a `dogbone` technical guide that supports the landing page and top SKUs | `dogbone` combines search visibility with missing authority content and the highest entity opportunity score. | `Executive_Reviews`, `Entity_Relationship_Map`, `Topic_Authority_Map` |
| 6 | Internal linking | Add category-to-child links across `powerfurl` continuous-line and single-line category pages | The cluster is fragmented and link recommendations exist at category level. | `Contextual_Links`, `Semantic_Clusters` |
| 7 | Content brief | Publish a `morfblock` technical guide focused on family selection, load classes, and variant differentiation | `morfblock` has two major product-heavy clusters with no pillar support and high content-gap scores. | `Content_Gap_Analysis`, `Semantic_Clusters`, `Topic_Authority_Map` |
| 8 | Metadata | Rewrite ES `padeye` landing metadata for `https://www.morfrac.com/es/padeye` | Existing page ranks for a commercial Spanish query and is flagged for CTR/title improvement. | `Executive_Reviews` |
| 9 | Content brief | Publish a `powerfurl` technical guide that links into the new pillar hub and key categories | `powerfurl` needs both authority content and central routing to product families. | `Executive_Reviews`, `Content_Gap_Analysis`, `Semantic_Clusters` |
| 10 | Internal linking | Add morfblock category-to-product links on the highest-value category pages | `morfblock` is fragmented and product-heavy; filtered link recommendations already map categories to products. | `Contextual_Links`, `Semantic_Clusters` |

## Constraints For Implementation

- Do not create net-new low-intent pages.
- Do not expand already fragmented topic areas without first assigning each page a supporting role.
- Treat semantic duplicate pairs in `powerfurl` and `morfblock` categories as consolidation-review items before launching more overlapping pages.

## Handoff Notes

- Start with metadata and link tasks because they affect already-visible commercial pages.
- The pillar page should be scoped before writing supporting `powerfurl` content so briefs can link to a stable commercial hub.
- Content briefs should route internal links toward commercial landing/category pages, not stand alone.

## Related Links

### Concepts
- [[PRODUCT_HEAVY_NO_PILLAR]]
