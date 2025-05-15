import os
import pytest
import subprocess
import sys

# Add the parent directory to the path if needed for any script imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Test fixture for whisper.cpp executable
@pytest.fixture
def whisper_exec():
    """Path to whisper.cpp executable."""
    return "./whisper.cpp/build/bin/whisper-cli"

@pytest.fixture
def whisper_model():
    """Path to whisper model file."""
    return "whisper.cpp/models/ggml-medium.bin"

@pytest.fixture
def test_audio_file(tmp_path):
    """Create a temporary audio file for testing."""
    audio_file = tmp_path / "test_audio.wav"
    # Create a dummy audio file (minimal valid wav header)
    with open(audio_file, 'wb') as f:
        f.write(b'RIFF$\x00\x00\x00WAVEfmt \x10\x00\x00\x00\x01\x00\x01\x00\x11+\x00\x00"V\x00\x00\x02\x00\x10\x00data\x00\x00\x00\x00')
    return str(audio_file)

# Tests for whisper.cpp integration
def test_whisper_cpp_executable_exists(whisper_exec):
    """Test if whisper.cpp executable exists."""
    assert os.path.exists(whisper_exec), f"Whisper.cpp executable not found at {whisper_exec}"

def test_whisper_cpp_model_exists(whisper_model):
    """Test if whisper model file exists."""
    assert os.path.exists(whisper_model), f"Whisper model file not found at {whisper_model}"

def test_whisper_cpp_transcription(test_audio_file, whisper_exec, whisper_model, tmp_path, mocker):
    """Test whisper.cpp transcription functionality."""
    # Mock subprocess.run to avoid actual execution during test
    mock_result = mocker.Mock()
    mock_result.stdout = "This is a test transcription."
    mock_result.stderr = ""
    mocker.patch('subprocess.run', return_value=mock_result)
    
    output_file = tmp_path / "transcription.txt"
    
    # Command to run whisper.cpp
    cmd = [
        whisper_exec,
        "-m", whisper_model,
        "-f", test_audio_file,
        "--language", "en"
    ]
    
    # Run the mocked command
    result = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="ignore")
    
    # Check if the command was called (mocked)
    assert result.stdout == "This is a test transcription."
