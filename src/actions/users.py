from flask_login import login_user
from src.models.user import User
from flask_socketio import emit
from flask_login import current_user
from src.models import db
from werkzeug.security import generate_password_hash, check_password_hash
from src.helpers import generate_user_token, encode_user_token
from flask import request, jsonify
from src.schemas.user_schema import UserSchema

def login(attributes):
    attributes = attributes['user']

    user = _get_user(attributes)

    if not user or not check_password_hash(user.password, attributes['password']):
        emit('login_failed', {'error': 'Authorization error'})
        return False

    if login_user(user, True):
        token = generate_user_token()

        User.query.filter_by(id=user.id).update({'token': token})

        emit('login_success', {'user': user.first_name, 'token': encode_user_token(token).decode('ascii')})
    else:
        emit('login_failed', {'error': 'User not authorized'})


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

        emit('registration_success', {
            'user': user.first_name
        })
    except Exception as e:
        emit('registration_failed', {
            'error': str(e)
        })


def get_current_user(attributes):
    user = current_user

    if not user.is_authenticated:
        emit('failed', {'error': 'User not authorized'})
        return False

    schema = UserSchema()
    emit('success', {'user': schema.dump(user).data})


def _get_user(attributes):
    return User.query.filter(User.email == attributes['email']).first()
