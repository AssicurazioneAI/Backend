from flask import Flask, jsonify, request
from flask_cors import CORS,cross_origin
#from datetime import datetime
###
# Import here the library needed for the model #
###
import sys
import base64
import numpy as np

faceCascade=None
modeloKeras=None
graph=None
sess=None
session=None

# Server Logic
app = Flask(__name__) 
app.config['CORS_HEADERS'] = 'Content-Type'
cors = CORS(app, resources={r"/receiveImage": {"origins": "*"}})

@app.route('/recibeImagen', methods = ['POST']) 
@cross_origin(origin='localhost',headers=['Content-Type'])
def receiveImage():     

    imgReceived = request.get_json(force=True)
    # print(imgReceived)

    imgdata = base64.b64decode(imgReceived['image'])
    
    res = getNeuralInference(imgdata)

    response = jsonify(res)
    return response

def getNeuralInference(image):
    #process the image 
    #print(image)
    aux = [5, "door"]
    res = {}    
    data = {}    
    data['score'] = 12.12121
    data['bbox'] = ["374.07073974609375","143.3466033935547","167.2783203125","489.75067138671875"]
    data['type'] = "light"
    data['superCategory'] = "part"
    data['imageWidth'] = 1024
    data['imageHeight'] = 1024   
    res['data'] = data    
    res['errorMessage'] = "Some error happened"
    res['responseCode'] = 200

    return res

if __name__ == '__main__':
    #####
    ## Load here the model ##       
    #####
    print("Starting...")
    #serverPort=sys.argv[1]
    #print("Puerto ", str(serverPort))
    app.run(debug = True,host='0.0.0.0') 
