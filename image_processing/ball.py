
from dataclasses import dataclass
from turtle import distance
import cv2
import numpy
import time
import math

cam = cv2.VideoCapture(0)
s = numpy.ones((5 ,5), numpy.uint8)
rangomax = numpy.array([255, 50, 50]) 
rangomin = numpy.array([51, 0, 0])
T1 = time.time()
moving_data ={
}
n=0
while (True):
    n+=1
    ret, frame = cam.read()
    img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    mask = cv2.inRange(frame, rangomin, rangomax)
    blue = cv2.morphologyEx(mask, cv2.MORPH_OPEN, s)
    x, y, w, h = cv2.boundingRect(blue)
    cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 3)
    x_position = x+w/2
    y_position = y+h/2
    T2 = time.time()
    
    ball_data=[x_position, y_position,T2-T1]
    moving_data[n]= ball_data
    if n >= 10:
        Distance = math.sqrt(((moving_data[n][0]-moving_data[n-1][0])**2)+((moving_data[n][1]-moving_data[n-1][1])**2))
        Distance = Distance/44.4
        moving_speed = Distance /(moving_data[n][2]-moving_data[n-1][2])
    
        print(moving_speed)

    cv2.imshow('camera', frame)
    cv2.imshow('blue',blue)

    if cv2.waitKey(1) ==ord('q'):
        break


 
cam.release()
cv2.destroyAllWindows()
