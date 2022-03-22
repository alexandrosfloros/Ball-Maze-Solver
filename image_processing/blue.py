
from turtle import distance
import cv2
import numpy
import time
import math

cam = cv2.VideoCapture(2)
s = numpy.ones((5 ,5), numpy.uint8)
rangomax = numpy.array([140,90,13])
rangomin = numpy.array([20, 11, 0]) 
T1 = time.time()
moving_data ={}
n=0

def mouse_detect(event, x, y, flags, param):
    global mouse_x, mouse_y
    if event == cv2.EVENT_LBUTTONDBLCLK:
        print('({}, {})'.format(x, y))




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
        Distance = math.sqrt(((moving_data[n][0]-moving_data[n-9][0])**2)+((moving_data[n][1]-moving_data[n-9][1])**2))
        Distance = Distance/18
        moving_speed = Distance /(moving_data[n][2]-moving_data[n-9][2])
        if moving_speed <1:
            moving_speed = 0
        elif moving_speed > 20:
            moving_speed = 0
        
        moving_speed = int(moving_speed)
        #print(moving_speed)
        if x_position >= 98 and y_position >= 37:
            x_position_cm = int((x_position-98)/18)
            y_position_cm = 23 - int((y_position-37)/18)
            print(x_position_cm,y_position_cm,moving_speed)

    cv2.imshow('camera', frame)
    cv2.setMouseCallback('camera',mouse_detect)
    cv2.imshow('blue',blue)


    if cv2.waitKey(1) ==ord('q'):
        break


 
cam.release()
cv2.destroyAllWindows()
