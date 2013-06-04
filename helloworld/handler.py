import webapp2
from webapp2_local.handlers.session import SessionHandler
from webapp2_local.handlers.jinja2  import Jinja2Handler

class BaseHandler(Jinja2Handler, SessionHandler):
  pass

class HomeHandler(BaseHandler):
  def get(self):
    count = self.session.get('count') or 0
    self.session['count'] = count + 1

    self.render_response('index.html', count = count)

class HelloHandler(BaseHandler):
  def get(self):
    return webapp2.Response("Hello World")
