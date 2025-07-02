from discord_webhook import DiscordWebhook
from spotipy.oauth2 import SpotifyOAuth
from translate import Translator
from tkinter import PhotoImage
from io import BytesIO
from sys import exit
from PIL import Image, ImageTk
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
import cv2
import datetime
import platform
import psutil
import socket

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

def listen_for_keyword(keyword="friday"):
    time.sleep(0.4)
    recognizer = sr.Recognizer()
    mic = sr.Microphone()
    print("Listening for keyword...")  # Sadece başlangıçta mesajı yazdır
    while True:
        with mic as source:
            audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio)
            if keyword.lower() in text.lower():
                print(f"Yes sir?")
                speak(f"Yes sir?")
                return
        except sr.UnknownValueError:
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

    mic = sr.Microphone()
    recognizer = sr.Recognizer()
    with mic as source:
        recognizer.adjust_for_ambient_noise(source)
        
    while True:
        listen_for_keyword()  # Program başlatıldığında keyword'u dinle
        if voice_mode:
            command = listen_for_command()  # Komutu sesli olarak dinle
        else:
            command = input("Send Command to Friday: ")  # Komutu yazılı olarak al
        if command:
            response = process_query(command)  # Komutu işle
            if response:
                if voice_mode:
                    speak(response)  # Yanıtı sesli olarak ver

if __name__ == "__main__":
    run_program()