import speech_recognition as sr # pip install speechrecognition # pip install pyaudio # 1 pip install pipwin 2 pipwin install pyaudio
import pyttsx3  # pip install pyttsx3

def speak(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 185)
    engine.setProperty('volume', 1.0)
    
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id) 
    
    print(f"[Nexus]: {text}")
    engine.say(text)
    engine.runAndWait()

# def speak(text):
#     """Converts text to speech with personality properties."""
#     engine = pyttsx3.init()
#     engine.setProperty('rate', 180)
#     engine.setProperty('volume', 1.0)
#     voices = engine.getProperty('voices')
#     engine.setProperty('voice', voices[0].id) 
    
#     print(f">> {text}")
#     engine.say(text)
#     engine.runAndWait()

def listen():
    """Captures audio and returns lowercase string with error handling."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        recognizer.pause_threshold = 1
        audio = recognizer.listen(source)

    try:
        query = recognizer.recognize_google(audio)
        return query.lower()
    except sr.UnknownValueError:
        return "error_unknown"
    except sr.RequestError:
        return "error_network"