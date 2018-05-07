from functools import wraps
import jwttoken
from flask import request

from models.user import User


def auth_required(func):
    @wraps(func)
    def auth_function(*args, **kwargs):
        user = None
        if 'Authorization' in request.headers:
            authorization = request.headers['Authorization']
            if authorization.startswith('Bearer '):
                token = jwttoken.decode(authorization[len('Bearer '):])
                print token
                if token:
                    user = User.find_by_id(token['sub'])
                    print user.id
        kwargs['user'] = user
        return func(*args, **kwargs)
    return auth_function
