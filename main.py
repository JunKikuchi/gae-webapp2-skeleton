import webapp2
import webapp2_local
import config

app = webapp2.WSGIApplication(config.route)
app.router.set_dispatcher(webapp2_local.custom_dispatcher)
