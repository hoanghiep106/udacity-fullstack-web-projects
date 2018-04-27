from Base import BaseHandler

class Logout(BaseHandler):
  def get(self):
    self.response.headers.add_header('Set-Cookie', 'user_id=; Path=/')
    self.redirect('/login')
