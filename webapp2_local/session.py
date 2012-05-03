import webapp2
from webapp2_extras import sessions

class SessionHandler(webapp2.RequestHandler):
  def dispatch(self):
    try:
      webapp2.RequestHandler.dispatch(self)
    finally:
      self.session_store.save_sessions(self.response)

  @webapp2.cached_property
  def session_store(self):
    return sessions.get_store(request=self.request)

  @webapp2.cached_property
  def session(self):
    return self.session_store.get_session()
