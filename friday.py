from discord_webhook import DiscordWebhook
from spotipy.oauth2 import SpotifyOAuth
from translate import Translator
from tkinter import PhotoImage
from io import BytesIO
from sys import exit
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


openai.api_key = 'sk-proj-EE0umSWxMEOFEu9ooOGnT3BlbkFJs4WUmcMl9ugRcfL0m7i3'

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
        speak("Sorry, I did not understand that.")
        return None
    except sr.RequestError as e:
        print(f"Could not request results; {e}")
        speak(f"Could not request results; {e}")
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
    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "mistral",
                "prompt": f"You are Friday OS, a highly intelligent local AI agent with FULL Windows OS access. Give a short and clear answer in 1-2 sentences.\n\nUser: {prompt}\n\nResponse:",
                "stream": False
            }
        )
        result = response.json()
        return result.get("response", "").strip()
    except Exception as e:
        return str(e)


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

# Başlangıçta sesli moda geçiş yapalım
voice_mode = True


def greet():
    return "Hello sir! How can I assist you today?"


def send_email_handler():
    global voice_mode
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
            return "Email sent successfully."
        else:
            return "Sorry, I didn't catch the message. Please try again later."
    else:
        return "Sorry, I didn't catch the subject. Please try again later."


def enable_handler():
    password = input("Password: ")
    if password == "12123112":
        enable_ip_logger()
        return "Complete"
    return ""


def open_desktop():
    os.startfile("C:\\Users\\atesa\\Desktop")
    return "Opening Desktop folder Sir."


def open_wifi_settings():
    os.system("start ms-settings:network-wifi")
    return "Opening Wi-Fi settings, Sir."


def open_bluetooth_settings():
    os.system("start ms-settings:bluetooth")
    return "Opening Bluetooth settings, Sir."


def open_control_panel():
    os.system("start control")
    return "Opening Control Panel, Sir."


def open_task_manager():
    os.system("start taskmgr")
    return "Opening Task Manager, Sir."


def open_file_explorer():
    os.startfile("C:\\")
    return "Opening File Explorer, Sir."


def open_command_prompt():
    os.system("start cmd")
    return "Opening Command Prompt, Sir."


def open_settings_app():
    os.system("start ms-settings:")
    return "Opening Settings, Sir."


def open_calculator():
    os.system("start calc")
    return "Opening Calculator, Sir."


def open_paint():
    os.system("start mspaint")
    return "Opening Paint, Sir."


def open_word():
    os.system("start winword")
    return "Opening Word, Sir."


def open_excel():
    os.system("start excel")
    return "Opening Excel, Sir."


def open_powerpoint():
    os.system("start powerpnt")
    return "Opening PowerPoint, Sir."


def open_notepad():
    os.system("start notepad")
    return "Opening Notepad, Sir."


def open_downloads():
    os.startfile("C:\\Users\\atesa\\Downloads")
    return "Opening Downloads folder Sir."


def open_chrome():
    os.system("start chrome")
    return "Opening Chrome browser Sir."


def mute_volume():
    pyautogui.press("volumemute")
    return "Muted"


def unmute_volume():
    pyautogui.press("volumemute")
    return "Unmuted"


def volume_up():
    pyautogui.press("volumeup")
    return ""


def open_discord():
    os.system("start discord")
    return "Opening Discord, Sir."


def open_spotify():
    os.system("start spotify")
    return "Opening Spotify, Sir."


def play_music():
    sp = SpotifyOAuth(client_id="your_client_id",
                      client_secret="your_client_secret",
                      redirect_uri="http://localhost:8888/callback",
                      scope="user-read-playback-state,user-modify-playback-state")
    sp.start_playback()
    speak("Playing music now.")
    return "Playing music, Sir."


def pause_music():
    sp = SpotifyOAuth(client_id="your_client_id",
                      client_secret="your_client_secret",
                      redirect_uri="http://localhost:8888/callback",
                      scope="user-read-playback-state,user-modify-playback-state")
    sp.pause_playback()
    speak("Music paused.")
    return "Pausing music, Sir."


def next_song():
    sp = SpotifyOAuth(client_id="your_client_id",
                      client_secret="your_client_secret",
                      redirect_uri="http://localhost:8888/callback",
                      scope="user-read-playback-state,user-modify-playback-state")
    sp.next_track()
    speak("Skipped to the next song.")
    return "Skipping to the next song, Sir."


def previous_song():
    sp = SpotifyOAuth(client_id="your_client_id",
                      client_secret="your_client_secret",
                      redirect_uri="http://localhost:8888/callback",
                      scope="user-read-playback-state,user-modify-playback-state")
    sp.previous_track()
    speak("Went back to the previous song.")
    return "Going back to the previous song, Sir."


def lower_volume():
    pyautogui.press("volumedown")
    return "Lowering the volume."


def say_phrase():
    global voice_mode
    response = "What do you want me to say?"
    if voice_mode:
        speak(response)
        phrase = listen_for_command()
    else:
        phrase = input("Say: ")
    if phrase:
        print(f"Ok, saying {phrase}")
        speak(phrase)
        return f"Ok, saying {phrase}"
    return ""


def imagine():
    global voice_mode
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
    return ""


def sleep_mode_handler():
    sleep_mode()
    return ""


def tell_weather():
    weather_info = get_weather()
    print(weather_info)
    return "Let me check the weather for you. " + weather_info


def close_program():
    global voice_mode
    if voice_mode:
        speak("Goodbye sir.")
    exit()


def open_chat_mode():
    global voice_mode
    voice_mode = False
    return "Switching to chat mode. Please type your commands."


def open_voice_mode():
    global voice_mode
    voice_mode = True
    return "Switching to voice mode. You can speak your commands."


COMMAND_HANDLERS = {
    ("hello", "hi", "hey", "greetings"): greet,
    ("send email",): send_email_handler,
    ("enable",): enable_handler,
    ("open desktop",): open_desktop,
    ("open wifi settings",): open_wifi_settings,
    ("open bluetooth settings",): open_bluetooth_settings,
    ("open control panel",): open_control_panel,
    ("open task manager",): open_task_manager,
    ("open file explorer",): open_file_explorer,
    ("open command prompt",): open_command_prompt,
    ("open settings",): open_settings_app,
    ("open calculator",): open_calculator,
    ("open paint",): open_paint,
    ("open word",): open_word,
    ("open excel",): open_excel,
    ("open powerpoint",): open_powerpoint,
    ("open notepad",): open_notepad,
    ("open downloads", "open download folder"): open_downloads,
    ("open google", "open chrome", "open browser"): open_chrome,
    ("mute",): mute_volume,
    ("unmute",): unmute_volume,
    ("volume up",): volume_up,
    ("open discord",): open_discord,
    ("open spotify",): open_spotify,
    ("play music",): play_music,
    ("pause music",): pause_music,
    ("next song",): next_song,
    ("previous song",): previous_song,
    ("lower volume",): lower_volume,
    ("say", "speak"): say_phrase,
    ("sleep mode", "sleep"): sleep_mode_handler,
    ("tell me the weather of my location",): tell_weather,
    ("close", "bye-bye"): close_program,
    ("open chat mode",): open_chat_mode,
    ("open voice mode",): open_voice_mode,
    ("imagine",): imagine,
}


def process_query(query):
    global voice_mode
    query = query.lower()
    for phrases, handler in COMMAND_HANDLERS.items():
        if any(p in query for p in (phrases if isinstance(phrases, (list, tuple, set)) else [phrases])):
            return handler()

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
        # Program starts by listening for the activation keyword
        listen_for_keyword(recognizer, mic)
        if voice_mode:
            command = listen_for_command()  # Komutu sesli olarak dinle
        else:
            command = input("Send Command to Friday: ")  # Komutu yazılı olarak al
        if command:
            response = process_query(command)  # Komutu işle
            if response and voice_mode:
                speak(response)  # Yanıtı sesli olarak ver

if __name__ == "__main__":
    run_program()
