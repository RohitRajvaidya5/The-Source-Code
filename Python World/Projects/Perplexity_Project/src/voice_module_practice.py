# Module for text to speech
import pyttsx3

# Speech to text module
import speech_recognition as sr

# Audio file to text module
import whisper

# text to speech file
from gtts import gTTS

import os


# Audio File To Text
def audio_to_text():
    model = whisper.load_model("tiny")
    result = model.transcribe("audio.mp3")
    print(result["text"])


# Speech to Text
def speech_to_text():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak:")
        audio = r.listen(source)
    text = r.recognize_google(audio)
    return text


# Text to speech
def text_to_speech(text_for_speech):
    engine = pyttsx3.init()
    engine.say(text_for_speech)
    engine.runAndWait()

# text to speech mp3 file conversion
def text_to_speech_file(text_for_speech):
    tts = gTTS(text_for_speech, lang="en")
    tts.save("hello.mp3")


spoken_text = speech_to_text()

spoken_text = spoken_text.lower()

if "notepad" in spoken_text:
    print("Opening Notepad...")
    os.system("notepad")
elif "exit" in spoken_text:
    print("Exiting.")
else:
    print("No matching command found.")


