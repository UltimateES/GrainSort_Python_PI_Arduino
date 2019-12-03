import matplotlib
import time
import cv2
import pandas as pd
x=cv2.imread("Capture.PNG")
cv2.imshow("fczxczfdf",x)
cv2.waitKey(255)
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import serial
import signal
import sys
import time
from time import gmtime, strftime
from sys import exit
from picamera.array import PiRGBArray
from picamera import PiCamera


import numpy as np

from array import *
 
# initialize the camera and grab a reference to the raw camera capture
camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(640, 480))
 
# allow the camera to warmup
time.sleep(1)
port = serial.Serial("/dev/ttyACM1", baudrate=9600, timeout=3.0)
port.write('A')
time.sleep(2)
# capture frames from the camera
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
	image = frame.array
	# show the frame
	cv2.imshow("Frame", image)
	cv2.imwrite('raw.jpg',image)
	key = cv2.waitKey(1) & 0xFF
 
	# clear the stream in preparation for the next frame
	rawCapture.truncate(0)
 
	# if the `q` key was pressed, break from the loop
	if key == ord("q"):
		break
image = cv2.imread('raw.jpg')
cv2.waitKey(0)
clone = image.copy()
roi = clone[80:390, 75: 480]
cv2.imshow("ROI", roi)
cv2.imwrite('ROI.jpg',roi)
cv2.waitKey(0)
img = cv2.imread('ROI.jpg',cv2.IMREAD_GRAYSCALE)
cv2.imshow("Selected Region",img)
cv2.waitKey(0)
ret,thresh = cv2.threshold(img,100,255,0)
cv2.imshow("ThreshholdImage",thresh)
im,cnt,hierarchy = cv2.findContours(thresh, 1, 2)
i=0;
size=[]
mid_quality=0;
low_quality=0;
high_quality=0;
for c in cnt:
    area = cv2.contourArea(c)
    if area<=40:
            low_quality+=1;
    if area>40 and area<=60:
            mid_quality+=1;
    if area>60:
            high_quality+=1;
    size.append(area)
    (x, y, w, h) = cv2.boundingRect(c)
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 255, 0), 1)
print(size)
print(mid_quality)
print(high_quality)
print(low_quality)
EstimateSize=np.mean(size)
print(EstimateSize)
cv2.waitKey(0)
import matplotlib.pyplot as plt

# The slices will be ordered and plotted counter-clockwise.
sizes = [low_quality, mid_quality, high_quality]
labels = 'Low Quality Grain Count = '+ str(sizes[0]),'Mid Quality Grain Count = '+ str(sizes[1]), 'High Quality Grain Count = '+ str(sizes[2])

colors = ['red', 'yellow', 'green']
explode = (0.02, 0.03, 0.04)  # only "explode" the 2nd slice (i.e. 'Hogs')

plt.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=90)
# Set aspect ratio to be equal so that pie is drawn as a circle.
plt.axis('equal')

plt.show()
if EstimateSize>58:
        port.write('B')
        time.sleep(5)
if EstimateSize<=58 and EstimateSize>40 :
        port.write('C')
        time.sleep(10)
if EstimateSize<=40:
        port.write('D')
        time.sleep(5)     
cv2.waitKey(0)
# close all open windows
cv2.destroyAllWindows()	

