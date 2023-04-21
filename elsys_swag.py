from flask import Flask, request, Response, json, render_template
from flasgger import Swagger
from flask_cors import CORS
import js2py
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

@app.route('/', methods=['POST'])
def fun():
 """API for decoding the payload of Elsys devices
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
 payload = request.args.get('payload')

 data = (

'const TYPE_TEMP = 0x01; //temp 2 bytes -3276.8°C -->3276.7°C\n'
'const TYPE_RH = 0x02; //Humidity 1 byte  0-100%\n'
'const TYPE_ACC = 0x03; //acceleration 3 bytes X,Y,Z -128 --> 127 +/-63=1G\n'
'const TYPE_LIGHT = 0x04; //Light 2 bytes 0-->65535 Lux\n'
'const TYPE_MOTION = 0x05; //No of motion 1 byte  0-255\n'
'const TYPE_CO2 = 0x06; //Co2 2 bytes 0-65535 ppm\n'
'const TYPE_VDD = 0x07; //VDD 2byte 0-65535mV\n'
'const TYPE_ANALOG1 = 0x08; //VDD 2byte 0-65535mV\n'
'const TYPE_GPS = 0x09; //3bytes lat 3bytes long binary\n'
'const TYPE_PULSE1 = 0x0A; //2bytes relative pulse count\n'
'const TYPE_PULSE1_ABS = 0x0B; //4bytes no 0->0xFFFFFFFF\n'
'const TYPE_EXT_TEMP1 = 0x0C; //2bytes -3276.5C-->3276.5C\n'
'const TYPE_EXT_DIGITAL = 0x0D; //1bytes value 1 or 0\n'
'const TYPE_EXT_DISTANCE = 0x0E; //2bytes distance in mm\n'
'const TYPE_ACC_MOTION = 0x0F; //1byte number of vibration/motion\n'
'const TYPE_IR_TEMP = 0x10; //2bytes internal temp 2bytes external temp -3276.5C-->3276.5C\n'
'const TYPE_OCCUPANCY = 0x11; //1byte data\n'
'const TYPE_WATERLEAK = 0x12; //1byte data 0-255\n'
'const TYPE_GRIDEYE = 0x13; //65byte temperature data 1byte ref+64byte external temp\n'
'const TYPE_PRESSURE = 0x14; //4byte pressure data (hPa)\n'
'const TYPE_SOUND = 0x15; //2byte sound data (peak/avg)\n'
'const TYPE_PULSE2 = 0x16; //2bytes 0-->0xFFFF\n'
'const TYPE_PULSE2_ABS = 0x17; //4bytes no 0->0xFFFFFFFF\n'
'const TYPE_ANALOG2 = 0x18; //2bytes voltage in mV\n'
'const TYPE_EXT_TEMP2 = 0x19; //2bytes -3276.5C-->3276.5C\n'
'const TYPE_EXT_DIGITAL2 = 0x1A; // 1bytes value 1 or 0\n'
'const TYPE_EXT_ANALOG_UV = 0x1B; // 4 bytes signed int (uV)\n'
'const TYPE_TVOC = 0x1C; // 2 bytes (ppb)\n'
'const TYPE_DEBUG = 0x3D; // 4bytes debug\n'

'function bin16dec(bin) {\n'
'    var num = bin & 0xFFFF;\n'
'    if (0x8000 & num)\n'
'        num = -(0x010000 - num);\n'
'    return num;\n'
'}\n'

'function bin8dec(bin) {\n'
'    var num = bin & 0xFF;\n'
'    if (0x80 & num)\n'
'        num = -(0x0100 - num);\n'
'    return num;\n'
'}\n'

'function hexToBytes(hex) {\n'


'    for (var bytes = [], c = 0; c < hex.length; c += 2)\n'
'        bytes.push(parseInt(hex.substr(c, 2), 16));\n'

       
'    return bytes;\n'
'}\n'

'function DecodeElsysPayload(data) {\n'

'    var obj = new Object();\n'
'    for (i = 0; i < data.length; i++) {\n'
'        switch (data[i]) {\n'
'        case TYPE_TEMP: //Temperature\n'
'            var temp = (data[i + 1] << 8) | (data[i + 2]);\n'
'            temp = bin16dec(temp);\n'
'            obj.temperature = temp / 10;\n'
'            i += 2;\n'
'            break\n'
'        case TYPE_RH: //Humidity\n'
'            var rh = (data[i + 1]);\n'
'            obj.humidity = rh;\n'
'            i += 1;\n'
'            break\n'
'        case TYPE_ACC: //Acceleration\n'
'            obj.x = bin8dec(data[i + 1]);\n'
'            obj.y = bin8dec(data[i + 2]);\n'
'            obj.z = bin8dec(data[i + 3]);\n'
'            i += 3;\n'
'            break\n'
'        case TYPE_LIGHT: //Light\n'
'            obj.light = (data[i + 1] << 8) | (data[i + 2]);\n'
'            i += 2;\n'
'            break\n'
'        case TYPE_MOTION: //Motion sensor(PIR)\n'
'            obj.motion = (data[i + 1]);\n'
'            i += 1;\n'
'            break\n'
'        case TYPE_CO2: //CO2\n'
'            obj.co2 = (data[i + 1] << 8) | (data[i + 2]);\n'
'            i += 2;\n'
'            break\n'
'        case TYPE_VDD: //Battery level\n'
'            obj.vdd = (data[i + 1] << 8) | (data[i + 2]);\n'
'            i += 2;\n'
'            break\n'
'        case TYPE_ANALOG1: //Analog input 1\n'
'            obj.analog1 = (data[i + 1] << 8) | (data[i + 2]);\n'
'            i += 2;\n'
'            break\n'
'        case TYPE_GPS: //gps\n'
'            i++;\n'
'            obj.lat = (data[i + 0] | data[i + 1] << 8 | data[i + 2] << 16 | (data[i + 2] & 0x80 ? 0xFF << 24 : 0)) / 10000;\n'
'            obj.long = (data[i + 3] | data[i + 4] << 8 | data[i + 5] << 16 | (data[i + 5] & 0x80 ? 0xFF << 24 : 0)) / 10000;\n'
'            i += 5;\n'
'            break\n'
'        case TYPE_PULSE1: //Pulse input 1\n'
'            obj.pulse1 = (data[i + 1] << 8) | (data[i + 2]);\n'
'            i += 2;\n'
'            break\n'
'        case TYPE_PULSE1_ABS: //Pulse input 1 absolute value\n'
'            var pulseAbs = (data[i + 1] << 24) | (data[i + 2] << 16) | (data[i + 3] << 8) | (data[i + 4]);\n'
'            obj.pulseAbs = pulseAbs;\n'
'            i += 4;\n'
'            break\n'
'        case TYPE_EXT_TEMP1: //External temp\n'
'            var temp = (data[i + 1] << 8) | (data[i + 2]);\n'
'            temp = bin16dec(temp);\n'
'            obj.externalTemperature = temp / 10;\n'
'            i += 2;\n'
'            break\n'
'        case TYPE_EXT_DIGITAL: //Digital input\n'
'            obj.digital = (data[i + 1]);\n'
'            i += 1;\n'
'            break\n'
'        case TYPE_EXT_DISTANCE: //Distance sensor input\n'
'            obj.distance = (data[i + 1] << 8) | (data[i + 2]);\n'
'            i += 2;\n'
'            break\n'
'        case TYPE_ACC_MOTION: //Acc motion\n'
'            obj.accMotion = (data[i + 1]);\n'
'            i += 1;\n'
'            break\n'
'        case TYPE_IR_TEMP: //IR temperature\n'
'            var iTemp = (data[i + 1] << 8) | (data[i + 2]);\n'
'            iTemp = bin16dec(iTemp);\n'
'            var eTemp = (data[i + 3] << 8) | (data[i + 4]);\n'
'            eTemp = bin16dec(eTemp);\n'
'            obj.irInternalTemperature = iTemp / 10;\n'
'            obj.irExternalTemperature = eTemp / 10;\n'
'            i += 4;\n'
'            break\n'
'        case TYPE_OCCUPANCY: //Body occupancy\n'
'            obj.occupancy = (data[i + 1]);\n'
'            i += 1;\n'
'            break\n'
'        case TYPE_WATERLEAK: //Water leak\n'
'            obj.waterleak = (data[i + 1]);\n'
'            i += 1;\n'
'            break\n'
'        case TYPE_GRIDEYE: //Grideye data\n'
'            var ref = data[i+1];\n'
'            i++;\n'
'            obj.grideye = [];\n'
'            for(var j = 0; j < 64; j++) {\n'
'                obj.grideye[j] = ref + (data[1+i+j] / 10.0);\n'
'            }\n'
'            i += 64;\n'
'            break\n'
'        case TYPE_PRESSURE: //External Pressure\n'
'            var temp = (data[i + 1] << 24) | (data[i + 2] << 16) | (data[i + 3] << 8) | (data[i + 4]);\n'
'            obj.pressure = temp / 1000;\n'
'            i += 4;\n'
'            break\n'
'        case TYPE_SOUND: //Sound\n'
'            obj.soundPeak = data[i + 1];\n'
'            obj.soundAvg = data[i + 2];\n'
'            i += 2;\n'
'            break\n'
'        case TYPE_PULSE2: //Pulse 2\n'
'            obj.pulse2 = (data[i + 1] << 8) | (data[i + 2]);\n'
'            i += 2;\n'
'            break\n'
'        case TYPE_PULSE2_ABS: //Pulse input 2 absolute value\n'
'            obj.pulseAbs2 = (data[i + 1] << 24) | (data[i + 2] << 16) | (data[i + 3] << 8) | (data[i + 4]);\n'
'            i += 4;\n'
'            break\n'
'        case TYPE_ANALOG2: //Analog input 2\n'
'            obj.analog2 = (data[i + 1] << 8) | (data[i + 2]);\n'
'            i += 2;\n'
'            break\n'
'        case TYPE_EXT_TEMP2: //External temp 2\n'
'            var temp = (data[i + 1] << 8) | (data[i + 2]);\n'
'            temp = bin16dec(temp);\n'
'            if(typeof obj.externalTemperature2 === "number") {\n'
'                obj.externalTemperature2 = [obj.externalTemperature2];\n'
'            }\n' 
'            if(typeof obj.externalTemperature2 === "object") {\n'
'                obj.externalTemperature2.push(temp / 10);\n'
'            } else {\n'
'                obj.externalTemperature2 = temp / 10;\n'
'            }\n'
'            i += 2;\n'
'            break\n'
'        case TYPE_EXT_DIGITAL2: //Digital input 2\n'
'            obj.digital2 = (data[i + 1]);\n'
'            i += 1;\n'
'           break\n'
'        case TYPE_EXT_ANALOG_UV: //Load cell analog uV\n'
'            obj.analogUv = (data[i + 1] << 24) | (data[i + 2] << 16) | (data[i + 3] << 8) | (data[i + 4]);\n'
'            i += 4;\n'
'            break\n'
'        case TYPE_TVOC:\n'
'            obj.tvoc = (data[i + 1] << 8) | (data[i + 2]);\n'
'            i += 2;\n'
'            break\n'
'        default: //somthing is wrong with data\n'
'            i = data.length;\n'
'            break\n'
'        }\n'
'    }\n'
'    console.log(obj)\n'
'    return obj;\n'
'}\n'
'\n'
'\n'
'var res = DecodeElsysPayload(hexToBytes("'+ str(payload) +'"));\n'
'var json = JSON.stringify(res, null, 4);\n')


 with open('decode.js','w') as f:
     print(data, file=f)
 eval_res, tempfile = js2py.run_file("decode.js")
 return eval_res 