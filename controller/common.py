import cherrypy
import jinja2

class CommonController(object):
  def __init__(self):
    self.templateLoader = jinja2.FileSystemLoader( searchpath="view" )
    self.templateEnv = jinja2.Environment( loader=self.templateLoader )

  def render(self, data):
    template = self.templateEnv.get_template('layout.jinja')
    data.update(dict(logedin=True, session=cherrypy.session))
    return template.render(data)
