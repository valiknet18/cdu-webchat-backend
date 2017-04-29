from app import ma
from app.schemas.room_schema import RoomSchema


class UserSchema(ma.Schema):
    class Meta:
        fields = ('first_name', 'last_name',
                  'email', 'username',
                  'role', 'is_super_admin',
                  'rooms', 'last_selected_room', 'id')

    rooms = ma.Nested(RoomSchema, many=True)