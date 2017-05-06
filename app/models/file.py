from app import db


class File(db.Model):
    __tablename__ = 'files'
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.VARCHAR(255))
    path = db.Column(db.VARCHAR(255))