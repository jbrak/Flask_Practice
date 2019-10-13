import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    #Forms
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'

    #DataBase
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
