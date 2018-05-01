from Base import BaseHandler


class HomePage(BaseHandler):
    def get(self):
        if self.get_user():
            self.redirect('/blog')
        else:
            self.redirect('/login')
