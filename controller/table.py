from auth import require
from common import CommonController

import cherrypy
import simplejson

class Table(CommonController):

  _cp_config = {
      'tools.sessions.on': True,
      'tools.auth.on': True
  }
    
  @cherrypy.expose
  @require()
  def list(self):
    table=self.model.get_list()
    data=dict(module_template='table.jinja', table=table)
    return self.render(data)

  @cherrypy.expose
  @require()
  def edit(self, value):
    content=self.model.get_item(value)
    str_content = simplejson.dumps(content, indent="\t")
    data=dict(module_template='detail.jinja', key=value, value=str_content)
    return self.render(data)

  @cherrypy.expose
  @require()
  def save(self, key, value, control):
    if control == "store":
      content = simplejson.loads(value)
      self.model.set_item(key, content)
    raise cherrypy.HTTPRedirect("/table/list")

  @cherrypy.expose
  @require()
  def remove(self, value):
    self.model.remove_item(value)
    raise cherrypy.HTTPRedirect("/table/list")

  @cherrypy.expose
  def __call__(self):
    data=dict(module_template='table.jinja')
    return self.render(data)

  def __init__(self, model):
    self.model = model
    super(Table, self).__init__()
