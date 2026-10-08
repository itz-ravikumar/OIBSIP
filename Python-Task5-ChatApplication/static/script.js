const socket = io();

// DOM Elements
const loginContainer = document.getElementById('login-container');
const chatContainer = document.getElementById('chat-container');
const usernameInput = document.getElementById('username');
const roomInput = document.getElementById('room');
const joinBtn = document.getElementById('join-btn');
const roomNameDisplay = document.getElementById('room-name-display');
const messagesDiv = document.getElementById('messages');
const msgInput = document.getElementById('msg-input');
const sendBtn = document.getElementById('send-btn');
const leaveBtn = document.getElementById('leave-btn');

let currentUsername = '';
let currentRoom = '';

// Event Listeners
joinBtn.addEventListener('click', joinRoom);
sendBtn.addEventListener('click', sendMessage);
leaveBtn.addEventListener('click', leaveRoom);
msgInput.addEventListener('keypress', (e) => {
    if (e.key === 'Enter') sendMessage();
});

function joinRoom() {
    const username = usernameInput.value.trim();
    const room = roomInput.value.trim();

    if (!username || !room) {
        alert("Please enter both Name and Room!");
        return;
    }

    currentUsername = username;
    currentRoom = room;

    socket.emit('join', { username, room });

    // Switch UI
    loginContainer.classList.add('hidden');
    chatContainer.classList.remove('hidden');
    roomNameDisplay.innerText = `Room: ${room}`;
    messagesDiv.innerHTML = ''; // clear old msgs
}

function leaveRoom() {
    socket.emit('leave', { username: currentUsername, room: currentRoom });
    
    // Switch UI
    chatContainer.classList.add('hidden');
    loginContainer.classList.remove('hidden');
}

function sendMessage() {
    const msg = msgInput.value.trim();
    if (!msg) return;

    socket.emit('message', { username: currentUsername, room: currentRoom, msg });
    msgInput.value = '';
}

// Socket Event Handlers
socket.on('status', (data) => {
    const div = document.createElement('div');
    div.classList.add('status-msg');
    div.innerText = `[${data.time}] ${data.msg}`;
    messagesDiv.appendChild(div);
    scrollToBottom();
});

socket.on('message', (data) => {
    const isOwn = data.username === currentUsername;
    
    const wrapper = document.createElement('div');
    wrapper.classList.add('msg-wrapper');
    wrapper.classList.add(isOwn ? 'own' : 'other');

    const bubble = document.createElement('div');
    bubble.classList.add('msg-bubble');
    bubble.innerText = data.msg;

    const info = document.createElement('div');
    info.classList.add('msg-info');
    if (!isOwn) {
        info.innerHTML = `<span>${data.username}</span> &bull; <span>${data.time}</span>`;
    } else {
        info.innerHTML = `<span>${data.time}</span>`;
    }

    wrapper.appendChild(bubble);
    wrapper.appendChild(info);
    messagesDiv.appendChild(wrapper);
    scrollToBottom();
});

function scrollToBottom() {
    messagesDiv.scrollTop = messagesDiv.scrollHeight;
}
