from flask import Flask, jsonify, request
from flask_cors import CORS,cross_origin
import torch
import os
import cv2
import skimage.io as io
from detectron2 import model_zoo
from detectron2.engine import DefaultPredictor
from detectron2.config import get_cfg
#from datetime import datetime
###
# Import here the library needed for the model #
###

import sys
import base64
import numpy as np

graph=None
sess=None
session=None
cfg=None

# Server Logic
app = Flask(__name__) 
app.config['CORS_HEADERS'] = 'Content-Type'
cors = CORS(app, resources={r"/receiveImage": {"origins": "*"}})

@app.route('/recibeImagen', methods = ['GET']) 
@cross_origin(origin='localhost',headers=['Content-Type'])
def receiveImage():     

    imgReceived = request.get_json(force=True)

    imgdata = base64.b64decode(imgReceived['image'])
    np_data = np.fromstring(imgdata,np.uint8)
    img = cv2.imdecode(np_data,cv2.IMREAD_UNCHANGED)
    res = getNeuralInference(img)
    response = jsonify(res)
    return response

def getNeuralInference(image):
    predictions = predict(image)
    res = {}    
    data = {}
    data['pred_classes'] = predictions['pred_classes']
    data['score'] = predictions['scores']
    data['bbox'] = predictions['pred_boxes']
    data['superCategory'] = "part"
    data['imageWidth'] = 300
    data['imageHeight'] = 300   
    res['data'] = data    
    res['errorMessage'] = "Some error happened"
    res['responseCode'] = 200

    return res

def predict(image):
  im = image 
  outputs = predictor(im)
  predictions = outputs["instances"].to("cpu").get_fields()
  predictions['pred_boxes'] = [box.tolist() for box in predictions['pred_boxes']]
  predictions['pred_classes'] = predictions['pred_classes'].tolist()
  predictions['scores'] = predictions['scores'].tolist()
  return predictions

if __name__ == '__main__':
    #####
    ## Load here the model ##       
    #####
    cfg = get_cfg()
    cfg.merge_from_file(model_zoo.get_config_file("COCO-Detection/faster_rcnn_R_50_FPN_3x.yaml"))
    cfg.OUTPUT_DIR = "./output/"
    cfg.DATALOADER.NUM_WORKERS = 1
    cfg.MODEL.ROI_HEADS.NUM_CLASSES = 2
    cfg.MODEL.RETINANET.NUM_CLASSES = 2
    cfg.MODEL.DEVICE = 'cpu'
    cfg.MODEL.WEIGHTS = "./output/model_final.pth"
    cfg.MODEL.ROI_HEADS.SCORE_THRESH_TEST = 0.7   # set a custom testing threshold for this model
    predictor = DefaultPredictor(cfg)


    print("Starting...")
    app.run(debug = True,host='0.0.0.0') 
