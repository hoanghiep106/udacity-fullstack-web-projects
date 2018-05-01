from google.appengine.ext import db

from utils.password import make_password_hash, valid_password


def users_key(name='default'):
    return db.Key.from_path('users', name)


class User(db.Model):
    username = db.StringProperty(required=True)
    password_hash = db.StringProperty(required=True)
    email = db.StringProperty()
  
    @classmethod
    def find_by_id(cls, uid):
        return User.get_by_id(uid, parent=users_key())
  
    @classmethod
    def find_by_username(cls, username):
        user = User.all().filter('username =', username).get()
        return user
  
    @classmethod
    def register(cls, username, password, email=None):
        password_hash = make_password_hash(username, password)
        return User(parent=users_key(),
                    username=username,
                    password_hash=password_hash,
                    email=email)
  
    @classmethod
    def login(cls, username, password):
        user = cls.find_by_username(username)
        if user and valid_password(username, password, user.password_hash):
            return user
