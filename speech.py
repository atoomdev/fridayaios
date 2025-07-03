import time
import speech_recognition as sr
import pyttsx3

# Konuşma motoru başlatma
engine = pyttsx3.init()
engine.setProperty('rate', 190)  # Konuşma hızı (varsayılan genelde 200’dür)
engine.setProperty('volume', 1.0)

# Ses seçimi (0 = erkek, 1 = kadın — bilgisayara göre değişebilir)
voices = engine.getProperty('voices')
engine.setProperty("voice", voices[0].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen_for_keyword(recognizer, mic, keyword="friday"):
    """Continuously listen for the given keyword using the provided recognizer
    and microphone instances."""
    time.sleep(0.4)
    print("Listening for keyword...")  # Sadece başlangıçta mesajı yazdır
    while True:
        with mic as source:
            try:
                audio = recognizer.listen(source, timeout=5, phrase_time_limit=3)
            except sr.WaitTimeoutError:
                # No speech detected within the timeout, continue listening
                continue
        try:
            text = recognizer.recognize_google(audio)
            if keyword.lower() in text.lower():
                print("Yes sir?")
                speak("Yes sir?")
                return
        except sr.UnknownValueError:
            # Speech was unintelligible, ignore and continue listening
            pass
        except sr.RequestError as e:
            print(f"Could not request results; {e}")

def listen_for_command():
    time.sleep(0.4)
    recognizer = sr.Recognizer()
    mic = sr.Microphone()
    print("Listening for command...")
    with mic as source:
        audio = recognizer.listen(source, phrase_time_limit=3)
    try:
        command = recognizer.recognize_google(audio)
        print(f"You said: {command}")
        return command
    except sr.UnknownValueError:
        print("Sorry, I did not understand that.")
        speak("Sorry, I did not understand that.")
        return None
    except sr.RequestError as e:
        print(f"Could not request results; {e}")
        speak(f"Could not request results; {e}")
        return None
