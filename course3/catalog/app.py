from flask import Flask
import config

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = config.DB_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = config.APP_SECRET

from handlers import *

if __name__ == '__main__':
    from db import db
    db.init_app(app)
    with app.app_context():
        db.create_all()
    app.debug = True
    app.run(host='127.0.0.1', port=5001)
