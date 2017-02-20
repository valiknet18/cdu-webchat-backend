class Config:
    def __init__(self, app):
        self.__init_application_config(app)
        self.__init_database_config(app)

    @staticmethod
    def __init_database_config(app):
        app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123123@localhost/cdu_webchat'
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

    @staticmethod
    def __init_application_config(app):
        app.config['SECRET_KEY'] = '85vyS5SL1KgNBAZ378W0MZaWxjr842sA'

        app.config['REMEMBER_COOKIE_NAME'] = 'token'
