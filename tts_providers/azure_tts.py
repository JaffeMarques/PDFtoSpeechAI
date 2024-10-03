from util import create_ssml
import time
import azure.cognitiveservices.speech as speechsdk
import config

def convert_text_to_speech_azure(
    input_text, 
    output_file, 
    api_key=config.AZURE_SPEACH_SECRET, 
    region=config.AZURE_SPEACH_REGION, 
    language_code=config.AZURE_SPEACH_LANGUAGE, 
    voice_name=config.AZURE_SPEACH_VOICE
 ):
    speech_config = speechsdk.SpeechConfig(subscription=api_key, region=region)
    speech_config.speech_synthesis_language = language_code
    speech_config.speech_synthesis_voice_name = voice_name
    audio_config = speechsdk.audio.AudioOutputConfig(filename=output_file)
    ssml_text = create_ssml(input_text, language_code, voice_name)

    synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)

    try:
        result = synthesizer.speak_ssml_async(ssml_text).get()

        if result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
            print(f'> Audio saved to {output_file}')
        elif result.reason == speechsdk.ResultReason.Canceled:
            cancellation_details = result.cancellation_details
            print(f'* Error: {result.reason}')
            print(f'* Cancellation reason: {cancellation_details.reason}')
            print(f'* Error code: {cancellation_details.error_code}')
            if cancellation_details.error_details:
                print(f'* Error details: {cancellation_details.error_details}')
            print("* Please check your input text and configuration.")
    except Exception as e:
        print(f"* An exception occurred: {e}")
    
    time.sleep(5)
