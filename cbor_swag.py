from flask import Flask, request, Response, json, render_template
from flasgger import Swagger
from flask_cors import CORS
import cbor2
import binascii
app = Flask(__name__)
CORS(app) 
app.config['SWAGGER'] = {
    'title': 'Decoding',
    'uiversion': 3,
    'version': "1.0.0",
    'description': "This is a simple `Payload Decoding` swagger UI where we can decode the payloads of type hexadecimal string. ",
    'termsOfService': "http://swagger.io/terms/",
    # 'hide_top_bar': True,
}
swagger = Swagger(app)


@app.route('/cbor', methods=['POST'])
def init():
 """API for decoding the payload using CBOR-Technique
    This API is used to `decode the payload.
    ---
    tags:
      - "Decoders"
    parameters:
      - name: payload
        in: query
        type: string
        required: false

      
    definitions:
      Palette:
        type: object
        properties:
          palette_name:
            type: array
            items:
              $ref: '#/definitions/Color'
      Color:
        type: string
    responses:
      200:
        description: A list of colors (may be filtered by palette)
        schema:
          $ref: '#/definitions/Palette'
        examples:
          rgb: ['red', 'green', 'blue']
    """

 payload=request.args.get('payload')

 hex= str(payload)
    
 decode=cbor2.loads(binascii.a2b_hex(hex))
 print(decode)

 return decode