import tkinter as tk
from tkinter import ttk, filedialog, messagebox, scrolledtext
import threading
import os
import sys
from moviepy.video.io.VideoFileClip import VideoFileClip
import queue
import time

class SplitVideoGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Split Video Tool - Công cụ cắt video")
        self.root.geometry("600x500")
        self.root.resizable(True, True)
        
        # Thiết lập style
        style = ttk.Style()
        style.theme_use('clam')
        
        # Biến lưu trữ
        self.input_file = tk.StringVar()
        self.output_prefix = tk.StringVar()
        self.chunk_duration = tk.IntVar(value=5)
        self.progress_var = tk.DoubleVar()
        self.is_processing = False
        
        # Queue để giao tiếp giữa thread xử lý và GUI
        self.log_queue = queue.Queue()
        
        self.create_widgets()
        self.update_log()
    
    def create_widgets(self):
        # Frame chính
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Cấu hình grid
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        
        # Tiêu đề
        title_label = ttk.Label(main_frame, text="🚀 Split Video Tool", 
                               font=("Arial", 16, "bold"))
        title_label.grid(row=0, column=0, columnspan=3, pady=(0, 20))
        
        # Frame chọn file
        file_frame = ttk.LabelFrame(main_frame, text="📁 Chọn file video", padding="10")
        file_frame.grid(row=1, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=(0, 10))
        file_frame.columnconfigure(1, weight=1)
        
        ttk.Label(file_frame, text="File video:").grid(row=0, column=0, sticky=tk.W, padx=(0, 10))
        ttk.Entry(file_frame, textvariable=self.input_file, width=50).grid(row=0, column=1, sticky=(tk.W, tk.E), padx=(0, 10))
        ttk.Button(file_frame, text="Chọn file", command=self.browse_file).grid(row=0, column=2)
        
        # Frame cài đặt
        settings_frame = ttk.LabelFrame(main_frame, text="⚙️ Cài đặt", padding="10")
        settings_frame.grid(row=2, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=(0, 10))
        settings_frame.columnconfigure(1, weight=1)
        
        ttk.Label(settings_frame, text="Tiền tố output:").grid(row=0, column=0, sticky=tk.W, padx=(0, 10))
        ttk.Entry(settings_frame, textvariable=self.output_prefix, width=30).grid(row=0, column=1, sticky=(tk.W, tk.E), padx=(0, 10))
        
        ttk.Label(settings_frame, text="Thời lượng chunk (giây):").grid(row=1, column=0, sticky=tk.W, padx=(0, 10), pady=(10, 0))
        duration_spinbox = ttk.Spinbox(settings_frame, from_=1, to=3600, textvariable=self.chunk_duration, width=10)
        duration_spinbox.grid(row=1, column=1, sticky=tk.W, padx=(0, 10), pady=(10, 0))
        
        # Frame nút điều khiển
        control_frame = ttk.Frame(main_frame)
        control_frame.grid(row=3, column=0, columnspan=3, pady=(0, 10))
        
        self.start_button = ttk.Button(control_frame, text="🚀 Bắt đầu cắt video", 
                                      command=self.start_processing, style="Accent.TButton")
        self.start_button.pack(side=tk.LEFT, padx=(0, 10))
        
        self.stop_button = ttk.Button(control_frame, text="⏹️ Dừng", 
                                     command=self.stop_processing, state=tk.DISABLED)
        self.stop_button.pack(side=tk.LEFT)
        
        # Progress bar
        progress_frame = ttk.Frame(main_frame)
        progress_frame.grid(row=4, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=(0, 10))
        progress_frame.columnconfigure(0, weight=1)
        
        self.progress_bar = ttk.Progressbar(progress_frame, variable=self.progress_var, 
                                           maximum=100, length=400)
        self.progress_bar.grid(row=0, column=0, sticky=(tk.W, tk.E))
        
        # Frame log
        log_frame = ttk.LabelFrame(main_frame, text="📋 Log", padding="10")
        log_frame.grid(row=5, column=0, columnspan=3, sticky=(tk.W, tk.E, tk.N, tk.S), pady=(0, 10))
        log_frame.columnconfigure(0, weight=1)
        log_frame.rowconfigure(0, weight=1)
        main_frame.rowconfigure(5, weight=1)
        
        self.log_text = scrolledtext.ScrolledText(log_frame, height=10, width=70)
        self.log_text.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Status bar
        self.status_var = tk.StringVar(value="Sẵn sàng")
        status_bar = ttk.Label(main_frame, textvariable=self.status_var, relief=tk.SUNKEN)
        status_bar.grid(row=6, column=0, columnspan=3, sticky=(tk.W, tk.E))
    
    def browse_file(self):
        filename = filedialog.askopenfilename(
            title="Chọn file video",
            filetypes=[
                ("Video files", "*.mp4 *.avi *.mov *.mkv *.wmv *.flv"),
                ("All files", "*.*")
            ]
        )
        if filename:
            self.input_file.set(filename)
            # Tự động đặt tên output
            base_name = os.path.splitext(os.path.basename(filename))[0]
            self.output_prefix.set(base_name)
    
    def log_message(self, message):
        self.log_queue.put(message)
    
    def update_log(self):
        try:
            while True:
                message = self.log_queue.get_nowait()
                self.log_text.insert(tk.END, f"{message}\n")
                self.log_text.see(tk.END)
        except queue.Empty:
            pass
        finally:
            self.root.after(100, self.update_log)
    
    def start_processing(self):
        if not self.input_file.get():
            messagebox.showerror("Lỗi", "Vui lòng chọn file video!")
            return
        
        if not self.output_prefix.get():
            messagebox.showerror("Lỗi", "Vui lòng nhập tiền tố output!")
            return
        
        if not os.path.exists(self.input_file.get()):
            messagebox.showerror("Lỗi", "File video không tồn tại!")
            return
        
        self.is_processing = True
        self.start_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)
        self.progress_var.set(0)
        self.status_var.set("Đang xử lý...")
        
        # Chạy xử lý trong thread riêng
        self.processing_thread = threading.Thread(target=self.process_video)
        self.processing_thread.daemon = True
        self.processing_thread.start()
    
    def stop_processing(self):
        self.is_processing = False
        self.status_var.set("Đã dừng")
        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)
    
    def process_video(self):
        try:
            input_path = self.input_file.get()
            output_prefix = self.output_prefix.get()
            chunk_duration = self.chunk_duration.get()
            
            self.log_message(f"Đang tải video: {input_path}")
            video = VideoFileClip(input_path)
            duration = video.duration
            self.log_message(f"Thời lượng video: {duration:.2f} giây")
            
            start = 0
            chunk_index = 1
            total_chunks = int(duration // chunk_duration) + (1 if duration % chunk_duration > 0 else 0)
            
            self.log_message(f"Sẽ tạo {total_chunks} chunk(s)")
            
            while start < duration and self.is_processing:
                end = min(start + chunk_duration, duration)
                progress = (chunk_index - 1) / total_chunks * 100
                
                self.log_message(f"Đang xử lý chunk {chunk_index}/{total_chunks} ({start:.1f}s - {end:.1f}s)")
                
                try:
                    chunk = video.subclip(t_start=start, t_end=end)
                except (AttributeError, TypeError):
                    try:
                        chunk = video.subclip(start, end)
                    except (AttributeError, TypeError):
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
                    self.log_message(f"✅ Đã tạo: {output_filename}")
                except Exception as write_error:
                    self.log_message(f"❌ Lỗi khi ghi file {output_filename}: {str(write_error)}")
                    try:
                        chunk.write_videofile(
                            output_filename, 
                            codec='h264',
                            audio_codec='aac',
                            verbose=False,
                            logger=None
                        )
                        self.log_message(f"✅ Đã tạo: {output_filename} (với codec h264)")
                    except Exception as write_error2:
                        self.log_message(f"❌ Lỗi khi ghi file với codec h264: {str(write_error2)}")
                
                start += chunk_duration
                chunk_index += 1
                
                # Cập nhật progress
                self.progress_var.set(progress)
            
            video.close()
            
            if self.is_processing:
                self.log_message("🎉 Hoàn thành!")
                self.status_var.set("Hoàn thành")
                messagebox.showinfo("Thành công", "Đã cắt video thành công!")
            else:
                self.log_message("⏹️ Đã dừng xử lý")
                
        except Exception as e:
            self.log_message(f"❌ Lỗi khi xử lý video: {str(e)}")
            self.status_var.set("Lỗi")
            messagebox.showerror("Lỗi", f"Lỗi khi xử lý video: {str(e)}")
        finally:
            self.is_processing = False
            self.start_button.config(state=tk.NORMAL)
            self.stop_button.config(state=tk.DISABLED)

def main():
    root = tk.Tk()
    app = SplitVideoGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main() 