@echo off
title PianoMind Auto-Publish  (keep this window open)
cd /d "%~dp0"
echo ==================================================
echo   PianoMind Auto-Publish is ON
echo   Every minute, new changes go live automatically.
echo   Close this window to turn it off.
echo ==================================================
echo.
:loop
git add -A >nul 2>&1
git diff --cached --quiet
if errorlevel 1 (
  git commit -q -m "Auto-publish %date% %time:~0,5%"
  git push -q
  if errorlevel 1 (
    echo [%time:~0,5%] PUSH FAILED - check the internet. Will try again in 1 minute.
  ) else (
    echo [%time:~0,5%] Published! The site updates in about 1-2 minutes.
  )
)
timeout /t 60 /nobreak >nul
goto loop
