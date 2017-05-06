from app import ma


class UserSchemaWithoutRooms(ma.Schema):
    class Meta:
        fields = ('first_name', 'last_name', 'email', 'username',)


class MessageSchema(ma.ModelSchema):
    class Meta:
        fields = ('author', 'created_at', 'msg')

    created_at = ma.Date()
    author = ma.Nested(UserSchemaWithoutRooms)
