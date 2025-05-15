import os
import pytest
import sys
import re

# Add the parent directory to the path so we can import from scripts
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from scripts.time_stamp_cleaner import read_transcription, clean_transcription, save_cleaned_transcription

# Test fixtures
@pytest.fixture
def sample_transcription(tmp_path):
    """Create a sample transcription file for testing."""
    content = """[00:00 - 00:10]
[00:00:00.000 --> 00:00:02.000] Hello, this is a test.
[00:00:02.000 --> 00:00:04.000] This is another line.

[00:10 - 00:20]
[00:10:00.000 --> 00:10:02.000] Another segment here.
[00:10:02.000 --> 00:10:04.000] More text in this segment.
"""
    transcription_file = tmp_path / "transcription.txt"
    with open(transcription_file, 'w', encoding='utf-8') as f:
        f.write(content)
    return str(transcription_file)

@pytest.fixture
def empty_transcription(tmp_path):
    """Create an empty transcription file for testing."""
    transcription_file = tmp_path / "empty_transcription.txt"
    with open(transcription_file, 'w', encoding='utf-8') as f:
        f.write("")
    return str(transcription_file)

# Tests for time_stamp_cleaner.py functions
def test_read_transcription(sample_transcription):
    """Test reading a transcription file."""
    content = read_transcription(sample_transcription)
    assert isinstance(content, str)
    assert "[00:00 - 00:10]" in content
    assert "Hello, this is a test." in content

def test_read_transcription_file_not_found(tmp_path):
    """Test reading a non-existent transcription file."""
    non_existent_file = str(tmp_path / "non_existent.txt")
    with pytest.raises(FileNotFoundError, match="Transcription file not found"):
        read_transcription(non_existent_file)

def test_clean_transcription(sample_transcription):
    """Test cleaning transcription content."""
    content = read_transcription(sample_transcription)
    cleaned_segments = clean_transcription(content)
    
    assert len(cleaned_segments) == 2
    assert cleaned_segments[0].startswith("[00:00 - 00:10]")
    assert "Hello, this is a test. This is another line." in cleaned_segments[0]
    assert cleaned_segments[1].startswith("[00:10 - 00:20]")
    assert "Another segment here. More text in this segment." in cleaned_segments[1]

def test_clean_transcription_empty(empty_transcription):
    """Test cleaning an empty transcription file."""
    content = read_transcription(empty_transcription)
    cleaned_segments = clean_transcription(content)
    assert len(cleaned_segments) == 0

def test_save_cleaned_transcription(tmp_path):
    """Test saving cleaned transcription segments to a file."""
    cleaned_segments = [
        "[00:00 - 00:10]\nHello, this is a test.",
        "[00:10 - 00:20]\nAnother segment here."
    ]
    output_file = str(tmp_path / "cleaned_transcription.txt")
    save_cleaned_transcription(cleaned_segments, output_file)
    
    assert os.path.exists(output_file)
    with open(output_file, 'r', encoding='utf-8') as f:
        content = f.read()
        assert "[00:00 - 00:10]" in content
        assert "Hello, this is a test." in content
        assert "\n\n" in content  # Check for double newline between segments
