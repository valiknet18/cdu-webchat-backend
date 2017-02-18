from . import db


class Room(db.Model):
    __tablename__ = 'rooms'
    id = db.Column(db.Integer, primary_key=True)
    created_by = db.Column(db.Integer, db.ForeignKey('users.id'))
    name = db.Column(db.VARCHAR(255))
    created_at = db.Column(db.DateTime)