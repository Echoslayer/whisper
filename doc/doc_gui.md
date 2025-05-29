# Audio Transcription Tool GUI Documentation

## Overview

This document provides a detailed explanation of the core concepts and architecture of the Graphical User Interface (GUI) for the Audio Transcription Tool. The tool is designed to facilitate the processing of audio files into transcriptions and further refine them into SRT subtitle files. It is built using Python's `tkinter` library for the GUI components and integrates various processing scripts for audio handling and transcription.

## Core Concepts

### 1. **Class Structure: `TranscriptionGUI`**

The main class `TranscriptionGUI` encapsulates the entire GUI application. It is initialized with a `root` window (the main window of the application) and sets up all UI elements, state variables, and processing logic.

- **Initialization**: The constructor (`__init__`) sets up default configuration values for input files, output directories, Whisper model settings, and processing parameters like clip duration and number of workers.
- **State Management**: It maintains state variables such as `is_processing` (to track if a process is running), `stop_requested` (to handle user interruption), and `current_thread` (to manage the active processing thread).

### 2. **User Interface Layout**

The GUI is divided into two main tabs using `ttk.Notebook`, allowing users to switch between processing modes:

- **Single File Tab**: For processing individual audio files. It includes fields for input file selection, output directory, clip duration (in seconds), Whisper executable and model paths, language selection, transcript filename, number of workers, and parallel processing method (multithreading or multiprocessing).
- **Folder Tab**: For batch processing multiple files in a folder. It mirrors the Single File Tab but adjusts clip duration to minutes (for longer segments) and adds a rest time parameter to prevent overheating during intensive processing.

Each tab contains:
- Input fields and browse buttons for file and folder selection.
- Sliders for numerical inputs like clip duration and workers.
- Dropdowns for categorical choices like language and parallel method.
- Process and stop buttons to start or interrupt processing.
- Status and log text areas to display current progress and historical logs.

Additionally, a bottom frame provides buttons for post-processing tasks like cleaning transcripts and converting to SRT format.

### 3. **Threading and Asynchronous Processing**

To prevent the GUI from freezing during long-running operations (like audio conversion or transcription), processing tasks are executed in separate threads:

- **Thread Creation**: Each processing method (`process_single`, `process_folder`, `clean_transcripts`, etc.) spawns a new `threading.Thread` with `daemon=True` to ensure threads terminate when the GUI closes.
- **State Flags**: `is_processing` and `stop_requested` flags manage the processing state and user interruptions. These are checked at key points in the processing pipeline to allow graceful stopping.
- **Queue for Updates**: A `queue.Queue` is used for thread-safe communication between processing threads and the GUI. Log messages are queued and periodically checked by the GUI to update the display without thread conflicts.

### 4. **Processing Pipeline**

The tool implements a pipeline for audio processing and transcription, ensuring each step completes before the next begins, especially in folder processing to avoid errors from premature execution:

- **Single File Processing** (`process_single`):
  1. Validates input file existence.
  2. Clears the output folder.
  3. Converts the input file to WAV format using `convert_to_wav`.
  4. Splits the WAV file into clips based on specified duration using `split_audio`.
  5. Transcribes clips using `transcribe_audio` with Whisper.cpp, supporting parallel processing.
  6. Saves the transcription to a file.

- **Folder Processing** (`process_folder`):
  1. Scans the input folder for supported audio/video files.
  2. Iterates through each file, repeating the single file pipeline (clear, convert, split, transcribe).
  3. Introduces a rest period between files to prevent overheating, configurable via a slider.
  4. Ensures sequential processing per file to avoid resource conflicts.

- **Post-Processing**:
  - `clean_transcripts`: Removes unnecessary timestamps and normalizes text into single-line segments per time interval.
  - `convert_to_srt`: Converts cleaned transcripts to SRT subtitle format with proper timing.
  - `clean_srt_files`: Filters out hallucinated or irrelevant subtitle entries based on a blacklist.
  - `one_click_srt`: Combines all steps (transcription, cleaning, SRT conversion, and SRT cleaning) into a single operation.

Each step checks `stop_requested` to allow user interruption, and logs progress or errors to the GUI.

### 5. **Progress Feedback and Logging**

User feedback is critical for long-running operations, implemented via:

- **Status Text Area**: Shows the current operation with an animated ellipsis ("...") to indicate progress.
- **Historical Log Text Area**: Maintains a scrollable record of all messages, errors, and completion statuses for user reference.
- **Animation Updates**: Uses `root.after` to periodically update the GUI with progress animations and queued log messages, ensuring responsiveness.

### 6. **Configuration and Customization**

The GUI provides extensive customization through input fields and saved defaults:

- **Default Values**: Hardcoded paths and settings (`DEFAULT_INPUT_FILE`, `DEFAULT_CLIP_DURATION_SEC`, etc.) initialize the GUI for quick use.
- **User Inputs**: Users can override defaults by typing paths or using browse dialogs to select files/folders, ensuring flexibility.
- **Dynamic Updates**: Sliders for clip duration and workers update associated labels in real-time for immediate feedback on settings.

### 7. **Error Handling and User Interruption**

Robust error handling prevents crashes and informs users of issues:

- **Exception Catching**: Each processing method wraps operations in try-except blocks, logging errors to the GUI and displaying message boxes for critical failures.
- **Stop Mechanism**: The `stop_processing` method sets `stop_requested=True` and `is_processing=False`, which processing threads check to halt operations. It logs the interruption to inform the user.

### 8. **Integration with Backend Scripts**

The GUI integrates with backend scripts for functionality, importing functions from:
- `voice2transcripts.py` for audio conversion, splitting, and transcription.
- `time_stamp_cleaner.py` for cleaning transcripts and SRT conversion.

This modular design separates UI from processing logic, enhancing maintainability.

## Architecture Summary

The GUI architecture follows a model of separation of concerns:
- **UI Layer**: Handles user input, displays status/logs, and provides controls via `tkinter` widgets.
- **Processing Layer**: Executes audio and transcription tasks in separate threads, communicating via a queue.
- **State Management**: Tracks processing status and user interruptions with boolean flags.
- **Feedback Loop**: Continuously updates the GUI with progress and results using `after` callbacks.

This design ensures a responsive interface, clear user feedback, and robust handling of intensive tasks, making the Audio Transcription Tool accessible for both single file and batch processing scenarios.

## Key Features

- **Dual Mode**: Supports both single file and folder batch processing with tailored settings.
- **Parallel Processing**: Configurable workers and threading/multiprocessing options for transcription speed.
- **User Control**: Stop button and real-time logs empower users to manage long operations.
- **Post-Processing**: Cleaning and SRT conversion streamline subtitle creation.
- **Platform Awareness**: Detects Apple Silicon for Core ML model optimization (in backend scripts).

This GUI serves as the central interface for an end-to-end audio-to-subtitle workflow, balancing usability with powerful processing capabilities.
