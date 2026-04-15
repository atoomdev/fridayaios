from spotipy.oauth2 import SpotifyOAuth
from sys import exit
import sys
import tkinter as tk
import speech_recognition as sr
import pyttsx3
import webbrowser
import requests
import time
import smtplib
import os
import pyautogui
import json
import openai
import datetime
import subprocess
import trimesh
from google import genai
from google.genai import types

os.system("echo off")
os.system("color a")
os.system("cls")
os.system(f'title FRIDAY AI OS - ALTINKAYNAK INDUSTRIES')

welcome = """


░██╗░░░░░░░██╗███████╗██╗░░░░░░█████╗░░█████╗░███╗░░░███╗███████╗  ███╗░░░███╗██████╗░
░██║░░██╗░░██║██╔════╝██║░░░░░██╔══██╗██╔══██╗████╗░████║██╔════╝  ████╗░████║██╔══██╗
░╚██╗████╗██╔╝█████╗░░██║░░░░░██║░░╚═╝██║░░██║██╔████╔██║█████╗░░  ██╔████╔██║██████╔╝
░░████╔═████║░██╔══╝░░██║░░░░░██║░░██╗██║░░██║██║╚██╔╝██║██╔══╝░░  ██║╚██╔╝██║██╔══██╗
░░╚██╔╝░╚██╔╝░███████╗███████╗╚█████╔╝╚█████╔╝██║░╚═╝░██║███████╗  ██║░╚═╝░██║██║░░██║
░░░╚═╝░░░╚═╝░░╚══════╝╚══════╝░╚════╝░░╚════╝░╚═╝░░░░░╚═╝╚══════╝  ╚═╝░░░░░╚═╝╚═╝░░╚═╝

░█████╗░██╗░░░░░████████╗██╗███╗░░██╗██╗░░██╗░█████╗░██╗░░░██╗███╗░░██╗░█████╗░██╗░░██╗
██╔══██╗██║░░░░░╚══██╔══╝██║████╗░██║██║░██╔╝██╔══██╗╚██╗░██╔╝████╗░██║██╔══██╗██║░██╔╝
███████║██║░░░░░░░░██║░░░██║██╔██╗██║█████═╝░███████║░╚████╔╝░██╔██╗██║███████║█████═╝░
██╔══██║██║░░░░░░░░██║░░░██║██║╚████║██╔═██╗░██╔══██║░░╚██╔╝░░██║╚████║██╔══██║██╔═██╗░
██║░░██║███████╗░░░██║░░░██║██║░╚███║██║░╚██╗██║░░██║░░░██║░░░██║░╚███║██║░░██║██║░╚██╗
╚═╝░░╚═╝╚══════╝░░░╚═╝░░░╚═╝╚═╝░░╚══╝╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░╚══╝╚═╝░░╚═╝╚═╝░░╚═╝
                                                                                                                                                                                                                                

"""
print(welcome)
time.sleep(5)
os.system("cls")

light = """
                                                                      


███████╗██████╗░██╗██████╗░░█████╗░██╗░░░██╗  ░█████╗░██╗  ░█████╗░░██████╗
██╔════╝██╔══██╗██║██╔══██╗██╔══██╗╚██╗░██╔╝  ██╔══██╗██║  ██╔══██╗██╔════╝
█████╗░░██████╔╝██║██║░░██║███████║░╚████╔╝░  ███████║██║  ██║░░██║╚█████╗░
██╔══╝░░██╔══██╗██║██║░░██║██╔══██║░░╚██╔╝░░  ██╔══██║██║  ██║░░██║░╚═══██╗
██║░░░░░██║░░██║██║██████╔╝██║░░██║░░░██║░░░  ██║░░██║██║  ╚█████╔╝██████╔╝
╚═╝░░░░░╚═╝░░╚═╝╚═╝╚═════╝░╚═╝░░╚═╝░░░╚═╝░░░  ╚═╝░░╚═╝╚═╝  ░╚════╝░╚═════╝░

"""
print(light)


# Konuşma motoru başlatma
engine = pyttsx3.init()
engine.setProperty('rate', 190)  # Konuşma hızı (varsayılan genelde 200’dür)
engine.setProperty('volume', 1.0)

# Ses seçimi (0 = erkek, 1 = kadın — bilgisayara göre değişebilir)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  # Dilersen 1 olarak da değiştirebilirsin

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
        return None
    except sr.RequestError as e:
        print(f"Could not request results; {e}")
        return None

def send_email(subject, message):
    smtp_server = "smtp.gmail.com"
    port = 587
    sender_email = "drmilonbot@gmail.com"
    sender_password = "eqmpakgannkiisdn"
    recipient_email = "atesaltinkaynak@gmail.com"

    email_message = f"Subject: {subject}\n\n{message}"

    with smtplib.SMTP(smtp_server, port) as server:
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, recipient_email, email_message)
    
def sleep_mode():
    print("Entering sleep mode...")
    speak("Entering sleep mode...")
    input("Press Enter to wake up...")  # Kullanıcıdan bir tuşa basmasını bekle
    print("Waking up...")
    speak("I am at your service sir.")



def send_email_to(subject, message):
    smtp_server = "smtp.gmail.com"
    port = 587
    sender_email = "drmilonbot@gmail.com"
    sender_password = "eqmpakgannkiisdn"
    recipient_email = input("Recipient Mail:")

    email_subject = subject
    print(f"\nSubject: {email_subject}")

    email_message = message
    print(f"Message: {email_message}\n")

    email_messagee = f"Subject: {subject}\n{message}"

    with smtplib.SMTP(smtp_server, port) as server:
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, recipient_email, email_messagee)

now = datetime.datetime.now()
hour = now.hour
minute = now.minute

day = now.day
month = now.month
year = now.year

def get_weather():
    url = "https://api.weatherapi.com/v1/current.json?key=d880c06435cf4a18a74184421232505&q=Ankara"
    response = requests.get(url)
    data = response.json()
    location = data["location"]["name"]
    country = data["location"]["country"]
    current_temp = data["current"]["temp_c"]
    condition = data["current"]["condition"]["text"]
    humidity = data["current"]["humidity"]
    wind_speed = data["current"]["wind_kph"]
    weather = data["current"]["condition"]["text"]
    temperature = data["current"]["temp_c"]
    return f"The current weather in Ankara, Turkey is {weather} with a temperature of {temperature} degrees and the wind speed is {wind_speed} kilometre per hour, sir."


def generate_response(prompt):
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise RuntimeError("GEMINI_API_KEY environment variable is not set.")

    try:
        with genai.Client(
            api_key=api_key,
            http_options=types.HttpOptions(timeout=30000)
        ) as client:
            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=(
                    "You are Friday OS, a highly intelligent AI with FULL Windows OS access. "
                    "Give short and clear answers in 1-2 sentences.\n\n"
                    f"User: {prompt}\n\nResponse:"
                ),
                config=types.GenerateContentConfig(
                    temperature=0.3,
                    max_output_tokens=120,
                ),
            )

        return (response.text or "").strip() or "I could not generate a response right now."
    except TimeoutError:
        return "Gemini API request timed out."
    except Exception as e:
        return f"Gemini API error: {e}"
    
def run_python_file(file_path):
    subprocess.Popen([sys.executable, file_path])

def show_results(ip, hostname, city, region, country, loc, isp, postal, timezone):
    window = tk.Tk()
    window.title("IP Logger Results")

    ip_label = tk.Label(window, text=f"IP: {ip}")
    ip_label.pack()

    hostname_label = tk.Label(window, text=f"Hostname: {hostname}")
    hostname_label.pack()

    city_label = tk.Label(window, text=f"City: {city}")
    city_label.pack()

    region_label = tk.Label(window, text=f"Region: {region}")
    region_label.pack()

    country_label = tk.Label(window, text=f"Country: {country}")
    country_label.pack()

    loc_label = tk.Label(window, text=f"Location: {loc}")
    loc_label.pack()

    isp_label = tk.Label(window, text=f"ISP: {isp}")
    isp_label.pack()

    postal_label = tk.Label(window, text=f"Postal Code: {postal}")
    postal_label.pack()

    timezone_label = tk.Label(window, text=f"Timezone: {timezone}")
    timezone_label.pack()

    window.mainloop()

def enable_ip_logger():
    ip = input("IP Address: ")

    url = f"https://ipinfo.io/{ip}/json"
    response = requests.get(url)
    data = json.loads(response.text)

    ip = data.get("ip", "")
    hostname = data.get("hostname", "")
    city = data.get("city", "")
    region = data.get("region", "")
    country = data.get("country", "")
    loc = data.get("loc", "")
    isp = data.get("org", "")
    postal = data.get("postal", "")
    timezone = data.get("timezone", "")

    email_subject = "IP Logger Report"
    email_message = f"IP: {ip}\nHOSTNAME: {hostname}\nCITY: {city}\nREGION: {region}\nCOUNTRY: {country}\nPOSTAL: {postal}\nLOC: {loc}\nTIMEZONE: {timezone}\nISP NAME: {isp}"
    report = f"------------------\nIP Logger Report\n↓↓↓↓↓↓↓↓↓↓↓↓↓↓\nIP: {ip}\nHOSTNAME: {hostname}\nCITY: {city}\nREGION: {region}\nCOUNTRY: {country}\nPOSTAL: {postal}\nLOC: {loc}\nTIMEZONE: {timezone}\nISP NAME: {isp}"
    send_email(email_subject, email_message)
    show_results(ip, hostname, city, region, country, loc, isp, postal, timezone)
    print("\n")

def generate_3d_model(description, output_path):
    """Create a simple 3D model based on the description and save it."""
    desc = description.lower()
    if "sphere" in desc:
        mesh = trimesh.creation.icosphere()
    elif "cylinder" in desc:
        mesh = trimesh.creation.cylinder(radius=1.0, height=2.0)
    elif "cone" in desc:
        mesh = trimesh.creation.cone(radius=1.0, height=2.0)
    else:
        mesh = trimesh.creation.box()
    mesh.export(output_path)


# Başlangıçta sesli moda geçiş yapalım
voice_mode = True

def process_query(query):
    global voice_mode
    response = ""

    if "hello" in query or "hi" in query or "hey" in query or "greetings" in query or "good morning" in query or "good afternoon" in query or "good evening" in query or "good night" in query or "how are you" in query or "how are you doing" in query or "how is it going" in query or "how's it going" in query or "what's up" in query      or "what's going on" in query or "how's everything" in query or "how's everything going" in query or "how's life" in query or "how's your day" in query or "how's your day going" in query or "how's your day been" in query or "how's your day treating you" in query or "how's your day been treating you" in query or "how's your day so far" in query or "how's your day been so far" in query or "how's your day going so far" in query or "how's your day treating you so far" in query  or "how's your day been treating you so far" in query or "how's your day going so far" in query or "how's your day treating you so far" in query:
        response = "Hello sir! How can I assist you today?"

    elif "send email" in query or "send an email" in query or "write an email" in query or "compose an email" in query or "email" in query or "write email" in query or "compose email" in query or "send an email to" in query or "write an email to" in query or "compose an email to" in query or "email to" in query or "write email to" in query or "compose email to" in query or "send an email to someone" in query or "write an email to someone" in query or "compose an email to someone" in query or "email to someone" in query or "write email to someone" in query or "compose email to someone" in query or "send an email to someone" in query or "write an email to someone" in query or "compose an email to someone" in query or "email to someone" in query or "write email to someone" in query or "compose email to someone" in query or "send an email to a person" in query or "write an email to a person" in query or "compose an email to a person" in query or "email to a person" in query or "write email to a person" in query or "compose email to a person" in query or "send an email to a person" in query or "write an email to a person" in query or "compose an email to a person" in query or "email to a person" in query or "write email to a person" in query or "compose email to a person" in query or "send an email to a person" in query or "write an email to a person" in query or "compose an email to a person" in query or "email to a person" in query or "write email to a person" in query or "compose email to a person" in query or "send an email to a person" in query or "write an email to a person" in query or "compose an email to a person" in query or "email to a person" in query or "write email to a person" in query or "compose email to a person" in query or "send an email to a person" in query or "write an email to a person" in query or "compose an email to a person" in query or "email to a person" in query or "write email to a person" in query or "compose email to a person" in query or "send an email to a person" in query or "write an email to a person" in query or "compose an email to a person" in query or "email to a person" in query or "write email to a person" in query or "compose email to a person" in query :
        response = "Sure, please provide the subject of the email."
        if voice_mode:
            speak(response)
            subject = listen_for_command()
        else:
            subject = input("Subject: ")
        if subject:
            response = "Please provide the message of the email."
            if voice_mode:
                speak(response)
                message = listen_for_command()
            else:
                message = input("Message: ")
            if message:
                if voice_mode:
                    speak("Please write the recipient's e-mail address.")
                send_email_to(subject, message)
                response = "Email sent successfully."
            else:
                response = "Sorry, I didn't catch the message. Please try again later."
        else:
            response = "Sorry, I didn't catch the subject. Please try again later."

    elif "enable" in query:
        password = input("Password: ")
        if password == "12123112":
            enable_ip_logger()
            response = "Complete"

    elif "open downloads" in query or "open download folder" in query or "open my downloads" in query or "open my download folder" in query or "open downloads folder" in query or "open download directory" in query or "open my downloads directory" in query or "open my download directory" in query:
        response = "Opening Downloads folder Sir."
        os.startfile("C:\\Users\\atesa\\Downloads")

    elif "open Chrome" in query or "open Google Chrome" in query or "open web browser" in query or "open my browser" in query or "open my web browser" in query or "open internet browser" in query or "open my internet browser" in query:
        response = "Opening Chrome browser Sir."
        speak(response)
        os.system("start chrome")

    elif "mute" in query:
        response = "Muted"
        pyautogui.press("volumemute")
    
    elif "volume up" in query:
        pyautogui.press("volumeup")
        
    elif "imagine" in query:
        response = "Tell me, what should I imagine?"
        if voice_mode:
            speak(response)
            photo = listen_for_command()
        else:
            photo = input("Imagine: ")
        if photo:
            x = f"Imagining '{photo}'"
            print(x)
            speak(x)
            photo = openai.Image.create(
                model="dall-e-3",
                prompt=photo,
                n=1,
                size="1024x1024"
            )
            image_url = photo['data'][0]['url']
            webbrowser.open(image_url, new=2)
            time.sleep(1)

    elif "design a 3D object" in query or "create a 3D model" in query:
        prompt = "What 3D object should I design?"
        if voice_mode:
            speak(prompt)
            obj_desc = listen_for_command()
        else:
            obj_desc = input("3D Object: ")
        if obj_desc:
            desktop = os.path.join(os.path.expanduser("~"), "Desktop")
            output_file = os.path.join(desktop, "friday_model.obj")
            generate_3d_model(obj_desc, output_file)
            response = f"3D model saved to {desktop}."
            if os.name == "nt":
                os.startfile(desktop)
            elif sys.platform == "darwin":
                subprocess.call(["open", desktop])
            else:
                subprocess.call(["xdg-open", desktop])

    elif "clear" in query:
        os.system("cls")
        print(light)

    elif "open desktop" in query or "open my desktop" in query or "open desktop folder" in query or "open my desktop folder" in query or "open desktop directory" in query or "open my desktop directory" in query:
        response = "Opening Desktop folder Sir."
        os.startfile("C:\\Users\\atesa\\Desktop")

    elif "open wifi settings" in query or "open wifi settings" in query or "open wifi" in query or "open my wifi settings" in query or "open my wifi" in query or "open wifi network settings" in query or "open my wifi network settings" in query:
        response = "Opening Wi-Fi settings, Sir."
        os.system("start ms-settings:network-wifi")

    elif "open bluetooth settings" in query or "open bluetooth" in query or "open my bluetooth settings" in query or "open my bluetooth" in query or "open bluetooth settings" in query or "open my bluetooth settings" in query:
        response = "Opening Bluetooth settings, Sir."
        os.system("start ms-settings:bluetooth")

    elif "open control panel" in query or "open my control panel" in query or "open control panel settings" in query or "open my control panel settings" in query or "open control panel directory" in query or "open my control panel directory" in query:
        response = "Opening Control Panel, Sir."
        os.system("start control")

    elif "open task manager" in query or "open my task manager" in query or "open task manager settings" in query or "open my task manager settings" in query or "open task manager directory" in query or "open my task manager directory" in query:
        response = "Opening Task Manager, Sir."
        os.system("start taskmgr")

    elif "open file explorer" in query or "open my file explorer" in query or "open file explorer settings" in query or "open my file explorer settings" in query or "open file explorer directory" in query or "open my file explorer directory" in query:
        response = "Opening File Explorer, Sir."
        os.startfile("C:\\")

    elif "open command prompt" in query or "open my command prompt" in query or "open command prompt settings" in query or "open my command prompt settings" in query or "open command prompt directory" in query or "open my command prompt directory" in query:
        response = "Opening Command Prompt, Sir."
        os.system("start cmd")

    elif "open settings" in query or "open my settings" in query or "open settings app" in query or "open my settings app" in query or "open settings directory" in query or "open my settings directory" in query:
        response = "Opening Settings, Sir."
        os.system("start ms-settings:")

    elif "open calculator" in query or "open my calculator" in query or "open calculator app" in query or "open my calculator app" in query or "open calculator directory" in query or "open my calculator directory" in query:
        response = "Opening Calculator, Sir."
        os.system("start calc")

    elif "open paint" in query or "open my paint" in query or "open paint app" in query or "open my paint app" in query or "open paint directory" in query or "open my paint directory" in query:
        response = "Opening Paint, Sir."
        os.system("start mspaint")

    elif "start" in query:
        app_name = listen_for_command()
        speak("Coming right up Sir.")
        if app_name:
            response = f"Starting {app_name}"
            os.system(f"start {app_name}")

    elif "open word" in query or "open my word" in query or "open word app" in query or "open my word app" in query or "open word directory" in query or "open my word directory" in query:
        response = "Opening Word, Sir."
        os.system("start winword")

    elif "open excel" in query or "open my excel" in query or "open excel app" in query or "open my excel app" in query or "open excel directory" in query or "open my excel directory" in query:
        response = "Opening Excel, Sir."
        os.system("start excel")

    elif "open powerpoint" in query or "open my powerpoint" in query or "open powerpoint app" in query or "open my powerpoint app" in query or "open powerpoint directory" in query or "open my powerpoint directory" in query: 
        response = "Opening PowerPoint, Sir."
        os.system("start powerpnt")
    
    elif "open notepad" in query or "open my notepad" in query or "open notepad app" in query or "open my notepad app" in query or "open notepad directory" in query or "open my notepad directory" in query:
        response = "Opening Notepad, Sir."
        os.system("start notepad")

    elif "open downloads" in query or "open download folder" in query or "open my downloads" in query or "open my download folder" in query or "open downloads folder" in query or "open download directory" in query or "open my downloads directory" in query or "open my download directory" in query:
        response = "Opening Downloads folder Sir."
        os.startfile("C:\\Users\\atesa\\Downloads")

    elif "open google" in query or "open Google Chrome" in query or "start brave" in query or "open my browser" in query or "open brave" in query or "open internet browser" in query or "open my internet browser" in query:
        response = "Opening Chrome browser Sir."
        os.system("start chrome")

    elif "mute" in query or "mute volume" in query or "turn off volume" in query or "turn off sound" in query or "silence" in query or "silent mode" in query or "sound off" in query or "volume off" in query or "disable sound" in query or "disable volume" in query or "turn off the sound" in query or "turn off the volume" in query:
        response = "Muted"
        pyautogui.press("volumemute")

    elif "unmute" in query or "unmute volume" in query or "turn on volume" in query or "turn on sound" in query or "enable sound" in query or "enable volume" in query or "sound on" in query or "volume on" in query or "enable sound" in query or "enable volume" in query or "turn on the sound" in query or "turn on the volume" in query:
        response = "Unmuted"
        pyautogui.press("volumemute")

    elif "open discord" in query or "open my discord" in query or "start discord" in query or "open discord app" in query or "open my discord app" in query or "open discord directory" in query or "open my discord directory" in query:
        response = "Opening Discord Sir."
        os.system("start discord")


    elif "open Spotify" in query or "open my Spotify" in query or "start Spotify" in query or "open Spotify app" in query or "open my Spotify app" in query or "open Spotify directory" in query or "open my Spotify directory" in query:
        response = "Opening Spotify Sir."
        os.system("start spotify")

    elif "play music" in query or "play song" in query or "play a song" in query or "play a track" in query or "play a tune" in query or "play some music" in query or "play some songs" in query or "play some tracks" in query or "play some tunes" in query:
        response = "Playing music, Sir."
        sp = SpotifyOAuth(client_id="your_client_id",
                          client_secret="your_client_secret",
                          redirect_uri="http://localhost:8888/callback",
                          scope="user-read-playback-state,user-modify-playback-state")
        sp.start_playback()
        speak("Playing music now.")

    elif "pause music" in query or "pause song" in query or "pause a song" in query or "pause a track" in query or "pause a tune" in query or "pause some music" in query or "pause some songs" in query or "pause some tracks" in query or "pause some tunes" in query:
        response = "Pausing music, Sir."
        sp = SpotifyOAuth(client_id="your_client_id",
                          client_secret="your_client_secret",
                          redirect_uri="http://localhost:8888/callback",
                          scope="user-read-playback-state,user-modify-playback-state")
        sp.pause_playback()
        speak("Music paused.")

    elif "next song" in query or "next track" in query or "next tune" in query or "skip song" in query or "skip track" in query or "skip tune" in query:
        response = "Skipping to the next song, Sir."
        sp = SpotifyOAuth(client_id="your_client_id",
                          client_secret="your_client_secret",
                          redirect_uri="http://localhost:8888/callback",
                          scope="user-read-playback-state,user-modify-playback-state")
        sp.next_track()
        speak("Skipped to the next song.")

    elif "previous song" in query or "previous track" in query or "previous tune" in query or "go back to previous song" in query or "go back to previous track" in query or "go back to previous tune" in query:
        response = "Going back to the previous song, Sir."
        sp = SpotifyOAuth(client_id="your_client_id",
                          client_secret="your_client_secret",
                          redirect_uri="http://localhost:8888/callback",
                          scope="user-read-playback-state,user-modify-playback-state")
        sp.previous_track()
        speak("Went back to the previous song.")

    elif "lower volume" in query or "decrease volume" in query or "volume down"in query or "turn down the volume" in query or "reduce the volume" in query or "quieter" in query or "make it quieter" in query or "make the volume quieter" in query or "turn down volume" in query or "decrease the volume" in query or "lower the volume" in query:
        response = "Lowering the volume."
        pyautogui.press("volumedown")

    elif "say" in query or "speak" in query:
        response = "What do you want me to say?"
        if voice_mode:
            speak(response)
            say = listen_for_command()
        else:
            say = input("Say: ")
        if say:
            x = f"Ok, saying {say}"
            print(x)
            speak(say)
    elif "sleep mode" in query or "sleep" in query or "enter sleep mode" in query or "enter sleep" in query or "go to sleep" in query or "go to sleep mode" in query or "sleep mode on" in query or "sleep on" in query or "go to sleep mode on" in query or "go to sleep on" in query:
        sleep_mode()

    elif "tell me the weather of my location" in query:
        response = "Let me check the weather for you."
        weather_info = get_weather()
        print(weather_info)
        response += " " + weather_info

    elif "close" in query or "bye-bye" in query:
        response = "Goodbye sir."
        if voice_mode:
            speak(response)
        exit()

    elif "open chat mode" in query:
        response = "Switching to chat mode. Please type your commands."
        voice_mode = False

    elif "open voice mode" in query:
        response = "Switching to voice mode. You can speak your commands."
        voice_mode = True

    else:
        response = generate_response(query)
        print(f"Response: {response}")
        

    return response


def run_program():
    """Main loop for the assistant."""

    mic = sr.Microphone()
    recognizer = sr.Recognizer()
    with mic as source:
        recognizer.adjust_for_ambient_noise(source)

    while True:
        # 1. Anahtar kelimeyi (keyword) bekle
        listen_for_keyword(recognizer, mic)

        # 2. Anahtar kelime algılandıysa komut dinleme döngüsüne gir
        while True:
            if voice_mode:
                command = listen_for_command()  # sesli komut al
            else:
                command = input("Send Command to Friday: ")  # yazılı komut al

            if command:
                response = process_query(command)  # komutu işle
                if response:
                    if voice_mode:
                        speak(response)
                # Komut algılandı ve işlendi → tekrar command döngüsüne gir
            else:
                # Komut anlaşılmadıysa → tekrar keyword beklemeye dön
                break


if __name__ == "__main__":
    run_program()
