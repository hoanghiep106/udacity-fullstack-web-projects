from flask import Flask
from flask_cors import CORS

import config

from controllers.auth import auth_bp
from controllers.catalog import catalog_bp
from controllers.item import item_bp

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = config.DB_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = config.APP_SECRET

app.register_blueprint(auth_bp)
app.register_blueprint(catalog_bp)
app.register_blueprint(item_bp)

cors = CORS(send_wildcard=True)
cors.init_app(app)


if __name__ == '__main__':
    from db import db
    db.init_app(app)
    with app.app_context():
        db.create_all()
    app.debug = True
    app.run(host='127.0.0.1', port=5001)
