import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123123@localhost/cdu_webchat'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SECRET_KEY = os.getenv('secret_key') or '85vyS5SL1KgNBAZ378W0MZaWxjr842sA'
    REMEMBER_COOKIE_NAME = 'token'

    @staticmethod
    def init_app(app):
        pass