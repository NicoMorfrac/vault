@echo off

cd /d C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC\02_AGENTS\Marketing

echo =========================
echo RUNNING GA4 REPORT
echo =========================

py weekly_ga4_report.py

echo.
echo =========================
echo RUNNING SEARCH CONSOLE REPORT
echo =========================

py search_console_report.py

echo.
echo =========================
echo RUNNING MARKETING REVIEW
echo =========================

py marketing_review.py

echo.
echo =========================
echo RUNNING LOCAL LLM REVIEW
echo =========================

py marketing_llm_review.py

echo.
echo =========================
echo RUNNING MARKETING DASHBOARD
echo =========================

py marketing_dashboard.py

echo.
echo =========================
echo RUNNING KEYWORD OPPORTUNITIES
echo =========================

py keyword_opportunities.py

echo.
echo =========================
echo RUNNING CONTENT ARCHETYPES
echo =========================

py content_archetypes.py

echo.
echo =========================
echo RUNNING COMPETITOR SUMMARY
echo =========================

py competitor_summary.py

echo.
echo =========================
echo RUNNING COMPETITOR CHANGES
echo =========================

py competitor_changes.py

echo.
echo =========================
echo RUNNING LINKEDIN TOPIC PROPOSALS
echo =========================

py linkedin_topic_proposals.py

echo.
echo =========================
echo MARKETING PIPELINE COMPLETE
echo =========================

pause