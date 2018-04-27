from webapp2 import RequestHandler
from jinja import jinja_env

from utils.secure_value import make_secure_val, check_secure_val

from models.user import User

class BaseHandler(RequestHandler):
    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(**params)

    def render(self, template, **kw):
        self.write(self.render_str(template, **kw))

    def set_secure_cookie(self, name, val):
        cookie_val = make_secure_val(val)
        self.response.headers.add_header('Set-Cookie', '%s=%s; Path=/' % (name, cookie_val))

    def read_secure_cookie(self, name):
        cookie_val = self.request.cookies.get(name)
        return cookie_val and check_secure_val(cookie_val)

    def get_user(self):
        _id = self.read_secure_cookie('user_id')
        user = _id and User.find_by_id(int(_id))
        return user
