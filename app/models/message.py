from app import db
from app.models.file import File


class Message(db.Model):
    __tablename__ = 'messages'
    id = db.Column(db.Integer, primary_key=True)
    msg = db.Column(db.UnicodeText)
    created_at = db.Column(db.DateTime)
    author_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    room_id = db.Column(db.Integer, db.ForeignKey('rooms.id'))
    file_id = db.Column(db.Integer, db.ForeignKey('files.id'))
