from sqlalchemy import subquery

from app.models.message import Message
from app.models import room, message
from app import db
from datetime import datetime

from flask_socketio import emit, join_room
from flask_login import current_user

from app.models.user import User
from app.schemas.room_schema import RoomSchema, RoomSchemaWithMessages
from app import socketio
from app.models.room import Room

schema = RoomSchema()
schema_with_messages = RoomSchemaWithMessages()


@socketio.on('join_to_room')
def join_to_room(attributes):
    room_id = attributes['id']

    room = Room.query.get(room_id)

    user = current_user
    user.rooms.append(room)
    user.last_selected_room = room_id

    db.session.commit()

    emit('successful_joined_to_room', {
        'room': schema_with_messages.dump(room).data
    })


@socketio.on('leave_from_room')
def leave_from_room(attributes):
    room_id = attributes['id']

    user = current_user
    user.rooms.remove(room_id)
    user.last_selected_room = None

    db.session.commit()

    emit('successful_leaved_from_room')


@socketio.on('select_room')
def select_room(attributes):
    room_id = attributes['id']
    user = current_user

    room = Room.query.get(room_id)
    user.last_selected_room = room_id
    db.session.commit()

    join_room(room_id)

    emit('successful_selected_room', {
        'room': schema_with_messages.dump(room).data
    })


@socketio.on('get_room_messages')
def get_last_room_messages(attributes):
    room_id = attributes['id']
    room = Room.query.get(room_id)


@socketio.on('send_message_to_room')
def send_room_messages(attributes):
    room_id = attributes['id']
    message_content = attributes['message']
    user = current_user

    message = Message(
        msg=message_content,
        created_at=datetime.now(),
        author_id=user.id,
        room_id=room_id
    )

    db.session.add(message)
    db.session.commit()

    room = Room.query.get(room_id)

    emit('receive_messages', {
        'room': schema_with_messages.dump(room).data
    }, room=room.id)


@socketio.on('create_room')
def create_room(attributes):
    attributes = attributes['room']
    user = current_user

    room = Room(
        name=attributes['name'],
        created_by=user.id,
        created_at=datetime.now()
    )

    try:
        db.session.add(room)
        db.session.commit()

        emit('successful room creating', {
            'room': schema.dump(room).data
        })
    except Exception as e:
        emit('failed room creating', {
            'error': str(e)
        })


@socketio.on('get_rooms')
def get_rooms(attributes):
    rooms = Room.query.all()

    emit('receive_rooms', {
        'rooms': schema.dump(rooms, many=True).data
    })


@socketio.on('search_rooms')
def search_rooms(attributes):
    pass


@socketio.on('invite_users')
def invite_users(attributes):
    users = []

    for user_id in attributes['users']:
        users.append(User.query.get(user_id))

    room = Room.query.get(attributes['room'])
    room.members = users

    db.session.commit()
