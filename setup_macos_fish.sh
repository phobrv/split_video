#!/bin/fish

echo "🚀 Thiết lập môi trường cho Split Video Tool trên macOS (Fish Shell)"
echo "=================================================="

# Kiểm tra Python3
if not command -q python3
    echo "❌ Python3 chưa được cài đặt. Vui lòng cài đặt Python3 trước."
    echo "Có thể tải từ: https://www.python.org/downloads/"
    exit 1
end

echo "✅ Python3 đã được cài đặt: "(python3 --version)

# Kiểm tra FFmpeg
if not command -q ffmpeg
    echo "⚠️  FFmpeg chưa được cài đặt."
    echo "Đang cài đặt FFmpeg bằng Homebrew..."
    if not command -q brew
        echo "❌ Homebrew chưa được cài đặt. Vui lòng cài đặt Homebrew trước:"
        echo '/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"'
        exit 1
    end
    brew install ffmpeg
else
    echo "✅ FFmpeg đã được cài đặt: "(ffmpeg -version | head -n1)
end

# Tạo môi trường ảo
echo "📦 Tạo môi trường ảo..."
python3 -m venv venv

# Kích hoạt môi trường ảo
echo "🔧 Kích hoạt môi trường ảo (fish shell)..."
source venv/bin/activate.fish

# Cài đặt dependencies
echo "📚 Cài đặt các thư viện Python..."
python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt

echo ""
echo "🎉 Thiết lập hoàn tất!"
echo ""
echo "Để sử dụng tool:"
echo "1. Kích hoạt môi trường ảo: source venv/bin/activate.fish"
echo "2. Chạy script: python3 split.py"
echo ""
echo "Hoặc chạy trực tiếp:"
echo "./venv/bin/python3 split.py" 