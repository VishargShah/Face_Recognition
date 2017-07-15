# -*- coding: utf-8 -*-
"""
Created on Tue May 23 12:05:25 2017
"MODULE TO CREATE THE SAMPLE OF USER DATA AND IMAGES"
@author: Visharg Shah
"""
#import dependencies:
import numpy as np
import cv2
from matplotlib import pyplot as plt
import sqlite3

#user data input:
ID = input("Enter the ID:  ")
Name = input("Enter the name : ")
Age = input("Enter your Age : ")
Gender = input("Enter your Gender : ")
Criminal = input("Any Criminal Records (Y/N):")

#creating variable for taking no. of photos:
samplenum = 0

#starting the video cam:
cam = cv2.VideoCapture(0)

#using Haar Cascade for creating classifier for front face:
facedetect = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#Creating function to connect the database and add the values into database ID is unique field:
def update(ID, Name, Age, Gender, Criminal) :
    connection = sqlite3.connect("V:/Software/SQLiteStudio/FaceDatabase.db")
    cmd = "SELECT * FROM People WHERE ID="+str(ID)
    details = connection.execute(cmd)
    recordexist = 0
    for row in details:
        recordexist = 1
    if(recordexist==1):
        cmd = "UPDATE People SET Name="+str(Name)+", Age="+str(Age)+", Gender="+str(Gender)+", CriminalRecords="+str(Criminal)+" WHERE ID=" + str(ID)
    else:
        cmd = "INSERT into People(ID,Name,Age,Gender,CriminalRecords) values (?,?,?,?,?)"
        par = (ID,Name,Age,Gender,Criminal)
        connection.execute(cmd,par)
        connection.commit()
        connection.close()

#Adding data from user into database:            
update(ID,Name,Age,Gender,Criminal)

#Capturing the image from video cam:
while(cam.isOpened()):  # check !
    # capture frame-by-frame
    ret,img = cam.read()

    if ret: # check ! (some webcam's need a "warmup")
        # our operation on frame come here
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = facedetect.detectMultiScale(gray,1.2,5)
        for(x,y,w,h) in faces :
            samplenum = samplenum+1
            cv2.rectangle(img,(x,y), (x+w, y+h),(0,255,0),2)
            cv2.imwrite("face_dataset/User." + str(ID)+ "." +str(samplenum)+".jpg",gray[y:y+h,x:x+w])
        cv2.imshow('face',img) # Display the resulting frame
        cv2.waitKey(1)
        if(samplenum>20): #Creating the sample of 20 images which will be stored in face_dataset folder 
            break;
           
# When everything is done release the capture
cam.release()
cv2.destroyAllWindows()