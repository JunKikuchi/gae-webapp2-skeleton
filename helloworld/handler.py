from webapp2_local.session import SessionHandler
from webapp2_local.jinja2  import Jinja2Handler

class BaseHandler(Jinja2Handler, SessionHandler):
  pass

class HomeHandler(BaseHandler):
  def get(self):
    count = self.session.get('count') or 0
    self.session['count'] = count + 1

    self.render_response('index.html', count = count)

class HelloHandler(BaseHandler):
  def get(self):
    return "Hello World"
