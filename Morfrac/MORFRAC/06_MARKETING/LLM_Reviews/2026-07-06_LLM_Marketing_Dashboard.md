---
type: llm_marketing_dashboard
source_agent: Marketing
created: 2026-07-06
related_findings: []
related_concepts: []
related_projects:
  - GA4
related_reports: []
---

# Latest LLM Marketing Review Dashboard

Generated: 2026-07-06

Source review: [[2026-07-06_LLM_Marketing_Review]]

```dashboard
title: LLM Review Overview
rows:
  - columns:
      - width: 3
        widget:
          type: stat
          label: 7-day sessions
          value: "-73.3%"
          trend: "-73.3% risk"
          icon: activity
      - width: 3
        widget:
          type: stat
          label: 28-day sessions
          value: "48.5%"
          trend: "+48.5%"
          icon: line-chart
      - width: 3
        widget:
          type: stat
          label: Organic clicks
          value: "-28.0%"
          trend: "-28% risk"
          icon: mouse-pointer-click
      - width: 3
        widget:
          type: stat
          label: Organic CTR
          value: "-30.9%"
          trend: "-30.9% risk"
          icon: gauge
  - columns:
      - width: 4
        widget:
          type: stat
          label: Impressions
          value: "4.1%"
          trend: "+4.1%"
          icon: eye
      - width: 4
        widget:
          type: stat
          label: Position change
          value: "0.24"
          trend: "+0.24 risk"
          icon: move-vertical
      - width: 4
        widget:
          type: markdown
          content: "### Detected Topics\ndogbone, dogbones, farr x2, furling, mreel, pad eye, rigging, soft pad eye"
  - columns:
      - width: 6
        widget:
          type: link
          target: "[[2026-07-06_LLM_Marketing_Review]]"
          description: Full generated LLM review
      - width: 6
        widget:
          type: link
          target: "[[Latest_Marketing_Dashboard]]"
          description: Marketing KPI dashboard
```

> [!summary] Executive Summary
> Over the past week, Morfrac experienced a 73.3% drop in sessions over 7 day
> days while seeing an increase of 48.5% in sessions over 28 days. Despite th
> this uptick, organic click-through rates (CTR) dropped by -30.9%, indicatin
> indicating a significant decline in conversion quality. The SEO landscape h
> highlights opportunities for improvement, particularly with terms related t
> to "dogbone," "soft pad eye," and "mreel." These findings suggest that whil
> while there is potential traffic growth, Morfrac needs immediate attention 
> on reversing the organic CTR decline and optimizing non-branded search quer
> queries.

> [!danger] Key Risks
> 1. **Traffic Drop**: A 73.3% decrease in sessions over 7 days poses a criti
> critical risk to visibility.
> 2. **CTR Deterioration**: An -30.9% drop in CTR signals a decline in the ef
> effectiveness of keyword targeting and landing page quality.
> 3. **Ranking Losses**: While there is no explicit mention of ranking losses
> losses, the significant changes suggest potential issues.
> 4. **Weak Channels**: The dependency on branded traffic is concerning as no
> non-branded acquisition needs reinforcement.

> [!success] Key Opportunities
> 1. **Low CTR + High Impressions Queries**: "Dogbone" and "soft pad eye" ter
> terms have high impressions but low CTR, offering room for optimization.
> 2. **Ranking Opportunities**: "mreel" and "Farr X2" show growing topics wit
> with good SEO visibility.
> 3. **Growing Topics**: Continued focus on dogbone-related queries could yie
> yield significant growth.

> [!todo] Strategic Priorities
> ### High Priority
> 1. **Reverse Organic CTR Decline**
>    - **Action**: Conduct a thorough audit of low-performing landing pages a
> and update content to improve relevance and user experience.
>    - **Reason**: Direct correlation between high impressions and low CTR in
> indicates poor page quality or outdated content.
>    - **Expected Impact**: Increase organic traffic conversion rates by 15% 
> within 3 months.
> 
> ### Medium Priority
> 2. **Optimize Non-Branded SEO Visibility**
>    - **Action**: Develop targeted keyword strategies for "dogbone," "soft p
> pad eye," and other related terms.
>    - **Reason**: These keywords have significant potential for high-quality
> high-quality traffic.
>    - **Expected Impact**: Boost non-branded traffic by 30% over the next qu
> quarter.
> 
> ### Low Priority
> 3. **Expand Content Around Rising Search Topics**
>    - **Action**: Create educational content focused on "dogbone" rigging sy
> systems and related performance optimization topics.
>    - **Reason**: Growing interest in these terms signals commercial opportu
> opportunities.
>    - **Expected Impact**: Enhance organic search visibility for rising topi
> topics by 20% within six months.

> [!tip] Recommended Actions
> ### High Priority
> 
> 1. **Investigate Traffic Drops**
>    - **Action**: Perform an A/B testing of website elements and meta descri
> descriptions to identify root causes.
>    - **Reason**: Immediate need to understand if changes correlate with rec
> recent updates or external factors.
>    - **Expected Impact**: Stabilize sessions by 7 days post-investigation.
> 
> 2. **Review Ranking Losses**
>    - **Action**: Analyze keyword rankings and update SEO strategies accordi
> accordingly.
>    - **Reason**: Ensures that Morfrac remains competitive in organic search
> search results.
>    - **Priority**: Urgent
>    - **Expected Impact**: Reclaim lost positions within 1-3 months.
> 
> ### Medium Priority
> 
> 3. **Improve Low CTR Queries**
>    - **Action**: Enhance content relevance and optimize meta tags for "dogb
> "dogbone" and "soft pad eye."
>    - **Reason**: Directly addresses the issue of high impressions with low 
> CTR.
>    - **Expected Impact**: Increase CTR by 10% over three months.
> 
> 4. **Strengthen Non-Branded SEO**
>    - **Action**: Implement keyword optimization strategies for new terms li
> like "dogbone" and "soft pad eye."
>    - **Reason**: Expands the reach of non-branded traffic.
>    - **Expected Impact**: Increase non-branded sessions by 30% in three mon
> months.
> 
> ### Low Priority
> 
> 5. **Monitor Current Trends**
>    - **Action**: Maintain regular monitoring of ongoing trends and adjust s
> strategies as needed.
>    - **Reason**: Ensures continuous optimization and adaptability to market
> market changes.
>    - **Priority**: Ongoing
>    - **Expected Impact**: Continuous improvement in SEO performance over ti
> time.

> [!quote] Final Assessment
> Overall, the situation is **Negative** due to significant traffic drops and
> and CTR deterioration. However, there are clear opportunities for growth th
> through focused SEO efforts and content optimization. Immediate actions can
> can mitigate risks and capitalize on emerging trends.

## Review Inputs

| Source | File |
| --- | --- |
| GA4 report | [[2026-07-06_Weekly_Marketing_Report]] |
| SEO report | [[2026-07-06_SEO_Query_Analysis]] |
| Marketing review | [[2026-07-06_Marketing_Review]] |
| Full LLM review | [[2026-07-06_LLM_Marketing_Review]] |

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
