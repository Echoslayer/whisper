import os
import sys
import time
import re
from pathlib import Path
import ipywidgets as widgets
from IPython.display import display, clear_output
from voice2transcripts import clear_output_folder, convert_to_wav, split_audio, transcribe_audio
from time_stamp_cleaner import clean_transcription, save_cleaned_transcription, convert_to_srt

def load_hallucinations(hallucinations_file="../doc/whisper_hallucinations.txt"):
    """Load hallucinated phrases from a file for filtering SRT content."""
    blacklisted_phrases = []
    if os.path.exists(hallucinations_file):
        with open(hallucinations_file, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            for line in lines:
                line = line.strip()
                if line and line.startswith('- '):
                    phrase = line[2:].strip()
                    blacklisted_phrases.append(phrase)
        print(f"✅ Loaded {len(blacklisted_phrases)} blacklisted phrases from {hallucinations_file}")
    else:
        print(f"⚠️ Hallucinations file {hallucinations_file} not found, using default blacklist")
        blacklisted_phrases = [
            "(字幕君:我看不懂,我看不懂)",
            "(字幕製作:貝爾)",
            "(字幕君:你真是個傻瓜)",
            "(字幕君:我聽不懂,我聽不懂)",
            "(字幕君:這是什麼意思)",
            "(字幕君:聽不清楚)",
            "(字幕君:我不知道你在說什麼)",
            "(字幕製作:未知)",
            "(字幕君:這是幻聽嗎)",
            "(字幕君:我無法理解)"
        ]
    return blacklisted_phrases

def clean_srt_file(srt_path, blacklisted_phrases, output_path=None):
    """Clean an SRT file by removing entries that contain blacklisted phrases."""
    if output_path is None:
        output_path = os.path.join(os.path.dirname(srt_path), f"cleaned_{os.path.basename(srt_path)}")
    
    if os.path.exists(srt_path):
        with open(srt_path, 'r', encoding='utf-8') as f:
            srt_content = f.read()
        
        # Split SRT content into entries
        entries = srt_content.split("\n\n")
        cleaned_entries = []
        removed_count = 0
        
        for entry in entries:
            lines = entry.split("\n")
            if len(lines) >= 3:
                subtitle_text = " ".join(lines[2:])
                # Check if the subtitle text contains any blacklisted phrases
                if any(phrase in subtitle_text for phrase in blacklisted_phrases):
                    removed_count += 1
                    continue  # Skip this entry if it contains a blacklisted phrase
                cleaned_entries.append(entry)
        
        # Write cleaned SRT content to a new file
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write("\n\n".join(cleaned_entries))
        
        print(f"🧹 Cleaned SRT file! Removed {removed_count} subtitle entries with blacklisted phrases")
        print(f"🎉 Cleaned SRT file saved to {output_path}")
        return output_path
    else:
        print(f"❌ SRT file not found: {srt_path}")
        return None

def process_single_audio(input_file, output_dir, clip_duration_sec, whisper_exec, whisper_model, language, transcript_filename, workers=2, use_threads=True):
    """Process a single audio file to generate a transcript."""
    try:
        # Check if input file exists
        if not os.path.exists(input_file):
            raise FileNotFoundError(f"❌ Input audio file not found: {input_file}")

        # Clear old files
        clear_output_folder(output_dir)

        # Execute the processing pipeline
        print("🚀 Starting audio processing and transcription pipeline...")
        wav_file = convert_to_wav(input_file, output_dir)
        clip_files = split_audio(wav_file, clip_duration_sec, output_dir)
        transcribe_audio(clip_files, output_dir, whisper_exec, whisper_model, language, transcript_filename=transcript_filename, workers=workers, use_threads=use_threads)
        transcript_path = os.path.join(os.path.dirname(output_dir), 'transcripts', transcript_filename)
        print(f"🎉 Transcription completed! Transcript saved to {transcript_path}")
        return transcript_path
    except Exception as e:
        print(f"❌ Error during processing: {e}")
        return None

def process_folder_audio(input_folder, output_dir, clip_duration_sec, whisper_exec, whisper_model, language, workers=2, use_threads=True, rest_time=180):
    """Process all audio/video files in a folder to generate transcripts."""
    try:
        # Check if input folder exists
        if not os.path.exists(input_folder):
            raise FileNotFoundError(f"❌ Input folder not found: {input_folder}")

        # Get list of audio/video files in the folder
        supported_extensions = ('.mp3', '.mp4', '.m4a', '.wav', '.flac', '.ogg', '.webm', '.mkv')
        input_files = [f for f in os.listdir(input_folder) if f.lower().endswith(supported_extensions)]
        
        if not input_files:
            raise FileNotFoundError(f"❌ No audio or video files found in {input_folder}")

        print(f"📁 Found {len(input_files)} files to process")
        
        # Process each file
        folder_name = os.path.basename(input_folder)
        total_files = len(input_files)
        processed_files = []
        for idx, input_file in enumerate(input_files, 1):
            input_file_path = os.path.join(input_folder, input_file)
            base_name = os.path.splitext(input_file)[0]
            transcript_filename = f"{folder_name}_{base_name}.txt"
            print(f"🚀 Processing file {idx}/{total_files}: {input_file}...")
            
            # Clear old files for this iteration
            clear_output_folder(output_dir)

            # Execute the processing pipeline
            wav_file = convert_to_wav(input_file_path, output_dir)
            clip_files = split_audio(wav_file, clip_duration_sec, output_dir)
            transcribe_audio(clip_files, output_dir, whisper_exec, whisper_model, language, transcript_filename, workers=workers, use_threads=use_threads)
            transcript_path = os.path.join(os.path.dirname(output_dir), 'transcripts', transcript_filename)
            print(f"✅ File {idx}/{total_files} processed! Transcript saved to {transcript_path}")
            processed_files.append(transcript_path)
            
            # Rest between transcriptions to avoid overheating, only if there are more files to process
            if idx < total_files and rest_time > 0:
                print(f"⏳ Resting for {rest_time} seconds to avoid overheating...")
                time.sleep(rest_time)
            else:
                print("ℹ️ This is the last file, no rest needed.")
        
        print(f"🎉 All files processed!")
        return processed_files
    except Exception as e:
        print(f"❌ Error during folder processing: {e}")
        return []

def clean_transcripts(transcript_dir, cleaned_filename_map=None):
    """Clean transcript files by removing per-sentence timestamps."""
    try:
        if not os.path.exists(transcript_dir):
            raise FileNotFoundError(f"❌ Transcript directory not found: {transcript_dir}")
        
        transcript_files = [f for f in os.listdir(transcript_dir) if f.endswith('.txt') and not f.startswith('clean_')]
        
        if not transcript_files:
            raise FileNotFoundError(f"❌ No transcript files found in {transcript_dir}")
        
        print(f"🧹 Found {len(transcript_files)} transcript files to clean")
        cleaned_segments_dict = {}
        
        for idx, transcript_file in enumerate(transcript_files, 1):
            transcript_path = os.path.join(transcript_dir, transcript_file)
            cleaned_filename = cleaned_filename_map.get(transcript_file, f"clean_{transcript_file}") if cleaned_filename_map else f"clean_{transcript_file}"
            cleaned_transcript_path = os.path.join(transcript_dir, cleaned_filename)
            
            print(f"Cleaning file {idx}/{len(transcript_files)}: {transcript_file}...")
            if os.path.exists(transcript_path):
                with open(transcript_path, 'r', encoding='utf-8') as f:
                    text = f.read()
                cleaned_segments = clean_transcription(text)
                cleaned_segments_dict[transcript_file] = cleaned_segments
                if cleaned_segments:
                    save_cleaned_transcription(cleaned_segments, cleaned_transcript_path)
                    print(f"✅ Cleaning completed! Cleaned transcript saved to {cleaned_transcript_path}")
                else:
                    print(f"⚠️ No valid transcript content found, unable to save cleaned file: {transcript_file}")
            else:
                print(f"❌ Transcript file not found: {transcript_path}")
        
        print(f"🎉 All transcript files cleaned!")
        return cleaned_segments_dict
    except Exception as e:
        print(f"❌ Error during transcript cleaning: {e}")
        return {}

def convert_to_srt_files(transcript_dir, cleaned_segments_dict, srt_filename_map=None):
    """Convert cleaned transcripts to SRT format."""
    try:
        if not os.path.exists(transcript_dir):
            raise FileNotFoundError(f"❌ Transcript directory not found: {transcript_dir}")
        
        transcript_files = [f for f in os.listdir(transcript_dir) if f.endswith('.txt') and not f.startswith('clean_')]
        
        if not transcript_files:
            raise FileNotFoundError(f"❌ No transcript files found in {transcript_dir}")
        
        print(f"📝 Starting conversion of {len(transcript_files)} files to SRT format")
        
        for idx, transcript_file in enumerate(transcript_files, 1):
            srt_filename = srt_filename_map.get(transcript_file, f"{os.path.splitext(transcript_file)[0]}.srt") if srt_filename_map else f"{os.path.splitext(transcript_file)[0]}.srt"
            srt_path = os.path.join(transcript_dir, srt_filename)
            
            print(f"Converting file {idx}/{len(transcript_files)}: {transcript_file}...")
            cleaned_segments = cleaned_segments_dict.get(transcript_file, [])
            if cleaned_segments:
                convert_to_srt(cleaned_segments, srt_path)
                print(f"✅ Conversion completed! SRT subtitle file saved to {srt_path}")
            else:
                print(f"⚠️ No valid cleaned content found, unable to convert to SRT format: {transcript_file}")
        
        print(f"🎉 All transcript files converted to SRT format!")
        return True
    except Exception as e:
        print(f"❌ Error during SRT conversion: {e}")
        return False
