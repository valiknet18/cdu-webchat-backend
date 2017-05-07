from flask_socketio import emit

from app import socketio, db
from flask_login import current_user

from app.models.event import Event
from app.models.room import Room
from app.models.user import Group
from app.schemas.event_schema import EventSchema

schema = EventSchema()


@socketio.on('get_events')
def get_events():
    user = current_user
    events = Room.query.filter(Room.groups.any(id=user.group_id)).filter(Room.role == Room.CONSULTATION).all()

    emit('receive_events', {
        'events': schema.dump(events).data
    })


@socketio.on('create_event')
def create_event(attributes):

    room = Room(
        name=attributes['name'],
        created_by=current_user,
        teacher=current_user
    )

    event = Event(
        name=attributes['name'],
        teacher=current_user,
        room=room,
        start_at=attributes['start_at']
    )

    groups = []

    for group_id in attributes['groups']:
        groups.append(
            Group.query.get(group_id)
        )

    room.groups = groups

    db.session.add(room)
    db.session.add(event)
    db.session.commit()


@socketio.on('edit_event')
def edit_event(attributes):
    event = Event.query.get(attributes['id'])

    event.name = attributes['name']
    event.start_at = attributes['start_at']

    event.room.name = attributes['name']

    groups = []

    for group_id in attributes['groups']:
        groups.append(
            Group.query.get(group_id)
        )

    event.room.groups = groups

    db.session.commit()
