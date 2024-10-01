# PDF to Audio Converter using Azure Text-to-Speech

This project converts PDF files into audio files using Azure's Text-to-Speech service. It extracts text from PDFs, processes it, and generates high-quality audio output, making it ideal for creating audiobooks or listening to documents on the go.

## Table of Contents

- [Description](#description)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Setup](#setup)
- [Usage](#usage)
- [Notes](#notes)
- [Dependencies](#dependencies)
- [License](#license)

---

## Description

The application reads PDF files from an `input` directory, extracts and splits the text into manageable chunks, and then uses Azure's Cognitive Services to convert each chunk into an audio file. The audio files are saved in the `output` directory. This allows for easy conversion of lengthy PDFs into accessible audio formats.

---

## Prerequisites

- **Azure Account**: An active Azure account with access to the Cognitive Services Speech service.
- **Azure Speech Service Credentials**: Your Azure Speech API key and region.
- **Python**: Version 3.12 installed on your system.
- **pip**: Version 23.0 or higher for package management.

---

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/JaffeMarques/pdf_to_mp3.git
cd pdf_to_mp3
```

### 2. Set Up a Virtual Environment

It's recommended to use a virtual environment to manage dependencies.

```bash
python3 -m venv myenv
```

Activate the virtual environment:

```bash
source myenv/bin/activate
```

### 3. Install Dependencies

Install the required Python packages using pip:

```bash
pip install -r requirements.txt
```

## Setup

### 1. Create Required Directories

In the project root directory, create the following folders:

```bash
mkdir input chunks output
```


- input: Place your PDF files here.
- chunks: This folder will store the text chunks extracted from the PDFs.
- output: The generated audio files will be saved here.

### 2. Configure Azure Credentials

Create a .env file in the project root directory to store your Azure credentials securely.

```bash
touch .env
```

Add your Azure Speech API key and region to the .env file:

```env
AZURE_SPEECH_KEY=your_azure_speech_key
AZURE_SPEECH_REGION=your_azure_speech_region
```

Replace your_azure_speech_key and your_azure_speech_region with your actual Azure credentials.

## Usage

### 1. Place PDF Files in the Input Folder

Copy or move the PDF files you wish to convert into the input directory.

### 2. Run the Conversion Script

Execute the main Python script:

```bash
python main.py
```

The script will perform the following steps:

- **Read PDFs**: Scans the input folder for PDF files.
- **Extract Text**: Converts the PDF content into text.
- **Split Text into Chunks**: Breaks down large texts into smaller chunks for processing.
- **Convert Text to Audio**: Uses Azure Text-to-Speech to generate audio files from text chunks.
- **Save Audio Files**: Outputs the audio files into the output folder.

### Notes

- **Azure Limits**: Be mindful of Azure's service limits and quotas. Excessive use may result in throttling or additional charges.
- **Folder Structure**: Ensure the input, chunks, and output folders exist in the project root to avoid runtime errors.
- **Voice and Language Settings**: You can customize the voice name and language code in the script to suit your preferences.
- **Error Handling**: The script includes basic error handling, but additional checks can be implemented as needed.