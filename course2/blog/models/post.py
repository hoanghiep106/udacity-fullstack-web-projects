from google.appengine.ext import db

from utils.render import render_str


def blog_key(name='default'):
    return db.Key.from_path('blogs', name)


class Post(db.Model):
    username = db.StringProperty(required=True)
    subject = db.StringProperty(required=True)
    content = db.TextProperty(required=True)
    created = db.DateTimeProperty(auto_now_add=True)
    last_modified = db.DateTimeProperty(auto_now=True)
  
    def render(self):
        self.content = self.content.replace('\n', '<br>')
        return render_str('post.html', post=self)
  
    def render_preview(self):
        self.content = self.content[:75] + (self.content[75:] and '..')
        return render_str('preview-post.html', post=self)
