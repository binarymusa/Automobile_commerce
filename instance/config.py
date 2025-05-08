
""" 
contains links to database connections, mail client.
ie.,mysql
ie.gmail, yahoo,
also hold the secret key used in form validations
"""
import os
from dotenv import load_dotenv
load_dotenv()

class Config:
    try:
        SECRET_KEY = os.environ.get('SECRET_KEY')
        SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
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
    except Exception as e:
        print(e)



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