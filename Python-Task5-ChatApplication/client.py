import socket
import threading
import tkinter as tk
from tkinter import messagebox
import os

PORT = 65432

class ChatClientUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Real-Time Chat Application")
        self.root.geometry("400x500")
        
        self.client_socket = None
        self.connected = False
        
        self.setup_login_screen()
        
    def setup_login_screen(self):
        self.login_frame = tk.Frame(self.root, pady=20)
        self.login_frame.pack(fill=tk.BOTH, expand=True)
        
        tk.Label(self.login_frame, text="Join Chat", font=("Helvetica", 16, "bold")).pack(pady=10)
        
        tk.Label(self.login_frame, text="Server IP:").pack()
        self.ip_entry = tk.Entry(self.login_frame)
        self.ip_entry.insert(0, "127.0.0.1")
        self.ip_entry.pack(pady=5)
        
        tk.Label(self.login_frame, text="Your Name:").pack()
        self.name_entry = tk.Entry(self.login_frame)
        self.name_entry.pack(pady=5)
        
        tk.Label(self.login_frame, text="Room Name:").pack()
        self.room_entry = tk.Entry(self.login_frame)
        self.room_entry.pack(pady=5)
        
        self.connect_btn = tk.Button(self.login_frame, text="Connect", command=self.connect_to_server, bg="#4CAF50", fg="white", width=15)
        self.connect_btn.pack(pady=20)
        
    def setup_chat_screen(self, room):
        self.login_frame.destroy()
        
        self.root.title(f"Room: {room}")
        
        self.chat_frame = tk.Frame(self.root)
        self.chat_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Scrollbar and Text area
        scrollbar = tk.Scrollbar(self.chat_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.chat_area = tk.Text(self.chat_frame, yscrollcommand=scrollbar.set, state='disabled', wrap=tk.WORD, bg="#f5f5f5")
        self.chat_area.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        scrollbar.config(command=self.chat_area.yview)
        
        # Input area
        self.input_frame = tk.Frame(self.chat_frame, pady=5)
        self.input_frame.pack(fill=tk.X, side=tk.BOTTOM)
        
        self.msg_entry = tk.Entry(self.input_frame)
        self.msg_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 5))
        self.msg_entry.bind("<Return>", self.send_message)
        
        self.send_btn = tk.Button(self.input_frame, text="Send", command=self.send_message, bg="#2196F3", fg="white", width=8)
        self.send_btn.pack(side=tk.RIGHT)
        
    def connect_to_server(self):
        ip = self.ip_entry.get().strip()
        name = self.name_entry.get().strip()
        room = self.room_entry.get().strip()
        
        if not ip or not name or not room:
            messagebox.showwarning("Input Error", "Please fill out all fields.")
            return
            
        try:
            self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.client_socket.connect((ip, PORT))
            
            # Handshake
            msg = self.client_socket.recv(1024).decode('utf-8')
            if msg == 'NAME':
                self.client_socket.send(name.encode('utf-8'))
                msg = self.client_socket.recv(1024).decode('utf-8')
                if msg == 'ROOM':
                    self.client_socket.send(room.encode('utf-8'))
                    
            self.connected = True
            self.setup_chat_screen(room)
            
            receive_thread = threading.Thread(target=self.receive_messages)
            receive_thread.daemon = True
            receive_thread.start()
            
        except Exception as e:
            messagebox.showerror("Connection Error", f"Failed to connect to server:\n{e}")
            if self.client_socket:
                self.client_socket.close()

    def receive_messages(self):
        while self.connected:
            try:
                message = self.client_socket.recv(1024).decode('utf-8')
                if not message:
                    break
                # Only insert the 'message' logic, don't ignore NAME/ROOM if they accidentally show up
                if message == 'NAME' or message == 'ROOM':
                    pass
                else:
                    self.append_message(message)
            except Exception:
                break
        
        self.append_message("\nDisconnected from server.")
        self.connected = False
        if self.client_socket:
            self.client_socket.close()
            
    def send_message(self, event=None):
        if not self.connected:
            return
        
        message = self.msg_entry.get().strip()
        if message:
            try:
                self.client_socket.send(message.encode('utf-8'))
                self.append_message(f"You: {message}")
                self.msg_entry.delete(0, tk.END)
            except Exception as e:
                self.append_message("Failed to send message.")
                
    def append_message(self, message):
        self.chat_area.config(state='normal')
        self.chat_area.insert(tk.END, message + "\n")
        self.chat_area.see(tk.END)
        self.chat_area.config(state='disabled')
        
    def on_closing(self):
        self.connected = False
        if self.client_socket:
            try:
                self.client_socket.close()
            except:
                pass
        self.root.destroy()
        os._exit(0)

if __name__ == "__main__":
    root = tk.Tk()
    app = ChatClientUI(root)
    root.protocol("WM_DELETE_WINDOW", app.on_closing)
    root.mainloop()
