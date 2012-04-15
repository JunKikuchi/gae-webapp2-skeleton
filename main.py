import webapp2
from webapp2_extras import jinja2

def jinja2_factory(app):
  j = jinja2.Jinja2(app)
  j.environment.globals.update({
    'uri_for': webapp2.uri_for,
  })
  return j

def custom_dispatcher(router, request, response):
  rv = router.default_dispatcher(request, response)
  if isinstance(rv, basestring):
    rv = webapp2.Response(rv)
  elif isinstance(rv, tuple):
    rv = webapp2.Response(*rv)
  return rv

class BaseHandler(webapp2.RequestHandler):
  @webapp2.cached_property
  def jinja2(self):
    return jinja2.get_jinja2(factory=jinja2_factory)

  def render_response(self, template, **context):
    self.response.write(self.jinja2.render_template(template, **context))

class IndexPage(BaseHandler):
  def get(self):
    self.response.headers['Content-Type'] = 'text/html'
    self.render_response('index.html')

class HelloPage(BaseHandler):
  def get(self):
    self.response.headers['Content-Type'] = 'text/html'
    return "Hello World"

app = webapp2.WSGIApplication([
  webapp2.Route(r'/',      handler=IndexPage, name='index'),
  webapp2.Route(r'/hello', handler=HelloPage, name='hello'),
])
app.router.set_dispatcher(custom_dispatcher)
