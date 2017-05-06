import os


class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI') or 'mysql+pymysql://root:112233@localhost/cdu_webchat?charset=utf8'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SECRET_KEY = os.getenv('SECRET_KEY') or '85vyS5SL1KgNBAZ378W0MZaWxjr842sA'

    @staticmethod
    def init_app(app):
        pass
