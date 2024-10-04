import os
import re
import time
import config
import pdfplumber
from pydub import AudioSegment
from moviepy.editor import concatenate_audioclips, AudioFileClip
from tts_providers.azure_tts import convert_text_to_speech_azure
from tts_providers.amazon_tts import convert_text_to_speech_amazon

def process_input_folder():
    input_folder = config.INPUT_FOLDER
    base_filenames = []
    for filename in os.listdir(input_folder):
        file_path = os.path.join(input_folder, filename)
        if os.path.isfile(file_path):
            base_name, extension = os.path.splitext(filename)
            print(f"Processing file: {filename}")
            base_filenames.append(base_name)

    return base_filenames

def convert_chunks_to_audio(chunks, output_folder, reprocess=[]):
    audio_files = []
    for i, chunk in enumerate(chunks):
        if reprocess:
            if (i + 1) in reprocess:
                print(f"> & Reprocessing chunk {i+1}")
            else:
                continue
        
        print(f"> Processing chunk {i+1}")
        output_file = os.path.join(output_folder, f"chunk_{i+1}.mp3")
        tts_provider = config.TTS_PROVIDER
        if(tts_provider == 'azure'):
            convert_text_to_speech_azure(chunk, output_file)
        elif (tts_provider == 'aws'):
            convert_text_to_speech_amazon(chunk, output_file)
            
        audio_files.append(output_file)

    return audio_files

def pdf_to_markdown(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        markdown_content = ""
        for page in pdf.pages:
            text = page.extract_text()
            if text:
                markdown_page = text.replace('\n', '\n\n')
                markdown_content += markdown_page + '\n\n---\n\n'

        return markdown_content

def markdown_to_plain_text(markdown_text):
    text = re.sub(r'\[([^\]]+)\]\([^\)]+\)', r'\1', markdown_text)

    text = re.sub(r'\*\*([^*]+)\*\*', r'\1', text)  # Bold with **
    text = re.sub(r'\*([^*]+)\*', r'\1', text)      # Italic with *
    text = re.sub(r'\_\_([^_]+)\_\_', r'\1', text)  # Bold with __
    text = re.sub(r'\_([^_]+)\_', r'\1', text)      # Italic with _

    text = re.sub(r'#+\s?', '', text)  # Headers
    text = re.sub(r'-\s?', '', text)   # List items
    text = re.sub(r'>\s?', '', text)   # Blockquotes

    return text

def split_text(text, max_chunk_size=config.MAX_CHUNK_SIZE):
    chunks = []
    current_chunk = ""

    for sentence in text.split('.'):
        sentence = sentence.strip()
        if not sentence:
            continue

        if len(current_chunk) + len(sentence) + 1 <= max_chunk_size:
            current_chunk += sentence + "."
        else:
            chunks.append(current_chunk)
            current_chunk = sentence + "."

    if current_chunk:
        chunks.append(current_chunk)

    return chunks

def combine_audio_with_moviepy(folder_path, output_file):
    audio_clips = []

    for file_name in sorted(os.listdir(folder_path), key=natural_sort_key):
        if file_name.endswith('.mp3'):
            file_path = os.path.join(folder_path, file_name)
            print(f"Processing file: {file_path}")

            try:
                clip = AudioFileClip(file_path)
                audio_clips.append(clip)
            except Exception as e:
                print(f"Error processing file {file_path}: {e}")

    if audio_clips:
        final_clip = concatenate_audioclips(audio_clips)
        final_clip.write_audiofile(output_file)
        print(f"Combined audio saved to {output_file}")
    else:
        print("No audio clips to combine.")

def combine_audio_with_pydub(folder_path, output_file):
    combined = AudioSegment.empty()
    for file_name in sorted(os.listdir(folder_path)):
        if file_name.endswith('.mp3'):
            file_path = os.path.join(folder_path, file_name)
            print(f"Processing file: {file_path}")
            try:
                audio = AudioSegment.from_file(file_path, format="mp3")
                combined += audio
            except Exception as e:
                print(f"Error processing file {file_path}: {e}")
    if len(combined) > 0:
        combined.export(output_file, format='mp3')
        print(f"Combined audio saved to {output_file}")
    else:
        print("No audio clips to combine.")

def natural_sort_key(file_name):
    return [int(text) if text.isdigit() else text for text in re.split(r'(\d+)', file_name)]

def process_file(filename):
    pdf_path = f'{config.INPUT_FOLDER}/{filename}.pdf'
    markdown_text = pdf_to_markdown(pdf_path)
    print('> Marked ready')

    plain_text = markdown_to_plain_text(markdown_text)
    print('> Plain text ready')

    chunks = split_text(plain_text)
    print('> Splited text ready')

    output_folder = "chunks"

    #reprocess = [137, 142]
    #convert_chunks_to_audio(chunks, output_folder, reprocess)

    convert_chunks_to_audio(chunks, output_folder)
    print('> Chunks ready')

    combine_audio_with_moviepy('chunks', f'{config.OUTPUT_FOLDER}/{filename}.mp3')
    # combine_audio_with_pydub('chunks', f'output/{filename}.mp3')
    print('> Audio ready')