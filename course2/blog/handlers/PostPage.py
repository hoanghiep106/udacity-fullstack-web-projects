from Base import BaseHandler
from google.appengine.ext import db

def blog_key(name='default'):
  return db.Key.from_path('blogs', name)

class PostPage(BaseHandler):
  def get(self, post_id):
    key = db.Key.from_path('Post', int(post_id), parent=blog_key())
    post = db.get(key)
    if not post:
      return self.error(404)
    self.render('post-page.html', post=post)
