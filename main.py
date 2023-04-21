from werkzeug.middleware.dispatcher import DispatcherMiddleware 
from flask import Flask
from flasgger import Swagger
from cbor_swag import app as CBOR_SWAG
from elsys_swag import app as ELSYS_SWAG
from werkzeug.serving import run_simple 
app =Flask(__name__)
# app.config['SWAGGER'] = {
#     'title': 'Decoding',
#     'uiversion': 3,
#     'version': "1.0.0",
#     'description': "This is a simple `Payload Decoding` swagger UI where we can decode the payloads of type hexadecimal string. ",
#     'termsOfService': "http://swagger.io/terms/",
#     # 'hide_top_bar': True,
# }
swagger = Swagger(app)





application = DispatcherMiddleware(CBOR_SWAG, {
    '/elsys': ELSYS_SWAG
 
})



if __name__ == '__main__':
    run_simple(port=2001, hostname='0.0.0.0', application=application, use_debugger=True, use_reloader=True)

   