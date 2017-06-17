import json

from app import db
from app.models.file import File


class Message(db.Model):
    __tablename__ = 'messages'
    mysql_character_set = 'utf8'

    id = db.Column(db.Integer, primary_key=True)
    msg = db.Column(db.UnicodeText)
    created_at = db.Column(db.DateTime)
    author_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    room_id = db.Column(db.Integer, db.ForeignKey('rooms.id'))
    file_id = db.Column(db.Integer, db.ForeignKey('files.id'))
    images = db.Column(db.UnicodeText())

    @property
    def photos(self):
        return json.loads(self.images)

    @photos.setter
    def photos(self, photos):
        self.images = json.dumps(photos)
