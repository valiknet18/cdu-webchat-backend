from datetime import datetime, timedelta

from flask_socketio import emit
from flask_login import current_user

from app import socketio, db
from app.models.event import Event
from app.models.room import Room
from app.models.user import Group
from app.schemas.event_schema import EventSchema

schema = EventSchema()

DATETIME_FORMAT = '%d/%m/%Y, %H:%M'
UTC_OFFSET = 3


def _get_events():
    user = current_user
    room_ids = []
    events = []

    if user.role == 'teacher':
        events = Event.query.filter(Event.teacher_id == user.id).all()
    else:
        rooms = Room.query.filter(Room.groups.any(id=user.group_id)).filter(Room.role == Room.CONSULTATION).all()

        for room in rooms:
            room_ids.append(room.id)

        if len(room_ids) > 0:
	    print(datetime.utcnow())
            events = Event.query.filter(Event.room_id.in_(room_ids)).filter(Event.start_at >= datetime.utcnow()).all()

    emit('receive_events', {
        'events': schema.dump(events, many=True).data
    })


@socketio.on('get_events')
def get_events(attributes):
    _get_events()


@socketio.on('get_event')
def get_event(attributes):
    event = Event.query.get(attributes['id'])

    emit('receive_event', {
        'event': schema.dump(event).data
    })


@socketio.on('create_event')
def create_event(attributes):
    start_at = datetime.strptime(attributes['start_at'], DATETIME_FORMAT) - timedelta(hours=UTC_OFFSET)

    room = Room(
        name=attributes['name'],
        teacher=current_user,
        role=Room.CONSULTATION
    )

    event = Event(
        name=attributes['name'],
        teacher=current_user,
        room=room,
        start_at=start_at
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

    _get_events()


@socketio.on('edit_event')
def edit_event(attributes):
    print(attributes['start_at'])
    start_at = datetime.strptime(attributes['start_at'], DATETIME_FORMAT) - timedelta(hours=UTC_OFFSET)
    print(start_at)

    event = Event.query.get(attributes['id'])

    event.name = attributes['name']
    event.start_at = start_at

    event.room.name = attributes['name']

    groups = []

    for group_id in attributes['groups']:
        groups.append(
            Group.query.get(group_id)
        )

    event.room.groups = groups

    db.session.commit()

    _get_events()
