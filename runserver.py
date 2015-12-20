from controller.login import Login
from controller.table import Table

import argparse
import cherrypy
import os

def GetTableModel(full_class_name, string):
  """ Dynamically construct class from fully qualified name. """
  module_class = full_class_name.split('.')
  module = __import__(module_class[0])
  for namespace in module_class[1:]:
    module = getattr(module, namespace)
  instance = module(string)  
  return instance

def main():
  path   = os.path.abspath(os.path.dirname(__file__))

  parser = argparse.ArgumentParser(description='Simple table server.')
  parser.add_argument('--port', type=int, nargs='?', default=8080, help='Port server runs on')
  parser.add_argument('--source', type=str, nargs='?', default='', help='Data source string')
  parser.add_argument('--classname', type=str, nargs='?', default='model.table.Table', help='Data source class')
  args = parser.parse_args()

  login = Login()
  table = Table(GetTableModel(args.classname, args.source))
  mapper = cherrypy.dispatch.RoutesDispatcher()
  mapper.connect('login_route', '/:action', controller=login)
  mapper.connect('default_route', '/', controller=login)
  mapper.connect('table_route', '/table/:action', controller=table)
  conf = {
      '/': {
        'tools.sessions.on': True,
        'request.dispatch': mapper,
        'tools.staticdir.on': True,
        'tools.staticdir.dir': path
      }
  }
  cherrypy.tree.mount(login, "/", conf)
  server_config = {
      'server.socket_host': '0.0.0.0',
      'server.socket_port': args.port
  }
  cherrypy.config.update(server_config)
  cherrypy.engine.start()
  cherrypy.engine.block()

if __name__ == '__main__':
  main()