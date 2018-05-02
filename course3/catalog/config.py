import json

APP_SECRET = 'very_secret_key'
DB_URL = 'sqlite:///catalog.db'
CLIENT_ID = json.loads(open('client_secrets.json', 'r').read())['web']['client_id']