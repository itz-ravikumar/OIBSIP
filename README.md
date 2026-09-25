# Oasis Infobyte Python Programming Internship (OIBSIP)

> A monorepo containing three practical Python applications developed during the Oasis Infobyte Python Programming Internship. The projects demonstrate proficiency in system automation, secure data generation, and multithreaded network programming.

## 📖 Overview

This repository holds my submissions for the Oasis Infobyte Python Programming track. Rather than just meeting the basic requirements, each task has been implemented with robustness, error handling, and a clear architectural separation in mind.

### 🎯 Implemented Tasks

| Task | Project Name | Core Technologies | Focus Area |
| :--- | :--- | :--- | :--- |
| **Task 1** | [Voice Assistant](./Python-Task1-VoiceAssistant) | `speech_recognition`, `pyttsx3`, `os`, `AppOpener` | Speech Processing & OS Automation |
| **Task 3** | [Random Password Generator](./Python-Task3-RandomPasswordGenerator) | `random`, `string` | CLI Interfaces & Data Generation |
| **Task 5** | [Chat Application](./Python-Task5-ChatApplication) | `socket`, `threading` | Network I/O & Concurrency |

---

## 🏗 Project Details

### 1. Voice Assistant (`Task 1`)
A desktop-based voice automation tool tailored for Windows systems. 
- **How it works:** Captures microphone input, transcribed via Google's Web Speech API, and processes intents locally using substring matching. Auditory feedback is generated entirely offline via `pyttsx3`.
- **Key Features:** Natively launches installed applications (via `AppOpener`), executes OS-level power commands (Sleep, Lock, Restart with voice confirmation), fetches Wikipedia summaries, and takes system screenshots natively to the user's Desktop.

### 2. Random Password Generator (`Task 3`)
A robust command-line utility for generating complex passwords based on strict user constraints.
- **How it works:** Enforces a minimum length (8-128 characters) and requires the user to select at least two character classes (Uppercase, Lowercase, Numbers, Symbols).
- **Key Features:** Guarantees inclusion of at least one character from every selected class before randomly filling the remaining length, followed by a cryptographic-style shuffle to prevent predictable patterns. 

### 3. Localhost Chat Application (`Task 5`)
A real-time, terminal-based chat platform demonstrating client-server architecture.
- **How it works:** Operates over IPv4 TCP sockets bound to `127.0.0.1:65432`. The server dispatches incoming connections to dedicated daemon threads to handle concurrent I/O.
- **Key Features:** Real-time broadcasting, connection/disconnection event tracking, injected timestamps, and gracefully handling unexpected client socket termination.

---

## 🚀 Getting Started

### Prerequisites
- **Python 3.x** installed.
- **Windows OS** (Recommended specifically for Task 1's system control commands).

### Installation & Execution

Clone the repository to your local machine:
```bash
git clone https://github.com/yourusername/OIBSIP.git
cd OIBSIP
```

**To run the Voice Assistant:**
```bash
cd Python-Task1-VoiceAssistant
pip install SpeechRecognition pyttsx3 psutil pyautogui keyboard wikipedia AppOpener
python voice_assistant.py
```
*(Ensure a working microphone is connected).*

**To run the Password Generator:**
```bash
cd Python-Task3-RandomPasswordGenerator
python password_generator.py
```

**To run the Chat Application:**
Requires two separate terminal windows.
1. *Terminal 1 (Server):*
   ```bash
   cd Python-Task5-ChatApplication
   python server.py
   ```
2. *Terminal 2 (Client):*
   ```bash
   cd Python-Task5-ChatApplication
   python client.py
   ```

---

## 📂 Repository Structure

```text
OIBSIP/
├── Python-Task1-VoiceAssistant/
│   ├── commands.json           # [TODO] Unimplemented custom commands config
│   ├── voice_assistant.py      # Main voice assistant logic
│   └── test_assistant.py       # Automated testing mock script
├── Python-Task3-RandomPasswordGenerator/
│   └── password_generator.py   # CLI password generator
└── Python-Task5-ChatApplication/
    ├── server.py               # TCP chat server
    └── client.py               # TCP chat client
```
*(Note: Documentation files like `README.md` and media demonstrations `.mp4` are also contained within their respective subdirectories).*

---

## ⚠️ Limitations & Technical Decisions
- **Voice Assistant:** Natural Language Understanding is purely based on string presence (`if "keyword" in command`), rather than intent classification like NLTK/spaCy.
- **Password Generator:** Utilizes the standard `random` module instead of `secrets`. While functionally correct and highly randomized, it is not considered cryptographically secure for highly sensitive production environments.
- **Chat Application:** Currently hardcoded to run on localhost (`127.0.0.1`). To expose to a LAN, the `HOST` variable in `server.py` and `client.py` must be updated to the machine's local IP address.
