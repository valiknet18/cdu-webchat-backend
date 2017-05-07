from app import ma


class SimpleStudentSchema(ma.Schema):
    class Meta:
        fields = ('id', 'first_name', 'last_name', )


class AdminGroupSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'students')

    students = ma.Nested(SimpleStudentSchema, many=True)

