import webapp2
from webapp2_extras import jinja2

def jinja2_factory(app):
  j = jinja2.Jinja2(app)
  j.environment.globals.update({
    'uri_for': webapp2.uri_for,
  })
  return j

class BaseHandler(webapp2.RequestHandler):
  @webapp2.cached_property
  def jinja2(self):
    return jinja2.get_jinja2(factory=jinja2_factory)

  def render_response(self, template, **context):
    self.response.write(self.jinja2.render_template(template, **context))
