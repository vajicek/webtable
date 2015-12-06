from auth import require
from common import CommonController

import cherrypy

class Table(CommonController):

  _cp_config = {
      'tools.sessions.on': True,
      'tools.auth.on': True
  }
    
  @cherrypy.expose
  @require()
  def list(self):
    table=self.model.get_view()
    data=dict(module_template='table.jinja', table=table)
    return self.render(data)

  @cherrypy.expose
  def __call__(self):
    data=dict(module_template='table.jinja')
    return self.render(data)

  def __init__(self, model):
    self.model = model
    super(Table, self).__init__()
