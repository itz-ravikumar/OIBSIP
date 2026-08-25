# Real-Time Chat Application

This is a real-time, bidirectional command-line chat application built in Python using sockets and multithreading. It acts as a local chat room where multiple users can connect, chat, and see timestamps on messages.

This project was developed as **Task 5** for the OIBSIP Internship (Beginner Tier).

## Features

- **Multithreaded Server:** Handles multiple client connections concurrently without blocking.
- **Real-Time Bidirectional Chat:** Clients can send and receive messages at the same time.
- **Timestamps:** Every message displays exactly when it was sent (e.g., `[14:35] Alice: Hello`).
- **Join/Leave Notifications:** The server alerts everyone in the room when a user connects or disconnects gracefully.
- **Custom Usernames:** Pick your name upon connecting.

## Tech Stack

- **Python 3**
- `socket` (for network connections)
- `threading` (to handle simultaneous sending/receiving)
- `datetime` (for formatting message timestamps)

## How to Run

Because this is a server-client architecture, you need to run the server first, and then connect your clients.

### 1. Start the Server
Open a terminal, navigate to this folder, and run:
```bash
python server.py
```
*The server will start listening on `127.0.0.1:65432`.*

### 2. Connect the Clients
Open a **new** terminal window for each user that wants to join the chat and run:
```bash
python client.py
```
You will be prompted to enter your name. After that, you're in the chat room! 

*Note: You must have the server running in the background for the clients to successfully connect.*

### Commands
- Type your message and hit `Enter` to broadcast it to the room.
- Type `/quit` to safely disconnect and exit the application.
