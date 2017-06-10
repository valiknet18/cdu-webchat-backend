from app import create_app, db
from app.models.user import User, Group
from app.models.room import Room

if __name__ == '__main__':
    app = create_app()

    with app.app_context():
        db.engine.execute("ALTER table messages CONVERT TO CHARACTER SET utf8 COLLATE utf8_general_ci")
        db.engine.execute("ALTER table events CONVERT TO CHARACTER SET utf8 COLLATE utf8_general_ci")
        db.engine.execute("ALTER table files CONVERT TO CHARACTER SET utf8 COLLATE utf8_general_ci")
        db.engine.execute("ALTER table groups CONVERT TO CHARACTER SET utf8 COLLATE utf8_general_ci")
        db.engine.execute("ALTER table rooms CONVERT TO CHARACTER SET utf8 COLLATE utf8_general_ci")
        db.engine.execute("ALTER table users CONVERT TO CHARACTER SET utf8 COLLATE utf8_general_ci")

        db.session.commit()
