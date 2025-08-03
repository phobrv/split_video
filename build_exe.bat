@echo off
chcp 65001 >nul
echo 🚀 Split Video Tool - Build Script
echo ==================================
echo.

REM Kiểm tra Python
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Python chưa được cài đặt.
    echo Vui lòng cài đặt Python trước.
    pause
    exit /b 1
)

echo ✅ Python đã được cài đặt

REM Cài đặt PyInstaller nếu chưa có
echo 📦 Kiểm tra PyInstaller...
python -c "import PyInstaller" >nul 2>&1
if %errorlevel% neq 0 (
    echo Đang cài đặt PyInstaller...
    python -m pip install pyinstaller
    if %errorlevel% neq 0 (
        echo ❌ Lỗi khi cài đặt PyInstaller
        pause
        exit /b 1
    )
    echo ✅ PyInstaller đã được cài đặt
) else (
    echo ✅ PyInstaller đã có sẵn
)

REM Kiểm tra file GUI
if not exist "split_gui.py" (
    echo ❌ Không tìm thấy file split_gui.py
    pause
    exit /b 1
)

echo 🔨 Đang build ứng dụng...
echo.

REM Xóa thư mục build cũ
if exist "build" rmdir /s /q "build"
if exist "dist" rmdir /s /q "dist"

REM Build với PyInstaller
python -m PyInstaller --onefile --windowed --name=SplitVideoTool --add-data=requirements.txt;. split_gui.py

if %errorlevel% neq 0 (
    echo ❌ Lỗi khi build
    pause
    exit /b 1
)

echo.
echo ✅ Build thành công!
echo 📁 File .exe được tạo tại: dist\SplitVideoTool.exe

REM Tạo thư mục release
if not exist "release" mkdir "release"

REM Copy file .exe vào release
copy "dist\SplitVideoTool.exe" "release\SplitVideoTool.exe" >nul
echo 📦 Đã copy file .exe vào release\

REM Copy README
if exist "README_Windows.md" copy "README_Windows.md" "release\README.txt" >nul

REM Copy requirements
if exist "requirements.txt" copy "requirements.txt" "release\" >nul

echo.
echo 🎉 Hoàn thành build!
echo 📋 Hướng dẫn phân phối:
echo 1. Copy thư mục 'release' đến máy đích
echo 2. Chạy SplitVideoTool.exe để sử dụng
echo.
pause 