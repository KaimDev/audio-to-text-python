# Audio To Text

## Description
This is a simple python script that converts audio files to text using the Openai's Whisper Model.

## Installation
1. Clone the repository
2. Install the Whisper Model from Github

```bash
pip install git+https://github.com/openai/whisper.git
```

## Usage
```bash
python main.py <path_to_audio_file>
```

It will create a file named same as the audio file with  `-transcribed.txt` suffix in the same directory.