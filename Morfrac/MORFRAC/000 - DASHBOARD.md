```dashboard
title: MORFRAC Control Dashboard
rows:
  - height: 150
    columns:
      - width: 3
        widget:
          type: stat
          label: Vault notes
          value: "223"
          icon: files
      - width: 3
        widget:
          type: stat
          label: Agent specs
          value: "6"
          icon: users
      - width: 3
        widget:
          type: stat
          label: Marketing notes
          value: "172"
          icon: megaphone
      - width: 3
        widget:
          type: stat
          label: Engineering notes
          value: "5"
          icon: cog
  - height: 70
    columns:
      - width: 12
        widget:
          type: heading
          text: Daily Command
          level: 2
  - height: 260
    columns:
      - width: 5
        widget:
          type: markdown
          content: |
            ## Today's operating loop
            - [ ] Review [[06_MARKETING/SEO_Execution_Queue/2026-05-23_Content_Briefs]]
            - [ ] Check [[06_MARKETING/SEO_Content_Proposals/2026-05-23_Furling_Integration_Opportunity]]
            - [ ] Triage [[06_MARKETING/SEO_Agent/Action_Plans/2026-05-17_seo_action_plan]]
            - [ ] Update agent memory after completed work
      - width: 4
        widget:
          type: markdown
          content: |
            ## Current priorities
            - Content briefs
            - Furling integration opportunity
            - Internal linking opportunities
            - SEO pipeline health
      - width: 3
        widget:
          type: link
          target: "[[06_MARKETING/SEO_Agent/Executive_Reviews/SEO_Executive_Review]]"
          description: Open the live SEO executive review.
  - height: 310
    columns:
      - width: 4
        widget:
          type: link
          target: "[[02_AGENTS/Project_Manager/AGENTS]]"
          description: Coordinate work, owners, and next actions.
      - width: 4
        widget:
          type: link
          target: "[[02_AGENTS/Engineering/AGENTS]]"
          description: Engineering analysis, calculations, and product constraints.
      - width: 4
        widget:
          type: link
          target: "[[02_AGENTS/SEO/AGENTS]]"
          description: SEO intelligence, execution, and review pipeline.
  - height: 360
    columns:
      - width: 6
        widget:
          type: markdown
          content: |
            ## Marketing command center
            - [[06_MARKETING/SEO_Execution_Queue/2026-05-23_Content_Briefs]]
            - [[06_MARKETING/SEO_Content_Drafts/2026-05-18_Dogbone_Technical_Guide]]
            - [[06_MARKETING/SEO_Agent/Pipeline_Health/2026-05-17_pipeline_health_report]]
            - [[06_MARKETING/SEO_Agent/Internal_Linking/2026-05-17_internal_link_opportunities]]
            - [[06_MARKETING/SEO_Agent/Fix_Recommendations/2026-05-17_seo_fix_recommendations]]
            - [[06_MARKETING/Competitors/Notes/2026-05-17_Competitor_Summary]]
      - width: 6
        widget:
          type: markdown
          content: |
            ## Engineering and system references
            - [[04_ENGINEERING/Materials/IglidurX_Bearing_Data]]
            - [[04_ENGINEERING/logs/MORAAAAA-21_Blocked_Bearing_Analysis]]
            - [[02_AGENTS/Engineering/SKILLS/bearing_design]]
            - [[02_AGENTS/Engineering/SKILLS/dyneema_loop_design]]
            - [[00_SYSTEM/PROJECT_RULES]]
            - [[00_SYSTEM/AGENT_COMMUNICATION]]
  - height: 420
    columns:
      - width: 6
        widget:
          type: embed
          target: "[[06_MARKETING/SEO_Execution_Queue/2026-05-23_Content_Briefs]]"
      - width: 6
        widget:
          type: embed
          target: "[[06_MARKETING/SEO_Content_Proposals/2026-05-23_Furling_Integration_Opportunity]]"
  - height: 340
    columns:
      - width: 4
        widget:
          type: link
          target: "[[06_MARKETING/Playbooks/SEO_Playbook]]"
          description: Repeatable SEO workflow and quality bar.
      - width: 4
        widget:
          type: link
          target: "[[06_MARKETING/Playbooks/Campaign_Playbook]]"
          description: Campaign planning and execution process.
      - width: 4
        widget:
          type: link
          target: "[[99_TEMPLATES/Project_Index_Template]]"
          description: Start structured project documentation.
  - height: 300
    columns:
      - width: 12
        widget:
          type: markdown
          content: |
            ## Add when Bases Chart is enabled
            The Dashboards plugin is active, but Bases Chart is not currently enabled in this vault. When you install it, replace this note with chart widgets for note volume, SEO report cadence, and content output by folder.
```
