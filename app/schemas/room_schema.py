from app import ma
from app.schemas.message_schema import MessageSchema, UserSchemaWithoutRooms


class RoomSchema(ma.Schema):
    class Meta:
        fields = ('id', 'created_by', 'name', 'created_at',)


class RoomSchemaWithMessages(ma.Schema):
    class Meta:
        fields = ('id', 'created_by', 'name', 'created_at', 'messages', 'members')

    messages = ma.Nested(MessageSchema, many=True)
    members = ma.Nested(UserSchemaWithoutRooms, many=True)
