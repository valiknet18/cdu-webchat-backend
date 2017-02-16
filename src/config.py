class Config:
    def __init__(self, app):
        self.__init_application_config(app)
        self.__init_database_config(app)

    @staticmethod
    def __init_database_config(app):
        app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123123@localhost/cdu_webchat'

    @staticmethod
    def __init_application_config(app):
        pass