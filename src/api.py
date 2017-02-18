from . import socketio

from src.actions.users import login, get_current_user

socketio.on_event('login', login, namespace='/auth')
socketio.on_event('current_user', get_current_user, namespace='/auth')

