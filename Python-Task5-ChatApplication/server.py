import socket
import threading
import datetime

HOST = '127.0.0.1'
PORT = 65432

# List of clients
clients = []

def get_timestamp():
    return datetime.datetime.now().strftime('%H:%M')

def broadcast(message, sender_conn):
    """Send a message to all connected clients except the sender."""
    for client in clients:
        if client != sender_conn:
            try:
                client.send(message)
            except:
                remove_client(client)

def remove_client(conn):
    if conn in clients:
        clients.remove(conn)

def handle_client(conn, addr):
    print(f"[{get_timestamp()}] [NEW CONNECTION] {addr} connected.")
    
    try:
        # Prompt for username
        conn.send("NAME".encode('utf-8'))
        name = conn.recv(1024).decode('utf-8').strip()
        if not name:
            name = f"User_{addr[1]}"
    except Exception:
        print(f"[{get_timestamp()}] [ERROR] Failed to get name from {addr}")
        remove_client(conn)
        conn.close()
        return

    welcome_msg = f"[{get_timestamp()}] System: {name} joined the chat!"
    print(welcome_msg)
    broadcast(welcome_msg.encode('utf-8'), conn)

    connected = True
    while connected:
        try:
            msg = conn.recv(1024)
            if msg:
                decoded_msg = msg.decode('utf-8').strip()
                if decoded_msg:
                    timestamp = get_timestamp()
                    final_msg = f"[{timestamp}] {name}: {decoded_msg}"
                    print(final_msg)
                    broadcast(final_msg.encode('utf-8'), conn)
            else:
                # Empty message means client disconnected gracefully
                connected = False
        except Exception:
            # Exception means client disconnected ungracefully
            connected = False

    remove_client(conn)
    conn.close()
    
    leave_msg = f"[{get_timestamp()}] System: {name} left the chat!"
    print(leave_msg)
    broadcast(leave_msg.encode('utf-8'), None)
    print(f"[{get_timestamp()}] [DISCONNECTED] {addr} disconnected.")

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Allow port reuse
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
            clients.append(conn)
            thread = threading.Thread(target=handle_client, args=(conn, addr))
            thread.daemon = True 
            thread.start()
        except KeyboardInterrupt:
            print(f"[{get_timestamp()}] Server is shutting down.")
            break
        except Exception as e:
            print(f"[{get_timestamp()}] [ERROR] {e}")
            break

    for client in clients:
        client.close()
    server.close()

if __name__ == "__main__":
    start_server()
