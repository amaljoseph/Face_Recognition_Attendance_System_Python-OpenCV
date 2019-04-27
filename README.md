# Face Recogntion Based Attendance System
An attendance system which could automatically mark attendance from iamges of students. This project uses Python, OpenCV and SQLite3 as database. An image of a class could be given as input and system detects indivuals in the image. Database is updated to mark attendance to students preset. Attendance Reports could be generated for more insights.


There are 2 parts in this attendance system.
  1. Face Detection and Recogniton (explained in detail [here](https://github.com/amaljoseph/python-opencv-multiple-face-recognition).)
  2. Database operations and attendance report generations.
  
## Requirements
1. [Python 2.7.x](https://www.python.org/downloads/)

2. [OpenCV 2](https://opencv.org/releases/) `sudo apt-get install libopencv-dev python-opencv`

3. [Numpy](https://www.numpy.org/) `sudo apt-get install python-numpy`

4. [SQLite3](https://www.sqlite.org/download.html) `pip install pysqlite`

## How to run?
To run the program, in terminal type `python ui.py`

The photos of each individual should be stored in a folder s[i] (example - s1, s2 etc) inside the training-data folder.
Test images are stored in test-data folder.

Initailly train the system using option 1 (Mark the attendance). It takes in all the student images and train the system. On later stages attendance could be marked using option 1 again.

Option 2 could be selected to view the attendance list.

Option 3 could be seleted to generate an attendance report. 

Use option 4 to close the terminal.

The face detection and recognition part is explained in detail [here](https://github.com/amaljoseph/python-opencv-face-recognition)

This project is done by [amaljoseph](https://github.com/amaljoseph/), [irksomeorangutan](https://github.com/irksomeorangutan), Kishan Chand and Amal Satheesh.
