import json


class Config(object):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///catalog.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


CLIENT_ID = json.loads(open('client_secrets.json', 'r').read())['web']['client_id']
JWT_SECRET = 'ioj12joijiofwaijooawefa12'
