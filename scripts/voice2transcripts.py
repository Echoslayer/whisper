import os
import subprocess
import platform
from pathlib import Path

# 清除輸出資料夾的所有檔案
def clear_output_folder(output_dir):
    """Clear all files and directories in the output folder."""
    if os.path.exists(output_dir):
        for item in os.listdir(output_dir):
            item_path = os.path.join(output_dir, item)
            try:
                if os.path.isfile(item_path):
                    os.remove(item_path)
                elif os.path.isdir(item_path):
                    os.rmdir(item_path)
            except Exception as e:
                print(f"⚠️ 無法刪除 {item_path}: {e}")
        print("🗑️ 輸出資料夾已清除！")

# 轉換影片或音訊為 .wav 格式 (適合 Whisper 處理)
def convert_to_wav(input_file, output_dir):
    """Convert input audio/video file to WAV format optimized for Whisper."""
    Path(output_dir).mkdir(parents=True, exist_ok=True)
    output_wav = os.path.join(output_dir, "converted.wav")
    
    try:
        cmd = [
            "ffmpeg", "-i", input_file,
            "-ac", "1",        # 單聲道
            "-ar", "16000",    # 16kHz 採樣率 (Whisper 建議)
            "-q:a", "0",       # 最高品質
            "-y",              # 覆蓋現有檔案
            output_wav
        ]
        subprocess.run(cmd, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        print(f"🔄 音訊已轉換為 WAV 格式：{output_wav}")
        return output_wav
    except subprocess.CalledProcessError as e:
        print(f"❌ 轉換音訊時發生錯誤：{e.stderr}")
        raise

# 切割音訊為多個片段
def split_audio(input_file, duration_sec, output_dir):
    """Split audio file into clips of specified duration."""
    Path(output_dir).mkdir(parents=True, exist_ok=True)
    clip_files = []
    timestamps = []

    # 獲取音訊總時長
    try:
        cmd = ["ffprobe", "-i", input_file, "-show_entries", "format=duration",
               "-of", "default=noprint_wrappers=1:nokey=1", "-v", "quiet"]
        total_duration = float(subprocess.check_output(cmd).decode().strip())
    except subprocess.CalledProcessError as e:
        print(f"❌ 無法獲取音訊時長：{e}")
        raise

    # 切割音訊
    for i, start_time in enumerate(range(0, int(total_duration), duration_sec)):
        end_time = min(start_time + duration_sec, total_duration)
        clip_filename = os.path.join(output_dir, f"clip_{i+1:03d}.wav")
        
        try:
            cmd = ["ffmpeg", "-i", input_file, "-ss", str(start_time), "-t", str(duration_sec),
                   "-acodec", "copy", "-y", clip_filename]
            subprocess.run(cmd, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            
            start_time_str = f"{int(start_time) // 3600:02d}:{(int(start_time) % 3600) // 60:02d}:{int(start_time) % 60:02d}"
            end_time_str = f"{int(end_time) // 3600:02d}:{(int(end_time) % 3600) // 60:02d}:{int(end_time) % 60:02d}"
            timestamps.append(f"Clip {i+1}: {start_time_str} - {end_time_str}\n")
            clip_files.append((clip_filename, start_time, end_time))
        except subprocess.CalledProcessError as e:
            print(f"❌ 切割音訊片段 {i+1} 時發生錯誤：{e.stderr}")
            continue

    # 儲存時間戳記
    with open(os.path.join(output_dir, "timestamps.txt"), "w", encoding="utf-8") as f:
        f.writelines(timestamps)
    
    print(f"✅ 音訊切割完成，共 {len(clip_files)} 個片段，時間戳已儲存")
    return clip_files

# 使用 Whisper.cpp 進行音訊轉錄
def transcribe_audio(clip_files, output_dir, whisper_exec, whisper_model, language, transcript_filename="transcription.txt"):
    """Transcribe audio clips using Whisper.cpp and generate transcript file with per-sentence timestamps.
    
    Args:
        clip_files: List of tuples containing (clip_filename, start_time, end_time)
        output_dir: Directory where audio clips are stored
        whisper_exec: Path to Whisper.cpp executable
        whisper_model: Path to Whisper model file
        language: Language code for transcription
        transcript_filename: Name of the output transcript file (default: "transcription.txt")
    """
    transcript_dir = os.path.join(output_dir, "../transcripts")
    Path(transcript_dir).mkdir(parents=True, exist_ok=True)
    transcript_file = os.path.join(transcript_dir, transcript_filename)

    # 檢查是否在 Apple Silicon 上執行並且有 Core ML 模型
    use_coreml = False
    if platform.system() == "Darwin" and platform.machine() == "arm64":
        coreml_model_path = whisper_model.replace(".bin", ".mlmodelc")
        if os.path.exists(coreml_model_path):
            use_coreml = True
            print("🍎 使用 Core ML 模型進行轉錄 (Apple Silicon 裝置)")

    with open(transcript_file, "w", encoding="utf-8") as f_txt:
        total_clips = len(clip_files)
        for i, (clip_filename, start_time, end_time) in enumerate(clip_files, 1):
            print(f"🎤 轉錄片段 {i}/{total_clips}: {os.path.basename(clip_filename)} ...")
            cmd = [whisper_exec, "-m", whisper_model if not use_coreml else coreml_model_path,
                   "-f", clip_filename, "-l", language, "-osrt", "-of", clip_filename]
            
            if use_coreml:
                cmd.append("--use-coreml")

            try:
                result = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="ignore")
                if result.stderr:
                    print(f"⚠️ Whisper.cpp 訊息: {result.stderr.strip()}")

                # Read the output SRT file generated by Whisper.cpp for per-sentence timestamps
                srt_file = clip_filename + ".srt"
                text = ""
                if os.path.exists(srt_file):
                    with open(srt_file, "r", encoding="utf-8") as sf:
                        srt_content = sf.read().strip()
                        # Parse SRT content to extract timestamps and text
                        entries = srt_content.split("\n\n")
                        for entry in entries:
                            lines = entry.split("\n")
                            if len(lines) >= 3:
                                timestamp_line = lines[1]
                                content = " ".join(lines[2:])
                                text += f"[{timestamp_line}]\n{content}\n"
                    os.remove(srt_file)  # Clean up the temporary SRT file

                start_time_str = f"{int(start_time) // 3600:02d}:{(int(start_time) % 3600) // 60:02d}:{int(start_time) % 60:02d}"
                end_time_str = f"{int(end_time) // 3600:02d}:{(int(end_time) % 3600) // 60:02d}:{int(end_time) % 60:02d}"
                timestamp = f"[{start_time_str} - {end_time_str}]"
                f_txt.write(f"{timestamp}\n{text}\n\n")
                
                print(f"✅ 片段 {i}/{total_clips} 轉錄完成")
            except Exception as e:
                print(f"❌ 轉錄片段 {i}/{total_clips} 時發生錯誤: {e}. 繼續處理下一個片段...")
                continue

if __name__ == "__main__":
    # 設定全域變數
    input_file = "./data/audio/full_audio.m4a"
    clip_duration_sec = 600  # 10 分鐘每個片段
    output_dir = "./data/output_clips"
    whisper_exec = "./whisper.cpp/build/bin/whisper-cli"
    whisper_model = "whisper.cpp/models/ggml-medium.bin"  # 會在 Apple Silicon 上檢查是否有 .mlmodelc
    language = "zh"  # 語言設定：zh (中文), en (英文)
    transcript_filename = "transcription.txt"  # 預設轉錄檔案名稱，可修改

    try:
        # 檢查輸入檔案是否存在
        if not os.path.exists(input_file):
            raise FileNotFoundError(f"❌ 找不到輸入音訊檔案：{input_file}")

        # 清除舊的檔案
        clear_output_folder(output_dir)

        # 執行流程
        print("🚀 開始音訊處理與轉錄流程...")
        wav_file = convert_to_wav(input_file, output_dir)
        clip_files = split_audio(wav_file, clip_duration_sec, output_dir)
        transcribe_audio(clip_files, output_dir, whisper_exec, whisper_model, language, transcript_filename)
        print(f"🎉 全部處理完成！轉錄結果已儲存至 {os.path.join(output_dir, '../transcripts/' + transcript_filename)}")
    except Exception as e:
        print(f"❌ 處理過程中發生錯誤：{e}")
