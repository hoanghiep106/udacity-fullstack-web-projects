from Base import BaseHandler

class HomePage(BaseHandler):
  def get(self):
      self.redirect('/blog')
