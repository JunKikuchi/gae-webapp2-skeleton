import fix_path
import fix_encoding
import webapp2
import config

app = webapp2.WSGIApplication(config.route, config=config.config)
