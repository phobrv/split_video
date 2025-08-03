# Split Video Tool

Công cụ cắt video thành các block 5 giây sử dụng Python.

## Yêu cầu hệ thống

- Python 3.7 trở lên
- FFmpeg (cần thiết cho moviepy)

## Cài đặt

### Cách nhanh (macOS):

**Với bash/zsh:**
```bash
chmod +x setup_macos.sh
./setup_macos.sh
```

**Với fish shell:**
```fish
chmod +x setup_macos_fish.sh
./setup_macos_fish.sh
```

### Cài đặt thủ công:

#### 1. Cài đặt FFmpeg

**Trên macOS (sử dụng Homebrew):**
```bash
brew install ffmpeg
```

**Trên Ubuntu/Debian:**
```bash
sudo apt update
sudo apt install ffmpeg
```

**Trên Windows:**

**Cách 1: Sử dụng Chocolatey (Khuyến nghị)**
```cmd
# Cài đặt Chocolatey trước (nếu chưa có)
# Mở PowerShell với quyền Administrator và chạy:
Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))

# Sau đó cài FFmpeg:
choco install ffmpeg
```

**Cách 2: Tải thủ công**
1. Truy cập: https://ffmpeg.org/download.html
2. Tải phiên bản Windows (chọn "Windows builds from gyan.dev")
3. Giải nén file zip
4. Copy thư mục `ffmpeg-xxx` vào `C:\ffmpeg`
5. Thêm `C:\ffmpeg\bin` vào PATH:
   - Mở "System Properties" → "Environment Variables"
   - Trong "System variables", tìm "Path" → "Edit"
   - Thêm `C:\ffmpeg\bin` vào danh sách
   - Click "OK" để lưu

**Cách 3: Sử dụng winget**
```cmd
winget install ffmpeg
```

**Kiểm tra cài đặt:**
```cmd
ffmpeg -version
```

#### Cài đặt Python (nếu chưa có):
- Tải Python từ: https://www.python.org/downloads/
- **Quan trọng**: Chọn "Add Python to PATH" khi cài đặt
- Kiểm tra: `python --version`

#### Tạo môi trường ảo (khuyến nghị):

**Trên macOS/Linux:**
```bash
# Tạo môi trường ảo
python3 -m venv venv

# Kích hoạt môi trường ảo
source venv/bin/activate
```

**Trên macOS với fish shell:**
```fish
# Tạo môi trường ảo
python3 -m venv venv

# Kích hoạt môi trường ảo (fish shell)
source venv/bin/activate.fish
```

**Trên Windows:**
```cmd
# Tạo môi trường ảo
python -m venv venv

# Kích hoạt môi trường ảo
venv\Scripts\activate

# Hoặc nếu dùng PowerShell:
venv\Scripts\Activate.ps1
```

#### Cài đặt các thư viện Python:

**Cách 1: Cài đặt trực tiếp**
```bash
pip install moviepy
```

**Cách 2: Cài đặt từ file requirements.txt**
```bash
pip install -r requirements.txt
```

**Kiểm tra cài đặt:**
```bash
python -c "import moviepy; print('MoviePy đã cài đặt thành công!')"
```

**Lưu ý quan trọng cho macOS:**
- Nếu gặp lỗi "externally-managed-environment", hãy đảm bảo đã kích hoạt môi trường ảo trước khi cài đặt
- Sử dụng `python3` thay vì `python` trên macOS
- Nếu vẫn gặp lỗi, thử: `python3 -m pip install -r requirements.txt`

## Sử dụng

1. Đặt video cần cắt vào thư mục dự án
2. Chạy script:

**Trên macOS/Linux:**
```bash
python3 split.py
```

**Trên Windows:**
```cmd
# Sử dụng Command Prompt
python split.py

# Hoặc sử dụng PowerShell
python split.py

# Nếu lệnh python không hoạt động, thử:
py split.py
```

3. Hoặc chỉnh sửa tham số trong file `split.py`:
```python
split_video_to_5s_chunks("ten_video_cua_ban.mp4", "ten_output")
```

4. Hoặc sử dụng command line arguments:
```bash
# Trên macOS/Linux:
python3 split.py video.mp4 output
python3 split.py video.mp4 output 10

# Trên Windows:
python split.py video.mp4 output
python split.py video.mp4 output 10
```

## Kết quả

Script sẽ tạo ra các file video nhỏ với tên:
- `ten_output_part1.mp4` (0-5s)
- `ten_output_part2.mp4` (5-10s)
- `ten_output_part3.mp4` (10-15s)
- ...

## Troubleshooting

### Lỗi "FFmpeg not found"
- Đảm bảo FFmpeg đã được cài đặt và có trong PATH
- Kiểm tra bằng lệnh: `ffmpeg -version`
- **Trên Windows**: Kiểm tra PATH có chứa đường dẫn đến thư mục bin của FFmpeg

### Lỗi "moviepy not found"
- Cài đặt lại moviepy: `pip install moviepy`
- **Trên Windows**: Đảm bảo đã kích hoạt môi trường ảo: `venv\Scripts\activate`
- **Trên macOS**: Sử dụng `python3 -m pip install moviepy`

### Lỗi "externally-managed-environment" (macOS)
- Đảm bảo đã tạo và kích hoạt môi trường ảo:
  ```bash
  python3 -m venv venv
  source venv/bin/activate
  python3 -m pip install -r requirements.txt
  ```
- **Với fish shell:**
  ```fish
  python3 -m venv venv
  source venv/bin/activate.fish
  python3 -m pip install -r requirements.txt
  ```
- Hoặc sử dụng `--break-system-packages` (không khuyến nghị):
  ```bash
  python3 -m pip install --break-system-packages -r requirements.txt
  ```

### Lỗi "python not found" (Windows)
- Kiểm tra Python đã được thêm vào PATH
- Thử sử dụng `py` thay vì `python`: `py split.py`

### Lỗi PowerShell Execution Policy
- Mở PowerShell với quyền Administrator
- Chạy: `Set-ExecutionPolicy RemoteSigned`

### Video không có âm thanh
- Đảm bảo codec video được hỗ trợ
- Thử thêm tham số audio codec: `audio_codec='aac'`

### Lỗi encoding trên Windows
- Thử thay đổi codec: `codec='libx264'` thành `codec='h264'`
- Hoặc cài đặt thêm: `pip install imageio-ffmpeg`

### Lỗi "subclip" không hoạt động
- Kiểm tra phiên bản moviepy: `python3 check_moviepy.py`
- Cập nhật moviepy: `pip install --upgrade moviepy`
- Hoặc cài đặt phiên bản cụ thể: `pip install moviepy==1.0.3` 