import os
import warnings

# Suppress the FP16 CPU warning from Whisper
warnings.filterwarnings("ignore", message="FP16 is not supported on CPU; using FP32 instead")

# Add Homebrew ffmpeg path to environment PATH for PyCharm
os.environ["PATH"] += os.pathsep + "/opt/homebrew/bin"  # Adjust if your ffmpeg is elsewhere

import whisper
import sounddevice as sd
from scipy.io.wavfile import write
from deep_translator import GoogleTranslator

def record_audio(filename="input.wav", duration=5, fs=16000):
    print(f"🎙️ Recording for {duration} seconds...")
    audio = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='int16')
    sd.wait()
    write(filename, fs, audio)
    print("✅ Recording complete!")

def transcribe_with_whisper(audio_path="input.wav"):
    print("🧠 Transcribing with Whisper...")
    model = whisper.load_model("base")  # or "small", "medium", "large"
    result = model.transcribe(audio_path)
    text = result["text"]
    print("📝 Transcribed text:", text)
    return text

def translate_text(text, target_lang="es"):
    print(f"🌍 Translating to {target_lang}...")
    translated = GoogleTranslator(source='auto', target=target_lang).translate(text)
    print("🗣️ Translated text:", translated)
    return translated

if __name__ == "__main__":
    print(print("""
Language Codes for Translation:

Arabic             : ar
Bengali            : bn
Chinese (Simplified): zh-cn
Chinese (Traditional): zh-tw
Danish             : da
Dutch              : nl
English            : en
French             : fr
German             : de
Greek              : el
Hebrew             : he
Hindi              : hi
Indonesian         : id
Italian            : it
Japanese           : ja
Korean             : ko
Malay              : ms
Norwegian          : no
Persian            : fa
Polish             : pl
Portuguese         : pt
Romanian           : ro
Russian            : ru
Spanish            : es
Swedish            : sv
Tamil              : ta
Telugu             : te
Turkish            : tr
Ukrainian          : uk
Vietnamese         : vi
""")
)
    user_input = input("Enter The Language Code: ")
    record_audio(duration=5)
    text = transcribe_with_whisper("input.wav")
    translate_text(text, target_lang=user_input)  # Change target language as needed
