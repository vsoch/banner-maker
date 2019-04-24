#!/usr/bin/env python

from flup.server.fcgi import WSGIServer
from index import app as application

WSGIServer(application).run()
