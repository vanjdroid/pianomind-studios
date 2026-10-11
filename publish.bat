@echo off
title Publish PianoMind Studios
cd /d "%~dp0"

echo ==========================================
echo   Publish PianoMind Studios to the website
echo ==========================================
echo.
echo Files that changed:
git status --short
echo.

set "msg="
set /p msg="Describe the change (or just press Enter): "
if "%msg%"=="" set "msg=Update %date% %time:~0,5%"

git add .
git commit -m "%msg%"
if errorlevel 1 (
  echo.
  echo Nothing new to publish, or the commit failed.
  echo.
  pause
  exit /b
)

echo.
echo Getting any changes made on the GitHub website first...
git pull --rebase --autostash
if errorlevel 1 (
  echo.
  echo Could not combine with the changes on GitHub. Nothing was published.
  echo Copy the message above and send it to Claude.
  echo.
  pause
  exit /b
)

git push
if errorlevel 1 (
  echo.
  echo PUSH FAILED. The website did NOT update. Read the message above.
) else (
  echo.
  echo Done! The site updates in about 1-2 minutes:
  echo https://vanjdroid.github.io/pianomind-studios/
)
echo.
pause
