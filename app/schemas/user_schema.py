from app import ma


class SimpleRoomSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'role',)


class GroupSchemaWithRooms(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'rooms')

    rooms = ma.Nested(SimpleRoomSchema, many=True)


class UserSchema(ma.Schema):
    class Meta:
        fields = ('first_name', 'last_name',
                  'email', 'username',
                  'role', 'last_selected_room', 'id', 'group')

    group = ma.Nested(GroupSchemaWithRooms)


