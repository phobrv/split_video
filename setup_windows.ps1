# PowerShell script để thiết lập môi trường cho Split Video Tool trên Windows 11
# Chạy với quyền Administrator để có thể cài đặt Chocolatey

param(
    [switch]$InstallChocolatey,
    [switch]$InstallFFmpeg
)

# Thiết lập encoding để hiển thị emoji
[Console]::OutputEncoding = [System.Text.Encoding]::UTF8

Write-Host "🚀 Thiết lập môi trường cho Split Video Tool trên Windows 11" -ForegroundColor Cyan
Write-Host "==================================================" -ForegroundColor Cyan
Write-Host ""

# Kiểm tra Python
Write-Host "🔍 Kiểm tra Python..." -ForegroundColor Yellow
try {
    $pythonVersion = python --version 2>&1
    if ($LASTEXITCODE -eq 0) {
        Write-Host "✅ Python đã được cài đặt: $pythonVersion" -ForegroundColor Green
    } else {
        throw "Python not found"
    }
} catch {
    Write-Host "❌ Python chưa được cài đặt." -ForegroundColor Red
    Write-Host "Vui lòng cài đặt Python từ: https://www.python.org/downloads/" -ForegroundColor Yellow
    Write-Host "Lưu ý: Hãy chọn 'Add Python to PATH' khi cài đặt" -ForegroundColor Yellow
    Read-Host "Nhấn Enter để thoát"
    exit 1
}

# Kiểm tra FFmpeg
Write-Host "🔍 Kiểm tra FFmpeg..." -ForegroundColor Yellow
try {
    $ffmpegVersion = ffmpeg -version 2>&1 | Select-Object -First 1
    if ($LASTEXITCODE -eq 0) {
        Write-Host "✅ FFmpeg đã được cài đặt: $ffmpegVersion" -ForegroundColor Green
    } else {
        throw "FFmpeg not found"
    }
} catch {
    Write-Host "⚠️  FFmpeg chưa được cài đặt." -ForegroundColor Yellow
    Write-Host ""
    
    if ($InstallChocolatey -or $InstallFFmpeg) {
        # Cài đặt Chocolatey nếu được yêu cầu
        if ($InstallChocolatey) {
            Write-Host "📦 Đang cài đặt Chocolatey..." -ForegroundColor Cyan
            Set-ExecutionPolicy Bypass -Scope Process -Force
            [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072
            iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))
            Write-Host "✅ Chocolatey đã được cài đặt" -ForegroundColor Green
        }
        
        # Cài đặt FFmpeg nếu được yêu cầu
        if ($InstallFFmpeg) {
            Write-Host "📦 Đang cài đặt FFmpeg..." -ForegroundColor Cyan
            choco install ffmpeg -y
            Write-Host "✅ FFmpeg đã được cài đặt" -ForegroundColor Green
            
            # Refresh environment variables
            $env:Path = [System.Environment]::GetEnvironmentVariable("Path","Machine") + ";" + [System.Environment]::GetEnvironmentVariable("Path","User")
        }
    } else {
        Write-Host "Hướng dẫn cài đặt FFmpeg:" -ForegroundColor Cyan
        Write-Host "1. Sử dụng Chocolatey (khuyến nghị):" -ForegroundColor White
        Write-Host "   - Chạy script với tham số: .\setup_windows.ps1 -InstallChocolatey -InstallFFmpeg" -ForegroundColor Gray
        Write-Host "   - Hoặc cài đặt thủ công:" -ForegroundColor Gray
        Write-Host "     Set-ExecutionPolicy Bypass -Scope Process -Force" -ForegroundColor Gray
        Write-Host "     iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))" -ForegroundColor Gray
        Write-Host "     choco install ffmpeg -y" -ForegroundColor Gray
        Write-Host ""
        Write-Host "2. Tải trực tiếp:" -ForegroundColor White
        Write-Host "   - Tải từ: https://ffmpeg.org/download.html" -ForegroundColor Gray
        Write-Host "   - Giải nén và thêm vào PATH" -ForegroundColor Gray
        Write-Host ""
        Write-Host "Sau khi cài đặt FFmpeg, hãy chạy lại script này." -ForegroundColor Yellow
        Read-Host "Nhấn Enter để thoát"
        exit 1
    }
}

# Tạo môi trường ảo
Write-Host "📦 Tạo môi trường ảo..." -ForegroundColor Cyan
python -m venv venv

# Kích hoạt môi trường ảo
Write-Host "🔧 Kích hoạt môi trường ảo..." -ForegroundColor Cyan
& "venv\Scripts\Activate.ps1"

# Cài đặt dependencies
Write-Host "📚 Cài đặt các thư viện Python..." -ForegroundColor Cyan
python -m pip install --upgrade pip
python -m pip install -r requirements.txt

Write-Host ""
Write-Host "🎉 Thiết lập hoàn tất!" -ForegroundColor Green
Write-Host ""
Write-Host "Để sử dụng tool:" -ForegroundColor White
Write-Host "1. Kích hoạt môi trường ảo: venv\Scripts\Activate.ps1" -ForegroundColor Gray
Write-Host "2. Chạy script: python split.py" -ForegroundColor Gray
Write-Host ""
Write-Host "Hoặc chạy trực tiếp:" -ForegroundColor White
Write-Host "venv\Scripts\python.exe split.py" -ForegroundColor Gray
Write-Host ""
Write-Host "Ví dụ sử dụng:" -ForegroundColor White
Write-Host "python split.py video.mp4 output" -ForegroundColor Gray
Write-Host "python split.py video.mp4 output 10" -ForegroundColor Gray
Write-Host ""
Read-Host "Nhấn Enter để thoát" 