import os

class Config(object):
    # ...
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'cannot-be-guess'

    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:HMVuong216@localhost:5432/task-management-app"
    #SQLALCHEMY_DATABASE_URI = "postgresql://postgres:HMVuong216@localhost:5432/postGIS"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
