import webapp2
from webapp2_extras                 import auth
from webapp2_local.handlers.session import SessionHandler

class AuthHandler(SessionHandler):
    @webapp2.cached_property
    def auth(self):
        return auth.get_auth()

    @webapp2.cached_property
    def user_model(self):
        return self.auth.store.user_model

    def get_user(self):
        user_info = self.auth.get_user_by_session()
        if user_info:
            return self.user_model.get_by_id(user_info['user_id'])
        else:
            return None
