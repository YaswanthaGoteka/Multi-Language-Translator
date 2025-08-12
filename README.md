## Speech-to-Text and Translation Script
This Python script records audio from your microphone, transcribes the speech to text using OpenAI’s Whisper model, and then translates the transcribed text into a target language using the Google Translator API (via the deep_translator package).

## Features
Audio Recording: Captures 5 seconds of audio from your microphone at 16 kHz sample rate.

## Speech Transcription: 
Uses Whisper’s pre-trained models (base by default, but can be changed) for highly accurate speech-to-text conversion.

## Language Translation: 
Translates the transcribed text automatically detected from source language into any supported language using Google Translate.

## Multi-language Support: 
Supports dozens of target languages specified via language codes.

Requirements
- Python 3.7+
- whisper (OpenAI Whisper)
- sounddevice
- scipy
- deep_translator
- ffmpeg installed and available in your system PATH (for Whisper audio processing)


## Usage:
Run the script:
1. When prompted, enter the target language code (e.g., es for Spanish, fr for French).

2. The script will record 5 seconds of audio, transcribe it, then translate and print the result.

3. You can enter any of the following codes when prompted to translate the text:
(ar, bn, zh-cn, zh-tw, da, nl, en, fr, de, el, he, hi, id, it, ja, ko, ms, no,
fa, pl, pt, ro, ru, es, sv, ta, te, tr, uk, vi)

## Example Usage:
~~~
Enter The Language Code: es
🎙️ Recording for 5 seconds...
✅ Recording complete!
🧠 Transcribing with Whisper...
📝 Transcribed text: Hello, how are you?
🌍 Translating to es...
🗣️ Translated text: Hola, ¿cómo estás?
~~~

Notes: 
- The script suppresses a known warning about FP16 not supported on CPU by Whisper.

- Adjust the audio recording duration or sample rate by modifying the record_audio() parameters.

- You can switch Whisper models by changing the model name in whisper.load_model("base") to "small", "medium", or "large" for better accuracy at the cost of speed.

