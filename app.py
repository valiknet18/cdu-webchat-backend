from src.config import Config
from src.models import db
from flask import Flask
from src import socketio

import src.api

app = Flask(__name__)
Config(app)

if __name__ == '__main__':
    db.init_app(app)
    socketio.init_app(app)
    socketio.run(app)