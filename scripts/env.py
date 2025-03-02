# Global configuration for scripts

# voice2transcripts.py
INPUT_FILE = "./SELF/data/audio/20250218LLMMT.m4a"
OUTPUT_AUDIO_FORMAT = "wav"
CLIP_DURATION_MIN = 10
CLIP_DURATION_SEC = CLIP_DURATION_MIN * 60
OUTPUT_DIR = "./SELF/data/transcripts"
WHISPER_EXEC = "./whisper.cpp/build/bin/whisper-cli"
WHISPER_MODEL = "whisper.cpp/models/ggml-medium.bin" # medium base
LANGUAGE = "zh"  # zh en

# time_stamp_cleaner.py
INPUT_TRANSCRIPTION_FILE = "./SELF/data/transcripts/transcription.txt"
OUTPUT_CLEAN_FILE = "./SELF/data/transcripts/clean_transcription.txt"

# transcripts_summary.py
LMSTUDIO_API_URL = "http://127.0.0.1:1234/v1/chat/completions"
MODEL_NAME = "meta-llama-3.1-8b-instruct"
# MODEL_NAME = "mistral-nemo-instruct-2407"
MAX_TOKENS = 200
TEMPERATURE = 0.7
INPUT_CLEAN_TRANSCRIPT = "./SELF/data/transcripts/clean_transcription.txt"
OUTPUT_SUMMARY_FILE = "./SELF/data/summarys/summary.txt"
