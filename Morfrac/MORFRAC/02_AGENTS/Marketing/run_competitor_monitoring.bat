@echo off

cd /d C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC\02_AGENTS\Marketing

echo =========================
echo RUNNING COMPETITOR SUMMARY
echo =========================

py competitor_summary.py

echo.
echo =========================
echo RUNNING CHANGE DETECTION
echo =========================

py competitor_change_detection.py

echo.
echo =========================
echo COMPETITOR MONITORING COMPLETE
echo =========================

exit