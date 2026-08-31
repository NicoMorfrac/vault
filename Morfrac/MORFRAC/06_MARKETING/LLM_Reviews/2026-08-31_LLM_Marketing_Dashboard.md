---
type: llm_marketing_dashboard
source_agent: Marketing
created: 2026-08-31
related_findings: []
related_concepts: []
related_projects:
  - GA4
related_reports: []
---

# Latest LLM Marketing Review Dashboard

Generated: 2026-08-31

Source review: [[2026-08-31_LLM_Marketing_Review]]

```dashboard
title: LLM Review Overview
rows:
  - columns:
      - width: 3
        widget:
          type: stat
          label: 7-day sessions
          value: "-89.8%"
          trend: "-89.8% risk"
          icon: activity
      - width: 3
        widget:
          type: stat
          label: 28-day sessions
          value: "125.0%"
          trend: "+125%"
          icon: line-chart
      - width: 3
        widget:
          type: stat
          label: Organic clicks
          value: "-41.3%"
          trend: "-41.3% risk"
          icon: mouse-pointer-click
      - width: 3
        widget:
          type: stat
          label: Organic CTR
          value: "-23.2%"
          trend: "-23.2% risk"
          icon: gauge
  - columns:
      - width: 4
        widget:
          type: stat
          label: Impressions
          value: "-23.6%"
          trend: "-23.6% risk"
          icon: eye
      - width: 4
        widget:
          type: stat
          label: Position change
          value: "0.45"
          trend: "+0.45 risk"
          icon: move-vertical
      - width: 4
        widget:
          type: markdown
          content: "### Detected Topics\ndogbone, dogbones, farr x2, mreel, pad eye, rigging, soft pad eye"
  - columns:
      - width: 6
        widget:
          type: link
          target: "[[2026-08-31_LLM_Marketing_Review]]"
          description: Full generated LLM review
      - width: 6
        widget:
          type: link
          target: "[[Latest_Marketing_Dashboard]]"
          description: Marketing KPI dashboard
```

> [!summary] Executive Summary
> Recent data shows a significant drop in 7-day sessions (-89.8%) and organic
> organic clicks (-41.3%) while 28-day sessions have increased by 125.0%. Org
> Organic CTR has deteriorated by 23.2%, and ranking positions have improved 
> slightly. Opportunities include dogbone-related queries, soft pad eye, mree
> mreel, and Farr X2 keyword visibility. Key risks include potential dependen
> dependency on branded traffic and the need to address declining organic CTR
> CTR and clicks. Strategic priorities should focus on improving non-branded 
> traffic, optimizing high-impact content, and maintaining trend analysis.

> [!danger] Key Risks
> - **Traffic Drops:** A sharp decline in 7-day sessions (-89.8%) and organic
> organic clicks (-41.3%) could indicate a significant issue with organic tra
> traffic.
> - **CTR Deterioration:** Organic CTR has dropped by 23.2%, which can negati
> negatively impact overall visibility and click-through rates.
> - **Ranking Losses:** While ranking positions have improved slightly, organ
> organic impression changes (-23.6%) suggest potential challenges in maintai
> maintaining visibility.
> - **Weak Channels:** The dependency on branded traffic can limit the compan
> company's overall reach and visibility.

> [!success] Key Opportunities
> - **SEO Growth:** Dogbone-related queries have significant SEO visibility, 
> indicating a market opportunity.
> - **Non-Branded Acquisition:** Soft pad eye and mreel keywords present oppo
> opportunities for non-branded traffic acquisition.
> - **Conversion Opportunities:** High-impression queries like dogbone and Fa
> Farr X2 can be leveraged for better conversion rates.
> - **Content Ideas:** Creating content around dogbone rigging systems, soft 
> pad eyes, and mreel can enhance visibility and engagement.

> [!todo] Strategic Priorities
> 1. **High Priority:**
>    - **Improve Non-Branded SEO Traffic:** Develop content around dogbone ri
> rigging systems, soft pad eyes, and mreel to enhance non-branded traffic an
> and CTR.
>    - **Optimize High-Impact Keywords:** Focus on high-impression queries li
> like dogbone to improve visibility and conversion rates.
> 
> 2. **Medium Priority:**
>    - **Address Declining CTR:** Analyze and optimize low CTR queries with s
> strong impressions to improve click-through rates.
>    - **Strengthen SEO Content:** Create educational content around soft pad
> pad eyes and mreel to strengthen overall SEO performance.
> 
> 3. **Low Priority:**
>    - **Monitor Trends:** Continue to monitor current trends and adjust stra
> strategies as needed.
>    - **Maintain Reporting Cadence:** Ensure consistent reporting to track p
> progress and identify new opportunities.

> [!tip] Recommended Actions
> 1. **Action:** Investigate major traffic or SEO drops immediately.
>    - **Reason:** Significant drops in 7-day sessions and organic clicks cou
> could indicate issues such as algorithm changes, website maintenance, or ex
> external market factors.
>    - **Expected Impact:** Quick resolution can prevent further declines and
> and ensure steady traffic.
>    - **Priority:** High
> 
> 2. **Action:** Review ranking losses and CTR deterioration.
>    - **Reason:** A drop in CTR and ranking positions indicates potential pr
> problems with keyword optimization and content relevance.
>    - **Expected Impact:** Improving CTR and rankings can significantly enha
> enhance organic traffic and visibility.
>    - **Priority:** High
> 
> 3. **Action:** Validate correlation with website changes, indexing changes,
> changes, or external factors.
>    - **Reason:** Understanding the cause of these changes is crucial to imp
> implement targeted solutions.
>    - **Expected Impact:** Identifying the root cause can prevent recurring 
> issues and ensure long-term stability.
>    - **Priority:** Medium
> 
> 4. **Action:** Develop SEO landing pages and LinkedIn content focused on do
> dogbone rigging systems.
>    - **Reason:** High SEO visibility for dogbone-related queries indicates 
> a market opportunity.
>    - **Expected Impact:** Enhanced organic traffic and improved conversion 
> rates.
>    - **Priority:** High
> 
> 5. **Action:** Create educational content around soft pad eyes and mreel.
>    - **Reason:** These keywords present opportunities for non-branded traff
> traffic acquisition.
>    - **Expected Impact:** Increased visibility and engagement, leading to b
> better SEO performance.
>    - **Priority:** Medium

> [!quote] Final Assessment
> Overall, the situation is **Negative** due to the significant drop in organ
> organic traffic and CTR. However, there are clear opportunities to capitali
> capitalize on high-impression queries and non-branded traffic. Addressing t
> these risks and leveraging the identified opportunities will help to mitiga
> mitigate negative trends and improve overall performance.
> 
> By focusing on specific, data-driven actions, MORFRAC can improve its SEO a
> and non-branded traffic, ultimately driving more conversions and enhancing 
> its market presence.

## Review Inputs

| Source | File |
| --- | --- |
| GA4 report | [[2026-08-31_Weekly_Marketing_Report]] |
| SEO report | [[2026-08-31_SEO_Query_Analysis]] |
| Marketing review | [[2026-08-31_Marketing_Review]] |
| Full LLM review | [[2026-08-31_LLM_Marketing_Review]] |

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
