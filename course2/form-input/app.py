import webapp2
from paste import httpserver

form  = """
<form action="/form-handler">
  <input name="q" type="checkbox">
  <input type="submit">
</form>
"""

class MainPage(webapp2.RequestHandler):
  def get(self):
    self.response.out.write(form)

class FormHandler(webapp2.RequestHandler):
  def get(self):
    q = self.request.get('q')
    self.response.out.write(q)


app = webapp2.WSGIApplication([('/', MainPage),
                              ('/form-handler', FormHandler)
                              ], debug=True)

httpserver.serve(app, host='127.0.0.1')
app.run()
