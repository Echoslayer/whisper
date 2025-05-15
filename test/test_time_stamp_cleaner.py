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
    content = """[00:00:00 - 00:01:00]
[00:00:00.000 --> 00:00:06.700]  Aesha Kriya是一個非常簡單的工具,但也很強烈的工具
[00:00:06.700 --> 00:00:12.520]  這三個材料,你的呼吸,你的思考,你的意識
[00:00:12.520 --> 00:00:18.400]  如果你使用它們,你能夠使用心理和身體
[00:00:18.400 --> 00:00:24.200]  會變得如此有力量,你會變得像其他人一樣的超人

[00:01:00 - 00:02:00]
[00:01:00.000 --> 00:01:02.000]  但我告訴你,這是人的
[00:01:02.000 --> 00:01:04.000]  這是我們的本質
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
    assert "[00:00:00 - 00:01:00]" in content
    assert "Aesha Kriya" in content

def test_read_transcription_file_not_found(tmp_path):
    """Test reading a non-existent transcription file."""
    non_existent_file = str(tmp_path / "non_existent.txt")
    with pytest.raises(Exception, match=r"Transcription file not found: .*non_existent\.txt"):
        read_transcription(non_existent_file)

def test_clean_transcription(sample_transcription):
    """Test cleaning transcription content."""
    content = read_transcription(sample_transcription)
    cleaned_segments = clean_transcription(content)
    
    assert len(cleaned_segments) == 2
    assert cleaned_segments[0].startswith("[00:00:00 - 00:01:00]")
    assert "Aesha Kriya是一個非常簡單的工具,但也很強烈的工具 這三個材料,你的呼吸,你的思考,你的意識 如果你使用它們,你能夠使用心理和身體 會變得如此有力量,你會變得像其他人一樣的超人" in cleaned_segments[0]
    assert cleaned_segments[1].startswith("[00:01:00 - 00:02:00]")
    assert "但我告訴你,這是人的 這是我們的本質" in cleaned_segments[1]

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
