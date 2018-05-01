import bleach
from handlers.Base import BaseHandler
from google.appengine.ext import db

from models.post import Post, blog_key


class EditPost(BaseHandler):
    def get(self, post_id):
        key = db.Key.from_path('Post', int(post_id), parent=blog_key())
        post = db.get(key)
        if not post:
            return self.error(404)
        self.render('post-form.html', title='Edit post', subject=post.subject, content=post.content)
    
    def post(self, post_id):
        key = db.Key.from_path('Post', int(post_id), parent=blog_key())
        post = db.get(key)
        if not post:
            return self.error(404)
        user = self.get_user()
        if post.username != user.username:
            msg = "Cannot edit other users' posts"
            self.render('notification.html', message=msg)
        else:
            subject = self.request.get('subject')
            content = self.request.get('content')

            content = bleach.clean(content)
      
            if subject and content:
                post.subject = subject
                post.content = content
                post.put()
                self.redirect('/blog/%s' % str(post.key().id()))
            else:
                error = 'Subject and content is required'
                self.render('post-form.html', title='Edit post', subject=subject, content=content, error=error)
