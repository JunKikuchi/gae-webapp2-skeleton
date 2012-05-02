import webapp2
from helloworld.handler import HomeHandler, HelloHandler

route = [
  webapp2.Route(r'/',      handler=HomeHandler,  name='home'),
  webapp2.Route(r'/hello', handler=HelloHandler, name='hello'),
]

config = {}
config['webapp2_extras.sessions'] = {
  'secret_key': '**** my super secret key ***',
}
