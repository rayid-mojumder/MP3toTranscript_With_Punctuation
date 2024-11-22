# MP3 to Text Converter with Punctuation Restoration

This repository provides a Python script that converts MP3 audio files to text using OpenAI's Whisper model for transcription and the Deep Multilingual Punctuation library for restoring punctuation. The script processes audio files from a specified folder, generates text transcripts, and saves them back into the same folder with improved readability.

---

## Features
- Converts MP3 files to WAV format for processing.
- Transcribes audio to text using the Whisper model.
- Restores punctuation using the Deep Multilingual Punctuation library for better readability.
- Automatically saves transcripts in the same folder as the input audio files.

---

## Installation

Install the following dependencies first:
```bash
pip install pydub openai-whisper ffmpeg
pip install transformers
pip install deepmultilingualpunctuation
```


## Dependencies
- Python: 3.8 or higher
- Libraries:
* pydub: For audio file conversion.
*  openai-whisper: For transcription.
* ffmpeg: Required for audio processing.
* deepmultilingualpunctuation: For punctuation restoration.

## Project Structure
```bash
mp3-to-text-punctuation/
├── mp3_to_text.py  # Main script for processing MP3 files
├── README.md       # Project documentation
```

## Acknowledgments
- OpenAI Whisper: Used for audio-to-text transcription.
- Deep Multilingual Punctuation: For restoring punctuation in text.
- FFmpeg: For audio conversion and processing.
