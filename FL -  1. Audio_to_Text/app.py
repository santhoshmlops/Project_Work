import os
from faster_whisper import WhisperModel


def convert_audio_to_text(audio_file):
    try:
        # "base" - CPU or "large-v3" - GPU or "distil-large-v3" - GPU
        model_size = "base"   

        # Run on GPU with FP16
        # model = WhisperModel(model_size, device="cuda", compute_type="float16")

        # or run on GPU with INT8
        # model = WhisperModel(model_size, device="cuda", compute_type="int8_float16")

        # or run on CPU with INT8
        model = WhisperModel(model_size, device="cpu", compute_type="int8")

        segments, info = model.transcribe(audio_file, beam_size=5)
        print("{}  - Language Detected '{}' Probability - {}".format(os.path.basename(audio_file),info.language, info.language_probability))

        # Collect all the text from segment.text
        text = []
        for segment in segments:
            text.append(segment.text)
        return '\n'.join(text)  
    except Exception as e:
        print("Error:", e)
        return "Whisper Model could not understand audio"


def process_audio_files(directory):
    try:
        for filename in os.listdir(directory):
            if filename.endswith(('.mp3', '.wav', '.ogg', '.flac')):
                audio_file = os.path.join(directory, filename)
                text = convert_audio_to_text(audio_file)
                output_filename = os.path.splitext(filename)[0] + ".txt"
                output_path = os.path.join(text_directory_path, output_filename)
                with open(output_path, "w") as text_file:
                    text_file.write(text)
    except Exception as e:
        print("Error:", e)
        return " Load the correct Directory"

# Specify the directory containing audio files
audio_directory_path = "Audio"
text_directory_path = "Text"

# Call the function to process audio files in the directory
process_audio_files(audio_directory_path)