# MORFRAC Metadata Tasks

## Date

2026-05-17

## Implementation Tasks

| Priority | URL | Query cluster | Current issue | Required change |
| --- | --- | --- | --- | --- |
| 1 | `https://www.morfrac.com/shop/mloop-dyneema-loop-12675` | `mloop`, `dyneema loop` | Page 1 visibility, `0` clicks, title too generic for commercial capture | Rewrite title to include `mloop`, `Dyneema loop`, and performance intent. Keep brand last. Rewrite meta to emphasize application, strength, and fit-for-rigging use cases. |
| 2 | `https://www.morfrac.com/es/shop/mloop-dyneema-loop-12675` | `mloop`, `dyneema loop` | Same CTR issue on ES URL, currently using English metadata pattern | Localize title and meta into Spanish while preserving product-family and performance terms. |
| 3 | `https://www.morfrac.com/dogbone` | `dogbone`, `dogbone shackle`, `dog bone sailing`, `dog bone steel` | Title is only `dogbones. | MORFRAC`; page is search-visible but under-positioned for its query cluster | Expand title to cover the primary commercial term and product context. Refresh meta around textile connection, sailing hardware, and material options. |
| 4 | `https://www.morfrac.com/es/dogbone` | `dogbone`, `dog bones` | Same short-title and CTR issue on ES landing page | Replace short English-led metadata with Spanish commercial phrasing aligned to the dogbone cluster. |
| 5 | `https://www.morfrac.com/es/padeye` | `cancamo pasante` | Search-visible Spanish commercial page with weak title capture | Update title to include the Spanish head term and MORFRAC product context. Tighten meta around marine hardware use and product value. |
| 6 | `https://www.morfrac.com/blog/news-1/farr-x2-5` | `farr x2`, `farr x2 for sale` | Missing metadata and blog URL ranking for commercial intent | Add title/meta immediately. If the page keeps ranking for buying-intent terms after rewrite, move this query cluster to a dedicated commercial landing page later. |

## Copy Direction

- Put the commercial head term in the first half of the title.
- Keep titles specific to product family or landing-page role rather than brand-only phrasing.
- Use meta descriptions to reinforce engineering value, application, and product-family fit.
- Preserve EN and ES language separation. Do not reuse English copy on Spanish URLs.

## Acceptance Criteria

- Each updated page has a unique title aligned to its query cluster.
- Each updated page has a meta description that supports CTR, not just brand language.
- Dogbone and mloop pages are updated first because they already have page-1 or near-page-1 visibility.
