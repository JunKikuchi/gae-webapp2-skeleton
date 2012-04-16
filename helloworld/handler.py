from webapp2_local.jinja2 import BaseHandler

class HomeHandler(BaseHandler):
  def get(self):
    self.response.headers['Content-Type'] = 'text/html'
    self.render_response('index.html')

class HelloHandler(BaseHandler):
  def get(self):
    self.response.headers['Content-Type'] = 'text/html'
    return "Hello World"
