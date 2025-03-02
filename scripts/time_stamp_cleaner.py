import re


# ✅ 讀取逐字稿
def read_transcription(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()

# ✅ 清理逐字稿，移除逐句時間戳，只保留 10 分鐘區間，且讓 content 不換行
def clean_transcription(text):
    cleaned_segments = []
    
    # ✅ 使用正則表達式，找出每 10 分鐘區段的標記，支援 100 分鐘以上
    sections = re.split(r"(\[\d{2,3}:\d{2} - \d{2,3}:\d{2}\])\n", text)

    for i in range(1, len(sections), 2):  # 逐個區塊處理
        header = sections[i].strip()  # 10 分鐘標記
        content = sections[i + 1]  # 內容
        
        # ✅ 移除逐句時間戳，例如：[00:00:00.000 --> 00:00:02.000]
        cleaned_text = re.sub(r"\[\d{2,3}:\d{2}:\d{2}\.\d{3} --> \d{2,3}:\d{2}:\d{2}\.\d{3}\]", "", content)
        cleaned_text = cleaned_text.replace("\n", " ").strip()  # ✅ 讓內容變成單行

        # ✅ 只保留有內容的段落
        if cleaned_text:
            cleaned_segments.append(f"{header}\n{cleaned_text}")

    return cleaned_segments

# ✅ 轉換並儲存結果
def save_cleaned_transcription(cleaned_segments, output_file):
    with open(output_file, "w", encoding="utf-8") as f:
        f.write("\n\n".join(cleaned_segments))  # ✅ 段落之間有 2 個換行

if __name__ == "__main__":
    # 固定的全域變數
    input_transcription_file = "./SELF/data/output_clips/transcription.txt"
    output_clean_file = "./SELF/data/transcripts/clean_transcription.txt"

    # Execute the process
    text = read_transcription(input_transcription_file)
    cleaned_segments = clean_transcription(text)
    save_cleaned_transcription(cleaned_segments, output_clean_file)

    print(f"✅ 逐字稿清理完成，結果已儲存至 {output_clean_file}")
