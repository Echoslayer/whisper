import re
import os
from pathlib import Path

def read_transcription(file_path):
    """Read the transcription text from a file.
    
    Args:
        file_path (str): Path to the transcription file.
        
    Returns:
        str: Content of the transcription file.
        
    Raises:
        FileNotFoundError: If the specified file does not exist.
        IOError: If there's an error reading the file.
    """
    try:
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Transcription file not found: {file_path}")
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()
    except IOError as e:
        raise IOError(f"Error reading transcription file {file_path}: {e}")

def clean_transcription(text):
    """Clean the transcription text by removing per-sentence timestamps and keeping 10-minute interval headers.
    The content of each segment is converted to a single line.
    
    Args:
        text (str): Raw transcription text.
        
    Returns:
        list: List of cleaned segments, each with a header and content as a single line.
    """
    cleaned_segments = []
    
    # Split text by 10-minute interval headers (supports over 100 minutes)
    sections = re.split(r"(\[\d{2,3}:\d{2} - \d{2,3}:\d{2}\])\n", text)

    for i in range(1, len(sections), 2):  # Process each block
        header = sections[i].strip()  # 10-minute interval header
        content = sections[i + 1]  # Content of the segment
        
        # Remove per-sentence timestamps like [00:00:00.000 --> 00:00:02.000]
        cleaned_text = re.sub(r"\[\d{2,3}:\d{2}:\d{2}\.\d{3} --> \d{2,3}:\d{2}:\d{2}\.\d{3}\]", "", content)
        cleaned_text = cleaned_text.replace("\n", " ").strip()  # Convert content to a single line

        # Only keep segments with content
        if cleaned_text:
            cleaned_segments.append(f"{header}\n{cleaned_text}")

    return cleaned_segments

def save_cleaned_transcription(cleaned_segments, output_file):
    """Save the cleaned transcription segments to a file.
    
    Args:
        cleaned_segments (list): List of cleaned transcription segments.
        output_file (str): Path to save the cleaned transcription.
        
    Raises:
        IOError: If there's an error writing to the file.
    """
    try:
        # Ensure the output directory exists
        output_dir = os.path.dirname(output_file)
        Path(output_dir).mkdir(parents=True, exist_ok=True)
        
        with open(output_file, "w", encoding="utf-8") as f:
            f.write("\n\n".join(cleaned_segments))  # Separate segments with double newlines
    except IOError as e:
        raise IOError(f"Error saving cleaned transcription to {output_file}: {e}")

if __name__ == "__main__":
    try:
        # Fixed global variables for input and output paths
        input_transcription_file = "./SELF/data/output_clips/transcription.txt"
        output_clean_file = "./SELF/data/transcripts/clean_transcription.txt"

        # Execute the cleaning process
        text = read_transcription(input_transcription_file)
        cleaned_segments = clean_transcription(text)
        save_cleaned_transcription(cleaned_segments, output_clean_file)

        print(f"✅ 逐字稿清理完成，結果已儲存至 {output_clean_file}")
    except (FileNotFoundError, IOError) as e:
        print(f"❌ 處理過程中發生錯誤：{e}")
    except Exception as e:
        print(f"❌ 未知錯誤：{e}")
