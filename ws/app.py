#!/bin/python

from flask import Flask, render_template
from flask_socketio import SocketIO, emit

from conn import QueueClient

app = Flask(__name__)
app.config['SECRET_KEY'] = '%}\xc0\xb5\xc9\xfd\xa8t\xed\x1a&\\\x9e\xfde3\xe4\xb88\xa0:\xb7\xe0\xd9'

ws = SocketIO(app)

client = QueueClient()

@app.route('/')
def index():
    return render_template('index.html')

def process(data):
    return client.process(data)

@ws.on('add_to_queue', '/ws')
def add(recieved):
    emit('processed', {'data': process(recieved['data'])})
    pass

if __name__ == "__main__":
    ws.run(app)
    pass

