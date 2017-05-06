from app import ma


class SimpleGroupSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name')