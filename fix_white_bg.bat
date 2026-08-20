@echo off
echo Fixing Pebbles white backgrounds...
echo.
python "%~dp0fix_pebbles.py"
if errorlevel 1 (
    echo.
    echo Hmm, that didn't work. Trying Python 3...
    py "%~dp0fix_pebbles.py"
)
pause
