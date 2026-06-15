---
type: llm_marketing_dashboard
source_agent: Marketing
created: 2026-06-15
related_findings: []
related_concepts: []
related_projects:
  - GA4
related_reports: []
---

# Latest LLM Marketing Review Dashboard

Generated: 2026-06-15

Source review: [[2026-06-15_LLM_Marketing_Review]]

```dashboard
title: LLM Review Overview
rows:
  - columns:
      - width: 3
        widget:
          type: stat
          label: 7-day sessions
          value: "46.3%"
          trend: "+46.3%"
          icon: activity
      - width: 3
        widget:
          type: stat
          label: 28-day sessions
          value: "-38.5%"
          trend: "-38.5% risk"
          icon: line-chart
      - width: 3
        widget:
          type: stat
          label: Organic clicks
          value: "41.2%"
          trend: "+41.2%"
          icon: mouse-pointer-click
      - width: 3
        widget:
          type: stat
          label: Organic CTR
          value: "18.4%"
          trend: "+18.4%"
          icon: gauge
  - columns:
      - width: 4
        widget:
          type: stat
          label: Impressions
          value: "19.2%"
          trend: "+19.2%"
          icon: eye
      - width: 4
        widget:
          type: stat
          label: Position change
          value: "-4.03"
          trend: "-4.03"
          icon: move-vertical
      - width: 4
        widget:
          type: markdown
          content: "### Detected Topics\ndogbone, dogbones, farr x2, friction ring, mreel, pad eye, rigging"
  - columns:
      - width: 6
        widget:
          type: link
          target: "[[2026-06-15_LLM_Marketing_Review]]"
          description: Full generated LLM review
      - width: 6
        widget:
          type: link
          target: "[[Latest_Marketing_Dashboard]]"
          description: Marketing KPI dashboard
```

> [!summary] Executive Summary
> MORFRAC's latest reports indicate significant fluctuations in traffic, with
> with a 28-day session decrease of -38.5%. Despite this, there are notable p
> positive trends such as increased organic click-through rates (CTR) by 18.4
> 18.4% and an overall improvement in organic clicks up 41.2%. SEO visibility
> visibility for specific queries like "dogbone," "mreel," and "Farr X2" has 
> improved. However, the critical risk of a substantial drop in branded traff
> traffic is present.

> [!danger] Key Risks
> - **Traffic Deterioration:** A significant -38.5% decrease in 28-day sessio
> sessions.
> - **CTR Deterioration:** An alarming -16.1% decline over two weeks, indicat
> indicating potential issues with content quality or relevance.
> - **Ranking Losses:** A position change of -4.03 suggests that some pages a
> are losing their rankings.
> - **Dependency on Branded Traffic:** There is a high reliance on branded se
> search terms for traffic acquisition.

> [!success] Key Opportunities
> - **Low CTR + High Impressions:** The "dogbone" query presents an opportuni
> opportunity with low CTR (18.4%) but high impressions, suggesting potential
> potential content optimization could improve engagement.
> - **Ranking Opportunities:** Specific queries like "mreel," "Farr X2," and 
> related terms have improved ranking positions, offering a chance to capital
> capitalize on growing interest in these areas.
> - **Growing Topics:** Emerging searches indicate rising interest around rig
> rigging systems and dogbone-related products.

> [!todo] Strategic Priorities
> 1. **High Priority**
>    - Investigate the cause of the 28-day session drop and address any under
> underlying issues promptly.
>    
> 2. **Medium Priority**
>    - Optimize content for low CTR high-impression queries to drive better e
> engagement.
>    - Strengthen non-branded SEO visibility through targeted keyword optimiz
> optimization.
> 3. **Low Priority**
>    - Continue monitoring traffic trends and adjust campaigns as needed.

> [!tip] Recommended Actions
> - **Action:** Investigate the reasons behind the significant decline in ses
> sessions over 28 days.
> - **Reason:** The drop could be due to changes in user behavior, indexing i
> issues, or recent website modifications.
> - **Expected Impact:** Identifying and addressing the root cause will stabi
> stabilize traffic.
> - **Priority:** High
> 
> - **Action:** Develop SEO content for low CTR high-impression queries like 
> "dogbone."
> - **Reason:** Improving engagement on these queries can lead to higher conv
> conversion rates.
> - **Expected Impact:** Enhanced content will increase click-through and pot
> potentially boost conversions.
> - **Priority:** Medium
> 
> - **Action:** Create targeted SEO landing pages focusing on emerging topics
> topics such as mreel, Farr X2, and dogbone rigging systems.
> - **Reason:** These queries indicate growing interest and potential for con
> conversion.
> - **Expected Impact:** Enhanced visibility will drive more traffic to high-
> high-performing product pages.
> - **Priority:** Medium
> 
> - **Action:** Monitor organic click-through rates (CTR) and make adjustment
> adjustments based on performance data.
> - **Reason:** Ensuring that content remains relevant and engaging is crucia
> crucial for maintaining high CTRs.
> - **Expected Impact:** Continuous optimization will maintain or improve eng
> engagement levels.
> - **Priority:** Low

> [!quote] Final Assessment
> **Overall: Negative**
> 
> The significant traffic drop, coupled with the deterioration in organic CTR
> CTR, indicates a pressing need to address these issues. However, positive t
> trends in certain SEO areas and growing topics suggest potential for recove
> recovery through strategic efforts.
> 
> Justification:
> - The data shows clear anomalies in key metrics such as session changes and
> and CTR.
> - Opportunities exist but require focused attention and action to capitaliz
> capitalize on them effectively.
> 
> By implementing the recommended actions, MORFRAC can mitigate risks and lev
> leverage opportunities to stabilize and improve its online presence.

## Review Inputs

| Source | File |
| --- | --- |
| GA4 report | [[2026-06-15_Weekly_Marketing_Report]] |
| SEO report | [[2026-06-15_SEO_Query_Analysis]] |
| Marketing review | [[2026-06-15_Marketing_Review]] |
| Full LLM review | [[2026-06-15_LLM_Marketing_Review]] |

## LLM Review History

```dataview
TABLE created AS "Created", source_agent AS "Agent", related_reports AS "Inputs"
FROM "06_MARKETING/LLM_Reviews"
WHERE type = "llm_marketing_review"
SORT created DESC
LIMIT 10
```

## Related Links

### Projects
- [[GA4]]
