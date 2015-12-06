from auth import check_credentials, SESSION_KEY 
from common import CommonController

import cherrypy

class Login(CommonController):

  def get_login_form(self, data=dict()):
    data.update(dict(module_template='login.jinja'))
    return self.render(data)

  @cherrypy.expose
  def login(self, username, password):
    if username is None or password is None:
        raise cherrypy.HTTPRedirect("/")
    error_msg = check_credentials(username, password)
    if error_msg:
      return self.get_login_form(dict(error_msg=error_msg))
    else:
      cherrypy.session[SESSION_KEY] = cherrypy.request.login = username
      raise cherrypy.HTTPRedirect("/table/list")

  @cherrypy.expose
  def logout(self):
      sess = cherrypy.session
      username = sess.get(SESSION_KEY, None)
      sess[SESSION_KEY] = None
      if username:
          cherrypy.request.login = None
      raise cherrypy.HTTPRedirect("/")

  @cherrypy.expose
  def __call__(self):
    return self.get_login_form()