from app import ma

class AdminGroupSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name',)

class AdminUserSchema(ma.Schema):
    class Meta:
        fields = ('id', 'first_name',
                  'last_name', 'email',
                  'username', 'role', 'group',)

    group = ma.Nested(AdminGroupSchema)
