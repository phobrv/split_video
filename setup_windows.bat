@echo off
chcp 65001 >nul
setlocal enabledelayedexpansion

echo 🚀 Thiết lập môi trường cho Split Video Tool trên Windows 11
echo ==================================================

REM Kiểm tra Python3
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Python chưa được cài đặt. Vui lòng cài đặt Python trước.
    echo Có thể tải từ: https://www.python.org/downloads/
    echo Lưu ý: Hãy chọn "Add Python to PATH" khi cài đặt
    pause
    exit /b 1
)

echo ✅ Python đã được cài đặt:
python --version

REM Kiểm tra FFmpeg
ffmpeg -version >nul 2>&1
if %errorlevel% neq 0 (
    echo ⚠️  FFmpeg chưa được cài đặt.
    echo Đang hướng dẫn cài đặt FFmpeg...
    echo.
    echo Cách 1: Sử dụng Chocolatey (khuyến nghị)
    echo 1. Cài đặt Chocolatey từ: https://chocolatey.org/install
    echo 2. Chạy lệnh: choco install ffmpeg
    echo.
    echo Cách 2: Tải trực tiếp
    echo 1. Tải FFmpeg từ: https://ffmpeg.org/download.html
    echo 2. Giải nén và thêm vào PATH
    echo.
    echo Sau khi cài đặt FFmpeg, hãy chạy lại script này.
    pause
    exit /b 1
) else (
    echo ✅ FFmpeg đã được cài đặt:
    ffmpeg -version | findstr "ffmpeg version"
)

REM Tạo môi trường ảo
echo 📦 Tạo môi trường ảo...
python -m venv venv

REM Kích hoạt môi trường ảo
echo 🔧 Kích hoạt môi trường ảo...
call venv\Scripts\activate.bat

REM Cài đặt dependencies
echo 📚 Cài đặt các thư viện Python...
python -m pip install --upgrade pip
python -m pip install -r requirements.txt

echo.
echo 🎉 Thiết lập hoàn tất!
echo.
echo Để sử dụng tool:
echo 1. Kích hoạt môi trường ảo: venv\Scripts\activate.bat
echo 2. Chạy script: python split.py
echo.
echo Hoặc chạy trực tiếp:
echo venv\Scripts\python.exe split.py
echo.
echo Ví dụ sử dụng:
echo python split.py video.mp4 output
echo python split.py video.mp4 output 10
echo.
pause 