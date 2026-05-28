@echo off

cd /d C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC\02_AGENTS\Marketing

set "PYTHON_EXE=C:\Users\nicol\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe"

echo =========================
echo RUNNING COMPETITOR SUMMARY
echo =========================

"%PYTHON_EXE%" competitor_summary.py
if errorlevel 1 exit /b %errorlevel%

echo.
echo =========================
echo RUNNING CHANGE DETECTION
echo =========================

"%PYTHON_EXE%" competitor_change_detection.py
if errorlevel 1 exit /b %errorlevel%

echo.
echo =========================
echo COMPETITOR MONITORING COMPLETE
echo =========================

exit
