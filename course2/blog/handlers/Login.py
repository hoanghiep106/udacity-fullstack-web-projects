from Base import BaseHandler
from models.user import User


class Login(BaseHandler):
    def get(self):
        self.render('login.html')
    
    def post(self):
        username = self.request.get('username').strip()
        password = self.request.get('password').strip()
    
        user = User.login(username, password)
        if user:
            self.set_secure_cookie('user_id', str(user.key().id()))
            self.redirect('/blog')
        else:
            msg = 'Invalid credentials'
            self.render('login.html', error=msg)
