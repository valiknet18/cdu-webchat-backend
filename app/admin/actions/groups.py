from flask_socketio import emit

from app import socketio, db
from app.models.user import Group
from app.schemas.admin.admin_group_schema import AdminGroupSchema

group_schema = AdminGroupSchema()


@socketio.on('admin_get_groups')
def get_groups(attributes):
    groups = Group.query.all()

    emit('admin_receive_groups', {
        'groups': group_schema.dump(groups, many=True).data
    })


@socketio.on('admin_get_group')
def get_group(attributes):
    group = Group.query.get()

    emit('admin_receive_group', {
        'group': group_schema.dump(group).data
    })


@socketio.on('admin_create_group')
def create_group(attributes):
    group = Group(
        name=attributes['name']
    )

    db.session.add(group)
    db.session.commit()


@socketio.on('admin_edit_group')
def edit_group(attributes):
    group = Group.query.get(attributes['id'])

    group.name = attributes['name']

    db.session.commit()


@socketio.on('admin_delete_group')
def delete_group(attributes):
    group = Group.query.get(attributes['id'])

    db.session.delete(group)
    db.session.commit()
