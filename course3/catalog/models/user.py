from db import db
from models.base import Base


class User(Base):
    __tablename__ = 'user'
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    picture = db.Column(db.String(250), nullable=False)
    id = db.Column(db.Integer, primary_key=True)

    def __init__(self, name, email, picture):
        self.name = name
        self.email = email
        self.picture = picture

    @classmethod
    def find_by_id(cls, id):
        user = cls.query.filter_by(id=id).first()
        return user

    @classmethod
    def find_by_email(cls, email):
        user = cls.query.filter_by(email=email).first()
        return user
