import socket
import threading
import datetime

HOST = '0.0.0.0'
PORT = 65432

# Dictionary mapping room names to a list of client connections
rooms = {}
# Dictionary keeping track of which room a client is in
client_rooms = {}

def get_timestamp():
    return datetime.datetime.now().strftime('%H:%M')

def broadcast(message, sender_conn, room_name):
    """Send a message to all connected clients in the room except the sender."""
    if room_name in rooms:
        for client in list(rooms[room_name]):
            if client != sender_conn:
                try:
                    client.send(message)
                except:
                    remove_client(client)

def remove_client(conn):
    if conn in client_rooms:
        room = client_rooms[conn]
        if room in rooms and conn in rooms[room]:
            rooms[room].remove(conn)
            # Optional: Clean up empty rooms
            if not rooms[room]:
                del rooms[room]
        del client_rooms[conn]

def handle_client(conn, addr):
    print(f"[{get_timestamp()}] [NEW CONNECTION] {addr} connected.")
    
    try:
        # Prompt for username
        conn.send("NAME".encode('utf-8'))
        name = conn.recv(1024).decode('utf-8').strip()
        if not name:
            name = f"User_{addr[1]}"
            
        # Prompt for room
        conn.send("ROOM".encode('utf-8'))
        room_name = conn.recv(1024).decode('utf-8').strip()
        if not room_name:
            room_name = "General"
            
    except Exception:
        print(f"[{get_timestamp()}] [ERROR] Failed to get name/room from {addr}")
        remove_client(conn)
        conn.close()
        return

    # Add to room
    if room_name not in rooms:
        rooms[room_name] = []
    rooms[room_name].append(conn)
    client_rooms[conn] = room_name

    welcome_msg = f"[{get_timestamp()}] System: {name} joined the room '{room_name}'!"
    print(welcome_msg)
    broadcast(welcome_msg.encode('utf-8'), conn, room_name)

    connected = True
    while connected:
        try:
            msg = conn.recv(1024)
            if msg:
                decoded_msg = msg.decode('utf-8').strip()
                if decoded_msg:
                    timestamp = get_timestamp()
                    final_msg = f"[{timestamp}] {name}: {decoded_msg}"
                    print(f"[Room: {room_name}] {final_msg}")
                    broadcast(final_msg.encode('utf-8'), conn, room_name)
            else:
                connected = False
        except Exception:
            connected = False

    remove_client(conn)
    conn.close()
    
    leave_msg = f"[{get_timestamp()}] System: {name} left the room '{room_name}'!"
    print(leave_msg)
    broadcast(leave_msg.encode('utf-8'), None, room_name)
    print(f"[{get_timestamp()}] [DISCONNECTED] {addr} disconnected.")

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    try:
        server.bind((HOST, PORT))
    except Exception as e:
        print(f"Failed to bind to {HOST}:{PORT} - {e}")
        return
        
    server.listen()
    print(f"[{get_timestamp()}] [LISTENING] Server is listening on {HOST}:{PORT}")
    
    while True:
        try:
            conn, addr = server.accept()
            thread = threading.Thread(target=handle_client, args=(conn, addr))
            thread.daemon = True 
            thread.start()
        except KeyboardInterrupt:
            print(f"[{get_timestamp()}] Server is shutting down.")
            break
        except Exception as e:
            print(f"[{get_timestamp()}] [ERROR] {e}")
            break

    for conn in list(client_rooms.keys()):
        conn.close()
    server.close()

if __name__ == "__main__":
    start_server()
