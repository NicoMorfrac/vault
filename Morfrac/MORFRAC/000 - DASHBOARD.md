```dashboard
title: MORFRAC Command Center
rows:
  - height: 145
    columns:
      - width: 12
        widget:
          type: markdown
          content: |
            <div class="morfrac-hero">
              <div>
                <p class="morfrac-kicker">MORFRAC operating system</p>
                <h1>Control center</h1>
                <p>SEO execution, engineering knowledge, agent workflows, and current priorities in one place.</p>
              </div>
              <div class="morfrac-hero-actions">
                <a data-href="06_MARKETING/SEO_Execution_Queue/2026-05-23_Content_Briefs" href="06_MARKETING/SEO_Execution_Queue/2026-05-23_Content_Briefs" class="internal-link">Content briefs</a>
                <a data-href="06_MARKETING/SEO_Agent/Executive_Reviews/SEO_Executive_Review" href="06_MARKETING/SEO_Agent/Executive_Reviews/SEO_Executive_Review" class="internal-link">Executive review</a>
              </div>
            </div>
  - height: 145
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
  - height: 285
    columns:
      - width: 7
        widget:
          type: markdown
          content: |
            ## Command queue
            - [ ] Review [[06_MARKETING/SEO_Execution_Queue/2026-05-23_Content_Briefs|today's content briefs]]
            - [ ] Convert [[06_MARKETING/SEO_Content_Proposals/2026-05-23_Furling_Integration_Opportunity|furling opportunity]] into a publishable asset
            - [ ] Pull next actions from [[06_MARKETING/SEO_Agent/Action_Plans/2026-05-17_seo_action_plan|SEO action plan]]
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
            - [[06_MARKETING/Playbooks/Campaign_Playbook|Campaign playbook]]
  - height: 310
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
            height: 280
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
            height: 280
  - height: 280
    columns:
      - width: 4
        widget:
          type: markdown
          content: |
            ## SEO execution
            - [[06_MARKETING/SEO_Execution_Queue/2026-05-23_Content_Briefs|Content briefs]]
            - [[06_MARKETING/SEO_Execution_Queue/2026-05-17_Pillar_Page_Tasks|Pillar page tasks]]
            - [[06_MARKETING/SEO_Execution_Queue/2026-05-17_Metadata_Tasks|Metadata tasks]]
            - [[06_MARKETING/SEO_Execution_Queue/2026-05-17_Internal_Link_Tasks|Internal links]]
      - width: 4
        widget:
          type: markdown
          content: |
            ## Intelligence
            - [[06_MARKETING/SEO_Agent/Executive_Reviews/SEO_Executive_Review|Executive review]]
            - [[06_MARKETING/SEO_Agent/Authority_Hubs/2026-05-17_authority_hub_analysis|Authority hubs]]
            - [[06_MARKETING/SEO_Agent/Semantic_Clusters/2026-05-17_semantic_cluster_report|Semantic clusters]]
            - [[06_MARKETING/Competitors/Notes/2026-05-17_Competitor_Summary|Competitor summary]]
      - width: 4
        widget:
          type: markdown
          content: |
            ## Engineering
            - [[04_ENGINEERING/Materials/IglidurX_Bearing_Data|Iglidur X bearing data]]
            - [[04_ENGINEERING/logs/MORAAAAA-21_Blocked_Bearing_Analysis|Blocked bearing analysis]]
            - [[02_AGENTS/Engineering/SKILLS/bearing_design|Bearing design skill]]
            - [[02_AGENTS/Engineering/SKILLS/dyneema_loop_design|Dyneema loop design]]
  - height: 300
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
            height: 270
```
