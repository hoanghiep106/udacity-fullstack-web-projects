from Base import BaseHandler

from models.post import Post, blog_key

class NewPost(BaseHandler):
  def get(self):
    self.render('new-post.html')
  
  def post(self):
    user = self.get_user()
    subject = self.request.get('subject')
    content = self.request.get('content')

    if subject and content:
      post = Post(parent=blog_key(), subject=subject, content=content, username=user.name)
      post.put()
      self.redirect('/blog/%s' % str(post.key().id()))
    else:
      error = 'Subject and content is required'
      self.render('new-post.html', subject=subject, content=content, error=error)
