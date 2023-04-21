from werkzeug.middleware.dispatcher import DispatcherMiddleware 
from flask import Flask
from flasgger import Swagger
from cbor import app as CBOR
from elsys import app as ELSYS
from werkzeug.serving import run_simple 
app =Flask(__name__)


application = DispatcherMiddleware(CBOR, {
    '/elsys': ELSYS
 
})

if __name__ == '__main__':
    run_simple(port=1000, hostname='0.0.0.0', application=application, use_debugger=True, use_reloader=True)
   