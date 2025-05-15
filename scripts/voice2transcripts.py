import os
import subprocess
import platform

from env import OUTPUT_AUDIO_FORMAT

# **清除輸出資料夾的所有檔案**
def clear_output_folder():
    if os.path.exists(output_dir):
        for file in os.listdir(output_dir):
            file_path = os.path.join(output_dir, file)
            try:
                if os.path.isfile(file_path):
                    os.remove(file_path)
                elif os.path.isdir(file_path):
                    os.rmdir(file_path)  # 如果有子目錄，確保刪除
            except Exception as e:
                print(f"⚠️ 無法刪除 {file_path}: {e}")
        print("🗑️ 輸出資料夾已清除！")

# 1. 轉換影片或音訊為 .wav
def convert_to_wav(input_file):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)  # 確保輸出目錄存在

    output_wav = os.path.join(output_dir, "converted.wav")
    cmd = [
        "ffmpeg",
        "-i", input_file,
        "-ac", "1",  # 轉換為單聲道
        "-ar", "16000",  # Whisper 建議 16kHz
        "-q:a", "0",
        output_wav
    ]
    subprocess.run(cmd, check=True)
    return output_wav

# 2. 切割音訊
def split_audio(input_file, duration_sec):
    clip_files = []
    timestamps = []

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    cmd = [
        "ffprobe",
        "-i", input_file,
        "-show_entries", "format=duration",
        "-of", "default=noprint_wrappers=1:nokey=1",
        "-v", "quiet"
    ]
    total_duration = float(subprocess.check_output(cmd).decode().strip())

    for i, start_time in enumerate(range(0, int(total_duration), duration_sec)):
        end_time = min(start_time + duration_sec, total_duration)

        clip_filename = os.path.join(output_dir, f"clip_{i+1:03d}.wav")

        cmd = [
            "ffmpeg",
            "-i", input_file,
            "-ss", str(start_time),
            "-t", str(duration_sec),
            "-acodec", "copy",
            clip_filename
        ]
        subprocess.run(cmd, check=True)

        start_time_str = f"{int(start_time) // 3600:02d}:{(int(start_time) % 3600) // 60:02d}:{int(start_time) % 60:02d}"
        end_time_str = f"{int(end_time) // 3600:02d}:{(int(end_time) % 3600) // 60:02d}:{int(end_time) % 60:02d}"
        
        timestamps.append(f"Clip {i+1}: {start_time_str} - {end_time_str}\n")
        clip_files.append((clip_filename, start_time, end_time))
    
    with open(os.path.join(output_dir, "timestamps.txt"), "w") as f:
        f.writelines(timestamps)
    
    print("✅ 音訊切割完成，時間戳已儲存至 timestamps.txt")
    return clip_files

# 3. 使用 Whisper.cpp 進行轉錄
def transcribe_audio(clip_files):
    transcript_file = os.path.join(output_dir, "transcription.txt")

    # Check if running on Apple Silicon and Core ML model is available
    use_coreml = False
    if platform.system() == "Darwin" and platform.machine() == "arm64":
        coreml_model_path = whisper_model.replace(".bin", ".mlmodelc")
        if os.path.exists(coreml_model_path):
            use_coreml = True
            print("🍎 使用 Core ML 模型進行轉錄 (Apple Silicon 裝置)")

    with open(transcript_file, "w", encoding="utf-8") as f:
        for clip_filename, start_time, end_time in clip_files:
            print(f"🎤 轉錄 {clip_filename} ...")

            cmd = [
                whisper_exec,
                "-m", whisper_model if not use_coreml else coreml_model_path,
                "-f", clip_filename,
                "--language", language
            ]
            
            if use_coreml:
                cmd.append("--use-coreml")

            try:
                result = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="ignore")

                text = result.stdout.strip()
                if result.stderr:
                    print(f"⚠️ Whisper.cpp 錯誤: {result.stderr}")

                start_time_str = f"{int(start_time) // 3600:02d}:{(int(start_time) % 3600) // 60:02d}:{int(start_time) % 60:02d}"
                end_time_str = f"{int(end_time) // 3600:02d}:{(int(end_time) % 3600) // 60:02d}:{int(end_time) % 60:02d}"
                timestamp = f"[{start_time_str} - {end_time_str}]"
                
                f.write(f"{timestamp}\n{text}\n\n")

            except UnicodeDecodeError as e:
                print(f"❌ UnicodeDecodeError: {e}. 嘗試繼續轉錄下一個片段...")
                continue

if __name__ == "__main__":
    # 固定的全域變數
    input_file = "./data/audio/full_audio.m4a"
    clip_duration_sec = 600  # 10 minutes
    output_dir = "./data/output_clips"
    whisper_exec = "./whisper.cpp/build/bin/whisper-cli"
    whisper_model = "whisper.cpp/models/ggml-medium.bin"  # medium base, will check for .mlmodelc on Apple Silicon
    language = "en"

    # **清除舊的檔案**
    clear_output_folder()

    # **執行流程**
    wav_file = convert_to_wav(input_file)
    clip_files = split_audio(wav_file, clip_duration_sec)
    transcribe_audio(clip_files)

    print("🎉 全部處理完成！請查看 output_clips 目錄。")
