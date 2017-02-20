from . import ma
from src.models.user import User


class UserSchema(ma.ModelSchema):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username',)