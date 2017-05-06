from app import ma
from app.schemas.message_schema import MessageSchema


class RoomSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name',)


class UserSchemaForRooms(ma.Schema):
    class Meta:
        fields = ('first_name', 'last_name', 'id')


class GroupSchemaWithStudents(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'students')

    students = ma.Nested(UserSchemaForRooms, many=True)


class RoomSchemaWithMessages(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'messages', 'groups')

    messages = ma.Nested(MessageSchema, many=True)
    groups = ma.Nested(GroupSchemaWithStudents, many=True)
