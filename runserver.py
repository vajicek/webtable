from controller.login import Login
from controller.table import Table

from model.table import Table as TableModel

import cherrypy
import os

def main():
  path   = os.path.abspath(os.path.dirname(__file__))
  
  login = Login()
  table = Table(TableModel())
  mapper = cherrypy.dispatch.RoutesDispatcher()
  mapper.connect('default_route', '/:action', controller=login)
  mapper.connect('default_route', '/', controller=login)
  mapper.connect('some_other', '/table/:action', controller=table)
  conf = {
      '/': {
        'tools.sessions.on': True,
        'request.dispatch': mapper,
        'tools.staticdir.on': True,
        'tools.staticdir.dir': path
      }
  }
  cherrypy.tree.mount(login, "/", conf)
  cherrypy.engine.start()
  cherrypy.engine.block()

if __name__ == '__main__':
  main()