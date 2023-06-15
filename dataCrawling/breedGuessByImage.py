from urllib import request
from io import BytesIO
from PIL import Image
import cv2
import tensorflow as tf
import numpy as np
import json
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

resnet50_pre = tf.keras.applications.resnet.ResNet50(weights='imagenet',input_shape=(224,224,3))

def pred_img(img):
  img_resized = cv2.resize(np.array(img),(224,224))
  pred = resnet50_pre.predict(img_resized.reshape([1,224,224,3]))
  decoded_pred = tf.keras.applications.imagenet_utils.decode_predictions(pred)
  return decoded_pred[0][0][1] + " : " + str(decoded_pred[0][0][2]*100)[:4] + "% 가능성"

def jsonOpen(directory):
    with open(directory, "r") as f:
        data = json.load(f)
    return data
def jsonSave(directory,result):
    with open(directory, "w") as f:
        json.dump(result, f, ensure_ascii=False,indent=4)

targetImageLink = jsonOpen('resultFromInstagramAddInfo copy.json')
result = []
for i in targetImageLink:
    url = i["imageLink"]
    if url != None:
    # request.urlopen()
        res = request.urlopen(url).read()

        # Image open
        img = Image.open(BytesIO(res))
        predictResult = pred_img(img)
        i['breed'] = 'AI예측 : ' + predictResult
        result.append(i)
jsonSave('resultFromInstagramAddInfo.json',result)
