@echo off
echo ==============================
echo MORFRAC MARKETING REPORTS
echo ==============================
echo.
cd /d C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC\02_AGENTS\Marketing
call run_marketing_reports.bat
if errorlevel 1 (
    echo.
    echo Script failed.
    pause
    exit /b %errorlevel%
)
echo.
echo Complete.
echo.
pause
