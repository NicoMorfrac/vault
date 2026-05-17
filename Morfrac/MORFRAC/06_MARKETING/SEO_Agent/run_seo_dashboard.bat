@echo off
echo ==============================
echo MORFRAC SEO DASHBOARD REFRESH
echo ==============================
echo.

cd /d C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC\06_MARKETING\SEO_Agent\Scripts

py seo_dashboard.py
if errorlevel 1 (
    echo.
    echo Dashboard refresh failed.
    pause
    exit /b %errorlevel%
)

echo.
echo Dashboard refreshed:
echo C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC\06_MARKETING\SEO_Agent\seo_dashboard.html
echo.
pause
