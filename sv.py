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
@cross_origin(origin='localhost',headers=['Content-Type','Authorization'])
def receiveImage():     

    imgReceived = request.get_json(force=True)
    # print(imgReceived)

    imgdata = base64.b64decode(imgReceived['image'])
    
    res = getNeuralInference(imgdata)

    response = jsonify({'damageRank':res[0], 'part':res[1]})
    return response

def getNeuralInference(image):
    #process the image
    pass

if __name__ == '__main__':
    #####
    ## Load here the model ##       
    #####

    serverPort=sys.argv[1]
    app.run(debug = False,host='0.0.0.0',port=serverPort) 
