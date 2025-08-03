#!/bin/bash

echo "🚀 Thiết lập môi trường cho Split Video Tool trên macOS"
echo "=================================================="

# Kiểm tra Python3
if ! command -v python3 &> /dev/null; then
    echo "❌ Python3 chưa được cài đặt. Vui lòng cài đặt Python3 trước."
    echo "Có thể tải từ: https://www.python.org/downloads/"
    exit 1
fi

echo "✅ Python3 đã được cài đặt: $(python3 --version)"

# Kiểm tra FFmpeg
if ! command -v ffmpeg &> /dev/null; then
    echo "⚠️  FFmpeg chưa được cài đặt."
    echo "Đang cài đặt FFmpeg bằng Homebrew..."
    if ! command -v brew &> /dev/null; then
        echo "❌ Homebrew chưa được cài đặt. Vui lòng cài đặt Homebrew trước:"
        echo "/bin/bash -c \"\$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)\""
        exit 1
    fi
    brew install ffmpeg
else
    echo "✅ FFmpeg đã được cài đặt: $(ffmpeg -version | head -n1)"
fi

# Tạo môi trường ảo
echo "📦 Tạo môi trường ảo..."
python3 -m venv venv

# Kích hoạt môi trường ảo
echo "🔧 Kích hoạt môi trường ảo..."
# Kiểm tra shell type
if [ "$SHELL" = "/bin/fish" ] || [ "$SHELL" = "/opt/homebrew/bin/fish" ]; then
    echo "🐟 Phát hiện fish shell, sử dụng activate.fish..."
    source venv/bin/activate.fish
else
    source venv/bin/activate
fi

# Cài đặt dependencies
echo "📚 Cài đặt các thư viện Python..."
python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt

echo ""
echo "🎉 Thiết lập hoàn tất!"
echo ""
echo "Để sử dụng tool:"
if [ "$SHELL" = "/bin/fish" ] || [ "$SHELL" = "/opt/homebrew/bin/fish" ]; then
    echo "1. Kích hoạt môi trường ảo: source venv/bin/activate.fish"
else
    echo "1. Kích hoạt môi trường ảo: source venv/bin/activate"
fi
echo "2. Chạy script: python3 split.py"
echo ""
echo "Hoặc chạy trực tiếp:"
echo "./venv/bin/python3 split.py" 