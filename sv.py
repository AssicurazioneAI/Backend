from flask import Flask, jsonify, request
from flask_cors import CORS,cross_origin
#from datetime import datetime
import keras as k
import tensorflow as tf
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
    print(imgReceived)

    imgdata = base64.b64decode(imgReceived['image'])
    
    res = getNeuralInference(imgdata)

    response = jsonify({'damageRank':res[0], 'part':res[1]})
    return response

def getNeuralInference(image):
    #process the image
    pass

if __name__ == '__main__':
    session = tf.Session(graph=tf.Graph())
    
    with session.graph.as_default():
        k.backend.set_session(session)                
    
    serverPort=sys.argv[1]
    app.run(debug = False,host='0.0.0.0',port=serverPort) 
