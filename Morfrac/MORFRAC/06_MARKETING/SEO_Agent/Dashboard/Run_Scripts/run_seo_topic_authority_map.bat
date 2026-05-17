@echo off
echo ==============================
echo MORFRAC SEO TOPIC AUTHORITY MAP
echo ==============================
echo.
cd /d C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC\06_MARKETING\SEO_Agent\Scripts
py seo_topic_authority_map.py
if errorlevel 1 exit /b %errorlevel%
py seo_dashboard.py
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
