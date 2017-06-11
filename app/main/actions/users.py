from flask_login import current_user, login_user
from flask_socketio import emit, join_room

from werkzeug.security import generate_password_hash, check_password_hash

from app import db, socketio
from app.helpers import generate_user_token, encode_user_token
from app.models.room import Room
from app.models.user import User, Group
from app.schemas.group_schema import SimpleGroupSchema
from app.schemas.room_schema import RoomSchema
from app.schemas.user_schema import UserSchema

schema = UserSchema()
room_schema = RoomSchema()

def _get_user_rooms():
    user = current_user

    if user.role == User.TEACHER:
        rooms = Room.query.filter(Room.teacher_id == user.id).all()
    else:
        rooms = Room.query.filter(Room.groups.any(id=user.group_id)).all()

    emit('receive_user_rooms', {
        'rooms': room_schema.dump(rooms, many=True).data
    })


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
        plain_password=attributes['password'],
        role=User.STUDENT,
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

    if user.group and len(user.group.rooms) > 0:
        for room in user.group.rooms:
            join_room(room.id)

    if not user.is_authenticated:
        emit('failed', {'error': 'User not authorized'})
        return False

    emit('success', {'user': schema.dump(user).data})


def _get_user(attributes):
    return User.query.filter(User.email == attributes['email']).first()


@socketio.on('get_users')
def get_users(attributes):
    users = User.query.all()

    emit('receive_users', {
        'users': schema.dump(users, many=True).data
    })


@socketio.on('get_groups')
def get_groups(attributes):
    groups = Group.query.all()
    groups_schema = SimpleGroupSchema()

    emit('receive_groups', {
        'groups': groups_schema.dump(groups, many=True).data
    })


@socketio.on('update_profile')
def update_user(attributes):
    user = current_user

    user.first_name = attributes['first_name']
    user.last_name = attributes['last_name']
    user.email = attributes['email']
    user.username = attributes['username']

    if 'password' in attributes:
        user.plain_password = attributes['password']

    db.session.commit()


@socketio.on('get_user_rooms')
def get_user_rooms(attributes):
    _get_user_rooms()
