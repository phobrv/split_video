#!/usr/bin/env python3

import sys
import importlib

def check_moviepy():
    """Kiểm tra phiên bản moviepy và API"""
    try:
        import moviepy
        print(f"✅ MoviePy version: {moviepy.__version__}")
        
        from moviepy.video.io.VideoFileClip import VideoFileClip
        
        # Kiểm tra các phương thức có sẵn
        print("\n🔍 Kiểm tra API MoviePy:")
        
        # Tạo một clip giả để test
        try:
            # Thử tạo clip từ file test (nếu có)
            import os
            if os.path.exists("test.mp4"):
                clip = VideoFileClip("test.mp4")
                print(f"✅ Có thể tạo VideoFileClip từ file")
                
                # Kiểm tra phương thức subclip
                methods = dir(clip)
                print(f"📋 Các phương thức có sẵn: {len(methods)}")
                
                if 'subclip' in methods:
                    print("✅ Phương thức subclip có sẵn")
                    
                    # Kiểm tra cách gọi subclip
                    try:
                        test_clip = clip.subclip(0, 1)
                        print("✅ subclip(start, end) - hoạt động")
                    except Exception as e:
                        print(f"❌ subclip(start, end) - lỗi: {e}")
                    
                    try:
                        test_clip = clip.subclip(t_start=0, t_end=1)
                        print("✅ subclip(t_start, t_end) - hoạt động")
                    except Exception as e:
                        print(f"❌ subclip(t_start, t_end) - lỗi: {e}")
                    
                    try:
                        test_clip = clip.subclip(t=(0, 1))
                        print("✅ subclip(t=(start, end)) - hoạt động")
                    except Exception as e:
                        print(f"❌ subclip(t=(start, end)) - lỗi: {e}")
                    
                else:
                    print("❌ Phương thức subclip không có sẵn")
                
                clip.close()
            else:
                print("⚠️  Không tìm thấy file test.mp4 để kiểm tra")
                
        except Exception as e:
            print(f"❌ Lỗi khi kiểm tra API: {e}")
            
    except ImportError as e:
        print(f"❌ Không thể import moviepy: {e}")
        print("Hãy cài đặt: pip install moviepy")
        return False
    
    return True

if __name__ == "__main__":
    print("🔍 Kiểm tra cài đặt MoviePy...")
    check_moviepy() 