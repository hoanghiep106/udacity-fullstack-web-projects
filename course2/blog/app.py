from webapp2 import WSGIApplication

from handlers.BlogPage import BlogPage
from handlers.HomePage import HomePage
from handlers.post.DeletePost import DeletePost
from handlers.post.EditPost import EditPost
from handlers.post.NewPost import NewPost
from handlers.post.PostPage import PostPage
from handlers.user.Login import Login
from handlers.user.Logout import Logout
from handlers.user.Register import Register

app = WSGIApplication([('/', HomePage),
                      ('/blog/?', BlogPage),
                      ('/blog/([0-9]+)', PostPage),
                      ('/blog/([0-9]+)/edit', EditPost),
                      ('/blog/([0-9]+)/delete', DeletePost),
                      ('/blog/new', NewPost),
                      ('/register', Register),
                      ('/login', Login),
                      ('/logout', Logout), ],
                      debug=True)
