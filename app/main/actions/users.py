from flask_login import current_user, login_user
from flask_socketio import emit, join_room

from werkzeug.security import generate_password_hash, check_password_hash

from app import db, socketio
from app.helpers import generate_user_token, encode_user_token
from app.models.user import User
from app.schemas.user_schema import UserSchema

schema = UserSchema()


@socketio.on('login')
def login(attributes):
    attributes = attributes['user']

    user = _get_user(attributes)

    if not user or not check_password_hash(user.password, attributes['password']):
        emit('login_failed', {'error': 'Authorization error'})
        return False

    if login_user(user, True):
        token = generate_user_token()

        User.query.filter_by(id=user.id).update({'token': token})
        db.session.commit()

        emit('login_success', {
            'user': schema.dump(user).data,
            'token': encode_user_token(token).decode('ascii')
        })
    else:
        emit('login_failed', {'error': 'User not authorized'})


@socketio.on('registration')
def registration(attributes):
    attributes = attributes['user']
    token = generate_user_token()

    user = User(
        first_name=attributes['first_name'],
        last_name=attributes['last_name'],
        email=attributes['email'],
        username=attributes['username'],
        password=generate_password_hash(attributes['password']),
        role='student',
        token=token
    )

    try:
        db.session.add(user)
        db.session.commit()

        login_user(user)

        emit('registration_success', {
            'user': schema.dump(user).data,
            'token': encode_user_token(token).decode('ascii')
        })
    except Exception as e:
        emit('registration_failed', {
            'error': str(e)
        })


@socketio.on('current_user')
def get_current_user(attributes):
    user = current_user

    for room in user.rooms:
        join_room(room.id)

    if not user.is_authenticated:
        emit('failed', {'error': 'User not authorized'})
        return False

    emit('success', {'user': schema.dump(user).data})


def _get_user(attributes):
    return User.query.filter(User.email == attributes['email']).first()