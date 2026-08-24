@echo off
setlocal
cd /d "%~dp0"
if "%~1"=="" (
  echo Drag your clean 1.02 Media folder onto this CMD file.
  echo.
  pause
  exit /b 2
)
where python >nul 2>nul
if errorlevel 1 (
  echo ERROR: Python 3 was not found in PATH.
  pause
  exit /b 1
)
python "%~dp0tools\apply_v001.py" "%~1"
echo.
pause
