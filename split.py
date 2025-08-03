from moviepy.video.io.VideoFileClip import VideoFileClip
import os
import sys

def split_video_to_5s_chunks(input_path, output_prefix, chunk_duration=5):
    """
    Cắt video thành các block có thời lượng cố định
    
    Args:
        input_path (str): Đường dẫn đến file video gốc
        output_prefix (str): Tiền tố cho tên file output
        chunk_duration (int): Thời lượng mỗi chunk (giây), mặc định 5s
    """
    
    # Kiểm tra file input có tồn tại không
    if not os.path.exists(input_path):
        print(f"Lỗi: Không tìm thấy file {input_path}")
        return
    
    try:
        print(f"Đang tải video: {input_path}")
        video = VideoFileClip(input_path)
        duration = video.duration
        print(f"Thời lượng video: {duration:.2f} giây")
        
        start = 0
        chunk_index = 1
        total_chunks = int(duration // chunk_duration) + (1 if duration % chunk_duration > 0 else 0)
        
        print(f"Sẽ tạo {total_chunks} chunk(s)")
        
        while start < duration:
            end = min(start + chunk_duration, duration)
            print(f"Đang xử lý chunk {chunk_index}/{total_chunks} ({start:.1f}s - {end:.1f}s)")
            
            try:
                # Thử phương thức subclip với t_start và t_end
                chunk = video.subclip(t_start=start, t_end=end)
            except (AttributeError, TypeError):
                try:
                    # Thử phương thức subclip với tham số vị trí
                    chunk = video.subclip(start, end)
                except (AttributeError, TypeError):
                    # Thử phương thức subclip với tham số t
                    chunk = video.subclip(t=(start, end))
            
            output_filename = f"{output_prefix}_part{chunk_index:03d}.mp4"
            
            try:
                chunk.write_videofile(
                    output_filename, 
                    codec='libx264',
                    audio_codec='aac',
                    verbose=False,
                    logger=None
                )
                print(f"Đã tạo: {output_filename}")
            except Exception as write_error:
                print(f"Lỗi khi ghi file {output_filename}: {str(write_error)}")
                # Thử với codec khác
                try:
                    chunk.write_videofile(
                        output_filename, 
                        codec='h264',
                        audio_codec='aac',
                        verbose=False,
                        logger=None
                    )
                    print(f"Đã tạo: {output_filename} (với codec h264)")
                except Exception as write_error2:
                    print(f"Lỗi khi ghi file với codec h264: {str(write_error2)}")
            
            start += chunk_duration
            chunk_index += 1
        
        video.close()
        print("Hoàn thành!")
        
    except Exception as e:
        print(f"Lỗi khi xử lý video: {str(e)}")
        print("Thử cài đặt lại moviepy: pip install --upgrade moviepy")
        return

def main():
    """Hàm main để chạy script"""
    if len(sys.argv) == 3:
        input_file = sys.argv[1]
        output_prefix = sys.argv[2]
        split_video_to_5s_chunks(input_file, output_prefix)
    elif len(sys.argv) == 4:
        input_file = sys.argv[1]
        output_prefix = sys.argv[2]
        chunk_duration = int(sys.argv[3])
        split_video_to_5s_chunks(input_file, output_prefix, chunk_duration)
    else:
        print("Cách sử dụng:")
        print("python3 split.py <input_video> <output_prefix>")
        print("python3 split.py <input_video> <output_prefix> <chunk_duration>")
        print("\nVí dụ:")
        print("python3 split.py video.mp4 output")
        print("python3 split.py video.mp4 output 10")
        
        # Chạy với tham số mặc định nếu không có argument
        if os.path.exists("video_goc.mp4"):
            print("\nChạy với file mặc định 'video_goc.mp4'...")
            split_video_to_5s_chunks("video_goc.mp4", "video_nho")

if __name__ == "__main__":
    main()
