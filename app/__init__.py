
from flask_socketio import SocketIO
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_marshmallow import Marshmallow
from app.config import Config
from flask_login import LoginManager


socketio = SocketIO()
db = SQLAlchemy()
ma = Marshmallow()
login_manager = LoginManager()


def create_app():
    app = Flask(__name__)

    config = Config
    app.config.from_object(config)

    config.init_app(app)
    socketio.init_app(app)
    db.init_app(app)
    ma.init_app(app)
    login_manager.init_app(app)

    from app.main import main as main_blueprint
    from app.admin import admin as admin_blueprint

    app.register_blueprint(main_blueprint)
    app.register_blueprint(admin_blueprint)

    return app
