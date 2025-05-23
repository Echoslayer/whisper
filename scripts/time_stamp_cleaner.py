import re
import os
from pathlib import Path

# Removed read_transcription function as we'll use direct file reading with 'with open'

def clean_transcription(text):
    """Clean the transcription text by removing per-sentence timestamps and keeping time interval headers.
    The content of each segment is converted to a single line.
    
    Args:
        text (str): Raw transcription text.
        
    Returns:
        list: List of cleaned segments, each with a header and content as a single line.
    """
    cleaned_segments = []
    
    if not text or len(text.strip()) == 0:
        return cleaned_segments
        
    # Split text by time interval headers (supports over 100 minutes)
    sections = re.split(r"(\[\d{2}:\d{2}:\d{2} - \d{2}:\d{2}:\d{2}\])\n", text)

    for i in range(1, len(sections), 2):  # Process each block
        header = sections[i].strip()  # Time interval header
        content = sections[i + 1] if i + 1 < len(sections) else ""  # Content of the segment
        
        # Remove all timestamps within square brackets from content
        cleaned_text = re.sub(r"\[.*?\]", "", content)
        cleaned_text = re.sub(r"\s+", " ", cleaned_text.replace("\n", " ")).strip()  # Convert content to a single line with normalized spaces

        # Only keep segments with content
        if cleaned_text:
            cleaned_segments.append(f"{header}\n{cleaned_text}")

    return cleaned_segments

def convert_to_srt(cleaned_segments, output_file):
    """Convert cleaned transcription segments to SRT format and save to a file.
    
    Args:
        cleaned_segments (list): List of cleaned transcription segments.
        output_file (str): Path to save the SRT file.
        
    Raises:
        IOError: If there's an error writing to the file.
    """
    srt_content = []
    for index, segment in enumerate(cleaned_segments, 1):
        lines = segment.split('\n')
        if len(lines) < 2:
            continue
            
        # Extract start and end times from header [HH:MM:SS - HH:MM:SS]
        header = lines[0]
        match = re.match(r"\[(\d{2}:\d{2}:\d{2}) - (\d{2}:\d{2}:\d{2})\]", header)
        if not match:
            continue
            
        start_time, end_time = match.groups()
        # Convert to SRT time format (HH:MM:SS,000)
        start_time_srt = f"{start_time},000"
        end_time_srt = f"{end_time},000"
        
        # Add SRT entry
        srt_content.append(f"{index}")
        srt_content.append(f"{start_time_srt} --> {end_time_srt}")
        srt_content.append(lines[1])
        srt_content.append("")  # Empty line between entries
    
    try:
        # Ensure the output directory exists
        output_dir = os.path.dirname(output_file)
        Path(output_dir).mkdir(parents=True, exist_ok=True)
        
        with open(output_file, "w", encoding="utf-8") as f:
            f.write("\n".join(srt_content))
    except IOError as e:
        raise IOError(f"Error saving SRT file to {output_file}: {e}")

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
        input_transcription_file = "./data/transcripts/transcription.txt"
        output_clean_file = "./data/transcripts/clean_transcription.txt"
        output_srt_file = "./data/transcripts/subtitles.srt"

        # Execute the cleaning process
        if not os.path.exists(input_transcription_file):
            raise FileNotFoundError(f"Transcription file not found: {input_transcription_file}")
        with open(input_transcription_file, "r", encoding="utf-8") as f:
            text = f.read()
        cleaned_segments = clean_transcription(text)
        save_cleaned_transcription(cleaned_segments, output_clean_file)
        convert_to_srt(cleaned_segments, output_srt_file)

        print(f"✅ 逐字稿清理完成，結果已儲存至 {output_clean_file}")
        print(f"✅ SRT字幕檔已生成，結果已儲存至 {output_srt_file}")
    except FileNotFoundError as e:
        print(f"❌ 找不到檔案：{e}")
    except IOError as e:
        print(f"❌ 讀取或寫入檔案時發生錯誤：{e}")
    except Exception as e:
        print(f"❌ 未知錯誤：{e}")
