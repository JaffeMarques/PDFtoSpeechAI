def prepare_ssml_text(text):
    text = text.replace('.', '<break time="500ms"/>')
    text = text.replace(',', '<break time="300ms"/>')
    text = text.replace(';', '<break time="400ms"/>')
    text = text.replace(':', '<break time="400ms"/>')
    text = text.replace('!', '<break time="500ms"/>')
    text = text.replace('?', '<break time="500ms"/>')
    return text

def create_ssml(text, language_code, voice_name, provider='azure'):
    if(provider == 'azure'):
        return f'''
        <speak version="1.0" xml:lang="{language_code}">
            <voice name="{voice_name}">
                {prepare_ssml_text(text)}
            </voice>
        </speak>
        '''
    return f'''
        <speak>
                {prepare_ssml_text(text)}
        </speak>
        '''