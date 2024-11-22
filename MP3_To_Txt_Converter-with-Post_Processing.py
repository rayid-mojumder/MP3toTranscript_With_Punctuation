#!/usr/bin/env python
# coding: utf-8

# In[3]:


#Install the following dependencies first
#pip install pydub openai-whisper ffmpeg
#pip install transformers pydub openai-whisper ffmpeg
#pip install deepmultilingualpunctuation


import os
from pydub import AudioSegment
import whisper
from deepmultilingualpunctuation import PunctuationModel

import warnings
warnings.filterwarnings("ignore", category=FutureWarning, module="torch.utils._pytree")
import warnings
warnings.filterwarnings("ignore", category=FutureWarning, module="whisper")
import warnings
warnings.filterwarnings("ignore", category=UserWarning, module="whisper")


# Suppress warnings
warnings.filterwarnings("ignore", category=FutureWarning, module="torch.utils._pytree")
warnings.filterwarnings("ignore", category=FutureWarning, module="whisper")
warnings.filterwarnings("ignore", category=UserWarning, module="whisper")

# Define paths
input_folder = r"E:\Current_Audio_file" #change to your folder 
output_folder = r"E:\Current_Audio_file" #change to your folder 

def restore_punctuation(text):
    """
    Use the deepmultilingualpunctuation model to add punctuation.
    """
    print("Restoring punctuation...")
    model = PunctuationModel()
    return model.restore_punctuation(text)

def mp3_to_text(input_folder, output_folder):
    # Get the MP3 file from the input folder
    mp3_files = [f for f in os.listdir(input_folder) if f.endswith('.mp3')]
    if not mp3_files:
        print("No MP3 files found in the input folder.")
        return
    
    # Process each MP3 file
    for mp3_file in mp3_files:
        mp3_path = os.path.join(input_folder, mp3_file)
        wav_path = os.path.join(output_folder, os.path.splitext(mp3_file)[0] + ".wav")
        
        # Convert MP3 to WAV
        print(f"Converting {mp3_file} to WAV format...")
        audio = AudioSegment.from_file(mp3_path)
        audio.export(wav_path, format="wav")
        
        # Load Whisper model
        print("Loading Whisper model...")
        model = whisper.load_model("base")
        
        # Transcribe WAV file
        print(f"Transcribing {mp3_file}...")
        result = model.transcribe(wav_path)
        raw_transcript = result['text']
        
        # Restore punctuation
        transcript_with_punctuation = restore_punctuation(raw_transcript)
        
        # Save transcript to text file
        transcript_path = os.path.join(output_folder, os.path.splitext(mp3_file)[0] + "_transcript.txt")
        with open(transcript_path, "w", encoding="utf-8") as f:
            f.write(transcript_with_punctuation)
        
        print(f"Transcription complete! Transcript with punctuation saved to {transcript_path}")

# Run the function
mp3_to_text(input_folder, output_folder)

