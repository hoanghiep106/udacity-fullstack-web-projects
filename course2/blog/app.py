from webapp2 import WSGIApplication

from handlers.HomePage import HomePage
from handlers.BlogPage import BlogPage
from handlers.PostPage import PostPage
from handlers.NewPost import NewPost
from handlers.EditPost import EditPost
from handlers.DeletePost import DeletePost
from handlers.Register import Register
from handlers.Login import Login
from handlers.Logout import Logout

app = WSGIApplication([('/', HomePage),
                              ('/blog/?', BlogPage),
                              ('/blog/([0-9]+)', PostPage),
                              ('/blog/([0-9]+)/edit', EditPost),
                              ('/blog/([0-9]+)/delete', DeletePost),
                              ('/blog/new', NewPost),
                              ('/register', Register),
                              ('/login', Login),
                              ('/logout', Logout),],
                              debug=True)
