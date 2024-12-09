
""" contains links to database connections, mail client.
    ie.,mysql
    ie.gmail, yahoo,
    also hold the secret key used in form validations
"""
import os

class Config:
    SECRET_KEY = 'c7c52ced176b65114f3e211f'
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://MUSTAFA:5m9l<18>_X!@localhost/Automobile'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True

    SESSION_TYPE = 'filesystem'
    SESSION_PERMANENT = False 
    SESSION_COOKIE_NAME = 'user_session' 
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SECURE = True

    MAIL_SERVER = 'smtp.google.com'
    MAIL_PORT = 587    
    MAIL_USE_TLS = True
    MAIL_USE_SSL = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')



""" unfinished """
# class DevelopmentConfig(Config):
#     DEBUG = True
#     SQLALCHEMY_DATABASE_URI = ''

# class TestingConfig(Config):
#     TESTING = True
#     SQLALCHEMY_DATABASE_URI = 'sqlite:/// data-test.sqlite'

# class ProductionConfig(Config):
#     SQLALCHEMY_DATABASE_URI = 'sqlite:/// data-test.sqlite'


# config = {
# 'development': DevelopmentConfig,
# 'testing': TestingConfig,
# 'production': ProductionConfig,
# 'default': DevelopmentConfig
# }