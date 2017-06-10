from app import db


class File(db.Model):
    __tablename__ = 'files'
    mysql_character_set = 'utf8'

    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.VARCHAR(255))
    path = db.Column(db.VARCHAR(255))