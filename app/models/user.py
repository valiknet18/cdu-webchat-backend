from app import db
from app.models.message import Message
from flask_login import UserMixin

if __name__ == '__main__':
    from app.models.room import Room

user_room = db.Table('user_room',
                     db.Column('user_id', db.Integer, db.ForeignKey('users.id')),
                     db.Column('room_id', db.Integer, db.ForeignKey('rooms.id'))
                     )

class User(db.Model, UserMixin):
    ADMIN = 'admin'
    STUDENT = 'student'
    TEACHER = 'teacher'

    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.VARCHAR(150))
    last_name = db.Column(db.VARCHAR(150))
    email = db.Column(db.VARCHAR(255), unique=True)
    username = db.Column(db.VARCHAR(255), unique=True)
    password = db.Column(db.VARCHAR(255))
    is_super_admin = db.Column(db.BOOLEAN(), default=False)
    role = db.Column(db.Enum(TEACHER, STUDENT, ADMIN))
    is_active = db.Column(db.BOOLEAN(), default=True)
    token = db.Column(db.VARCHAR(255), nullable=True)
    last_selected_room = db.Column(db.Integer(), db.ForeignKey('rooms.id'), nullable=True)
    messages = db.relationship('Message', backref='author', lazy='dynamic')
    rooms = db.relationship('Room', secondary=user_room, back_populates='members')
