# Hướng dẫn Build Split Video Tool thành .exe

## Giới thiệu

Hướng dẫn này sẽ giúp bạn đóng gói Split Video Tool thành file .exe để phân phối trên Windows.

## Yêu cầu hệ thống

- Windows 10/11
- Python 3.7 trở lên
- FFmpeg (cho việc test)

## Cách 1: Build nhanh (Khuyến nghị)

### Bước 1: Thiết lập môi trường build

```cmd
setup_build.bat
```

### Bước 2: Build ứng dụng

```cmd
build_exe.bat
```

## Cách 2: Build thủ công

### Bước 1: Cài đặt PyInstaller

```cmd
pip install pyinstaller
```

### Bước 2: Cài đặt dependencies

```cmd
pip install -r requirements_build.txt
```

### Bước 3: Build ứng dụng

```cmd
python -m PyInstaller --onefile --windowed --name=SplitVideoTool split_gui.py
```

## Cấu trúc file sau khi build

```
release/
├── SplitVideoTool.exe      # File .exe chính
├── README.txt             # Hướng dẫn sử dụng
└── requirements.txt       # Dependencies (tham khảo)
```

## Tùy chọn build nâng cao

### Thêm icon cho .exe

1. Tạo file `icon.ico` (16x16, 32x32, 48x48, 256x256)
2. Build với tham số icon:

```cmd
python -m PyInstaller --onefile --windowed --icon=icon.ico --name=SplitVideoTool split_gui.py
```

### Build với tất cả dependencies

```cmd
python -m PyInstaller --onefile --windowed --hidden-import=moviepy --hidden-import=imageio --name=SplitVideoTool split_gui.py
```

### Build với console (để debug)

```cmd
python -m PyInstaller --onefile --name=SplitVideoTool split_gui.py
```

## Phân phối ứng dụng

### Cách 1: Phân phối đơn giản

1. Copy thư mục `release` đến máy đích
2. Chạy `SplitVideoTool.exe`

### Cách 2: Tạo installer

Sử dụng tools như:
- Inno Setup
- NSIS
- Advanced Installer

### Cách 3: Tạo portable package

1. Tạo thư mục `SplitVideoTool_Portable`
2. Copy `SplitVideoTool.exe` vào thư mục
3. Nén thành file zip

## Xử lý lỗi build

### Lỗi "Module not found"

```cmd
pip install --upgrade pyinstaller
pip install --upgrade -r requirements_build.txt
```

### Lỗi "FFmpeg not found"

- Ứng dụng .exe sẽ tự động tải FFmpeg khi cần
- Hoặc cài đặt FFmpeg trên máy đích

### Lỗi "Permission denied"

- Chạy Command Prompt với quyền Administrator
- Kiểm tra antivirus có chặn không

### Lỗi "File too large"

- Sử dụng `--onedir` thay vì `--onefile`
- Loại bỏ các module không cần thiết

## Tối ưu hóa kích thước file

### Loại bỏ modules không cần

```cmd
python -m PyInstaller --onefile --windowed --exclude-module=matplotlib --exclude-module=scipy --name=SplitVideoTool split_gui.py
```

### Sử dụng UPX để nén

```cmd
python -m PyInstaller --onefile --windowed --upx-dir=path/to/upx --name=SplitVideoTool split_gui.py
```

## Test ứng dụng

### Test trên máy build

```cmd
release\SplitVideoTool.exe
```

### Test trên máy khác

1. Copy thư mục `release` đến máy test
2. Chạy `SplitVideoTool.exe`
3. Test với các loại video khác nhau

## Ghi chú quan trọng

1. **FFmpeg**: Ứng dụng .exe sẽ tự động tải FFmpeg khi cần thiết
2. **Antivirus**: Một số antivirus có thể cảnh báo file .exe tự build
3. **Windows Defender**: Có thể cần thêm exception cho file .exe
4. **Dependencies**: File .exe đã bao gồm tất cả dependencies cần thiết

## Troubleshooting

### Lỗi "Application Error"

1. Kiểm tra Windows Event Viewer
2. Chạy với console để xem lỗi:
   ```cmd
   python -m PyInstaller --onefile --name=SplitVideoTool split_gui.py
   ```

### Lỗi "Missing DLL"

1. Cài đặt Visual C++ Redistributable
2. Kiểm tra Windows Update

### Lỗi "Access Denied"

1. Chạy với quyền Administrator
2. Kiểm tra antivirus settings

## Liên hệ hỗ trợ

Nếu gặp vấn đề khi build, hãy:
1. Kiểm tra log trong thư mục `build`
2. Chạy với console để xem lỗi chi tiết
3. Kiểm tra phiên bản Python và PyInstaller 