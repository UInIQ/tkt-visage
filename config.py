import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    LOGGING_LEVEL = 10  #integer. 0=notset, 10=debug, 20=info, 30=warning, 40=error, 50=critical

    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'tktf.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    API_URL_PREFIX = '/api'