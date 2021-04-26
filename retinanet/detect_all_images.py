# import keras_retinanet
from keras_retinanet import models
from keras_retinanet.utils.image import read_image_bgr, preprocess_image, resize_image
from keras_retinanet.utils.visualization import draw_box, draw_caption
from keras_retinanet.utils.colors import label_color
from keras_retinanet.utils.gpu import setup_gpu

# import miscellaneous modules
import cv2
import os
import numpy as np
import time
import argparse
from datetime import datetime 
import json
from tqdm import tqdm

import tensorflow as tf
import logging
tf.get_logger().setLevel(logging.ERROR)


model_interface_name = 'teknofest19_huma_resnet50_21_37_inference.h5'
thresh = 0.22

model_path = os.path.join('models', '', model_interface_name)
model = models.load_model(model_path, backbone_name='resnet50')

labels_to_names = {0: 'arac', 1: 'yaya'}

if not os.path.exists('results/'):
    os.mkdir('results/')

dt_now = datetime.now().strftime("%Y%m%d_%H%M%S")
results_path = os.path.join("results/", "{0}_{1}".format(dt_now, model_interface_name))
os.mkdir(results_path)


images_root_folder = "../dataset_test/"

# load retinanet model
model = models.load_model(model_path, backbone_name='resnet50')

sdd_images = os.listdir(images_root_folder)
sdd_images = sorted(sdd_images, key=lambda name: int(name[:-4]))

##sdd_images=sdd_images[20:120]

results_json = []
index = 0

start = time.time()
for image_filename in tqdm(sdd_images):
    #print("image_filename",image_filename)
    image = read_image_bgr(images_root_folder + image_filename)
    # copy to draw on
    draw = image.copy()
    draw = cv2.cvtColor(draw, cv2.COLOR_BGR2RGB)

    # preprocess image for network
    image = preprocess_image(image)
    image, scale = resize_image(image)

    # process image
    boxes, scores, labels = model.predict_on_batch(np.expand_dims(image, axis=0))
    
    boxes /= scale


    frame_json = {}

    frame_json["frame_id"] = int(image_filename.replace(".jpg","").replace("../dataset_test/",""))
    frame_json["nesneler"] = []
        
    
    # visualize detections
    for box, score, label in zip(boxes[0], scores[0], labels[0]):
        #print(box, score, label)
        # scores are sorted so we can break
        if score < thresh:
            break

        #color = label_color(label)
        colors = [[255,172,31], [161, 222, 251]]
        color = colors[label]

        landing_status = -1 #inis_durumunis

        b = box.astype(int)
        
        if labels_to_names[label] == "arac":
            draw_box(draw, b, color=color)
            #print("label",labels_to_names[label])
            #print("score",score)
            #caption = "{} {:.3f}".format(labels_to_names[label], score)
            caption = "{} {:.2f}%".format(labels_to_names[label], score*100)
            draw_caption(draw, b, caption, color=color)

        #JSON ADD
        if labels_to_names[label] == "arac":
            frame_json["nesneler"].append({
                "sinif": int(label), 
                "inis_durumu": landing_status,
                "sinirlayici_kutu": {
                    "ust_sol": {
                        "x":int(box[0]), 
                        "y":int(box[1]), 
                    },
                    "alt_sag": {
                        "x":int(box[2]), 
                        "y":int(box[3]), 
                    }
                }
            }) 
    
    
    results_json.append(frame_json)


    file_, ext = os.path.splitext(image_filename)
    image_name = file_.split('/')[-1] + ext
    output_path = os.path.join(results_path, image_name)
    
    draw_conv = cv2.cvtColor(draw, cv2.COLOR_BGR2RGB)
    cv2.imwrite(output_path, draw_conv)

#results = {}
#results["cevaplar"] = results_json

#SAVE RESULT JSON
with open('{0}/results_{1}.json'.format(results_path,dt_now), 'w') as fp:
    json.dump(results_json, fp)

#SAVE RESULT JSON
#with open('{0}/results_{1}_toplu.json'.format(results_path,dt_now), 'w') as fp:
#    json.dump(results, fp)
