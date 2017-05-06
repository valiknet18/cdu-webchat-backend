from flask import Blueprint

admin = Blueprint('admin', __name__)

from app.admin.actions import users, groups, events
