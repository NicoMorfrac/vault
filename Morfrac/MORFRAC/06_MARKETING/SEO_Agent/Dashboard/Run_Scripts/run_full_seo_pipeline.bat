@echo off
echo ==============================
echo MORFRAC FULL SEO PIPELINE
echo ==============================
echo.
cd /d C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC\02_AGENTS\SEO
call run_seo_pipeline.bat
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
