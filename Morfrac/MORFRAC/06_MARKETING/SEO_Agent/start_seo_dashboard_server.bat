@echo off
echo ==============================
echo MORFRAC SEO DASHBOARD SERVER
echo ==============================
echo.

cd /d C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC\06_MARKETING\SEO_Agent\Scripts

start "" http://127.0.0.1:8765/

set "PYTHON_EXE=C:\Users\nicol\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe"

"%PYTHON_EXE%" seo_dashboard_server.py
if errorlevel 1 (
    echo.
    echo Dashboard server failed.
    pause
    exit /b %errorlevel%
)
