# Split Video Tool - Hướng dẫn cho Windows 11

## Giới thiệu

Split Video Tool là một công cụ Python để cắt video thành các đoạn nhỏ có thời lượng cố định. Tool này hỗ trợ nhiều định dạng video và sử dụng thư viện MoviePy để xử lý video.

## Yêu cầu hệ thống

- Windows 11 (hoặc Windows 10)
- Python 3.7 trở lên
- FFmpeg

## Cài đặt

### Bước 1: Cài đặt Python

1. Tải Python từ [python.org](https://www.python.org/downloads/)
2. **Quan trọng**: Chọn "Add Python to PATH" khi cài đặt
3. Kiểm tra cài đặt bằng cách mở Command Prompt và chạy:
   ```
   python --version
   ```

### Bước 2: Cài đặt FFmpeg

#### Cách 1: Sử dụng Chocolatey (Khuyến nghị)

1. Mở PowerShell với quyền Administrator
2. Chạy lệnh sau để cài đặt Chocolatey:
   ```powershell
   Set-ExecutionPolicy Bypass -Scope Process -Force
   iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))
   ```
3. Cài đặt FFmpeg:
   ```powershell
   choco install ffmpeg -y
   ```

#### Cách 2: Tải trực tiếp

1. Tải FFmpeg từ [ffmpeg.org](https://ffmpeg.org/download.html)
2. Giải nén vào thư mục (ví dụ: `C:\ffmpeg`)
3. Thêm đường dẫn vào PATH:
   - Mở System Properties → Advanced → Environment Variables
   - Thêm `C:\ffmpeg\bin` vào Path

### Bước 3: Thiết lập môi trường

Có 2 cách để thiết lập môi trường:

#### Cách 1: Sử dụng script PowerShell (Khuyến nghị)

1. Mở PowerShell với quyền Administrator
2. Chạy script setup:
   ```powershell
   .\setup_windows.ps1 -InstallChocolatey -InstallFFmpeg
   ```

#### Cách 2: Sử dụng script Batch

1. Mở Command Prompt
2. Chạy script setup:
   ```cmd
   setup_windows.bat
   ```

#### Cách 3: Thiết lập thủ công

1. Tạo môi trường ảo:
   ```cmd
   python -m venv venv
   ```

2. Kích hoạt môi trường ảo:
   ```cmd
   venv\Scripts\activate.bat
   ```

3. Cài đặt dependencies:
   ```cmd
   python -m pip install --upgrade pip
   python -m pip install -r requirements.txt
   ```

## Sử dụng

### Kích hoạt môi trường ảo

Trước khi sử dụng, luôn kích hoạt môi trường ảo:

```cmd
venv\Scripts\activate.bat
```

### Cú pháp cơ bản

```cmd
python split.py <input_video> <output_prefix>
```

### Ví dụ sử dụng

1. Cắt video thành các đoạn 5 giây (mặc định):
   ```cmd
   python split.py video.mp4 output
   ```

2. Cắt video thành các đoạn 10 giây:
   ```cmd
   python split.py video.mp4 output 10
   ```

3. Cắt video thành các đoạn 30 giây:
   ```cmd
   python split.py video.mp4 output 30
   ```

### Kết quả

Script sẽ tạo các file video với tên:
- `output_part001.mp4`
- `output_part002.mp4`
- `output_part003.mp4`
- ...

## Xử lý lỗi

### Lỗi "Python not found"
- Đảm bảo Python đã được cài đặt và thêm vào PATH
- Thử chạy lại script setup

### Lỗi "FFmpeg not found"
- Cài đặt FFmpeg theo hướng dẫn ở trên
- Đảm bảo FFmpeg đã được thêm vào PATH

### Lỗi khi xử lý video
- Kiểm tra định dạng video có được hỗ trợ không
- Thử với video khác để kiểm tra
- Cập nhật MoviePy: `pip install --upgrade moviepy`

### Lỗi quyền truy cập
- Chạy Command Prompt hoặc PowerShell với quyền Administrator
- Kiểm tra quyền ghi vào thư mục hiện tại

## Tính năng

- Hỗ trợ nhiều định dạng video (MP4, AVI, MOV, MKV, ...)
- Cắt video thành các đoạn có thời lượng cố định
- Tự động xử lý codec video
- Hiển thị tiến trình xử lý
- Xử lý lỗi thông minh

## Hỗ trợ

Nếu gặp vấn đề, hãy kiểm tra:
1. Python và FFmpeg đã được cài đặt đúng cách
2. Môi trường ảo đã được kích hoạt
3. Tất cả dependencies đã được cài đặt
4. File video đầu vào hợp lệ

## Ghi chú

- Tool này sử dụng MoviePy để xử lý video
- FFmpeg được sử dụng làm backend cho việc xử lý video
- Các file output sẽ có định dạng MP4 với codec H.264 