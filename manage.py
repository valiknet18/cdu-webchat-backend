from app import create_app, db
from app.models import user, room, message, event, file

from flask_script import Manager, Shell
from flask_migrate import MigrateCommand, Migrate

app = create_app()

def _make_context():
    return dict(app=app, db=db, user=user, room=room, message=message, event=event)

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)
manager.add_command('shell', Shell(make_context=_make_context))

if __name__ == "__main__":
    manager.run()
