from app import ma


class AdminEventSchema(ma.Schema):
    class Meta:
        fields = ('id', 'start_at', 'name')
