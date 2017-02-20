from flask_login import LoginManager
from src.models.user import User
from src.helpers import decode_user_token

login_manager = LoginManager()

@login_manager.request_loader
def user_load(request):
    if 'token' not in request.args:
        return None

    token = request.args['token']

    if not token:
        return None

    token = decode_user_token(token).decode('ascii')

    return User.query.filter_by(token=token).first()

@login_manager.user_loader
def get_sess_user(user_id):
    return User.query.get(user_id)