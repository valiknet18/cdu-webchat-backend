from app import db
# from app.models.user import User, user_room


class Room(db.Model):
    __tablename__ = 'rooms'
    id = db.Column(db.Integer, primary_key=True)
    created_by = db.Column(db.Integer, db.ForeignKey('users.id'))
    name = db.Column(db.VARCHAR(255))
    created_at = db.Column(db.DateTime)
    # users = db.relationship('User', backref=db.backref('rooms', lazy='dynamic'))