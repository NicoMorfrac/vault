```dashboard
title: MORFRAC Command Center
rows:
  - height: 138
    columns:
      - width: 3
        widget:
          type: stat
          label: Vault notes
          value: "228"
          trend: +5
          icon: files
      - width: 3
        widget:
          type: stat
          label: Created today
          value: "13"
          trend: +13
          icon: plus-circle
      - width: 3
        widget:
          type: stat
          label: Modified today
          value: "21"
          trend: +21
          icon: refresh-cw
      - width: 3
        widget:
          type: stat
          label: SEO reports
          value: "69"
          trend: +0
          icon: line-chart
  - height: 245
    columns:
      - width: 7
        widget:
          type: markdown
          content: |
            ## Command queue
            - [ ] Review [[06_MARKETING/SEO_Execution_Queue/2026-05-23_Content_Briefs|content briefs]]
            - [ ] Turn [[06_MARKETING/SEO_Content_Proposals/2026-05-23_Furling_Integration_Opportunity|furling opportunity]] into an asset
            - [ ] Pull next moves from [[06_MARKETING/SEO_Agent/Action_Plans/2026-05-17_seo_action_plan|SEO action plan]]
            - [ ] Check [[06_MARKETING/SEO_Agent/Pipeline_Health/2026-05-17_pipeline_health_report|pipeline health]]
      - width: 5
        widget:
          type: markdown
          content: |
            ## Launchpad
            - [[02_AGENTS/Project_Manager/AGENTS|Project manager]]
            - [[02_AGENTS/SEO/AGENTS|SEO agent]]
            - [[02_AGENTS/Engineering/AGENTS|Engineering agent]]
            - [[06_MARKETING/Playbooks/SEO_Playbook|SEO playbook]]
            - [[06_MARKETING/SEO_Agent/Executive_Reviews/SEO_Executive_Review|Executive review]]
  - height: 305
    columns:
      - width: 8
        widget:
          type: chart
          chart:
            type: bar
            sql: SELECT COUNT(*) FROM notes GROUP BY month(file.ctime) ORDER BY label asc
            title: Notes created by month
            dataLabels: top
            showGridlines: false
            colors:
              - "#4e79a7"
              - "#f28e2b"
            height: 275
      - width: 4
        widget:
          type: chart
          chart:
            type: pie
            sql: SELECT COUNT(*) FROM notes GROUP BY month(file.mtime) ORDER BY label asc
            title: Notes updated by month
            dataLabels: outside
            colors:
              - "#4e79a7"
              - "#f28e2b"
              - "#59a14f"
            height: 275
  - height: 245
    columns:
      - width: 4
        widget:
          type: markdown
          content: |
            ## SEO execution
            - [[06_MARKETING/SEO_Execution_Queue/2026-05-23_Content_Briefs|Content briefs]]
            - [[06_MARKETING/SEO_Execution_Queue/2026-05-17_Pillar_Page_Tasks|Pillar pages]]
            - [[06_MARKETING/SEO_Execution_Queue/2026-05-17_Metadata_Tasks|Metadata]]
            - [[06_MARKETING/SEO_Execution_Queue/2026-05-17_Internal_Link_Tasks|Internal links]]
      - width: 4
        widget:
          type: markdown
          content: |
            ## Intelligence
            - [[06_MARKETING/SEO_Agent/Executive_Reviews/SEO_Executive_Review|Executive review]]
            - [[06_MARKETING/SEO_Agent/Authority_Hubs/2026-05-17_authority_hub_analysis|Authority hubs]]
            - [[06_MARKETING/SEO_Agent/Semantic_Clusters/2026-05-17_semantic_cluster_report|Semantic clusters]]
            - [[06_MARKETING/Competitors/Notes/2026-05-17_Competitor_Summary|Competitors]]
      - width: 4
        widget:
          type: markdown
          content: |
            ## Engineering
            - [[04_ENGINEERING/Materials/IglidurX_Bearing_Data|Iglidur X bearing data]]
            - [[04_ENGINEERING/logs/MORAAAAA-21_Blocked_Bearing_Analysis|Blocked bearing analysis]]
            - [[02_AGENTS/Engineering/SKILLS/bearing_design|Bearing design]]
            - [[02_AGENTS/Engineering/SKILLS/dyneema_loop_design|Dyneema loops]]
  - height: 295
    columns:
      - width: 12
        widget:
          type: chart
          chart:
            type: calendar
            sql: SELECT COUNT(*) FROM notes
            title: Vault activity
            colors:
              - "#264653"
              - "#2a9d8f"
              - "#e9c46a"
              - "#f4a261"
            height: 265
```
## Recent Reports

```dataview
TABLE source_agent, type, created
FROM ""
WHERE source_agent
SORT created DESC
LIMIT 25
```

## Findings

```dataview
TABLE related_concepts
FROM ""
WHERE contains(file.name,"MORAAAAAA")
SORT file.name DESC
```

## Retrofit Complexity

```dataview
LIST
WHERE contains(related_concepts,"RETROFIT_COMPLEXITY")
```

## Reports by Agent

```dataview
TABLE length(related_findings) AS Findings
FROM ""
WHERE source_agent
SORT source_agent ASC
```

## Reports Missing Relationships

```dataview
TABLE source_agent, created
FROM ""
WHERE
length(related_findings)=0 AND
length(related_concepts)=0 AND
length(related_projects)=0 AND
length(related_reports)=0
```
