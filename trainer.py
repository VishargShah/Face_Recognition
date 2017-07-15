# -*- coding: utf-8 -*-
"""
Created on Wed May 24 07:47:27 2017
"MODULE TO TRAIN THE MODEL OF SAMPLE IMAGES CREATED"
@author: Visharg Shah
"""
#importing dependencies:
import os
import cv2
import numpy as np
from PIL import Image

#creating recognizer using local binary pattern histogram:
recognizer = cv2.face.createLBPHFaceRecognizer()

#giving the path of images stored in face_dataset folder:
path = 'face_dataset'

#Creating the function to get the image and id of every image and train the model:
def getImageId(path):
    imgpaths = [os.path.join(path,f) for f in os.listdir(path)]
    faces = []
    ids = []
    for imgpath in imgpaths:
        faceimg = Image.open(imgpath).convert('L')
        facenp = np.array(faceimg,'uint8')
        ID = int(os.path.split(imgpath)[-1].split(".")[1])
        faces.append(facenp)
        ids.append(ID)
        cv2.imshow("training",facenp)
        cv2.waitKey(10)
    return np.array(ids) , faces

#using function to get the id and images:
ID , faces = getImageId(path)

#train the model:
recognizer.train(faces,ID)

#save the model in the recogizer folder:
recognizer.save("recognizer/trainer.yml")

#closing all the windows:
cv2.destroyAllWindows()
        
    

    
