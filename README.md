# whisper

brew install cmake

git clone https://github.com/ggerganov/whisper.cpp.git
cd whisper.cpp


cmake -B build
cmake --build build --config Release

sh ./models/download-ggml-model.sh medium


conda activate p312 

uv sync

uv run aider --model xai/grok-3

tree -I 'whisper.cpp|output_clips' > doc/doc_tree.md

uv run pytest test/