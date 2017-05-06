from app import ma


class AdminGroupSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name')
