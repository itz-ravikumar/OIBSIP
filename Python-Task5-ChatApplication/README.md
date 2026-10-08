# 💬 Real-Time Multi-Room Chat Application (Task 5)

This project provides a real-time, bi-directional multi-room chat application. It is implemented using two completely distinct architectures:
1. **Modern Web Application** (Flask, Flask-SocketIO, HTML/CSS/JS)
2. **Desktop Application** (Raw TCP Sockets, Tkinter GUI)

This project was developed as **Task 5** for the OIBSIP Internship.

## ✨ Key Features

### Web Application (`web_app.py`)
- **Responsive Web UI:** Built with HTML5, vanilla CSS3 (Glassmorphism & Dark Mode), and JavaScript.
- **Real-Time WebSockets:** Uses `Flask-SocketIO` to enable sub-second message broadcasting.
- **Multi-Room Isolation:** Connect to distinct rooms via SocketIO namespaces; messages are isolated by room.
- **LAN Connectivity:** Binds to `0.0.0.0:5000`, allowing any device on the local network (Wi-Fi) to connect via the host machine's IP address.
- **Live Notifications:** Broadcasts system messages when users join or leave a room.

### Desktop GUI Application (`server.py` & `client.py`)
- **Raw TCP Sockets:** Custom multithreaded server handling multiple concurrent client connections.
- **Tkinter Interface:** A native desktop GUI for logging in (IP, Name, Room) and chatting.
- **Multi-Room Support:** The TCP server dynamically groups clients into rooms, ensuring messages are only broadcast to users in the same room.
- **Timestamps:** Every message displays exactly when it was sent (e.g., `[14:35] Alice: Hello`).

## 🛠️ Technology Stack

- **Backend / Server:** Python 3.x, Flask, Flask-SocketIO, `socket`, `threading`
- **Frontend (Web):** HTML5, CSS3, Vanilla JavaScript (Socket.IO client)
- **Frontend (Desktop):** Tkinter

## 📂 Project Structure

```text
Python-Task5-ChatApplication/
├── web_app.py              # Flask + SocketIO Web Server
├── server.py               # Raw TCP Socket Server
├── client.py               # Tkinter TCP Desktop Client
├── static/                 
│   ├── script.js           # WebSocket client logic for the Web App
│   └── style.css           # Styling for the Web App
└── templates/              
    └── index.html          # HTML entrypoint for the Web App
```

## 🚀 Installation and Setup

### Prerequisites
- **Python 3.8+** installed on your local machine.

### Install Dependencies
Navigate to the project directory and install the required packages (only needed for the Web App):
```bash
pip install flask flask-socketio
```
*(Note: The TCP Desktop Application uses built-in Python libraries and requires no external dependencies).*

## 🏃 Running the Application Locally

You can choose to run either the Web Application or the Desktop GUI Application.

### Option 1: Run the Web Application (Recommended)

1. Start the Flask-SocketIO server:
   ```bash
   python web_app.py
   ```
2. Open a web browser and navigate to `http://localhost:5000`.
3. Enter your Name and Room, and click "Join Chat".
4. To chat with others on your local network, find your machine's IPv4 address (e.g. `192.168.1.15`) and have them navigate to `http://192.168.1.15:5000`.

### Option 2: Run the Desktop GUI Application (TCP Sockets)

1. Start the raw TCP server:
   ```bash
   python server.py
   ```
   *(The server will listen on `0.0.0.0:65432`)*
2. Start one or more clients:
   ```bash
   python client.py
   ```
3. In the Tkinter GUI, enter the Server IP (use `127.0.0.1` if running locally), your Name, and your desired Room Name. Click "Connect".

## 🚧 Known Limitations & Roadmap
- **Persistence:** Chat messages are currently ephemeral and retained only in memory or the browser DOM. Connecting a lightweight SQLite database to persist room histories is a potential future enhancement.
- **Security:** The raw TCP server does not currently implement SSL/TLS encryption.
