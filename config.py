import os
from dotenv import load_dotenv

load_dotenv()

INPUT_FOLDER = os.getenv('INPUT_FOLDER', 'input')
OUTPUT_FOLDER = os.getenv('OUTPUT_FOLDER', 'output')

TTS_PROVIDER = os.getenv('TTS_PROVIDER', 'azure')

AZURE_SPEACH_SECRET = os.getenv('AZURE_SPEACH_SECRET')
AZURE_SPEACH_REGION = os.getenv('AZURE_SPEACH_REGION')
AZURE_SPEACH_VOICE = os.getenv('AZURE_SPEACH_VOICE', 'pt-BR-ThalitaNeural')
AZURE_SPEACH_LANGUAGE = os.getenv('AZURE_SPEACH_LANGUAGE', 'pt-BR') 

AWS_SPEACH_SECRET = os.getenv('AWS_SPEACH_SECRET') 
AWS_SPEACH_REGION = os.getenv('AWS_SPEACH_REGION') 
AWS_SPEACH_VOICE = os.getenv('AWS_SPEACH_VOICE', 'Camila') 
AWS_SPEACH_LANGUAGE = os.getenv('AWS_SPEACH_LANGUAGE', 'pt-BR') 