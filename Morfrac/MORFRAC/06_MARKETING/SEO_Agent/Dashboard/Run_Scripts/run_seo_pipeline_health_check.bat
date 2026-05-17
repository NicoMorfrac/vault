@echo off
echo ==============================
echo MORFRAC SEO PIPELINE HEALTH CHECK
echo ==============================
echo.
cd /d C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC\06_MARKETING\SEO_Agent\Scripts
py seo_pipeline_health_check.py
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
