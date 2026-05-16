@echo off
cd /d C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC

echo ==============================
echo MORFRAC SEO PIPELINE START
echo ==============================

echo.
echo STEP 1 - Search Console Report
cd /d C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC\02_AGENTS\Marketing
py search_console_report.py
if errorlevel 1 exit /b %errorlevel%

echo.
echo STEP 2 - SEO Crawl
cd /d C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC\06_MARKETING\SEO_Agent\Scripts
py seo_crawler.py
if errorlevel 1 exit /b %errorlevel%

echo.
echo STEP 3 - SEO Leverage Analysis
py seo_leverage_analysis.py
if errorlevel 1 exit /b %errorlevel%

echo.
echo STEP 4 - Template Cluster Analysis
py seo_template_cluster_analysis.py
if errorlevel 1 exit /b %errorlevel%

echo.
echo STEP 5 - SEO Fix Recommendations
py seo_fix_generator.py
if errorlevel 1 exit /b %errorlevel%

echo.
echo STEP 6 - Internal Linking Opportunities
py seo_internal_link_opportunities.py
if errorlevel 1 exit /b %errorlevel%

echo.
echo STEP 7 - Metadata Targets
py seo_metadata_targets.py
if errorlevel 1 exit /b %errorlevel%

echo.
echo STEP 8 - Metadata Recommendations
py seo_metadata_recommendation_engine.py
if errorlevel 1 exit /b %errorlevel%

echo.
echo STEP 9 - Duplicate Content Analysis
py seo_duplicate_content_analysis.py
if errorlevel 1 exit /b %errorlevel%

echo.
echo STEP 10 - Indexation Audit
py seo_indexation_audit.py
if errorlevel 1 exit /b %errorlevel%

echo.
echo STEP 11 - Authority Hub Analysis
py seo_authority_hub_analysis.py
if errorlevel 1 exit /b %errorlevel%

echo.
echo STEP 12 - SEO Action Plan
py seo_agent_action_plan.py
if errorlevel 1 exit /b %errorlevel%

echo.
echo STEP 13 - Internal Link Graph Analysis
py seo_internal_link_graph.py
if errorlevel 1 exit /b %errorlevel%

echo.
echo STEP 14 - Contextual Link Recommendations
py seo_contextual_link_recommender.py
if errorlevel 1 exit /b %errorlevel%

echo.
echo STEP 15 - Search Console Merge Analysis
py seo_search_console_merge.py
if errorlevel 1 exit /b %errorlevel%

echo.
echo STEP 16 - Executive SEO Review
py seo_executive_review.py
if errorlevel 1 exit /b %errorlevel%

echo.
echo STEP 17 - Historical SEO Comparison
py seo_historical_comparison.py
if errorlevel 1 exit /b %errorlevel%

echo.
echo ==============================
echo MORFRAC SEO PIPELINE COMPLETE
echo ==============================

pause
