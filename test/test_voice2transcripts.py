import os
import sys
import pytest
import subprocess
from pathlib import Path

# Add the parent directory to the path so we can import from scripts
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from scripts.voice2transcripts import clear_output_folder, convert_to_wav, split_audio, transcribe_audio

# Test fixtures
@pytest.fixture
def test_audio_file(tmp_path):
    """Create a temporary audio file for testing."""
    audio_file = tmp_path / "test_audio.mp3"
    # Create a dummy audio file (minimal valid mp3 header)
    with open(audio_file, 'wb') as f:
        f.write(b'\xFF\xFB\x90\x64\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
    return str(audio_file)

@pytest.fixture
def test_output_dir(tmp_path):
    """Create a temporary output directory for testing."""
    output_dir = tmp_path / "output"
    output_dir.mkdir(parents=True, exist_ok=True)
    return str(output_dir)

# Tests for voice2transcripts.py functions
def test_clear_output_folder(test_output_dir):
    """Test clearing the output folder."""
    # Create a dummy file in the output directory
    dummy_file = os.path.join(test_output_dir, "dummy.txt")
    with open(dummy_file, 'w') as f:
        f.write("test")
    
    # Clear the folder
    clear_output_folder(test_output_dir)
    
    # Check if the folder is empty
    assert len(os.listdir(test_output_dir)) == 0

def test_convert_to_wav(test_audio_file, test_output_dir, mocker):
    """Test audio conversion to WAV format."""
    # Mock subprocess.run to avoid actual ffmpeg execution
    mocker.patch('subprocess.run', return_value=None)
    
    # Call the function
    output_wav = convert_to_wav(test_audio_file, test_output_dir)
    
    # Check if the output path is correct
    expected_output = os.path.join(test_output_dir, "converted.wav")
    assert output_wav == expected_output

def test_split_audio(test_audio_file, test_output_dir, mocker):
    """Test splitting audio into clips."""
    # Mock subprocess.check_output to return a fixed duration
    mocker.patch('subprocess.check_output', return_value=b"10.0")
    # Mock subprocess.run to avoid actual ffmpeg execution
    mocker.patch('subprocess.run', return_value=None)
    
    # Call the function with a short duration for testing
    clip_files = split_audio(test_audio_file, 5, test_output_dir)
    
    # Check if clips are created (mocked, so just check the return value structure)
    assert len(clip_files) > 0
    assert isinstance(clip_files[0], tuple)
    assert len(clip_files[0]) == 3  # (filename, start_time, end_time)

def test_transcribe_audio(test_output_dir, mocker):
    """Test transcription of audio clips."""
    # Mock subprocess.run to return dummy transcription output
    mock_result = mocker.Mock()
    mock_result.stdout = "This is a test transcription."
    mock_result.stderr = ""
    mocker.patch('subprocess.run', return_value=mock_result)
    
    # Create dummy clip files list
    clip_files = [
        (os.path.join(test_output_dir, "clip_001.wav"), 0, 5),
    ]
    
    # Call the function
    transcribe_audio(clip_files, test_output_dir, "whisper_exec", "whisper_model", "en", "test_transcription.txt")
    
    # Check if transcription file is created (mocked, so just check if file path is correct)
    transcript_file = os.path.join(test_output_dir, "../transcripts/test_transcription.txt")
    assert os.path.exists(os.path.dirname(transcript_file))
