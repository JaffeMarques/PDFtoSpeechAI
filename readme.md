# PDF to Audio Converter using Azure, AWS, Eleven Labs, or OpenAI Text-to-Speech

This project converts PDF files into high-quality audio files using Azure, AWS, Eleven Labs, or OpenAI Text-to-Speech services. It extracts text from PDFs, processes it, and generates audio output, making it ideal for creating audiobooks or listening to documents on the go. 

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Setup](#setup)
- [Usage](#usage)
- [Configuration](#configuration)
- [Notes](#notes)
- [Troubleshooting](#troubleshooting)
- [Dependencies](#dependencies)
- [Contributing](#contributing)
- [License](#license)

## Features

- Support for multiple Text-to-Speech providers: Azure, AWS, elevenlabs, and OpenAI
- Batch processing of multiple PDF files
- Automatic text chunking for efficient processing
- Customizable voice and language settings
- Error handling and logging

## Prerequisites

- An active account with one of the following services:
  - Azure Cognitive Services
  - AWS Polly
  - Eleven Labs
  - OpenAI
- API credentials for the chosen service
- Python 3.12 or higher
- pip 23.0 or higher

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/JaffeMarques/PDFtoSpeechAI.git
   cd PDFtoSpeechAI
   ```

2. Set up a virtual environment:
   ```bash
   python3 -m venv myenv
   source myenv/bin/activate  # On Windows, use `myenv\Scripts\activate`
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Setup

1. Create required directories:
   ```bash
   mkdir input chunks output
   ```

2. Configure environment variables:
   The project includes an `env.example` file with all the necessary environment variables. To set up your configuration:

   a. Copy the `env.example` file to `.env`:
      ```bash
      cp env.example .env
      ```

   b. Open the `.env` file and fill in your credentials and preferences:

   ```plaintext
   # Choose your provider (azure, aws, elevenlabs, or openai)
   TTS_PROVIDER=

   # General settings
   MAX_CHUNK_SIZE=1000
   SLOW_DOWN_RATE=

   # Eleven Labs credentials
   ELEVENLABS_SPEACH_SECRET=
   ELEVENLABS_SPEACH_URL=
   ELEVENLABS_SPEACH_VOICE_ID=

   # OpenAI credentials
   OPENAI_SPEACH_SECRET=
   OPENAI_SPEACH_VOICE=
   OPENAI_SPEACH_MODEL=tts-1

   # Azure credentials
   AZURE_SPEACH_SECRET=
   AZURE_SPEACH_REGION=
   AZURE_SPEACH_VOICE=
   AZURE_SPEACH_LANGUAGE=

   # AWS credentials
   AWS_SPEACH_KEY=
   AWS_SPEACH_SECRET=
   AWS_SPEACH_REGION=
   AWS_SPEACH_VOICE=
   AWS_SPEACH_LANGUAGE=
   ```

   Fill in the appropriate values for your chosen provider and preferences. You only need to fill in the credentials for the provider you're using.

## Usage

1. Place PDF files in the `input` folder.

2. Run the conversion script:
   ```bash
   python main.py
   ```

3. Find the generated audio files in the `output` folder.

## Configuration

You can customize the following settings in the `.env` file:

- `TTS_PROVIDER`: Choose between 'azure', 'aws', 'elevenlabs', or 'openai'
- `MAX_CHUNK_SIZE`: Maximum number of characters per text chunk
- `SLOW_DOWN_RATE`: Adjust the speech rate (if supported by the provider)
- Provider-specific settings like voice, language, and region

## Notes

- This project is designed for educational purposes and may not be suitable for production environments without further optimization.
- Be mindful of service limits and quotas to avoid throttling or additional charges.
- Large PDFs may take considerable time to process.
- The script includes basic error handling, but you may need to implement additional checks for specific use cases.

## Troubleshooting

- If you encounter "File not found" errors, ensure that the `input`, `chunks`, and `output` folders exist in the project root.
- For API-related issues, verify your credentials in the `.env` file and check your account status with the chosen provider.
- If the audio quality is not satisfactory, try adjusting the `MAX_CHUNK_SIZE` or experimenting with different voice settings.

## Dependencies

See `requirements.txt` for a full list of dependencies.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
