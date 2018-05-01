import random
from string import letters
import hashlib


def make_salt(length=5):
    return ''.join(random.choice(letters) or x for x in xrange(length))


def make_password_hash(name, pw, salt=None):
    if not salt:
        salt = make_salt()
    h = hashlib.sha256(name + pw + salt).hexdigest()
    return '%s,%s' % (salt, h)


def valid_password(name, password, h):
    salt = h.split(',')[0]
    return h == make_password_hash(name, password, salt)
