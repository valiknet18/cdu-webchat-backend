from app import ma


class UserSchemaWithoutRooms(ma.Schema):
    class Meta:
        fields = ('first_name', 'last_name', 'email', 'username',)


class MessageSchema(ma.ModelSchema):
    class Meta:
        fields = ('message', 'created_at', 'author')

    author = ma.Nested(UserSchemaWithoutRooms)