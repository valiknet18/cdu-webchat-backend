from app import create_app, db
from app.models.user import User, Group
from app.models.room import Room

def create_default_group(db):
    group = Group(
        name='default_group'
    )

    db.session.add(group)

    return group

def create_default_user(db, group):
    user = User(
        first_name='Admin',
        last_name='Admin',
        email='admin@mail.com',
        username='admin',
        role=User.ADMIN,
        plain_password='admin',
        group=group
    )

    db.session.add(user)

    return user

def create_default_room(db, group):
    room = Room(
        name='Default',
        role=Room.SIMPLE
    )

    db.session.add(room)

    group.rooms.append(room)

    return room

if __name__ == '__main__':
    app = create_app()

    with app.app_context():
        db.create_all()

        group = create_default_group(db)
        create_default_user(db, group)
        create_default_room(db, group)

        db.session.commit()