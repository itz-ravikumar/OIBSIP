import socket
import threading
import sys
import os

HOST = '127.0.0.1'
PORT = 65432

def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                print("\nDisconnected from server.")
                break
                
            if message == 'NAME':
                pass
            else:
                # Clear current line and print message
                # \r moves the cursor to the beginning of the line
                print(f"\r{message}")
                print("You: ", end="", flush=True)
                
        except Exception:
            print("\nConnection closed.")
            break
            
    client_socket.close()
    os._exit(0)

def start_client():
    name = input("Enter your name: ")
    
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client.connect((HOST, PORT))
    except Exception as e:
        print(f"Failed to connect to server: {e}")
        return

    # Receive the first message which should be the NAME request
    try:
        msg = client.recv(1024).decode('utf-8')
        if msg == 'NAME':
            client.send(name.encode('utf-8'))
        else:
            print(msg)
    except Exception as e:
        print(f"Error during initial handshake: {e}")
        client.close()
        return
        
    receive_thread = threading.Thread(target=receive_messages, args=(client,))
    receive_thread.daemon = True
    receive_thread.start()

    print("Connected to chat! Type your messages. Type '/quit' to exit.")
    print("You: ", end="", flush=True)
    try:
        while True:
            message = input()
            if message.lower() == '/quit':
                break
            if message.strip():
                client.send(message.encode('utf-8'))
            print("You: ", end="", flush=True)
    except KeyboardInterrupt:
        pass
    finally:
        client.close()
        print("\nDisconnected.")

if __name__ == "__main__":
    start_client()
