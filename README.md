# 🚀 OIBSIP Python Development Internship Portfolio

![Python Version](https://img.shields.io/badge/Python-3.x-blue.svg)
![Flask](https://img.shields.io/badge/Flask-Web_App-black)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
![Status: Completed](https://img.shields.io/badge/Status-Completed-success)

> A verified portfolio of Python software engineering projects developed during the Oasis Infobyte SIP (OIBSIP) Internship, demonstrating full-stack capabilities ranging from low-level systems integration to real-time WebSockets.

---

## 📖 Overview
This repository contains the complete, implemented source code for three core engineering tasks assigned during the OIBSIP program. The overarching goal of this repository is to demonstrate practical proficiency in Python by solving distinct real-world problems:
1. **Desktop Automation & Speech Recognition** (Task 1)
2. **Cryptographically Secure Entropy Generation** (Task 3)
3. **Real-time Concurrent Networking** (Task 5)

## 🧩 The Projects

### Task 1: Intelligent Voice Assistant
**Problem:** Users need a hands-free way to interact with their operating system, search for information, and automate local utilities without breaking workflow.  
**Solution:** A fully functional, locally-hosted voice assistant that parses natural language audio into actionable system commands.

**Key Features:**
- **System Control:** Lock, sleep, restart, or shutdown the computer via voice commands.
- **Hardware Integration:** Real-time battery status (`psutil`), screen capturing (`pyautogui`), and volume control (`keyboard`).
- **Knowledge Retrieval:** Real-time querying and reading of Wikipedia summaries.
- **Universal App Launcher:** Fuzzy-matching application opening using the `AppOpener` library.

### Task 3: Secure Random Password Generator
**Problem:** Manual password creation often results in predictable patterns, lacking the entropy required to defend against brute-force attacks.  
**Solution:** A command-line utility that programmatically constructs cryptographically secure passwords based on strict user constraints.

**Key Features:**
- **Granular Constraint Enforcement:** Generates passwords between 8 and 128 characters, forcing the inclusion of at least two distinct character types (Uppercase, Lowercase, Digits, Symbols).
- **Guaranteed Entropy:** Instead of purely random generation, the algorithm deterministically picks one character from every requested subset before filling the remaining length, followed by a final shuffle to eliminate pattern predictability.

### Task 5: Real-Time Multi-Room Chat Platform
**Problem:** Multiple users across different devices on a local network need a synchronized platform for parallel discussions without message interference.  
**Solution:** A real-time, bi-directional multi-room chat application deployed as both a raw TCP socket client-server architecture and a modern Flask-based Web Application.

**Key Features:**
- **Web Application:** A responsive, glassmorphism-styled UI built with HTML/CSS/JS, served via a Flask backend.
- **Real-Time WebSockets:** Uses `Flask-SocketIO` to manage persistent connections, enabling sub-second message broadcasting.
- **Multi-Room Isolation:** The server dynamically categorizes connected TCP/WebSocket clients into distinct "rooms", ensuring messages are only broadcast to targeted namespaces.
- **LAN Connectivity:** Binds to `0.0.0.0`, allowing any device on the local network (Wi-Fi) to connect via the host machine's IP address.
- **Legacy GUI & CLI Support:** Also contains `client.py` and `server.py` implementing a Tkinter-based TCP socket variant of the application.

---

## 🏗️ Technical Architecture & Workflow

### Chat Application Data Flow (Task 5)
1. **Connection:** Client navigates to `http://<HOST_IP>:5000`. The browser initiates a WebSocket upgrade request.
2. **Handshake:** Client emits a `join` event with a JSON payload containing `username` and `room`.
3. **State Management:** The Flask-SocketIO server binds the client's session ID to the requested room namespace and broadcasts a system join notification to that specific room.
4. **Message Broadcasting:** Client emits a `message` event. The server intercepts it, injects a server-side timestamp, and emits the payload exclusively to the originating room namespace.

---

## 🛠️ Technology Stack

**Backend & Core Logic:**
- Python 3.x
- Flask & Flask-SocketIO (Web Server & WebSockets)
- `socket`, `threading` (Raw TCP implementation)

**Frontend:**
- HTML5, Vanilla CSS3 (Glassmorphism & Dark Mode)
- JavaScript (Socket.IO client)
- Tkinter (Legacy Desktop GUI)

**Hardware & OS Integration:**
- `speech_recognition`, `pyttsx3` (Audio I/O)
- `pyautogui`, `keyboard`, `psutil` (System automation)

---

## 📂 Project Structure

```text
OIBSIP/
├── Python-Task1-VoiceAssistant/
│   ├── voice_assistant.py      # Core speech-to-intent engine
│   ├── test_assistant.py       # Automated testing script
│   └── commands.json           # [Planned] Custom commands configuration
├── Python-Task3-RandomPasswordGenerator/
│   └── password_generator.py   # CLI entropy generator
├── Python-Task5-ChatApplication/
│   ├── web_app.py              # Flask + SocketIO Server
│   ├── server.py               # Raw TCP Socket Server (Alternative)
│   ├── client.py               # Tkinter TCP Client (Alternative)
│   ├── static/
│   │   ├── script.js           # WebSocket client logic
│   │   └── style.css           # Premium Web UI styling
│   └── templates/
│       └── index.html          # Web App Entrypoint
├── Appreciation Certificate.pdf
└── Completion Certificate.pdf
```

---

## 💻 Installation and Setup

### Prerequisites
- Python 3.8+ installed on your local machine.
- A working microphone (for Task 1).

### 1. Clone the Repository
```bash
git clone https://github.com/itz-ravikumar/OIBSIP.git
cd OIBSIP
```

### 2. Install Dependencies
```bash
# For Task 1 (Voice Assistant)
pip install SpeechRecognition pyttsx3 wikipedia psutil pyautogui keyboard AppOpener pyaudio

# For Task 5 (Web Chat App)
pip install flask flask-socketio
```

---

## 🏃 Running the Projects Locally

### Running the Voice Assistant (Task 1)
```bash
cd Python-Task1-VoiceAssistant
python voice_assistant.py
```
*Wait for the "Listening..." prompt and try saying: "Open Google", "What is Python on Wikipedia", or "Battery".*

### Running the Password Generator (Task 3)
```bash
cd Python-Task3-RandomPasswordGenerator
python password_generator.py
```
*Follow the interactive CLI prompts to define length and character sets.*

### Running the Multi-Room Web Chat (Task 5)
```bash
cd Python-Task5-ChatApplication
python web_app.py
```
1. Open a web browser on your machine and navigate to `http://localhost:5000`.
2. **To invite friends:** Find your computer's local IPv4 address (e.g., `192.168.1.15`) by running `ipconfig` in your terminal. Have anyone on the same Wi-Fi enter `http://192.168.1.15:5000` on their phone or laptop.

---

## 🚧 Known Limitations & Roadmap

- **Task 1 JSON Mapping (Future Work):** The `commands.json` file is currently mocked/unimplemented. Future iterations will dynamically parse this JSON file to allow users to inject custom voice intents without modifying the core Python script.
- **Task 1 Audio Permissions:** `pyaudio` may require specific C++ build tools on Windows or PortAudio on macOS/Linux for microphone access to function correctly.
- **Task 5 Persistence:** Chat messages are currently ephemeral and retained only in the browser DOM. Connecting a lightweight SQLite database to persist room histories is planned for future versions.

---

## 🤝 Contributing
Contributions, issues, and feature requests are welcome! 
1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 👤 Author
**Ravikumar**
- GitHub: [@itz-ravikumar](https://github.com/itz-ravikumar)
