import re
import requests
import json
import time
import os

import os

from env import LMSTUDIO_API_URL, MODEL_NAME, MAX_TOKENS, TEMPERATURE

# ✅ 解析逐字稿，支援 100 分鐘以上的時間格式
def parse_transcription(file_path):
    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()
    
    # ✅ 修改時間格式匹配 100 分鐘以上的標記
    pattern = r"\[(\d{2,3}:\d{2}) - (\d{2,3}:\d{2})\]\n(.+?)\n\n"
    matches = re.findall(pattern, content, re.DOTALL)
    
    segments = []
    for start, end, text in matches:
        segments.append({"start": start, "end": end, "text": text.strip()})
    
    return segments

# ✅ 透過 LM Studio API 進行摘要
def summarize_text(text):
    payload = {
        "model": MODEL_NAME,
        "messages": [
            {"role": "user", "content": f"請將以下內容總結成 200 字以內，不需要回應問題：\n{text}"}
        ],
        "max_tokens": MAX_TOKENS,
        "temperature": TEMPERATURE
    }

    try:
        headers = {"Content-Type": "application/json"}
        response = requests.post(LMSTUDIO_API_URL, headers=headers, data=json.dumps(payload))
        response.raise_for_status()  # 若 API 回傳錯誤，拋出異常
        
        # ✅ 解析回應格式，確保支援不同的 API 格式
        response_json = response.json()
        print(f"📩 API 回應: {response_json}")  # ✅ 用於 Debug，查看 API 回應內容

        # ✅ 修正 JSON 解析，確保 `choices` 格式正確
        choices = response_json.get("choices", [])
        if choices and "message" in choices[0]:
            summary = choices[0]["message"].get("content", "").strip()
        else:
            summary = choices[0].get("text", "").strip()  # 兼容不同格式
        
        return summary if summary else "摘要失敗"
    
    except requests.exceptions.RequestException as e:
        print(f"❌ API 請求失敗: {e}")
        return "摘要失敗"

if __name__ == "__main__":
    # 固定的全域變數
    input_clean_transcript = "./SELF/data/transcripts/clean_transcription.txt"
    output_summary_file = "./SELF/data/summarys/summary.txt"

    # Execute the process
    segments = parse_transcription(input_clean_transcript)
    summary_results = []

    for segment in segments:
        print(f"🔍 正在摘要: {segment['start']} - {segment['end']} ...")
        summary = summarize_text(segment["text"])
        summary_results.append(f"[{segment['start']} - {segment['end']}]\n{summary}\n")
        time.sleep(1)  # 避免 API 過載

    # Save summary results
    with open(output_summary_file, "w", encoding="utf-8", errors="ignore") as f:
        f.writelines(summary_results)

    print(f"✅ 摘要完成，結果已儲存於 {output_summary_file}")
