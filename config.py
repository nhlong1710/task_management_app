import os

class Config(object):
    # ...
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'cannot-be-guess'

    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:HMVuong216@localhost:5432/task-management-app"
    #SQLALCHEMY_DATABASE_URI = "postgresql://postgres:HMVuong216@localhost:5432/postGIS"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
