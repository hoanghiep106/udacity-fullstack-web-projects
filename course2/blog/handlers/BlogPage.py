from Base import BaseHandler
from models.post import Post

class BlogPage(BaseHandler):
    def get(self):
        posts = Post.all().order('-created')
        self.render('blog-page.html', posts=posts)
