import time
import config
import requests

def convert_text_to_speech_elevenlabs(
    input_text, 
    output_file, 
    api_key=config.ELEVENLABS_SPEACH_SECRET,
    voice_id=config.ELEVENLABS_SPEACH_VOICE_ID,
):
    url = f'{config.ELEVENLABS_SPEACH_URL}text-to-speech/{voice_id}'
    headers = {
        'xi-api-key': api_key,
        'Content-Type': 'application/json'
    }
    data = {
        'text': input_text,
        'voice_settings': {
            'stability': 0.75,
            'similarity_boost': 1.0
        }
    }
    
    try:
        response = requests.post(url, json=data, headers=headers)
        response.raise_for_status()
        with open(output_file, 'wb') as audio_file:
            audio_file.write(response.content)

        print(f'> Audio saved to {output_file}')

    except Exception as e:
        print(f'* An exception occurred: {e}')

    time.sleep(5)
    
def list_elevenlabs_voices(api_key=config.ELEVENLABS_SPEACH_SECRET):
    url = f'{config.ELEVENLABS_SPEACH_URL}voices'
    headers = {
        'xi-api-key': api_key
    }
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        voices = response.json()
        
        for voice in voices['voices']:
            print(f"Name: {voice['name']}, Voice ID: {voice['voice_id']}")
            
    except Exception as e:
        print(f'* An error occurred: {e}')
