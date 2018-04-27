from Base import BaseHandler

from utils.validate import valid_email, valid_password, valid_username

from models.user import User

class Register(BaseHandler):
  def get(self):
    self.render('register.html')

  def post(self):
    have_error = False
    self.username = self.request.get('username')
    self.password = self.request.get('password')
    self.verify = self.request.get('verify')
    self.email = self.request.get('email')

    params = dict(username = self.username,
                  email = self.email)

    if not valid_username(self.username):
      params['error_username'] = "That's not a valid username."
      have_error = True

    if not valid_password(self.password):
      params['error_password'] = "That wasn't a valid password."
      have_error = True
    elif self.password != self.verify:
      params['error_verify'] = "Your passwords didn't match."
      have_error = True

    if not valid_email(self.email):
      params['error_email'] = "That's not a valid email."
      have_error = True

    if have_error:
      self.render('register.html', **params)
    else:
      self.done()

  def done(self):
    user = User.find_by_name(self.username)
    if user:
      msg = 'That user already exists.'
      self.render('register.html', error_username = msg)
    else:
      user = User.register(self.username, self.password, self.email)
      user.put()
      self.set_secure_cookie('user_id', str(user.key().id()))
      self.redirect('/blog')
