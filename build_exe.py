#!/usr/bin/env python3
"""
Script để build Split Video Tool thành file .exe
Sử dụng PyInstaller để đóng gói ứng dụng
"""

import os
import sys
import subprocess
import shutil
from pathlib import Path

def check_pyinstaller():
    """Kiểm tra PyInstaller đã được cài đặt chưa"""
    try:
        import PyInstaller
        print("✅ PyInstaller đã được cài đặt")
        return True
    except ImportError:
        print("❌ PyInstaller chưa được cài đặt")
        return False

def install_pyinstaller():
    """Cài đặt PyInstaller"""
    print("📦 Đang cài đặt PyInstaller...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "pyinstaller"])
        print("✅ PyInstaller đã được cài đặt thành công")
        return True
    except subprocess.CalledProcessError:
        print("❌ Lỗi khi cài đặt PyInstaller")
        return False

def create_spec_file():
    """Tạo file spec cho PyInstaller"""
    spec_content = '''# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(
    ['split_gui.py'],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=[
        'moviepy.video.io.VideoFileClip',
        'moviepy.video.fx.all',
        'moviepy.audio.fx.all',
        'moviepy.video.io.ffmpeg_reader',
        'moviepy.video.io.ffmpeg_writer',
        'imageio',
        'imageio_ffmpeg',
        'proglog',
        'tqdm',
        'numpy',
        'decorator',
        'requests'
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='SplitVideoTool',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon='icon.ico' if os.path.exists('icon.ico') else None,
)
'''
    
    with open('SplitVideoTool.spec', 'w', encoding='utf-8') as f:
        f.write(spec_content)
    
    print("✅ Đã tạo file SplitVideoTool.spec")

def build_exe():
    """Build ứng dụng thành file .exe"""
    print("🔨 Đang build ứng dụng...")
    
    # Xóa thư mục build cũ nếu có
    if os.path.exists('build'):
        shutil.rmtree('build')
    if os.path.exists('dist'):
        shutil.rmtree('dist')
    
    try:
        # Build với PyInstaller
        cmd = [
            sys.executable, "-m", "PyInstaller",
            "--onefile",
            "--windowed",
            "--name=SplitVideoTool",
            "--add-data=requirements.txt;.",
            "split_gui.py"
        ]
        
        # Thêm icon nếu có
        if os.path.exists('icon.ico'):
            cmd.extend(['--icon=icon.ico'])
        
        subprocess.check_call(cmd)
        
        print("✅ Build thành công!")
        print(f"📁 File .exe được tạo tại: {os.path.abspath('dist/SplitVideoTool.exe')}")
        
        # Tạo thư mục release
        release_dir = Path("release")
        release_dir.mkdir(exist_ok=True)
        
        # Copy file .exe vào thư mục release
        exe_path = Path("dist/SplitVideoTool.exe")
        if exe_path.exists():
            shutil.copy2(exe_path, release_dir / "SplitVideoTool.exe")
            print(f"📦 Đã copy file .exe vào: {release_dir / 'SplitVideoTool.exe'}")
        
        # Copy README và requirements
        if os.path.exists('README_Windows.md'):
            shutil.copy2('README_Windows.md', release_dir / 'README.txt')
        
        if os.path.exists('requirements.txt'):
            shutil.copy2('requirements.txt', release_dir)
        
        print("🎉 Hoàn thành build!")
        return True
        
    except subprocess.CalledProcessError as e:
        print(f"❌ Lỗi khi build: {e}")
        return False

def create_installer_script():
    """Tạo script cài đặt cho người dùng"""
    installer_content = '''@echo off
chcp 65001 >nul
echo 🚀 Split Video Tool - Cài đặt
echo ================================
echo.

REM Kiểm tra Python
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Python chưa được cài đặt.
    echo Vui lòng cài đặt Python từ: https://www.python.org/downloads/
    echo Lưu ý: Chọn "Add Python to PATH" khi cài đặt
    pause
    exit /b 1
)

echo ✅ Python đã được cài đặt

REM Kiểm tra FFmpeg
ffmpeg -version >nul 2>&1
if %errorlevel% neq 0 (
    echo ⚠️  FFmpeg chưa được cài đặt.
    echo Đang hướng dẫn cài đặt FFmpeg...
    echo.
    echo Cách 1: Sử dụng Chocolatey
    echo 1. Cài đặt Chocolatey từ: https://chocolatey.org/install
    echo 2. Chạy: choco install ffmpeg -y
    echo.
    echo Cách 2: Tải trực tiếp từ: https://ffmpeg.org/download.html
    echo.
    echo Sau khi cài đặt FFmpeg, hãy chạy lại script này.
    pause
    exit /b 1
)

echo ✅ FFmpeg đã được cài đặt
echo.
echo 🎉 Môi trường đã sẵn sàng!
echo Bạn có thể chạy SplitVideoTool.exe
pause
'''
    
    with open('release/install.bat', 'w', encoding='utf-8') as f:
        f.write(installer_content)
    
    print("✅ Đã tạo script cài đặt")

def main():
    """Hàm chính"""
    print("🚀 Split Video Tool - Build Script")
    print("==================================")
    print()
    
    # Kiểm tra PyInstaller
    if not check_pyinstaller():
        if not install_pyinstaller():
            print("❌ Không thể cài đặt PyInstaller")
            return False
    
    # Kiểm tra file GUI
    if not os.path.exists('split_gui.py'):
        print("❌ Không tìm thấy file split_gui.py")
        return False
    
    # Tạo file spec
    create_spec_file()
    
    # Build ứng dụng
    if build_exe():
        # Tạo script cài đặt
        create_installer_script()
        
        print()
        print("📋 Hướng dẫn phân phối:")
        print("1. Copy thư mục 'release' đến máy đích")
        print("2. Chạy install.bat để kiểm tra môi trường")
        print("3. Chạy SplitVideoTool.exe để sử dụng")
        print()
        print("🎉 Build hoàn thành!")
        return True
    else:
        print("❌ Build thất bại!")
        return False

if __name__ == "__main__":
    main() 