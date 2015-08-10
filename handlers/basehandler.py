from torndsession.sessionhandler import SessionBaseHandler

class BaseHandler(SessionBaseHandler):
    def __init__(self, *argc, **argkw):
        super(BaseHandler, self).__init__(*argc, **argkw)
        self.session = session.Session(self.application.session_manager, self)
    def get_current_user(self):
        return self.session.get("uname")