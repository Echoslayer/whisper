import os
import sys
import time
import re
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from pathlib import Path
import threading
import queue
# Adjust the path to import from the correct location
sys.path.append(os.path.abspath(os.path.dirname(__file__)))
from voice2transcripts import clear_output_folder, convert_to_wav, split_audio, transcribe_audio
from time_stamp_cleaner import clean_transcription, save_cleaned_transcription, convert_to_srt

class TranscriptionGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Audio Transcription Tool")
        self.root.geometry("800x800")
        
        # Queue for thread-safe GUI updates
        self.queue = queue.Queue()
        
        # Default configuration values
        self.DEFAULT_INPUT_FILE = "../data/demo/demo.wav"
        self.DEFAULT_INPUT_FOLDER = "../data/demo"
        self.DEFAULT_OUTPUT_DIR = "../data/output_clips"
        self.DEFAULT_CLIP_DURATION_SEC = 15  # in seconds for single file
        self.DEFAULT_CLIP_DURATION_MIN = 0.25  # in minutes for folder processing (15 seconds)
        self.DEFAULT_WHISPER_EXEC = "../whisper.cpp/build/bin/whisper-cli"
        self.DEFAULT_WHISPER_MODEL = "../whisper.cpp/models/ggml-medium.bin"
        self.DEFAULT_LANGUAGE = "zh"
        self.DEFAULT_TRANSCRIPT_FILENAME = "transcription.txt"
        self.DEFAULT_WORKERS = 3
        self.DEFAULT_USE_THREADS = False
        self.DEFAULT_REST_TIME = 180  # in seconds, default rest time between transcriptions
        
        # State variables for progress animation
        self.is_processing = False
        self.progress_text = ""
        self.progress_counter = 0
        self.stop_requested = False
        
        # Variable to store the current processing thread for interruption
        self.current_thread = None
        
        self.setup_ui()
        
    def setup_ui(self):
        # Notebook (tabbed interface)
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(pady=10, expand=True, fill='both')
        
        # Single File Tab
        self.single_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.single_frame, text="Single File")
        
        # Folder Tab
        self.folder_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.folder_frame, text="Folder")
        
        # Setup Single File Tab
        ttk.Label(self.single_frame, text="Input Audio File:").grid(row=0, column=0, padx=5, pady=5, sticky='w')
        self.input_file_entry = ttk.Entry(self.single_frame, width=50)
        self.input_file_entry.grid(row=0, column=1, padx=5, pady=5)
        self.input_file_entry.insert(0, self.DEFAULT_INPUT_FILE)
        ttk.Button(self.single_frame, text="Browse", command=self.browse_input_file).grid(row=0, column=2, padx=5, pady=5)
        
        ttk.Label(self.single_frame, text="Output Directory:").grid(row=1, column=0, padx=5, pady=5, sticky='w')
        self.output_dir_single_entry = ttk.Entry(self.single_frame, width=50)
        self.output_dir_single_entry.grid(row=1, column=1, padx=5, pady=5)
        self.output_dir_single_entry.insert(0, self.DEFAULT_OUTPUT_DIR)
        ttk.Button(self.single_frame, text="Browse", command=self.browse_output_dir_single).grid(row=1, column=2, padx=5, pady=5)
        
        ttk.Label(self.single_frame, text="Clip Duration (sec):").grid(row=2, column=0, padx=5, pady=5, sticky='w')
        self.clip_duration_sec = ttk.Scale(self.single_frame, from_=1, to=1800, orient='horizontal')
        self.clip_duration_sec.grid(row=2, column=1, padx=5, pady=5, sticky='ew')
        self.clip_duration_sec.set(self.DEFAULT_CLIP_DURATION_SEC)
        self.clip_duration_sec_label = ttk.Label(self.single_frame, text=str(self.DEFAULT_CLIP_DURATION_SEC))
        self.clip_duration_sec_label.grid(row=2, column=2, padx=5, pady=5)
        self.clip_duration_sec.bind("<ButtonRelease-1>", self.update_clip_duration_sec_label)
        
        ttk.Label(self.single_frame, text="Whisper Executable:").grid(row=3, column=0, padx=5, pady=5, sticky='w')
        self.whisper_exec_single_entry = ttk.Entry(self.single_frame, width=50)
        self.whisper_exec_single_entry.grid(row=3, column=1, padx=5, pady=5)
        self.whisper_exec_single_entry.insert(0, self.DEFAULT_WHISPER_EXEC)
        ttk.Button(self.single_frame, text="Browse", command=self.browse_whisper_exec_single).grid(row=3, column=2, padx=5, pady=5)
        
        ttk.Label(self.single_frame, text="Whisper Model:").grid(row=4, column=0, padx=5, pady=5, sticky='w')
        self.whisper_model_single_entry = ttk.Entry(self.single_frame, width=50)
        self.whisper_model_single_entry.grid(row=4, column=1, padx=5, pady=5)
        self.whisper_model_single_entry.insert(0, self.DEFAULT_WHISPER_MODEL)
        ttk.Button(self.single_frame, text="Browse", command=self.browse_whisper_model_single).grid(row=4, column=2, padx=5, pady=5)
        
        ttk.Label(self.single_frame, text="Language:").grid(row=5, column=0, padx=5, pady=5, sticky='w')
        self.language_single = ttk.Combobox(self.single_frame, values=["zh", "en"], state='readonly')
        self.language_single.grid(row=5, column=1, padx=5, pady=5, sticky='w')
        self.language_single.set(self.DEFAULT_LANGUAGE)
        
        ttk.Label(self.single_frame, text="Transcript Filename:").grid(row=6, column=0, padx=5, pady=5, sticky='w')
        self.transcript_filename_entry = ttk.Entry(self.single_frame, width=50)
        self.transcript_filename_entry.grid(row=6, column=1, padx=5, pady=5)
        self.transcript_filename_entry.insert(0, self.DEFAULT_TRANSCRIPT_FILENAME)
        
        ttk.Label(self.single_frame, text="Workers:").grid(row=7, column=0, padx=5, pady=5, sticky='w')
        self.workers_single = ttk.Scale(self.single_frame, from_=1, to=8, orient='horizontal')
        self.workers_single.grid(row=7, column=1, padx=5, pady=5, sticky='ew')
        self.workers_single.set(self.DEFAULT_WORKERS)
        self.workers_single_label = ttk.Label(self.single_frame, text=str(self.DEFAULT_WORKERS))
        self.workers_single_label.grid(row=7, column=2, padx=5, pady=5)
        self.workers_single.bind("<ButtonRelease-1>", self.update_workers_single_label)
        
        ttk.Label(self.single_frame, text="Parallel Method:").grid(row=8, column=0, padx=5, pady=5, sticky='w')
        self.use_threads_single = ttk.Combobox(self.single_frame, values=["Multithreading", "Multiprocessing"], state='readonly')
        self.use_threads_single.grid(row=8, column=1, padx=5, pady=5, sticky='w')
        self.use_threads_single.set("Multithreading" if self.DEFAULT_USE_THREADS else "Multiprocessing")
        
        # Frame for process buttons in Single File Tab
        single_button_frame = ttk.Frame(self.single_frame)
        single_button_frame.grid(row=9, column=0, columnspan=3, pady=10)
        ttk.Button(single_button_frame, text="Process Single File", command=self.process_single).pack(side='left', padx=5)
        ttk.Button(single_button_frame, text="Stop Processing", command=self.stop_processing).pack(side='left', padx=5)
        
        # Current Status Log Area for Single File (updates continuously)
        single_status_frame = ttk.Frame(self.single_frame)
        single_status_frame.grid(row=10, column=0, columnspan=3, padx=5, pady=5, sticky='ew')
        ttk.Label(single_status_frame, text="Current Status:").pack(side='top', anchor='w')
        self.single_status_text = tk.Text(single_status_frame, height=2, width=80, wrap=tk.WORD)
        self.single_status_text.pack(side='left', fill='x', expand=True, padx=5, pady=5)
        
        # Historical Log Text Area for Single File (persists all logs)
        single_log_frame = ttk.Frame(self.single_frame)
        single_log_frame.grid(row=11, column=0, columnspan=3, padx=5, pady=5, sticky='nsew')
        ttk.Label(single_log_frame, text="Historical Logs:").pack(side='top', anchor='w')
        self.single_log_text = tk.Text(single_log_frame, height=8, width=80, wrap=tk.WORD)
        self.single_log_text.pack(side='left', fill='both', expand=True, padx=5, pady=5)
        single_scrollbar = ttk.Scrollbar(single_log_frame, orient='vertical', command=self.single_log_text.yview)
        single_scrollbar.pack(side='right', fill='y')
        self.single_log_text['yscrollcommand'] = single_scrollbar.set
        
        # Setup Folder Tab
        ttk.Label(self.folder_frame, text="Input Folder:").grid(row=0, column=0, padx=5, pady=5, sticky='w')
        self.input_folder_entry = ttk.Entry(self.folder_frame, width=50)
        self.input_folder_entry.grid(row=0, column=1, padx=5, pady=5)
        self.input_folder_entry.insert(0, self.DEFAULT_INPUT_FOLDER)
        ttk.Button(self.folder_frame, text="Browse", command=self.browse_input_folder).grid(row=0, column=2, padx=5, pady=5)
        
        ttk.Label(self.folder_frame, text="Output Directory:").grid(row=1, column=0, padx=5, pady=5, sticky='w')
        self.output_dir_folder_entry = ttk.Entry(self.folder_frame, width=50)
        self.output_dir_folder_entry.grid(row=1, column=1, padx=5, pady=5)
        self.output_dir_folder_entry.insert(0, self.DEFAULT_OUTPUT_DIR)
        ttk.Button(self.folder_frame, text="Browse", command=self.browse_output_dir_folder).grid(row=1, column=2, padx=5, pady=5)
        
        ttk.Label(self.folder_frame, text="Clip Duration (min):").grid(row=2, column=0, padx=5, pady=5, sticky='w')
        self.clip_duration_min = ttk.Scale(self.folder_frame, from_=1, to=30, orient='horizontal')
        self.clip_duration_min.grid(row=2, column=1, padx=5, pady=5, sticky='ew')
        self.clip_duration_min.set(self.DEFAULT_CLIP_DURATION_MIN)
        self.clip_duration_min_label = ttk.Label(self.folder_frame, text=str(self.DEFAULT_CLIP_DURATION_MIN))
        self.clip_duration_min_label.grid(row=2, column=2, padx=5, pady=5)
        self.clip_duration_min.bind("<ButtonRelease-1>", self.update_clip_duration_min_label)
        
        ttk.Label(self.folder_frame, text="Whisper Executable:").grid(row=3, column=0, padx=5, pady=5, sticky='w')
        self.whisper_exec_folder_entry = ttk.Entry(self.folder_frame, width=50)
        self.whisper_exec_folder_entry.grid(row=3, column=1, padx=5, pady=5)
        self.whisper_exec_folder_entry.insert(0, self.DEFAULT_WHISPER_EXEC)
        ttk.Button(self.folder_frame, text="Browse", command=self.browse_whisper_exec_folder).grid(row=3, column=2, padx=5, pady=5)
        
        ttk.Label(self.folder_frame, text="Whisper Model:").grid(row=4, column=0, padx=5, pady=5, sticky='w')
        self.whisper_model_folder_entry = ttk.Entry(self.folder_frame, width=50)
        self.whisper_model_folder_entry.grid(row=4, column=1, padx=5, pady=5)
        self.whisper_model_folder_entry.insert(0, self.DEFAULT_WHISPER_MODEL)
        ttk.Button(self.folder_frame, text="Browse", command=self.browse_whisper_model_folder).grid(row=4, column=2, padx=5, pady=5)
        
        ttk.Label(self.folder_frame, text="Language:").grid(row=5, column=0, padx=5, pady=5, sticky='w')
        self.language_folder = ttk.Combobox(self.folder_frame, values=["zh", "en"], state='readonly')
        self.language_folder.grid(row=5, column=1, padx=5, pady=5, sticky='w')
        self.language_folder.set(self.DEFAULT_LANGUAGE)
        
        ttk.Label(self.folder_frame, text="Workers:").grid(row=6, column=0, padx=5, pady=5, sticky='w')
        self.workers_folder = ttk.Scale(self.folder_frame, from_=1, to=8, orient='horizontal')
        self.workers_folder.grid(row=6, column=1, padx=5, pady=5, sticky='ew')
        self.workers_folder.set(self.DEFAULT_WORKERS)
        self.workers_folder_label = ttk.Label(self.folder_frame, text=str(self.DEFAULT_WORKERS))
        self.workers_folder_label.grid(row=6, column=2, padx=5, pady=5)
        self.workers_folder.bind("<ButtonRelease-1>", self.update_workers_folder_label)
        
        ttk.Label(self.folder_frame, text="Parallel Method:").grid(row=7, column=0, padx=5, pady=5, sticky='w')
        self.use_threads_folder = ttk.Combobox(self.folder_frame, values=["Multithreading", "Multiprocessing"], state='readonly')
        self.use_threads_folder.grid(row=7, column=1, padx=5, pady=5, sticky='w')
        self.use_threads_folder.set("Multithreading" if self.DEFAULT_USE_THREADS else "Multiprocessing")
        
        ttk.Label(self.folder_frame, text="Rest Time (sec):").grid(row=8, column=0, padx=5, pady=5, sticky='w')
        self.rest_time = ttk.Scale(self.folder_frame, from_=0, to=600, orient='horizontal')
        self.rest_time.grid(row=8, column=1, padx=5, pady=5, sticky='ew')
        self.rest_time.set(self.DEFAULT_REST_TIME)
        self.rest_time_label = ttk.Label(self.folder_frame, text=str(self.DEFAULT_REST_TIME))
        self.rest_time_label.grid(row=8, column=2, padx=5, pady=5)
        self.rest_time.bind("<ButtonRelease-1>", self.update_rest_time_label)
        
        # Frame for process buttons in Folder Tab
        folder_button_frame = ttk.Frame(self.folder_frame)
        folder_button_frame.grid(row=9, column=0, columnspan=3, pady=10)
        ttk.Button(folder_button_frame, text="Process Folder", command=self.process_folder).pack(side='left', padx=5)
        ttk.Button(folder_button_frame, text="Stop Processing", command=self.stop_processing).pack(side='left', padx=5)
        
        # Current Status Log Area for Folder (updates continuously)
        folder_status_frame = ttk.Frame(self.folder_frame)
        folder_status_frame.grid(row=10, column=0, columnspan=3, padx=5, pady=5, sticky='ew')
        ttk.Label(folder_status_frame, text="Current Status:").pack(side='top', anchor='w')
        self.folder_status_text = tk.Text(folder_status_frame, height=2, width=80, wrap=tk.WORD)
        self.folder_status_text.pack(side='left', fill='x', expand=True, padx=5, pady=5)
        
        # Historical Log Text Area for Folder (persists all logs)
        folder_log_frame = ttk.Frame(self.folder_frame)
        folder_log_frame.grid(row=11, column=0, columnspan=3, padx=5, pady=5, sticky='nsew')
        ttk.Label(folder_log_frame, text="Historical Logs:").pack(side='top', anchor='w')
        self.folder_log_text = tk.Text(folder_log_frame, height=8, width=80, wrap=tk.WORD)
        self.folder_log_text.pack(side='left', fill='both', expand=True, padx=5, pady=5)
        folder_scrollbar = ttk.Scrollbar(folder_log_frame, orient='vertical', command=self.folder_log_text.yview)
        folder_scrollbar.pack(side='right', fill='y')
        self.folder_log_text['yscrollcommand'] = folder_scrollbar.set
        
        # Bottom Buttons for Cleaning and SRT Conversion
        bottom_frame = ttk.Frame(self.root)
        bottom_frame.pack(pady=5, fill='x', side='bottom')
        ttk.Button(bottom_frame, text="Clean Transcripts", command=self.clean_transcripts).pack(side='left', padx=5)
        ttk.Button(bottom_frame, text="Convert to SRT", command=self.convert_to_srt).pack(side='left', padx=5)
        ttk.Button(bottom_frame, text="Clean SRT Files", command=self.clean_srt_files).pack(side='left', padx=5)
        ttk.Button(bottom_frame, text="One-Click SRT (All Steps)", command=self.one_click_srt).pack(side='left', padx=5)
        ttk.Button(bottom_frame, text="Stop Processing", command=self.stop_processing).pack(side='left', padx=5)
        
        # Configure grid weights
        self.single_frame.grid_columnconfigure(1, weight=1)
        self.single_frame.grid_rowconfigure(11, weight=1)
        self.folder_frame.grid_columnconfigure(1, weight=1)
        self.folder_frame.grid_rowconfigure(11, weight=1)
        
        # Check queue for updates
        self.root.after(100, self.check_queue)
        self.root.after(500, self.update_progress_animation)
    
    def update_clip_duration_sec_label(self, event=None):
        self.clip_duration_sec_label.config(text=str(int(self.clip_duration_sec.get())))
    
    def update_clip_duration_min_label(self, event=None):
        self.clip_duration_min_label.config(text=str(int(self.clip_duration_min.get())))
    
    def update_workers_single_label(self, event=None):
        self.workers_single_label.config(text=str(int(self.workers_single.get())))
    
    def update_workers_folder_label(self, event=None):
        self.workers_folder_label.config(text=str(int(self.workers_folder.get())))
    
    def update_rest_time_label(self, event=None):
        self.rest_time_label.config(text=str(int(self.rest_time.get())))
    
    def browse_input_file(self):
        filename = filedialog.askopenfilename(filetypes=[("Audio/Video Files", "*.mp3 *.mp4 *.m4a *.wav *.flac *.ogg *.webm *.mkv")])
        if filename:
            self.input_file_entry.delete(0, tk.END)
            self.input_file_entry.insert(0, filename)
    
    def browse_input_folder(self):
        foldername = filedialog.askdirectory()
        if foldername:
            self.input_folder_entry.delete(0, tk.END)
            self.input_folder_entry.insert(0, foldername)
    
    def browse_output_dir_single(self):
        foldername = filedialog.askdirectory()
        if foldername:
            self.output_dir_single_entry.delete(0, tk.END)
            self.output_dir_single_entry.insert(0, foldername)
    
    def browse_output_dir_folder(self):
        foldername = filedialog.askdirectory()
        if foldername:
            self.output_dir_folder_entry.delete(0, tk.END)
            self.output_dir_folder_entry.insert(0, foldername)
    
    def browse_whisper_exec_single(self):
        filename = filedialog.askopenfilename(filetypes=[("Executable Files", "*")])
        if filename:
            self.whisper_exec_single_entry.delete(0, tk.END)
            self.whisper_exec_single_entry.insert(0, filename)
    
    def browse_whisper_exec_folder(self):
        filename = filedialog.askopenfilename(filetypes=[("Executable Files", "*")])
        if filename:
            self.whisper_exec_folder_entry.delete(0, tk.END)
            self.whisper_exec_folder_entry.insert(0, filename)
    
    def browse_whisper_model_single(self):
        filename = filedialog.askopenfilename(filetypes=[("Model Files", "*.bin *.mlmodelc")])
        if filename:
            self.whisper_model_single_entry.delete(0, tk.END)
            self.whisper_model_single_entry.insert(0, filename)
    
    def browse_whisper_model_folder(self):
        filename = filedialog.askopenfilename(filetypes=[("Model Files", "*.bin *.mlmodelc")])
        if filename:
            self.whisper_model_folder_entry.delete(0, tk.END)
            self.whisper_model_folder_entry.insert(0, filename)
    
    def log_message(self, message, target=None):
        """Add message to the queue for thread-safe GUI update."""
        self.queue.put(("log", message, target))
        if "Starting" in message or "Processing" in message:
            self.is_processing = True
            self.progress_text = message
        elif any(phrase in message.lower() for phrase in ["completed", "all files processed", "error", "stopped by user"]):
            self.is_processing = False
            self.progress_text = ""
    
    def update_progress_animation(self):
        """Update the progress animation text if a process is running."""
        if self.is_processing:
            self.progress_counter = (self.progress_counter + 1) % 4
            dots = "." * self.progress_counter + " " * (3 - self.progress_counter)
            animated_text = f"{self.progress_text}{dots}"
            if self.notebook.index(self.notebook.select()) == 0:  # Single File Tab
                self.single_status_text.delete(1.0, tk.END)
                self.single_status_text.insert(tk.END, animated_text + "\n")
                self.single_status_text.see(tk.END)
            else:  # Folder Tab
                self.folder_status_text.delete(1.0, tk.END)
                self.folder_status_text.insert(tk.END, animated_text + "\n")
                self.folder_status_text.see(tk.END)
        self.root.after(500, self.update_progress_animation)
    
    def check_queue(self):
        """Check the queue for new messages and update GUI."""
        try:
            while not self.queue.empty():
                action, *args = self.queue.get_nowait()
                if action == "log":
                    message, target = args
                    if target == "single":
                        self.single_log_text.insert(tk.END, message + "\n")
                        self.single_log_text.see(tk.END)
                        self.single_status_text.delete(1.0, tk.END)
                        self.single_status_text.insert(tk.END, message + "\n")
                        self.single_status_text.see(tk.END)
                    elif target == "folder":
                        self.folder_log_text.insert(tk.END, message + "\n")
                        self.folder_log_text.see(tk.END)
                        self.folder_status_text.delete(1.0, tk.END)
                        self.folder_status_text.insert(tk.END, message + "\n")
                        self.folder_status_text.see(tk.END)
                    else:
                        self.single_log_text.insert(tk.END, message + "\n")
                        self.single_log_text.see(tk.END)
                        self.folder_log_text.insert(tk.END, message + "\n")
                        self.folder_log_text.see(tk.END)
                        self.single_status_text.delete(1.0, tk.END)
                        self.single_status_text.insert(tk.END, message + "\n")
                        self.single_status_text.see(tk.END)
                        self.folder_status_text.delete(1.0, tk.END)
                        self.folder_status_text.insert(tk.END, message + "\n")
                        self.folder_status_text.see(tk.END)
        except queue.Empty:
            pass
        finally:
            self.root.after(100, self.check_queue)
    
    def stop_processing(self):
        """Attempt to stop the current processing thread."""
        if self.is_processing and not self.stop_requested:
            self.is_processing = False
            self.stop_requested = True
            self.log_message("🛑 Processing interrupted by user.", "both")
            # Note: Actual thread termination is complex in Python. For simplicity, we just set a flag.
            # In a real-world scenario, you'd need to implement a more robust interruption mechanism.
        else:
            if not self.stop_requested:
                self.log_message("ℹ️ No active processing to stop.", "both")
    
    def process_single(self):
        def run():
            try:
                input_file = self.input_file_entry.get()
                output_dir = self.output_dir_single_entry.get()
                clip_duration_sec = int(self.clip_duration_sec.get())
                whisper_exec = self.whisper_exec_single_entry.get()
                whisper_model = self.whisper_model_single_entry.get()
                language = self.language_single.get()
                transcript_filename = self.transcript_filename_entry.get()
                workers = int(self.workers_single.get())
                use_threads = self.use_threads_single.get() == "Multithreading"
                
                if not os.path.exists(input_file):
                    self.log_message(f"❌ Input file not found: {input_file}", "single")
                    return
                
                self.log_message("🚀 Starting audio processing...", "single")
                
                # Clear old files
                clear_output_folder(output_dir)
                
                if self.stop_requested:
                    self.log_message("🛑 Processing stopped by user.", "single")
                    return
                
                # Process audio
                wav_file = convert_to_wav(input_file, output_dir)
                self.log_message("🔄 Audio converted to WAV format", "single")
                
                if self.stop_requested:
                    self.log_message("🛑 Processing stopped by user.", "single")
                    return
                
                clip_files = split_audio(wav_file, clip_duration_sec, output_dir)
                self.log_message(f"✅ Audio split into {len(clip_files)} clips", "single")
                
                if self.stop_requested:
                    self.log_message("🛑 Processing stopped by user.", "single")
                    return
                
                transcribe_audio(clip_files, output_dir, whisper_exec, whisper_model, language, transcript_filename=transcript_filename, workers=workers, use_threads=use_threads)
                transcript_path = os.path.join(os.path.dirname(output_dir), 'transcripts', transcript_filename)
                self.log_message(f"🎉 Transcription completed! Saved to {transcript_path}", "single")
            except Exception as e:
                self.log_message(f"❌ Error during processing: {e}", "single")
            finally:
                self.is_processing = False
                self.stop_requested = False
                self.log_message("ℹ️ Processing finished.", "single")
        
        self.is_processing = True
        self.stop_requested = False
        self.current_thread = threading.Thread(target=run, daemon=True)
        self.current_thread.start()
    
    def process_folder(self):
        def run():
            try:
                input_folder = self.input_folder_entry.get()
                output_dir = self.output_dir_folder_entry.get()
                clip_duration_sec = int(self.clip_duration_min.get()) * 60  # Convert minutes to seconds
                whisper_exec = self.whisper_exec_folder_entry.get()
                whisper_model = self.whisper_model_folder_entry.get()
                language = self.language_folder.get()
                workers = int(self.workers_folder.get())
                use_threads = self.use_threads_folder.get() == "Multithreading"
                rest_time = int(self.rest_time.get())
                
                if not os.path.exists(input_folder):
                    self.log_message(f"❌ Input folder not found: {input_folder}", "folder")
                    return
                
                supported_extensions = ('.mp3', '.mp4', '.m4a', '.wav', '.flac', '.ogg', '.webm', '.mkv')
                input_files = [f for f in os.listdir(input_folder) if f.lower().endswith(supported_extensions)]
                
                if not input_files:
                    self.log_message(f"❌ No audio/video files found in {input_folder}", "folder")
                    return
                
                total_files = len(input_files)
                self.log_message(f"📁 Found {total_files} files to process", "folder")
                
                folder_name = os.path.basename(input_folder)
                transcript_dir = os.path.join(os.path.dirname(output_dir), 'transcripts', folder_name)
                Path(transcript_dir).mkdir(parents=True, exist_ok=True)
                
                processed_count = 0
                for idx, input_file in enumerate(input_files, 1):
                    if self.stop_requested:
                        self.log_message("🛑 Processing stopped by user.", "folder")
                        break
                    input_file_path = os.path.join(input_folder, input_file)
                    base_name = os.path.splitext(input_file)[0]
                    transcript_filename = f"{base_name}.txt"
                    self.log_message(f"🚀 Processing file {idx}/{total_files}: {input_file}...", "folder")
                    
                    # Step 1: Clear output folder
                    clear_output_folder(output_dir)
                    
                    if self.stop_requested:
                        self.log_message("🛑 Processing stopped by user.", "folder")
                        break
                    
                    # Step 2: Convert to WAV
                    wav_file = convert_to_wav(input_file_path, output_dir)
                    
                    if self.stop_requested:
                        self.log_message("🛑 Processing stopped by user.", "folder")
                        break
                    
                    # Step 3: Split audio
                    clip_files = split_audio(wav_file, clip_duration_sec, output_dir)
                    
                    if self.stop_requested:
                        self.log_message("🛑 Processing stopped by user.", "folder")
                        break
                    
                    # Step 4: Transcribe audio (ensure this completes before moving to the next file)
                    transcribe_audio(clip_files, output_dir, whisper_exec, whisper_model, language, transcript_filename, workers=workers, use_threads=use_threads)
                    transcript_path = os.path.join(transcript_dir, transcript_filename)
                    os.rename(os.path.join(os.path.dirname(output_dir), 'transcripts', transcript_filename), transcript_path)
                    self.log_message(f"✅ File {idx}/{total_files} processed! Transcript saved to {transcript_path}", "folder")
                    
                    processed_count += 1
                    
                    if idx < total_files and rest_time > 0:
                        self.log_message(f"⏳ Resting for {rest_time} seconds to avoid overheating...", "folder")
                        time.sleep(rest_time)
                    else:
                        self.log_message("ℹ️ This is the last file, no rest needed.", "folder")
                
                if not self.stop_requested and processed_count == total_files:
                    self.log_message("🎉 All files processed!", "folder")
                elif self.stop_requested:
                    self.log_message(f"🛑 Stopped after processing {processed_count}/{total_files} files.", "folder")
            except Exception as e:
                self.log_message(f"❌ Error during folder processing: {e}", "folder")
            finally:
                self.is_processing = False
                self.stop_requested = False
                self.log_message("ℹ️ Processing finished.", "folder")
        
        self.is_processing = True
        self.stop_requested = False
        self.current_thread = threading.Thread(target=run, daemon=True)
        self.current_thread.start()
    
    def clean_transcripts(self):
        def run():
            try:
                output_dir = self.output_dir_single_entry.get() if self.notebook.index(self.notebook.select()) == 0 else self.output_dir_folder_entry.get()
                transcript_dir = os.path.join(os.path.dirname(output_dir), 'transcripts')
                
                if not os.path.exists(transcript_dir):
                    messagebox.showerror("Error", f"Transcript directory not found: {transcript_dir}")
                    return
                
                transcript_files = []
                for root, _, files in os.walk(transcript_dir):
                    for f in files:
                        if f.endswith('.txt') and not f.startswith('clean_'):
                            transcript_files.append(os.path.join(root, f))
                
                if not transcript_files:
                    messagebox.showerror("Error", f"No transcript files found in {transcript_dir}")
                    return
                
                self.log_message(f"🧹 Found {len(transcript_files)} transcript files to clean", "both")
                cleaned_segments_dict = {}
                processed_count = 0
                total_files = len(transcript_files)
                
                for idx, transcript_path in enumerate(transcript_files, 1):
                    if self.stop_requested:
                        self.log_message("🛑 Processing stopped by user.", "both")
                        break
                    transcript_file = os.path.basename(transcript_path)
                    cleaned_filename = f"clean_{transcript_file}"
                    cleaned_transcript_path = os.path.join(os.path.dirname(transcript_path), cleaned_filename)
                    
                    self.log_message(f"Cleaning file {idx}/{total_files}: {transcript_file}...", "both")
                    if os.path.exists(transcript_path):
                        with open(transcript_path, 'r', encoding='utf-8') as f:
                            text = f.read()
                        cleaned_segments = clean_transcription(text)
                        cleaned_segments_dict[transcript_path] = cleaned_segments
                        if cleaned_segments:
                            save_cleaned_transcription(cleaned_segments, cleaned_transcript_path)
                            self.log_message(f"✅ Cleaning completed! Cleaned transcript saved to {cleaned_transcript_path}", "both")
                        else:
                            self.log_message(f"⚠️ No valid transcript content found for {transcript_file}", "both")
                        processed_count += 1
                    else:
                        self.log_message(f"❌ Transcript file not found: {transcript_path}", "both")
                
                if not self.stop_requested and processed_count == total_files:
                    self.log_message("🎉 All transcript files cleaned!", "both")
                elif self.stop_requested:
                    self.log_message(f"🛑 Stopped after cleaning {processed_count}/{total_files} files.", "both")
                self.cleaned_segments_dict = cleaned_segments_dict
            except Exception as e:
                messagebox.showerror("Error", f"Error during transcript cleaning: {e}")
                self.log_message(f"❌ Error during transcript cleaning: {e}", "both")
            finally:
                self.is_processing = False
                self.stop_requested = False
                self.log_message("ℹ️ Cleaning process finished.", "both")
        
        self.is_processing = True
        self.stop_requested = False
        self.current_thread = threading.Thread(target=run, daemon=True)
        self.current_thread.start()
    
    def convert_to_srt(self):
        def run():
            try:
                output_dir = self.output_dir_single_entry.get() if self.notebook.index(self.notebook.select()) == 0 else self.output_dir_folder_entry.get()
                transcript_dir = os.path.join(os.path.dirname(output_dir), 'transcripts')
                
                if not os.path.exists(transcript_dir):
                    messagebox.showerror("Error", f"Transcript directory not found: {transcript_dir}")
                    return
                
                transcript_files = []
                for root, _, files in os.walk(transcript_dir):
                    for f in files:
                        if f.endswith('.txt') and not f.startswith('clean_'):
                            transcript_files.append(os.path.join(root, f))
                
                if not transcript_files:
                    messagebox.showerror("Error", f"No transcript files found in {transcript_dir}")
                    return
                
                if not hasattr(self, 'cleaned_segments_dict'):
                    messagebox.showerror("Error", "Please clean transcripts first.")
                    return
                
                self.log_message(f"📝 Starting conversion of {len(transcript_files)} files to SRT format", "both")
                processed_count = 0
                total_files = len(transcript_files)
                
                for idx, transcript_path in enumerate(transcript_files, 1):
                    if self.stop_requested:
                        self.log_message("🛑 Processing stopped by user.", "both")
                        break
                    transcript_file = os.path.basename(transcript_path)
                    srt_filename = f"{os.path.splitext(transcript_file)[0]}.srt"
                    srt_path = os.path.join(os.path.dirname(transcript_path), srt_filename)
                    
                    self.log_message(f"Converting file {idx}/{total_files}: {transcript_file}...", "both")
                    cleaned_segments = self.cleaned_segments_dict.get(transcript_path, [])
                    if cleaned_segments:
                        convert_to_srt(cleaned_segments, srt_path)
                        self.log_message(f"✅ Conversion completed! SRT file saved to {srt_path}", "both")
                    else:
                        self.log_message(f"⚠️ No valid cleaned content found for {transcript_file}", "both")
                    processed_count += 1
                
                if not self.stop_requested and processed_count == total_files:
                    self.log_message("🎉 All transcript files converted to SRT format!", "both")
                elif self.stop_requested:
                    self.log_message(f"🛑 Stopped after converting {processed_count}/{total_files} files.", "both")
            except Exception as e:
                messagebox.showerror("Error", f"Error during SRT conversion: {e}")
                self.log_message(f"❌ Error during SRT conversion: {e}", "both")
            finally:
                self.is_processing = False
                self.stop_requested = False
                self.log_message("ℹ️ SRT conversion process finished.", "both")
        
        self.is_processing = True
        self.stop_requested = False
        self.current_thread = threading.Thread(target=run, daemon=True)
        self.current_thread.start()
    
    def clean_srt_files(self):
        def run():
            try:
                output_dir = self.output_dir_single_entry.get() if self.notebook.index(self.notebook.select()) == 0 else self.output_dir_folder_entry.get()
                transcript_dir = os.path.join(os.path.dirname(output_dir), 'transcripts')
                
                if not os.path.exists(transcript_dir):
                    messagebox.showerror("Error", f"Transcript directory not found: {transcript_dir}")
                    return
                
                srt_files = []
                for root, _, files in os.walk(transcript_dir):
                    for f in files:
                        if f.endswith('.srt') and not f.startswith('cleaned_'):
                            srt_files.append(os.path.join(root, f))
                
                if not srt_files:
                    messagebox.showerror("Error", f"No SRT files found in {transcript_dir}")
                    return
                
                blacklisted_phrases = self.load_hallucinations()
                self.log_message(f"📝 Found {len(srt_files)} SRT files to clean", "both")
                processed_count = 0
                total_files = len(srt_files)
                
                for idx, srt_path in enumerate(srt_files, 1):
                    if self.stop_requested:
                        self.log_message("🛑 Processing stopped by user.", "both")
                        break
                    srt_file = os.path.basename(srt_path)
                    self.log_message(f"Cleaning SRT file {idx}/{total_files}: {srt_file}...", "both")
                    output_path = os.path.join(os.path.dirname(srt_path), f"cleaned_{srt_file}")
                    
                    if os.path.exists(srt_path):
                        with open(srt_path, 'r', encoding='utf-8') as f:
                            srt_content = f.read()
                        
                        entries = srt_content.split("\n\n")
                        cleaned_entries = []
                        removed_count = 0
                        
                        for entry in entries:
                            lines = entry.split("\n")
                            if len(lines) >= 3:
                                subtitle_text = " ".join(lines[2:])
                                if any(phrase in subtitle_text for phrase in blacklisted_phrases):
                                    removed_count += 1
                                    continue
                                cleaned_entries.append(entry)
                        
                        with open(output_path, 'w', encoding='utf-8') as f:
                            f.write("\n\n".join(cleaned_entries))
                        
                        self.log_message(f"🧹 Cleaned {srt_file}! Removed {removed_count} entries", "both")
                        processed_count += 1
                
                if not self.stop_requested and processed_count == total_files:
                    self.log_message("🎉 All SRT files cleaned!", "both")
                elif self.stop_requested:
                    self.log_message(f"🛑 Stopped after cleaning {processed_count}/{total_files} SRT files.", "both")
            except Exception as e:
                messagebox.showerror("Error", f"Error during SRT cleaning: {e}")
                self.log_message(f"❌ Error during SRT cleaning: {e}", "both")
            finally:
                self.is_processing = False
                self.stop_requested = False
                self.log_message("ℹ️ SRT cleaning process finished.", "both")
        
        self.is_processing = True
        self.stop_requested = False
        self.current_thread = threading.Thread(target=run, daemon=True)
        self.current_thread.start()
    
    def one_click_srt(self):
        def run():
            try:
                # Determine if we're processing a single file or a folder based on the active tab
                active_tab = self.notebook.index(self.notebook.select())
                if active_tab == 0:  # Single File Tab
                    input_source = self.input_file_entry.get()
                    output_dir = self.output_dir_single_entry.get()
                    clip_duration_sec = int(self.clip_duration_sec.get())
                    whisper_exec = self.whisper_exec_single_entry.get()
                    whisper_model = self.whisper_model_single_entry.get()
                    language = self.language_single.get()
                    transcript_filename = self.transcript_filename_entry.get()
                    workers = int(self.workers_single.get())
                    use_threads = self.use_threads_single.get() == "Multithreading"
                    
                    if not os.path.exists(input_source):
                        self.log_message(f"❌ Input file not found: {input_source}", "single")
                        return
                    
                    self.log_message("🚀 Starting One-Click SRT Processing for Single File...", "single")
                    
                    # Step 1: Process the audio file (transcription)
                    self.log_message("🚀 Starting audio processing...", "single")
                    clear_output_folder(output_dir)
                    
                    if self.stop_requested:
                        self.log_message("🛑 Processing stopped by user.", "single")
                        return
                    
                    wav_file = convert_to_wav(input_source, output_dir)
                    self.log_message("🔄 Audio converted to WAV format", "single")
                    
                    if self.stop_requested:
                        self.log_message("🛑 Processing stopped by user.", "single")
                        return
                    
                    clip_files = split_audio(wav_file, clip_duration_sec, output_dir)
                    self.log_message(f"✅ Audio split into {len(clip_files)} clips", "single")
                    
                    if self.stop_requested:
                        self.log_message("🛑 Processing stopped by user.", "single")
                        return
                    
                    transcribe_audio(clip_files, output_dir, whisper_exec, whisper_model, language, transcript_filename=transcript_filename, workers=workers, use_threads=use_threads)
                    transcript_path = os.path.join(os.path.dirname(output_dir), 'transcripts', transcript_filename)
                    self.log_message(f"🎉 Transcription completed! Saved to {transcript_path}", "single")
                    
                    if self.stop_requested:
                        self.log_message("🛑 Processing stopped by user.", "single")
                        return
                
                else:  # Folder Tab
                    input_folder = self.input_folder_entry.get()
                    output_dir = self.output_dir_folder_entry.get()
                    clip_duration_sec = int(self.clip_duration_min.get()) * 60  # Convert minutes to seconds
                    whisper_exec = self.whisper_exec_folder_entry.get()
                    whisper_model = self.whisper_model_folder_entry.get()
                    language = self.language_folder.get()
                    workers = int(self.workers_folder.get())
                    use_threads = self.use_threads_folder.get() == "Multithreading"
                    rest_time = int(self.rest_time.get())
                    
                    if not os.path.exists(input_folder):
                        self.log_message(f"❌ Input folder not found: {input_folder}", "folder")
                        return
                    
                    supported_extensions = ('.mp3', '.mp4', '.m4a', '.wav', '.flac', '.ogg', '.webm', '.mkv')
                    input_files = [f for f in os.listdir(input_folder) if f.lower().endswith(supported_extensions)]
                    
                    if not input_files:
                        self.log_message(f"❌ No audio/video files found in {input_folder}", "folder")
                        return
                    
                    total_files = len(input_files)
                    self.log_message(f"📁 Found {total_files} files to process", "folder")
                    
                    folder_name = os.path.basename(input_folder)
                    transcript_dir = os.path.join(os.path.dirname(output_dir), 'transcripts', folder_name)
                    Path(transcript_dir).mkdir(parents=True, exist_ok=True)
                    
                    processed_count = 0
                    
                    for idx, input_file in enumerate(input_files, 1):
                        if self.stop_requested:
                            self.log_message("🛑 Processing stopped by user.", "folder")
                            break
                        input_file_path = os.path.join(input_folder, input_file)
                        base_name = os.path.splitext(input_file)[0]
                        transcript_filename = f"{base_name}.txt"
                        self.log_message(f"🚀 Processing file {idx}/{total_files}: {input_file}...", "folder")
                        
                        clear_output_folder(output_dir)
                        
                        if self.stop_requested:
                            self.log_message("🛑 Processing stopped by user.", "folder")
                            break
                        
                        wav_file = convert_to_wav(input_file_path, output_dir)
                        
                        if self.stop_requested:
                            self.log_message("🛑 Processing stopped by user.", "folder")
                            break
                        
                        clip_files = split_audio(wav_file, clip_duration_sec, output_dir)
                        
                        if self.stop_requested:
                            self.log_message("🛑 Processing stopped by user.", "folder")
                            break
                        
                        transcribe_audio(clip_files, output_dir, whisper_exec, whisper_model, language, transcript_filename, workers=workers, use_threads=use_threads)
                        transcript_path = os.path.join(transcript_dir, transcript_filename)
                        os.rename(os.path.join(os.path.dirname(output_dir), 'transcripts', transcript_filename), transcript_path)
                        self.log_message(f"✅ File {idx}/{total_files} processed! Transcript saved to {transcript_path}", "folder")
                        
                        processed_count += 1
                        
                        if idx < total_files and rest_time > 0:
                            self.log_message(f"⏳ Resting for {rest_time} seconds to avoid overheating...", "folder")
                            time.sleep(rest_time)
                        else:
                            self.log_message("ℹ️ This is the last file, no rest needed.", "folder")
                    
                    if not self.stop_requested and processed_count == total_files:
                        self.log_message("🎉 All files processed!", "folder")
                    elif self.stop_requested:
                        self.log_message(f"🛑 Stopped after processing {processed_count}/{total_files} files.", "folder")
                        return
                
                # Common steps for both single file and folder after transcription
                transcript_dir = os.path.join(os.path.dirname(output_dir), 'transcripts')
                if not os.path.exists(transcript_dir):
                    messagebox.showerror("Error", f"Transcript directory not found: {transcript_dir}")
                    return
                
                transcript_files = []
                for root, _, files in os.walk(transcript_dir):
                    for f in files:
                        if f.endswith('.txt') and not f.startswith('clean_'):
                            transcript_files.append(os.path.join(root, f))
                
                if not transcript_files:
                    messagebox.showerror("Error", f"No transcript files found in {transcript_dir}")
                    return
                
                # Step 2: Clean Transcripts
                self.log_message("🧹 Cleaning transcript files...", "both")
                cleaned_segments_dict = {}
                processed_clean_count = 0
                total_transcripts = len(transcript_files)
                for idx, transcript_path in enumerate(transcript_files, 1):
                    if self.stop_requested:
                        self.log_message("🛑 Processing stopped by user.", "both")
                        break
                    transcript_file = os.path.basename(transcript_path)
                    cleaned_filename = f"clean_{transcript_file}"
                    cleaned_transcript_path = os.path.join(os.path.dirname(transcript_path), cleaned_filename)
                    
                    self.log_message(f"Cleaning file {idx}/{total_transcripts}: {transcript_file}...", "both")
                    if os.path.exists(transcript_path):
                        with open(transcript_path, 'r', encoding='utf-8') as f:
                            text = f.read()
                        cleaned_segments = clean_transcription(text)
                        cleaned_segments_dict[transcript_path] = cleaned_segments
                        if cleaned_segments:
                            save_cleaned_transcription(cleaned_segments, cleaned_transcript_path)
                            self.log_message(f"✅ Cleaning completed! Cleaned transcript saved to {cleaned_transcript_path}", "both")
                        else:
                            self.log_message(f"⚠️ No valid transcript content found for {transcript_file}", "both")
                        processed_clean_count += 1
                    else:
                        self.log_message(f"❌ Transcript file not found: {transcript_path}", "both")
                
                self.cleaned_segments_dict = cleaned_segments_dict
                if not self.stop_requested and processed_clean_count == total_transcripts:
                    self.log_message("🎉 All transcript files cleaned!", "both")
                elif self.stop_requested:
                    self.log_message(f"🛑 Stopped after cleaning {processed_clean_count}/{total_transcripts} transcript files.", "both")
                    return
                
                # Step 3: Convert to SRT
                self.log_message(f"📝 Starting conversion of {len(transcript_files)} files to SRT format", "both")
                processed_srt_count = 0
                for idx, transcript_path in enumerate(transcript_files, 1):
                    if self.stop_requested:
                        self.log_message("🛑 Processing stopped by user.", "both")
                        break
                    transcript_file = os.path.basename(transcript_path)
                    srt_filename = f"{os.path.splitext(transcript_file)[0]}.srt"
                    srt_path = os.path.join(os.path.dirname(transcript_path), srt_filename)
                    
                    self.log_message(f"Converting file {idx}/{total_transcripts}: {transcript_file}...", "both")
                    cleaned_segments = self.cleaned_segments_dict.get(transcript_path, [])
                    if cleaned_segments:
                        convert_to_srt(cleaned_segments, srt_path)
                        self.log_message(f"✅ Conversion completed! SRT file saved to {srt_path}", "both")
                    else:
                        self.log_message(f"⚠️ No valid cleaned content found for {transcript_file}", "both")
                    processed_srt_count += 1
                
                if not self.stop_requested and processed_srt_count == total_transcripts:
                    self.log_message("🎉 All transcript files converted to SRT format!", "both")
                elif self.stop_requested:
                    self.log_message(f"🛑 Stopped after converting {processed_srt_count}/{total_transcripts} files to SRT.", "both")
                    return
                
                # Step 4: Clean SRT Files
                srt_files = []
                for root, _, files in os.walk(transcript_dir):
                    for f in files:
                        if f.endswith('.srt') and not f.startswith('cleaned_'):
                            srt_files.append(os.path.join(root, f))
                
                if not srt_files:
                    self.log_message("❌ No SRT files found to clean", "both")
                    return
                
                blacklisted_phrases = self.load_hallucinations()
                self.log_message(f"📝 Found {len(srt_files)} SRT files to clean", "both")
                processed_clean_srt_count = 0
                total_srt_files = len(srt_files)
                
                for idx, srt_path in enumerate(srt_files, 1):
                    if self.stop_requested:
                        self.log_message("🛑 Processing stopped by user.", "both")
                        break
                    srt_file = os.path.basename(srt_path)
                    self.log_message(f"Cleaning SRT file {idx}/{total_srt_files}: {srt_file}...", "both")
                    output_path = os.path.join(os.path.dirname(srt_path), f"cleaned_{srt_file}")
                    
                    if os.path.exists(srt_path):
                        with open(srt_path, 'r', encoding='utf-8') as f:
                            srt_content = f.read()
                        
                        entries = srt_content.split("\n\n")
                        cleaned_entries = []
                        removed_count = 0
                        
                        for entry in entries:
                            lines = entry.split("\n")
                            if len(lines) >= 3:
                                subtitle_text = " ".join(lines[2:])
                                if any(phrase in subtitle_text for phrase in blacklisted_phrases):
                                    removed_count += 1
                                    continue
                                cleaned_entries.append(entry)
                        
                        with open(output_path, 'w', encoding='utf-8') as f:
                            f.write("\n\n".join(cleaned_entries))
                        
                        self.log_message(f"🧹 Cleaned {srt_file}! Removed {removed_count} entries", "both")
                        processed_clean_srt_count += 1
                
                if not self.stop_requested and processed_clean_srt_count == total_srt_files:
                    self.log_message("🎉 All SRT files cleaned! One-Click SRT Processing Complete!", "both")
                elif self.stop_requested:
                    self.log_message(f"🛑 Stopped after cleaning {processed_clean_srt_count}/{total_srt_files} SRT files.", "both")
            except Exception as e:
                messagebox.showerror("Error", f"Error during One-Click SRT processing: {e}")
                self.log_message(f"❌ Error during One-Click SRT processing: {e}", "both")
            finally:
                self.is_processing = False
                self.stop_requested = False
                self.log_message("ℹ️ One-Click SRT process finished.", "both")
        
        self.is_processing = True
        self.stop_requested = False
        self.current_thread = threading.Thread(target=run, daemon=True)
        self.current_thread.start()
    
    def load_hallucinations(self, hallucinations_file="../doc/whisper_hallucinations.txt"):
        """Load hallucinated phrases from a file for filtering SRT content."""
        blacklisted_phrases = []
        if os.path.exists(hallucinations_file):
            with open(hallucinations_file, 'r', encoding='utf-8') as f:
                lines = f.readlines()
                for line in lines:
                    line = line.strip()
                    if line and line.startswith('- '):
                        phrase = line[2:].strip()
                        blacklisted_phrases.append(phrase)
            return blacklisted_phrases
        else:
            return [
                "(字幕君:我看不懂,我看不懂)",
                "(字幕製作:貝爾)",
                "(字幕君:你真是個傻瓜)",
                "(字幕君:我聽不懂,我聽不懂)",
                "(字幕君:這是什麼意思)",
                "(字幕君:聽不清楚)",
                "(字幕君:我不知道你在說什麼)",
                "(字幕製作:未知)",
                "(字幕君:這是幻聽嗎)",
                "(字幕君:我無法理解)"
            ]

if __name__ == "__main__":
    # Ensure the script works regardless of the current working directory by resolving paths relative to the script's location
    script_dir = os.path.abspath(os.path.dirname(__file__))
    os.chdir(script_dir)  # Change working directory to the script's directory
    
    root = tk.Tk()
    app = TranscriptionGUI(root)
    root.mainloop()
