@echo off
echo ==============================
echo MORFRAC SEO DASHBOARD REFRESH
echo ==============================
echo.
cd /d C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC\06_MARKETING\SEO_Agent\Scripts
"C:\Users\nicol\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe" seo_dashboard.py
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
