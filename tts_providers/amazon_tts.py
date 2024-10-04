from util import create_ssml
import boto3
import os
import time
import config

def convert_text_to_speech_amazon(text, output_file, language_code=config.AWS_SPEACH_LANGUAGE, voice_name=config.AWS_SPEACH_VOICE):
    polly_client = boto3.client(
        'polly',
        aws_access_key_id=config.AWS_SPEACH_KEY,
        aws_secret_access_key=config.AWS_SPEACH_SECRET,
        region_name=config.AWS_SPEACH_REGION
    )
    text = create_ssml(text, language_code, voice_name)

    try:
        response = polly_client.synthesize_speech(
            Text=text,
            OutputFormat='mp3',
            VoiceId=voice_name,
            LanguageCode=language_code,
            TextType='ssml'
        )

        with open(output_file, 'wb') as audio_file:
            audio_file.write(response['AudioStream'].read())

        print(f'> Audio saved to {output_file}')

    except Exception as e:
        print(f"* An exception occurred: {e}")

    time.sleep(1)