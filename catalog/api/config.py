import json

APP_SECRET = 'very_secret_key'
JWT_SECRET = 'ioj12joijiofwaijooawefa12'
DB_URL = 'sqlite:///catalog.db'
CLIENT_ID = json.loads(open('client_secrets.json', 'r').read())['web']['client_id']
