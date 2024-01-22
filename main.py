import argparse
import whisper

# Receive the audio file path as a command line argument
parser = argparse.ArgumentParser()
parser.add_argument("audio_file", help="Path to the audio file")
args = parser.parse_args()

# Load the model and transcribe the audio
model = whisper.load_model("base")
result = model.transcribe(args.audio_file)
transcribed_text = result["text"]
print(transcribed_text)

# Save the transcribed text using the file name of the audio file
with open(args.audio_file[:-4] + "-transcribed.txt", "w") as f:
    f.write(transcribed_text)
