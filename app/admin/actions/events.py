from flask_login import current_user
from flask_socketio import emit

from app import socketio, db
from app.models.event import Event
from datetime import datetime

from app.models.room import Room
from app.schemas.admin.admin_event_schema import AdminEventSchema

event_schema = AdminEventSchema()


@socketio.on('admin_get_events')
def get_events(attributes):
    events = Event.query.filter(Event.start_at >= datetime.now()).all()

    emit('admin_receive_events', {
        'events': event_schema.dump(events, many=True).data
    })

