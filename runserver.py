from controller.login import Login
from controller.table import Table

from model.table import Table as TableModel

import argparse
import cherrypy
import os

def main():
  path   = os.path.abspath(os.path.dirname(__file__))

  parser = argparse.ArgumentParser(description='Simple table server.')
  parser.add_argument('--port', metavar='N', type=int, nargs='?', default=8080, help='Port server runs on')
  args = parser.parse_args()

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
  server_config = {
      'server.socket_host': '0.0.0.0',
      'server.socket_port': args.port
  }
  cherrypy.config.update(server_config)
  cherrypy.engine.start()
  cherrypy.engine.block()

if __name__ == '__main__':
  main()