from flask import Flask, request, Response, json, render_template
from flasgger import Swagger
from flask_cors import CORS
import cbor2
import binascii
app = Flask(__name__)
CORS(app) 



@app.route('/cbor', methods=['POST'])
def init():


 payload=request.args.get('payload')

 hex= str(payload)
    
 decode=cbor2.loads(binascii.a2b_hex(hex))
 print(decode)

 return decode