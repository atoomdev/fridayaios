import os
import time
import openai
import speech_recognition as sr

from speech import speak, listen_for_keyword, listen_for_command
import commands



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



def run_program():
    """Main loop for the assistant."""

    mic = sr.Microphone()
    recognizer = sr.Recognizer()
    with mic as source:
        recognizer.adjust_for_ambient_noise(source)

    while True:
        # Program starts by listening for the activation keyword
        listen_for_keyword(recognizer, mic)
        if commands.voice_mode:
            command = listen_for_command()  # Komutu sesli olarak dinle
        else:
            command = input("Send Command to Friday: ")  # Komutu yazılı olarak al
        if command:
            response = commands.process_query(command)  # Komutu işle
            if response and commands.voice_mode:
                speak(response)  # Yanıtı sesli olarak ver

if __name__ == "__main__":
    run_program()

