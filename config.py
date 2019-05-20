class Config:
    SECRET_KEY = 'HADR TO GUESS STRING'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    FLASKY_MAIL_SUBJECT_PREFIX = '[Flasky]'
    FLASKY_MAIL_SENDER = 'TEST_DASH_ARGS_AI'

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'near.3dsmax@gmail.com'
    MAIL_PASSWORD = 'zictyriyzgszjpyp'
    RBAC_USE_WHITE = False


class MongoConfig:
    MONGO_URI = 'mongodb://192.168.99.100:32768'

config = {
    'default': DevelopmentConfig,
    'development': DevelopmentConfig
}



