@echo off
chcp 65001 >nul
echo 🚀 Thiết lập môi trường build cho Split Video Tool
echo ===================================================
echo.

REM Kiểm tra Python
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Python chưa được cài đặt. Vui lòng cài đặt Python trước.
    echo Có thể tải từ: https://www.python.org/downloads/
    pause
    exit /b 1
)

echo ✅ Python đã được cài đặt: 
python --version

REM Tạo môi trường ảo cho build
echo 📦 Tạo môi trường ảo cho build...
python -m venv venv_build

REM Kích hoạt môi trường ảo
echo 🔧 Kích hoạt môi trường ảo...
call venv_build\Scripts\activate.bat

REM Cài đặt dependencies cho build
echo 📚 Cài đặt các thư viện Python...
python -m pip install --upgrade pip
python -m pip install -r requirements_build.txt

echo.
echo 🎉 Thiết lập build hoàn tất!
echo.
echo Để build ứng dụng:
echo 1. Kích hoạt môi trường ảo: venv_build\Scripts\activate.bat
echo 2. Chạy script build: build_exe.bat
echo.
echo Hoặc chạy trực tiếp:
echo venv_build\Scripts\python.exe build_exe.py
echo.
pause 