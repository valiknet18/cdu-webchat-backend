from app import db
from app.models.message import Message
from app.models.user import group_room, User, Group


class Room(db.Model):
    CONSULTATION = 'consultation'
    SIMPLE = 'simple'

    __tablename__ = 'rooms'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.VARCHAR(255))
    role = db.Column(db.VARCHAR(100))
    messages = db.relationship('Message', backref='room', lazy='dynamic')
    groups = db.relationship('Group', secondary=group_room, back_populates='rooms')
    teacher_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    teacher = db.relationship('User', foreign_keys=[teacher_id])
