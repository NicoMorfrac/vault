@echo off

cd /d C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC\02_AGENTS\Marketing

set "PYTHON_EXE=C:\Users\nicol\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe"

echo =========================
echo RUNNING GA4 REPORT
echo =========================

"%PYTHON_EXE%" weekly_ga4_report.py
if errorlevel 1 exit /b %errorlevel%

echo.
echo =========================
echo RUNNING SEARCH CONSOLE REPORT
echo =========================

"%PYTHON_EXE%" search_console_report.py
if errorlevel 1 exit /b %errorlevel%

echo.
echo =========================
echo RUNNING MARKETING REVIEW
echo =========================

"%PYTHON_EXE%" marketing_review.py
if errorlevel 1 exit /b %errorlevel%

echo.
echo =========================
echo RUNNING LOCAL LLM REVIEW
echo =========================

"%PYTHON_EXE%" marketing_llm_review.py
if errorlevel 1 exit /b %errorlevel%

echo.
echo =========================
echo RUNNING MARKETING DASHBOARD
echo =========================

"%PYTHON_EXE%" marketing_dashboard.py
if errorlevel 1 exit /b %errorlevel%

echo.
echo =========================
echo RUNNING KEYWORD OPPORTUNITIES
echo =========================

"%PYTHON_EXE%" keyword_opportunities.py
if errorlevel 1 exit /b %errorlevel%

echo.
echo =========================
echo RUNNING CONTENT ARCHETYPES
echo =========================

"%PYTHON_EXE%" content_archetypes.py
if errorlevel 1 exit /b %errorlevel%

echo.
echo =========================
echo RUNNING COMPETITOR SUMMARY
echo =========================

"%PYTHON_EXE%" competitor_summary.py
if errorlevel 1 exit /b %errorlevel%

echo.
echo =========================
echo RUNNING COMPETITOR CHANGES
echo =========================

"%PYTHON_EXE%" competitor_change_detection.py
if errorlevel 1 exit /b %errorlevel%

echo.
echo =========================
echo RUNNING LINKEDIN TOPIC PROPOSALS
echo =========================

"%PYTHON_EXE%" linkedin_topic_proposals.py
if errorlevel 1 exit /b %errorlevel%

echo.
echo =========================
echo MARKETING PIPELINE COMPLETE
echo =========================

pause
