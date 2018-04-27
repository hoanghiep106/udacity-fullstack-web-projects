from Base import BaseHandler
from google.appengine.ext import db

from models.post import blog_key

class DeletePost(BaseHandler):
  def get(self, post_id):
    key = db.Key.from_path('Post', int(post_id), parent=blog_key())
    post = db.get(key)
    if not post:
      return self.error(404)
    post.delete()
    msg = 'Delete successfully'
    self.render('success.html', message=msg)
