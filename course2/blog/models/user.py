from google.appengine.ext import db

from utils.secure_password import make_pw_hash, valid_pw

def users_key(name='default'):
  return db.Key.from_path('users', name)

class User(db.Model):
  name = db.StringProperty(required = True)
  pw_hash = db.StringProperty(required = True)
  email = db.StringProperty()

  @classmethod
  def find_by_id(cls, uid):
    return User.get_by_id(uid, parent = users_key())

  @classmethod
  def find_by_name(cls, name):
    user = User.all().filter('name =', name).get()
    return user

  @classmethod
  def register(cls, name, pw, email = None):
    pw_hash = make_pw_hash(name, pw)
    return User(parent = users_key(),
                name = name,
                pw_hash = pw_hash,
                email = email)

  @classmethod
  def login(cls, name, pw):
    user = cls.find_by_name(name)
    if user and valid_pw(name, pw, user.pw_hash):
      return user
