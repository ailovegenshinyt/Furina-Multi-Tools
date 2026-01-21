@echo off
setlocal enabledelayedexpansion
title Furina's Master Command Center 🎭
set "current_version=1.0"
set "repo_url=https://raw.githubusercontent.com/ailovegenshinyt/Furina-Multi-Tools/main"

:: --- 1. เช็กการอัปเดตเวอร์ชัน ---
powershell -Command "Invoke-WebRequest -Uri '%repo_url%/version.txt' -OutFile 'v_check.txt'" >nul 2>&1
set /p online_version=<v_check.txt
del v_check.txt
if not "%current_version%"=="%online_version%" (
    echo 📢 New Version !online_version! found!
    set /p "u=Update now? (y/n): "
    if /i "!u!"=="y" (
        powershell -Command "Invoke-WebRequest -Uri '%repo_url%/furina_tool.bat' -OutFile 'furina_tool.bat'"
        echo ✅ Updated! Please restart. & pause & exit
    )
)

:: --- 2. เช็กและติดตั้ง Requirements ---
for /f "tokens=*" %%a in (requirements.txt) do (
    where %%a >nul 2>&1 || (
        echo 📦 Installing %%a...
        if "%%a"=="yt-dlp" pip install yt-dlp
        if "%%a"=="ffmpeg" winget install ffmpeg --silent
    )
)

:menu
cls
color 0B
echo ============================================
echo      ✨ FURINA'S COMMAND CENTER ✨
echo ============================================
echo   Select your act:
echo.
set count=0
for /f "tokens=1,2 delims==" %%a in (commandscode.txt) do (
    set /a count+=1
    set "tool_name[!count!]=%%a"
    set "tool_args[!count!]=%%b"
    echo   [!count!] %%a
)
echo   [E] Exit
echo ============================================
set /p "choice=Choose (1-!count!): "
if /i "%choice%"=="E" exit

if defined tool_name[%choice%] (
    set "name=!tool_name[%choice%]!"
    set "args=!tool_args[%choice%]!"
    echo.
    set /p "url=Enter URL/Input: "
    :: รันคำสั่งตามที่ดึงมาจากไฟล์ txt
    !name! !args! !url!
    pause
    goto menu
)
goto menu

