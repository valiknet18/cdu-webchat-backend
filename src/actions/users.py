from flask_login import login_user
from src.models.user import User
from flask_socketio import emit
from flask_login import current_user
from src.models import db
from werkzeug.security import generate_password_hash, check_password_hash
from . import login_manager


def login(attributes):
    attributes = attributes['user']

    user = _get_user(attributes)

    if not user or not check_password_hash(user.password, attributes['password']):
        emit('login_failed', {'error': 'Authorization error'}, namespace='/auth')
        return False

    if login_user(user, True):
        emit('login_success', {'user': user.first_name}, namespace='/auth')
    else:
        emit('login_failed', {'error': 'User not authorized'}, namespace='/auth')

def _get_user(attributes):
    return User.query.filter(User.email == attributes['email']).first()


def registration(attributes):
    attributes = attributes['user']

    user = User(
        first_name=attributes['first_name'],
        last_name=attributes['last_name'],
        email=attributes['email'],
        username=attributes['username'],
        password=generate_password_hash(attributes['password']),
        role='student'
    )

    try:
        db.session.add(user)
        db.session.commit()

        emit('registration_success', {
            'user': user.first_name
        }, namespace='/auth')
    except Exception as e:
        emit('registration_failed', {
            'error': str(e)
        }, namespace='/auth')

def get_current_user(attributes):
    user = current_user

    if not user.is_authenticated:
        emit('failed', {'error': 'User not authorized'}, namespace='/auth')
        return False

    emit('success', {'user': user.first_name}, namespace='/auth')

@login_manager.user_loader
def user_load(user_id):
    return User.query.get(int(user_id))

