from app import ma


class AdminEventTeacher(ma.Schema):
    class Meta:
        fields = ('id', 'first_name', 'last_name',)


class AdminEventSchema(ma.Schema):
    class Meta:
        fields = ('start_at', 'name', 'id', 'teacher',)

    start_at = ma.DateTime()
    teacher = ma.Nested(AdminEventTeacher)

