import webapp2
import webapp2_local

from helloworld.handler import HomeHandler, HelloHandler

app = webapp2.WSGIApplication([
  webapp2.Route(r'/',      handler=HomeHandler,  name='index'),
  webapp2.Route(r'/hello', handler=HelloHandler, name='hello'),
])
app.router.set_dispatcher(webapp2_local.custom_dispatcher)
