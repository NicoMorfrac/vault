@echo off
cd /d C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC
powershell.exe -NoProfile -ExecutionPolicy Bypass -File "C:\Users\nicol\Documents\Obsidian\Morfrac\MORFRAC\02_AGENTS\run_morfrac_automation.ps1"
exit /b %errorlevel%
