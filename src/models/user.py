from . import db
from flask_login import UserMixin

# rooms = db.Table('user_room',
#     db.Column('user_id', db.Integer, db.ForeignKey('users.id')),
#     db.Column('room_id', db.Integer, db.ForeignKey('rooms.id'))
# )


class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.VARCHAR(150))
    last_name = db.Column(db.VARCHAR(150))
    email = db.Column(db.VARCHAR(255), unique=True)
    username = db.Column(db.VARCHAR(255), unique=True)
    password = db.Column(db.VARCHAR(255))
    is_super_admin = db.Column(db.BOOLEAN(), default=False)
    role = db.Column(db.Enum('teacher', 'student'))
    is_active = db.Column(db.BOOLEAN(), default=True)
    # rooms = db.relationship('Room', secondary=rooms,
    #                         backref=db.backref('users', lazy='dynamic'))