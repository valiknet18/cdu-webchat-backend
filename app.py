from src.config import Config
from src.models import db
from flask import Flask
from src import socketio
from flask_migrate import Migrate
from flask_login import LoginManager

import src.api

app = Flask(__name__)
Config(app)
Migrate(app, db)
login_manager = LoginManager()

if __name__ == '__main__':
    db.init_app(app)
    socketio.init_app(app)
    login_manager.init_app(app)
    socketio.run(app)