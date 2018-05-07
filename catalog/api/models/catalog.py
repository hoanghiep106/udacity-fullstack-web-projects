from db import db
from models.base import Base
from models.user import User


class Catalog(Base):
    __tablename__ = 'catalog'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(120))
    
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship(User)

    def __init__(self, name, description, user_id):
        self.name = name
        self.description = description
        self.user_id = user_id

    @property
    def serializer(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'user_id': self.user_id
        }

    @classmethod
    def find_by_id(cls, catalog_id):
        return cls.query.filter_by(id=catalog_id).first()
    
    @classmethod
    def find_all(cls):
        return cls.query.all()
