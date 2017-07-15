# Face_Recognition
Detecting the face in real time video and displaying information of the detected faces.

Language -> Python3.6,
Database -> Sqlite Studio


Used OpenCV + contrib modules for LBPH(Local Binary Patterns Histogram) face recognizer and Haar Cascade as classifier for front face. Please chcek the file haarcascade_frontalface_default.xml for detecting front face.

You can download the wheel from here: http://www.lfd.uci.edu/~gohlke/pythonlibs/#opencv , 
Install it using pip install, but before installing set the directory in the whl is present.

The project is divided into 3 modules.
1) dataset_creator.py
2) trainer.py
3) detector.py

dataset_creator.py ->
It ask user initially the data such as ID(Unique), Name, Age, Gender, Criminal Records.
Then it connects to the database and stores all the information into the database.
Then it takes the sample of images from the cam, I kept it as 20 images for one user.
This creates a basic dataset of the user.

trainer.py ->
It will first take all the Images and ID from the database.
It will then train the recognizer model using LBPH recognizer and save the model.

detector.py ->
It will load the model and then recognize the face using LBPH recognizer.
Also training model has ID so from Images it will get the ID and then will get all the information from the database and display it.

Check the output image for single and multi face in the file above.

Thanks!






