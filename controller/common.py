import cherrypy
import jinja2

@jinja2.contextfilter
def call_macro_by_name(context, macro_name, *args, **kwargs):
    return context.vars[macro_name](*args, **kwargs)

class CommonController(object):
  def __init__(self):
    self.templateLoader = jinja2.FileSystemLoader( searchpath="view" )
    self.templateEnv = jinja2.Environment( loader=self.templateLoader )
    self.templateEnv.filters['callMacroByName'] = call_macro_by_name

  def render(self, data):
    template = self.templateEnv.get_template('layout.jinja')
    data.update(dict(logedin=True, session=cherrypy.session))
    return template.render(data)
