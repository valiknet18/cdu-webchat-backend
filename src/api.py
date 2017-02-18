from . import socketio

from src.actions.users import login, get_current_user, registration
from src.actions.rooms import join_to_room

socketio.on_event('login', login, namespace='/auth')
socketio.on_event('current_user', get_current_user, namespace='/auth')
socketio.on_event('registration', registration, namespace='/auth')

socketio.on_event('join', join_to_room, namespace='/rooms')