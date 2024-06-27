import pyttsx3
import re
import os

def generate_audio_from_text(file_path, output_directory):
    # Ensures the output directory exists
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    # Initializing the text-to-speech engine
    engine = pyttsx3.init()

    # Set properties (optional)
    engine.setProperty('rate', 150)    # Speed percent (can go over 100)
    engine.setProperty('volume', 0.9)  # Volume 0-1

    # Function to save text to a file with a given filename
    def save_to_audio(text, filename):
        # Split the text into parts, keeping the full stop and comma
        parts = re.split(r'(\. |, )', text)  # Split at full stops and commas while keeping the delimiter
        full_text = ''
        for part in parts:
            if part.strip():
                if 'script' in part.lower():  # Skip converting line with "script"
                    continue
                full_text += part.strip() + ' '

        # Save the full text to an audio file
        engine.save_to_file(full_text, filename)
        engine.runAndWait()

    # Read the script text from file
    with open(file_path, 'r', encoding='utf-8') as file:
        script_text = file.read()

    # Format 1: Script with Narrator: prefix
    if 'Narrator:' in script_text:
        # Extract narrator's content
        narrator_lines = re.findall(r'Narrator: (.*?)(?=\nNarrator: |\Z)', script_text, re.DOTALL)

        # Remove special characters and format the text
        for line in narrator_lines:
            cleaned_line = re.sub(r'[\"*(){}[\]]', '', line)
            cleaned_line = re.sub(r'\.\s*', '. ', cleaned_line)
            cleaned_line = re.sub(r',\s*', ', ', cleaned_line)
            cleaned_line = re.sub(r'Narrator\s*', ' ', cleaned_line)
            save_to_audio(cleaned_line, os.path.join(output_directory, 'audio.mp3'))

    # Format 2: Script without Narrator: prefix
    else:
        cleaned_text = re.sub(r'[\"*(){}[\]]', '', script_text)
        cleaned_text = re.sub(r'\.\s*', '. ', cleaned_text)
        cleaned_text = re.sub(r',\s*', ', ', cleaned_text)
        save_to_audio(cleaned_text, os.path.join(output_directory, 'audio.mp3'))

    print(f'Generated audio file in the "{output_directory}" directory.')
    