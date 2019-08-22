import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    # ...
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'a136cd5b52647248f0008722d0ff2a36'





