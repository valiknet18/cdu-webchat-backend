from app import ma


class AdminUserSchema(ma.Schema):
    class Meta:
        fields = ('id', 'first_name',
                  'last_name', 'email',
                  'username', 'role')
