from datetime import datetime

from app import db
from app.models.user import User
from app.models.room import Room


class Event(db.Model):
    __tablename__ = 'events'
    id = db.Column(db.Integer, primary_key=True)
    start_at = db.Column(db.DateTime)
    name = db.Column(db.VARCHAR(150))
    teacher_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    teacher = db.relationship('User')
    room_id = db.Column(db.Integer, db.ForeignKey('rooms.id'))
    room = db.relationship('Room')
