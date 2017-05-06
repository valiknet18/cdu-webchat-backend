from app import ma
from app.schemas.room_schema import RoomSchema


class EventSchema(ma.Schema):
    class Meta:
        fields = ('id', 'start_at', 'name', 'room')

    room = ma.Nested(RoomSchema)