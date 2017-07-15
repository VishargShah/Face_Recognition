# Face_Recognition
Detecting the face in real time video and displaying information of the detected faces.

Language -> Python3.6
Database -> Sqlite Studio


Used OpenCV + contrib modules for LBPH(Local Binary Patterns Histogram) face recognizer and Haar Cascade as classifier for front face.
You can download the wheel from here: http://www.lfd.uci.edu/~gohlke/pythonlibs/#opencv
Install it using pip install but before installing set the directory in the whl is present.

The project is divided into 3 modules.
1) dataset_creator.py
2) trainer.py
3) detector.py

dataset_creator.py ->
It ask user initially the data such as ID, Name, Age, Gender, Criminal Records.
Then it connects to the database and stores all the information into the database.
Then it takes the sample of images from the cam, I kept it as 20 images for one user.
This creates a basic dataset of the user.

trainer.py ->



