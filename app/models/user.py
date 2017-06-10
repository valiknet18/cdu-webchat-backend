from werkzeug.security import generate_password_hash

from app import db
from app.models.message import Message
from flask_login import UserMixin

if __name__ == '__main__':
    from app.models.room import Room

group_room = db.Table('group_room',
                 db.Column('group_id', db.Integer, db.ForeignKey('groups.id')),
                 db.Column('room_id', db.Integer, db.ForeignKey('rooms.id'))
             )


class User(db.Model, UserMixin):
    ADMIN = 'admin'
    STUDENT = 'student'
    TEACHER = 'teacher'

    __tablename__ = 'users'
    mysql_character_set = 'utf8'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.VARCHAR(150))
    last_name = db.Column(db.VARCHAR(150))
    email = db.Column(db.VARCHAR(255), unique=True)
    username = db.Column(db.VARCHAR(255), unique=True)
    password = db.Column(db.VARCHAR(255))
    role = db.Column(db.Enum(TEACHER, STUDENT, ADMIN))
    is_active = db.Column(db.BOOLEAN(), default=True)
    token = db.Column(db.VARCHAR(255), nullable=True)
    last_selected_room = db.Column(db.Integer(), db.ForeignKey('rooms.id'), nullable=True)
    messages = db.relationship('Message', backref='author', lazy='dynamic')
    group_id = db.Column(db.Integer, db.ForeignKey('groups.id'))
    group = db.relationship('Group')

    @property
    def plain_password(self):
        return None

    @plain_password.setter
    def plain_password(self, password):
        if password:
            self.password = generate_password_hash(password),


class Group(db.Model):
    __tablename__ = 'groups'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.VARCHAR(150))
    rooms = db.relationship('Room', secondary=group_room, back_populates='groups')
    students = db.relationship('User', back_populates='group')
