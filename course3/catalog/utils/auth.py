from functools import wraps

from flask import redirect, flash
from flask import session as login_session


def auth_required(func):
    @wraps(func)
    def auth_function(*args, **kwargs):
        if 'user_id' not in login_session:
            flash('Please login to use this function.')
            return redirect('/login')
        return func(*args, **kwargs)

    return auth_function
