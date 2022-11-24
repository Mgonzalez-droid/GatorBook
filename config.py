#Flask-SQLAlchemy implementation

import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config (object):
    SQLALCHEMY_DATABASE_URI = ('mysql+pymysql://username:password@localhost/20200830MYSQL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False