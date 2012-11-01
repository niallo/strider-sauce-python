import os
import logging

from pyramid.config import Configurator
from pyramid.view import view_config
from pyramid.response import Response

from wsgiref.simple_server import make_server

logging.basicConfig()
log = logging.getLogger(__file__)

here = os.path.dirname(os.path.abspath(__file__))

@view_config(route_name='index')
def root_view(request):
    return Response("this is a body")

if __name__ == '__main__':
    # configuration settings
    settings = {}
    # session factory
    # configuration setup
    config = Configurator(settings=settings)
    config.add_route('index', '/')
    config.scan()
    # serve app
    app = config.make_wsgi_app()
    server = make_server('0.0.0.0', os.environ.get('PORT', 8080), app)
    server.serve_forever()
