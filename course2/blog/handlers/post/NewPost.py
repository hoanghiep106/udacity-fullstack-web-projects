import bleach
from handlers.Base import BaseHandler

from models.post import Post, blog_key


class NewPost(BaseHandler):
    def get(self):
        self.render('post-form.html', title='New Post')
    
    def post(self):
        user = self.get_user()
        subject = self.request.get('subject').strip()
        content = self.request.get('content').strip()
        
        content = bleach.clean(content)
    
        if subject and content:
            post = Post(parent=blog_key(), subject=subject, content=content, username=user.username)
            post.put()
            self.redirect('/blog/%s' % str(post.key().id()))
        else:
            error = 'Subject and content is required'
            self.render('post-form.html', title='New Post', subject=subject, content=content, error=error)
