# 🎙️ Intelligent Voice Assistant

> A voice-controlled assistant built in Python that allows users to perform computer operations through spoken commands.

## 📖 Overview

**Problem:** Performing common computer operations manually can be inconvenient and time-consuming, especially when hands-free interaction is preferred.

**Utility:** A fully functional, locally-hosted voice assistant that allows users to perform computer operations through spoken commands without breaking workflow.

## ✨ Key Utilities

- 🔍 **Search Google and Wikipedia**
- 🌐 **Open applications and websites**
- 🕒 **Check time, date, and battery status**
- 🔊 **Control system volume**
- 📸 **Take screenshots**
- 🔌 **Lock, sleep, restart, and shut down the computer**

## ⚙️ How We Did It

Converted spoken input into text, processed the command using Python, executed the corresponding system/web operation, and returned the result through voice output.

**Workflow:**
`Voice Input` → `Speech Recognition` → `Command Processing` → `Action` → `Voice Response`

## 🛠️ Technologies

- **Python**
- **SpeechRecognition**
- **pyttsx3**
- **AppOpener**
- **Wikipedia**
- **psutil**
- **PyAutoGUI**
- **Keyboard**

## 🔬 Engineering Highlight

**Automated Testing:** Implemented automated testing by replacing microphone input with predefined commands in `test_assistant.py` to seamlessly verify the assistant's functionality without requiring manual voice prompts.

## 🚀 Quick Start

Ensure all dependencies are installed via `pip`:
```bash
pip install SpeechRecognition pyttsx3 wikipedia psutil pyautogui keyboard AppOpener pyaudio
```

Run the assistant:
```bash
python voice_assistant.py
```

Run the automated tests:
```bash
python test_assistant.py
```
