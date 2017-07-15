# -*- coding: utf-8 -*-
"""
Created on Wed Jul 12 13:31:29 2017
"MODULE FOR DETECTING THE IMAGE AND DISPLAYING THE INFORMATION OF PERSON"
@author: Visharg Shah
"""
#importing dependencies:
import numpy as np
import cv2
from matplotlib import pyplot as plt
import sqlite3

#Opening the video cam:
cam = cv2.VideoCapture(0)

#making a lbph recognizer and loading the train model from previous module:
recognizer = cv2.face.createLBPHFaceRecognizer()
recognizer.load('recognizer/trainer.yml')

#creating classifier to detect the face:
facedetect = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#Creating the function to get the ID to get the information of detected face: 
def getID(ID):
    connection = sqlite3.connect("V:/Software/SQLiteStudio/FaceDatabase.db")
    cmd = "SELECT * FROM People where ID="+str(ID)
    details = connection.execute(cmd)
    profile = None
    for det in details:
        profile = det
    connection.close()
    return profile
    
#selecting the font style:
font = cv2.FONT_HERSHEY_PLAIN

#will detect the face and display all the information from databases:
while(cam.isOpened()):  # check !
    # capture frame-by-frame
    ret, img = cam.read()

    if ret: # check ! (some webcam's need a "warmup")
        # our operation on frame come here
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = facedetect.detectMultiScale(gray,1.3,5)
        for(x,y,w,h) in faces :       
            cv2.rectangle(img,(x,y), (x+w,y+h),(0,0,255),3)
            ID, conf = recognizer.predict(gray[y:y+h,x:x+w])
            profile = getID(ID)
            if(profile!=None):
                cv2.putText(img,"ID: "+str(profile[0]),(x,y+h+50),font,2,(0,255,0),2,cv2.LINE_AA)
                cv2.putText(img,"Name: "+str(profile[1]),(x,y+h+75),font,2,(0,255,0),2,cv2.LINE_AA)
                cv2.putText(img,"Age: "+str(profile[2]),(x,y+h+100),font,2,(0,255,0),2,cv2.LINE_AA)
                cv2.putText(img,"Gender: "+str(profile[3]),(x,y+h+125),font,2,(0,255,0),2,cv2.LINE_AA)
                cv2.putText(img,"Criminal Records: "+str(profile[4]),(x,y+h+150),font,2,(0,255,0),2,cv2.LINE_AA)
            
        cv2.imshow('Face', img) # Display the resulting frame
        if(cv2.waitKey(1)==ord('q')): #close the window by pressing q
            break;

#Close all the windows: 
cam.release()
cv2.destroyAllWindows()