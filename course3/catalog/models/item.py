from db import db
from models.base import Base
from models.user import User
from models.catalog import Catalog


class Item(Base):
    __tablename__ = 'item'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    description = db.Column(db.String(250))

    catalog_id = db.Column(db.Integer, db.ForeignKey('catalog.id'))
    catalog = db.relationship(Catalog)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship(User)

    def __init__(self, name, description, catalog_id, user_id):
        self.name = name
        self.description = description
        self.catalog_id = catalog_id
        self.user_id = user_id

    @property
    def serialize(self):
        return {
           'id': self.id,
           'name': self.name,
           'description': self.description
        }

    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first()

    @classmethod
    def find_by_catalog_id(cls, catalog_id):
        return cls.query.filter_by(catalog_id=catalog_id).all()
