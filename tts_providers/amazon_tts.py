from util import prepare_ssml_text
import boto3
import os
import time

def convert_text_to_speech_amazon(text, output_file, aws_access_key, aws_secret_key, aws_region, language_code='pt-BR', voice_name='Camila'):
    polly_client = boto3.client('polly')

    try:
        response = polly_client.synthesize_speech(
            Text=text,
            OutputFormat='mp3',
            VoiceId=voice_name,
            LanguageCode=language_code
        )

        # Save the synthesized speech to an MP3 file
        with open(output_file, 'wb') as audio_file:
            audio_file.write(response['AudioStream'].read())

        print(f'> Audio saved to {output_file}')

    except Exception as e:
        print(f"* An exception occurred: {e}")

    time.sleep(1)