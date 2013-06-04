import webapp2
from webapp2_extras import jinja2

def jinja2_factory(app):
    j = jinja2.Jinja2(app)
    j.environment.globals.update({
        'uri_for': webapp2.uri_for,
    })
    return j

class Jinja2Handler(webapp2.RequestHandler):
    @webapp2.cached_property
    def jinja2(self):
        return jinja2.get_jinja2(app=self.app, factory=jinja2_factory)

    def render_response(self, _template, **context):
        rv = self.jinja2.render_template(_template, **context)
        self.response.write(rv)
