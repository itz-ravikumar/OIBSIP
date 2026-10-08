from flask import Flask, render_template, request
from flask_socketio import SocketIO, join_room, leave_room, send, emit
import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, cors_allowed_origins="*")

def get_timestamp():
    return datetime.datetime.now().strftime('%H:%M')

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('join')
def on_join(data):
    username = data['username']
    room = data['room']
    join_room(room)
    msg = f"{username} has joined the room."
    emit('status', {'msg': msg, 'time': get_timestamp()}, to=room)

@socketio.on('leave')
def on_leave(data):
    username = data['username']
    room = data['room']
    leave_room(room)
    msg = f"{username} has left the room."
    emit('status', {'msg': msg, 'time': get_timestamp()}, to=room)

@socketio.on('message')
def on_message(data):
    username = data['username']
    room = data['room']
    msg = data['msg']
    emit('message', {'username': username, 'msg': msg, 'time': get_timestamp()}, to=room)

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000, debug=True)
