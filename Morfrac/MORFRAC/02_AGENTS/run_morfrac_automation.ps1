$ErrorActionPreference = "Stop"

$BasePath = "C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC"
$MarketingPath = Join-Path $BasePath "02_AGENTS\Marketing"
$SeoScriptsPath = Join-Path $BasePath "06_MARKETING\SEO_Agent\Scripts"
$LogPath = Join-Path $BasePath "06_MARKETING\Automation_Logs"

New-Item -ItemType Directory -Force -Path $LogPath | Out-Null

$RunStamp = Get-Date -Format "yyyy-MM-dd_HH-mm-ss"
$MainLog = Join-Path $LogPath "$RunStamp`_morfrac_automation.log"

function Write-Log {
    param([string]$Message)
    $line = "[{0}] {1}" -f (Get-Date -Format "yyyy-MM-dd HH:mm:ss"), $Message
    $line | Tee-Object -FilePath $MainLog -Append
}

function Run-Step {
    param(
        [string]$Name,
        [string]$WorkingDirectory,
        [string]$ScriptName
    )

    $stepSafeName = ($Name -replace '[^a-zA-Z0-9_-]+', '_').Trim('_')
    $StepLog = Join-Path $LogPath "$RunStamp`_$stepSafeName.log"

    Write-Log "START: $Name"
    Write-Log "Directory: $WorkingDirectory"
    Write-Log "Command: py $ScriptName"
    Write-Log "Step log: $StepLog"

    Push-Location $WorkingDirectory
    try {
        & py $ScriptName *> $StepLog
        $exitCode = $LASTEXITCODE
    }
    finally {
        Pop-Location
    }

    if ($exitCode -ne 0) {
        Write-Log "FAILED: $Name exited with code $exitCode"
        Write-Log "See step log: $StepLog"
        exit $exitCode
    }

    Write-Log "OK: $Name"
}

Write-Log "MORFRAC automation started."
Write-Log "Base path: $BasePath"

$MarketingSteps = @(
    @{ Name = "Marketing - GA4 Report"; Script = "weekly_ga4_report.py" },
    @{ Name = "Marketing - Search Console Report"; Script = "search_console_report.py" },
    @{ Name = "Marketing - Marketing Review"; Script = "marketing_review.py" },
    @{ Name = "Marketing - Local LLM Review"; Script = "marketing_llm_review.py" },
    @{ Name = "Marketing - Marketing Dashboard"; Script = "marketing_dashboard.py" },
    @{ Name = "Marketing - Keyword Opportunities"; Script = "keyword_opportunities.py" },
    @{ Name = "Marketing - Content Archetypes"; Script = "content_archetypes.py" },
    @{ Name = "Marketing - Competitor Summary"; Script = "competitor_summary.py" },
    @{ Name = "Marketing - Competitor Changes"; Script = "competitor_change_detection.py" },
    @{ Name = "Marketing - LinkedIn Topic Proposals"; Script = "linkedin_topic_proposals.py" }
)

foreach ($step in $MarketingSteps) {
    Run-Step -Name $step.Name -WorkingDirectory $MarketingPath -ScriptName $step.Script
}

$SeoSteps = @(
    @{ Name = "SEO - Crawl"; Script = "seo_crawler.py" },
    @{ Name = "SEO - Leverage Analysis"; Script = "seo_leverage_analysis.py" },
    @{ Name = "SEO - Template Cluster Analysis"; Script = "seo_template_cluster_analysis.py" },
    @{ Name = "SEO - Fix Recommendations"; Script = "seo_fix_generator.py" },
    @{ Name = "SEO - Internal Linking Opportunities"; Script = "seo_internal_link_opportunities.py" },
    @{ Name = "SEO - Metadata Targets"; Script = "seo_metadata_targets.py" },
    @{ Name = "SEO - Metadata Recommendations"; Script = "seo_metadata_recommendation_engine.py" },
    @{ Name = "SEO - Duplicate Content Analysis"; Script = "seo_duplicate_content_analysis.py" },
    @{ Name = "SEO - Indexation Audit"; Script = "seo_indexation_audit.py" },
    @{ Name = "SEO - Authority Hub Analysis"; Script = "seo_authority_hub_analysis.py" },
    @{ Name = "SEO - Action Plan"; Script = "seo_agent_action_plan.py" },
    @{ Name = "SEO - Internal Link Graph Analysis"; Script = "seo_internal_link_graph.py" },
    @{ Name = "SEO - Contextual Link Recommendations"; Script = "seo_contextual_link_recommender.py" },
    @{ Name = "SEO - Search Console Merge Analysis"; Script = "seo_search_console_merge.py" },
    @{ Name = "SEO - Semantic Cluster Analysis"; Script = "seo_semantic_cluster_analysis.py" },
    @{ Name = "SEO - Content Gap Analysis"; Script = "seo_content_gap_analysis.py" },
    @{ Name = "SEO - Topic Authority Map"; Script = "seo_topic_authority_map.py" },
    @{ Name = "SEO - Entity Relationship Map"; Script = "seo_entity_relationship_map.py" },
    @{ Name = "SEO - Executive Review"; Script = "seo_executive_review.py" },
    @{ Name = "SEO - Historical Comparison"; Script = "seo_historical_comparison.py" },
    @{ Name = "SEO - Pipeline Health Check"; Script = "seo_pipeline_health_check.py" },
    @{ Name = "SEO - Dashboard"; Script = "seo_dashboard.py" }
)

foreach ($step in $SeoSteps) {
    Run-Step -Name $step.Name -WorkingDirectory $SeoScriptsPath -ScriptName $step.Script
}

Write-Log "MORFRAC automation completed successfully."
exit 0
