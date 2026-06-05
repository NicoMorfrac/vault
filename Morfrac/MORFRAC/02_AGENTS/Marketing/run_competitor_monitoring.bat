@echo off
setlocal

cd /d C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC\02_AGENTS\Marketing

set "PYTHON_EXE=C:\Users\nicol\AppData\Local\Python\pythoncore-3.14-64\python.exe"
set "PYTHONUTF8=1"
set "PYTHONIOENCODING=utf-8"
set "LOG_DIR=C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC\06_MARKETING\Automation_Logs"

if not exist "%LOG_DIR%" mkdir "%LOG_DIR%"

for /f %%I in ('powershell -NoProfile -Command "Get-Date -Format yyyy-MM-dd_HH-mm-ss"') do set "RUN_STAMP=%%I"
set "LOG_FILE=%LOG_DIR%\%RUN_STAMP%_competitor_monitoring.log"

call :run_step "COMPETITOR SUMMARY" competitor_summary.py
if errorlevel 1 exit /b %errorlevel%

call :run_step "CHANGE DETECTION" competitor_change_detection.py
if errorlevel 1 exit /b %errorlevel%

echo.
echo =========================
echo COMPETITOR MONITORING COMPLETE
echo =========================
echo [%DATE% %TIME%] COMPETITOR MONITORING COMPLETE>> "%LOG_FILE%"

exit /b 0

:run_step
echo.
echo =========================
echo RUNNING %~1
echo =========================
echo [%DATE% %TIME%] RUNNING %~1>> "%LOG_FILE%"

"%PYTHON_EXE%" "%~2" >> "%LOG_FILE%" 2>&1
set "EXIT_CODE=%ERRORLEVEL%"

if not "%EXIT_CODE%"=="0" (
    echo FAILED %~1 with exit code %EXIT_CODE%
    echo [%DATE% %TIME%] FAILED %~1 with exit code %EXIT_CODE%>> "%LOG_FILE%"
    echo See log: "%LOG_FILE%"
    exit /b %EXIT_CODE%
)

echo OK %~1
echo [%DATE% %TIME%] OK %~1>> "%LOG_FILE%"
exit /b 0
