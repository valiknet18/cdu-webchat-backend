from app import ma
from app.schemas.room_schema import RoomSchema, UserSchemaForRooms


class SimpleGroupSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name')


class RoomSchemaWithGroups(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'groups')

    groups = ma.Nested(SimpleGroupSchema, many=True)


class EventSchema(ma.Schema):
    class Meta:
        fields = ('id', 'start_at', 'name', 'room', 'teacher')

    room = ma.Nested(RoomSchemaWithGroups)
    teacher = ma.Nested(UserSchemaForRooms)
