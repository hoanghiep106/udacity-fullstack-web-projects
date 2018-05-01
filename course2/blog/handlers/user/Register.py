from handlers.Base import BaseHandler

from utils.validate import valid_email, valid_password, valid_username

from models.user import User


class Register(BaseHandler):
    def get(self):
        self.render('register.html')

    def post(self):
        have_error = False
        username = self.request.get('username').strip()
        password = self.request.get('password').strip()
        verify = self.request.get('verify').strip()
        email = self.request.get('email').strip()
    
        params = dict(username=username, email=email)
    
        if not valid_username(username):
            params['error_username'] = "That's not a valid username."
            have_error = True
    
        if not valid_password(password):
            params['error_password'] = "That wasn't a valid password."
            have_error = True
        elif password != verify:
            params['error_verify'] = "Your passwords didn't match."
            have_error = True
    
        if not valid_email(email):
            params['error_email'] = "That's not a valid email."
            have_error = True
    
        if have_error:
            self.render('register.html', **params)
        else:
            user = User.find_by_username(username)
            if user:
                msg = 'That user already exists.'
                self.render('register.html', error_username=msg)
            else:
                user = User.register(username, password, email)
                user.put()
                self.set_secure_cookie('user_id', str(user.key().id()))
                self.redirect('/blog')
