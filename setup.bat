@echo off
setlocal enabledelayedexpansion

echo ========================================================
echo    Welcome to Manim AI Studio Setup
echo ========================================================
echo.

:: 1. Check or install uv
echo [1/3] Checking uv package manager...
where uv >nul 2>&1
if %ERRORLEVEL% neq 0 (
    echo uv is not found. Installing uv automatically...
    powershell -NoProfile -ExecutionPolicy Bypass -Command "irm https://astral.sh/uv/install.ps1 | iex"
    set "PATH=%USERPROFILE%\.local\bin;%PATH%"
) else (
    echo  uv is already installed!
)

:: 2. Check FFmpeg (required by Manim)
echo.
echo [2/3] Checking FFmpeg (video rendering engine)...
where ffmpeg >nul 2>&1
if %ERRORLEVEL% neq 0 (
    echo FFmpeg was not detected. Attempting automatic installation via winget...
    winget install Gyan.FFmpeg --accept-package-agreements --accept-source-agreements
    if %ERRORLEVEL% neq 0 (
        echo [WARNING] Could not auto-install FFmpeg. Please install FFmpeg or run: winget install Gyan.FFmpeg
    )
) else (
    echo  FFmpeg is installed and ready!
)

:: 3. Setup Python virtual environment & Manim dependencies
echo.
echo [3/3] Setting up Python, Manim, and Voiceover dependencies...
uv sync --python 3.11

echo.
echo ========================================================
echo   Setup Complete!
echo ========================================================
echo.
echo Launching project in Antigravity IDE...
where antigravity-ide >nul 2>&1
if %ERRORLEVEL% equ 0 (
    antigravity-ide "%~dp0"
) else if exist "%LOCALAPPDATA%\Programs\Antigravity IDE\bin\antigravity-ide.cmd" (
    call "%LOCALAPPDATA%\Programs\Antigravity IDE\bin\antigravity-ide.cmd" "%~dp0"
) else (
    echo Please open this folder (%~dp0) inside Antigravity IDE.
)

pause
