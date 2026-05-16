@echo off

cd /d C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC\02_AGENTS\Marketing

echo =========================
echo RUNNING GA4 REPORT
echo =========================

py weekly_ga4_report.py
if errorlevel 1 exit /b %errorlevel%

echo.
echo =========================
echo RUNNING SEARCH CONSOLE REPORT
echo =========================

py search_console_report.py
if errorlevel 1 exit /b %errorlevel%

echo.
echo =========================
echo RUNNING MARKETING REVIEW
echo =========================

py marketing_review.py
if errorlevel 1 exit /b %errorlevel%

echo.
echo =========================
echo RUNNING LOCAL LLM REVIEW
echo =========================

py marketing_llm_review.py
if errorlevel 1 exit /b %errorlevel%

echo.
echo =========================
echo RUNNING MARKETING DASHBOARD
echo =========================

py marketing_dashboard.py
if errorlevel 1 exit /b %errorlevel%

echo.
echo =========================
echo RUNNING KEYWORD OPPORTUNITIES
echo =========================

py keyword_opportunities.py
if errorlevel 1 exit /b %errorlevel%

echo.
echo =========================
echo RUNNING CONTENT ARCHETYPES
echo =========================

py content_archetypes.py
if errorlevel 1 exit /b %errorlevel%

echo.
echo =========================
echo RUNNING COMPETITOR SUMMARY
echo =========================

py competitor_summary.py
if errorlevel 1 exit /b %errorlevel%

echo.
echo =========================
echo RUNNING COMPETITOR CHANGES
echo =========================

py competitor_change_detection.py
if errorlevel 1 exit /b %errorlevel%

echo.
echo =========================
echo RUNNING LINKEDIN TOPIC PROPOSALS
echo =========================

py linkedin_topic_proposals.py
if errorlevel 1 exit /b %errorlevel%

echo.
echo =========================
echo MARKETING PIPELINE COMPLETE
echo =========================

pause
