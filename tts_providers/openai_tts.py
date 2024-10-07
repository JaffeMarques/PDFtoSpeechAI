import time
import config
from openai import OpenAI

def convert_text_to_speech_openai(
    input_text, 
    output_file, 
    api_key=config.OPENAI_SPEACH_SECRET,
    voice_name=config.OPENAI_SPEACH_VOICE,
    model=config.OPENAI_SPEACH_MODEL
 ):
    OpenAI.api_key=api_key
    client = OpenAI()
    try:
        with client.audio.speech.with_streaming_response.create(
            model=model,
            voice=voice_name,
            input=input_text
        ) as response:
            response.stream_to_file(output_file)

        print(f'> Audio saved to {output_file}')

    except Exception as e:
        print(f'* An exception occurred: {e}')

    time.sleep(5)
