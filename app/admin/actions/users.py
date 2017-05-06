from app import socketio, db
from app.models.user import User, Group
from app.schemas.admin.admin_user_schema import AdminUserSchema
from app.schemas.user_schema import UserSchema
from flask_socketio import emit

schema = AdminUserSchema()


def _get_users():
    users = User.query.all()

    emit('admin_receive_users', {
        'users': schema.dump(users, many=True).data
    })


def _get_user(id):
    user = User.query.get(id)

    emit('admin_receive_user', {
        'user': schema.dump(user).data
    })


@socketio.on('admin_get_users')
def get_users(attributes):
    _get_users()


@socketio.on('admin_get_user')
def get_user(attributes):
    _get_user(attributes['id'])


@socketio.on('admin_create_user')
def create_user(attributes):
    user = User(
        first_name=attributes['first_name'],
        last_name=attributes['last_name'],
        username=attributes['username'],
        email=attributes['email'],
        plain_password=attributes['password'],
        role=attributes['role'],
    )

    if attributes['role'] == User.STUDENT and attributes['group']:
        group = Group.query.get(attributes['group'])

        user.group = group

    db.session.add(user)
    db.session.commit()


@socketio.on('admin_edit_user')
def edit_user(attributes):
    user = User.query.get(attributes['id'])

    user.first_name = attributes['first_name']
    user.last_name = attributes['last_name']
    user.email = attributes['email']
    user.username = attributes['username']
    user.plain_password = attributes['password']
    user.role = attributes['role']

    if attributes['role'] == User.STUDENT and attributes['group']:
        group = Group.query.get(attributes['group'])

        user.group = group

    db.session.commit()

    _get_user(user.id)


@socketio.on('admin_delete_user')
def delete_user(attributes):
    user = User.query.get(attributes['id'])

    db.session.delete(user)
    db.session.commit()

    _get_users()
