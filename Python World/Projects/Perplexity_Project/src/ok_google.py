import struct
import pyaudio
import pyttsx3
import os
import json
from vosk import Model, KaldiRecognizer
from pvporcupine import create
import speech_recognition as sr

# 🔑 Put your real Picovoice access key here
ACCESS_KEY = "vjSQNkDuV/TNMKdQPosCVY1q3kNPT9JKcA2kW1eAt5cYjub+6Mzc3A=="

# 🎤 Setup Text-to-Speech
tts = pyttsx3.init()
def speak(text):
    print("Assistant:", text)
    tts.say(text)
    tts.runAndWait()

# Speech to Text
def speech_to_text():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak:")
        audio = r.listen(source)
    text2 = r.recognize_google(audio)
    return text2

# 🗣 Load Vosk speech model
vosk_model = Model(model_name="vosk-model-small-en-us-0.15")
recognizer = KaldiRecognizer(vosk_model, 16000)

# 🔊 Setup Porcupine wake word detection
porcupine = create(
    access_key=ACCESS_KEY,
    keywords=["hey google", "ok google"]  # You can use: "jarvis", "computer", etc.
)

# 🎧 Setup audio stream
pa = pyaudio.PyAudio()
stream = pa.open(format=pyaudio.paInt16,
                 channels=1,
                 rate=16000,
                 input=True,
                 frames_per_buffer=porcupine.frame_length)

print("✅ Listening for 'Hey Google'...")

try:
    while True:
        pcm = stream.read(porcupine.frame_length, exception_on_overflow=False)
        pcm_unpacked = struct.unpack_from("h" * porcupine.frame_length, pcm)
        if porcupine.process(pcm_unpacked) >= 0:
            speak("Yes, I'm listening...")
            text = speech_to_text()
            if "notepad" in text:
                print("opening notepad")

except KeyboardInterrupt:
    print("Exiting...")

finally:
    stream.stop_stream()
    stream.close()
    pa.terminate()
    porcupine.delete()
