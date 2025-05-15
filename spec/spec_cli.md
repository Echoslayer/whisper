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
