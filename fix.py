from app import create_app, db
from app.models.user import User, Group
from app.models.room import Room


def update_rooms():
    user = User.query.get(1)
    rooms = Room.query.all()

    for room in rooms:
        room.teacher = user

if __name__ == '__main__':
    app = create_app()

    with app.app_context():
        update_rooms()

        db.session.commit()
