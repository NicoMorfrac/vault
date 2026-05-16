@echo off

cd /d C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC\02_AGENTS\Marketing

echo =========================
echo RUNNING COMPETITOR SUMMARY
echo =========================

py competitor_summary.py
if errorlevel 1 exit /b %errorlevel%

echo.
echo =========================
echo RUNNING CHANGE DETECTION
echo =========================

py competitor_change_detection.py
if errorlevel 1 exit /b %errorlevel%

echo.
echo =========================
echo COMPETITOR MONITORING COMPLETE
echo =========================

exit
