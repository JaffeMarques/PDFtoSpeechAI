import config

def prepare_ssml_text(text):
    text = text.replace('.', '<break time="500ms"/>')
    text = text.replace(',', '<break time="300ms"/>')
    text = text.replace(';', '<break time="400ms"/>')
    text = text.replace(':', '<break time="400ms"/>')
    text = text.replace('!', '<break time="500ms"/>')
    text = text.replace('?', '<break time="500ms"/>')
    return text

def create_ssml(text, language_code, voice_name, provider=config.TTS_PROVIDER):
    ssml_text = prepare_ssml_text(text)
    slow_down_rate = config.SLOW_DOWN_RATE
    
    if(provider == 'azure'):
        return f'''
        <speak version="1.0" xml:lang="{language_code}">
            <voice name="{voice_name}">
                {ssml_text}
            </voice>
        </speak>
        '''
    return f'''
        <speak>
            <prosody rate="{slow_down_rate}">
                {ssml_text}
            </prosody>
        </speak>
        '''