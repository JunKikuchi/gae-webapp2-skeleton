import webapp2
from webapp2_extras import sessions

class SessionHandler(webapp2.RequestHandler):
    @webapp2.cached_property
    def session(self):
        return self.session_store.get_session()

    def dispatch(self):
        self.session_store = sessions.get_store(request=self.request)
        try:
            return super(SessionHandler, self).dispatch()
        finally:
            self.session_store.save_sessions(self.response)
