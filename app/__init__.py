from flask_socketio import SocketIO
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_marshmallow import Marshmallow
from flask_login import LoginManager
from app.config import Config

socketio = SocketIO()
db = SQLAlchemy()
login_manager = LoginManager()
ma = Marshmallow()


def create_app():
    app = Flask(__name__)

    config = Config
    app.config.from_object(config)

    config.init_app(app)
    socketio.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    ma.init_app(app)

    from app.main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
