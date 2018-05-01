from Base import BaseHandler
from google.appengine.ext import db

from models.post import blog_key


class DeletePost(BaseHandler):
    def post(self, post_id):
        key = db.Key.from_path('Post', int(post_id), parent=blog_key())
        post = db.get(key)
        if not post:
            return self.error(404)
        user = self.get_user()
        if post.username != user.username:
            msg = "Cannot delete other users' posts"
            self.render('notification.html', message=msg)
        else:
            post.delete()
            msg = 'Delete successfully'
            self.render('notification.html', message=msg)
