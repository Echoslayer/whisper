import os
import subprocess
import yt_dlp as youtube_dl

# 設定下載資料夾和音訊檔名
DOWNLOAD_DIR = "./data"
BASE_FILENAME = "full_audio"
EXTENSION = ".m4a"
OUTPUT_FILE = os.path.join(DOWNLOAD_DIR, f"{BASE_FILENAME}{EXTENSION}")
TEMP_WAV_FILE = os.path.join(DOWNLOAD_DIR, "temp_audio.wav")
TRIMMED_FILE = os.path.join(DOWNLOAD_DIR, "trimmed_audio.mp3")

# 確保下載資料夾存在
os.makedirs(DOWNLOAD_DIR, exist_ok=True)

# 下載音訊
def download_audio(url):
    print("🎵 正在下載音訊...")
    ydl_opts = {
        'format': 'bestaudio[ext=m4a]',
        'outtmpl': os.path.join(DOWNLOAD_DIR, f'{BASE_FILENAME}.%(ext)s'),  # 讓下載的檔案有正確的副檔名
        'quiet': False,
        'verbose': True
    }
    
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

# 裁切音訊片段
def trim_audio():
    print("✂️ 正在裁切音訊片段...")
    if not os.path.isfile(OUTPUT_FILE):
        raise FileNotFoundError("❌ 找不到下載完成的音訊檔案")

    # 先將 m4a 轉換為 wav 格式
    subprocess.run([
        'ffmpeg', '-y',
        '-i', OUTPUT_FILE,
        TEMP_WAV_FILE
    ], check=True)

    # 設定裁切的時間範圍
    start_time = '00:04:07'  # 開始時間
    duration = '00:15:05'  # 持續時間

    # 使用 ffmpeg 進行裁切並轉換為 mp3 格式
    subprocess.run([
        'ffmpeg', '-y',
        '-i', TEMP_WAV_FILE,
        '-ss', start_time,
        '-t', duration,
        '-acodec', 'libmp3lame',  # 設定編碼器為 mp3
        '-ab', '192k',  # 設定比特率
        TRIMMED_FILE
    ], check=True)

    print(f"✅ 裁切完成，檔案已儲存為：{TRIMMED_FILE}")

    # 刪除臨時的 wav 檔案
    os.remove(TEMP_WAV_FILE)

# 主程式
if __name__ == "__main__":
    url = "https://www.youtube.com/watch?v=vzGxmtYXJkY"  # 你要下載的 YouTube 影片 URL
    download_audio(url)
    trim_audio()
