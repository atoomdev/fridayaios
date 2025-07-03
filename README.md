# 💡 Friday AI OS

**Friday AI Assistant** is a powerful, modular, and lightweight AI assistant written in Python. It supports both voice and text interaction, integrates with LLM and DALL·E, provides real-time weather data, sends emails, logs IP information, and more. Designed to run efficiently even on modest systems, it serves as a fully interactive, customizable AI companion.

---

## 🚀 Features

* 🎤 Voice recognition (multi-language support)
* 🔊 Text-to-Speech using `pyttsx3`
* 📬 Send emails via Gmail SMTP
* 🌦️ Real-time weather info using WeatherAPI
* 🧠 Natural responses via OpenAI GPT-3.5
* 🎨 Image generation via DALL·E 3
* 🕵️ IP logger with email report and GUI display
* 🪿 Tkinter GUI for result display
* 🌐 Chat and Voice modes with easy switching
* 🔐 Secure IP logger access with password

---

## 📆 Dependencies

Install required packages:

```bash
pip install openai speechrecognition pyttsx3 pillow requests spotipy discord-webhook translate opencv-python psutil python-dotenv
```

> `tkinter`, `smtplib`, `sys`, and `os` are included in most standard Python installations.

## 🔧 Setup

Create a `.env` file in the project root and define the following variables:

```bash
OPENAI_API_KEY=your-openai-key
GMAIL_PASSWORD=your-gmail-app-password
WEATHERAPI_KEY=your-weatherapi-key
```

---

## 🧠 Technologies Used

| Library                                   | Purpose                        |
| ----------------------------------------- | ------------------------------ |
| `ollama`                                  | LLM and DALL·E integration     |
| `speech_recognition`                      | Voice command recognition      |
| `pyttsx3`                                 | Offline TTS engine             |
| `tkinter` + `PIL`                         | GUI and image rendering        |
| `requests` + `json`                       | API and HTTP communication     |
| `cv2`                                     | OpenCV (for vision extensions) |
| `smtplib`                                 | Email sending via SMTP         |
| `spotipy`, `discord_webhook`, `translate` | Extra integrations             |
| `psutil`, `platform`, `socket`            | System and network info        |

---

## ⚙️ Usage

Run the script using Python. A simple Tkinter window will open showing an animated face, the last recognized command and the assistant's response. Use the **Start** and **Stop** buttons to control listening.

```bash
python friday.py
```

Once launched, say the **keyword** "friday" to activate the assistant. You can switch to **text mode** by saying "open chat mode" or back to voice with "open voice mode".

---

## 💬 Sample Commands

| Command                              | Behavior                            |
| ------------------------------------ | ----------------------------------- |
| `Friday`                             | Wake the assistant                  |
| `send email`                         | Starts email sending flow           |
| `imagine`                            | Generates an image with DALL·E 3    |
| `enable` (password: `12123112`)      | IP logger activation and GUI report |
| `say Hello`                          | Repeats your message aloud          |
| `tell me the weather of my location` | Reports current weather for Ankara  |
| `open chat mode` / `open voice mode` | Toggle between input modes          |
| `close` or `bye-bye`                 | Terminates the program              |

---

## 📁 Project Structure

All logic is contained in a single `.py` file for simplicity. You are encouraged to modularize it into files like `listener.py`, `tts.py`, `commands.py` for scalability.

---

## 💪 TODO (Roadmap)

* [ ] Integrate OpenAI's Text-to-Speech (TTS) for more natural voices
* [ ] Add object detection via YOLO or segmentation model
* [ ] Persistent conversation memory & context tracking
* [ ] Emotion detection and voice tone adaptation

---

## 🔐 Security Notice

This is a **demo project**. Do **not** use real passwords or sensitive API keys in production environments. Always move credentials to `.env` files or encrypted secrets.

---

## 👨‍💻 Developer

**Ateş Altınkaynak**
Developed by Cage Development - Sapienties Group

---

## 📜 License

This project is licensed under the MIT License.

---

> ⚡ *A lightweight, customizable voice assistant designed for real-world interaction and daily automation.*
