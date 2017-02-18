from flask_login import login_user
from src.models.user import User
from flask_socketio import emit
from flask_login import current_user


def login(attributes):
    user = _get_user(attributes)

    if not user:
        emit('failed', {'error': 'Authorization error'}, namespace='/auth')
        return False

    login_user(user)
    emit('success', {'user': user}, namespace='/auth')


def _get_user(attributes):
    return User.query.filter(email=attributes['email'], password=attributes['password']).first()


def get_current_user():
    if not current_user.is_authenticated:
        emit('failed', {'error': 'User not authorized'})
        return False

    emit('success', {'user': current_user})