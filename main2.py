from flask import Flask, render_template
from flask_socketio import SocketIO, send

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, async_mode='threading')

@app.route('/')
def index():
    return render_template('index2.html')

@socketio.on('message')
def handleMessage(data):
    sender = data['sender']
    message = data['message']
    print(f'Message from {sender}: {message}')
    send({'sender': sender, 'message': message}, broadcast=True)

if __name__ == '__main__':
    socketio.run(app)
