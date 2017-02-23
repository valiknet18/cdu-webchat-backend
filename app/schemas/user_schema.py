from app import ma
from app.models.user import User


class UserSchema(ma.ModelSchema):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username', 'role', 'is_super_admin',)
