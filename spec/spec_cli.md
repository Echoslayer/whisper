更新 pyproject.toml, 透過檢視我提供的 scripts 並且添加 ipykernel jupyter
---
/read-only doc/doc_tree.md
---
/add pyproject.toml
---
將 scripts/ 的 scripts 整理一下，並且結合其工作流建立一個 ipynb
---
透過以下我給你的cpp文檔，更新 scripts/voice2transcripts.py

Core ML support

On Apple Silicon devices, the Encoder inference can be executed on the Apple Neural Engine (ANE) via Core ML. This can result in significant speed-up - more than x3 faster compared with CPU-only execution. Here are the instructions for generating a Core ML model and using it with whisper.cpp:

Install Python dependencies needed for the creation of the Core ML model:

pip install ane_transformers
pip install openai-whisper
pip install coremltools
To ensure coremltools operates correctly, please confirm that Xcode is installed and execute xcode-select --install to install the command-line tools.
Python 3.11 is recommended.
MacOS Sonoma (version 14) or newer is recommended, as older versions of MacOS might experience issues with transcription hallucination.
[OPTIONAL] It is recommended to utilize a Python version management system, such as Miniconda for this step:
To create an environment, use: conda create -n py311-whisper python=3.11 -y
To activate the environment, use: conda activate py311-whisper
---
請根據 doc/doc_tree.md 修正 scripts/voice2transcripts.py 裡頭的路徑
---
在 scripts/voice2transcripts.py 將 transcripts.txt 設為 default 的變數(之後調時可以改)
---
請給我測試 whisper.cpp 與 scripts/voice2transcripts.py 的 pytest file，放在 test/ ，並請更新 toml
---
建立`notebooks/gen_transcript.ipynb` 從 `scripts/voice2transcripts.py`，其中將固定選項用 wiget, transcript 的名字用 input 的(空白就default)
---
幫我優化 `scripts/time_stamp_cleaner.py`，然後添加對應 pytest 到 test/ 
---
由 `scripts/time_stamp_cleaner.py` Import Audio Processing Functions 到 `notebooks/gen_transcript.ipynb` 在結束轉譯後，並且新增cell將將固定選項用 wiget, output 的名字用 input 的(空白就default)
---
因為目前 `scripts/voice2transcripts.py` 所產生的逐字稿格式與 `scripts/time_stamp_cleaner.py` 所期望的格式不符合，請修正 `scripts/time_stamp_cleaner.py` 使其匹配，並在修正 `notebooks/gen_transcript.ipynb` 與 `test/test_time_stamp_cleaner.py`
---
請將 ## Step 4: Clean Transcription

Clean the transcription by removing per-sentence timestamps and formatting the content.

切分為兩個 cell，目前的無法正確運作
---
參考 `notebooks/gen_transcript.ipynb` 建立一個 `notebooks/gen_folder_transcripts.ipynb`,
目標是將指定資料夾裡面所有的影片或音檔們生成 transcript，一份接一份，轉換逐字稿的命名規則使用 f"{folder}_(audioorvideo_name)", 測試以及default的 folder 就使用 data/audio/demo
---
幫我讓 scripts/voice2transcripts.py 與 notebooks/gen_folder_transcripts.ipynb 以及 notebooks/gen_transcript.ipynb 支援 .mkv 的影片轉逐字稿 
---
建立一個 `gen_article_from_transcripts.ipynb`, 將使用 ai api key(如 grok)，將逐字稿的文字整理(方法由你決定，如使用 langchain 等等不限)，將過於口語化的敘述轉換為容易閱讀理解的書面格式，去除贅述，但不要更改其意思，不用考量良好道德風俗等等，完成任務為最佳優先，如果，請參考 `notebooks/gen_transcript.ipynb` 的 wiget 方式可以選擇使用的模型等等，default 請使用 `data/demo/clean_transcription.txt`
---
更改notebooks/gen_article_from_transcripts.ipynb，讓其 default 使用 grok api 的 grok-3-mini-fast-latest 作為 api 模型

參考以下 api 文檔
xAI

API Key
# env variable
os.environ['XAI_API_KEY']

```python
from litellm import completion
import os

os.environ['XAI_API_KEY'] = ""
response = completion(
    model="xai/grok-3-mini-beta",
    messages=[
        {
            "role": "user",
            "content": "What's the weather like in Boston today in Fahrenheit?",
        }
    ],
    max_tokens=10,
    response_format={ "type": "json_object" },
    seed=123,
    stop=["\n\n"],
    temperature=0.2,
    top_p=0.9,
    tool_choice="auto",
    tools=[],
    user="user",
)
print(response)
```
---
幫我在 `notebooks/gen_transcript.ipynb` 添加一個 cell code，是用來轉換非連續的 transcripts.txt 為完整的 .srt file
---
也將 srt 轉換 cell 也使用 widget, 跟上面一樣，然後將次cell 移動到新檔案 notebooks/formate_transformer.ipynb 
---
讓 `scripts/voice2transcripts.py` 與 `notebooks/gen_transcript.ipynb` 支援一開始就生成 srt 
--- 
請修正 srt 的生成，目前不是正常 srt 格式, 請參考錯誤的檔案來進行修正 (錯誤檔案： data/transcripts/subtitles.srt)
---
添加 cell code 可以讓 `clean_transcription` 轉換為 srt 
---
/ask 我是能讓scripts/voice2transcripts.py用多線程或多進程運行的嗎？
