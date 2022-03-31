"""
This is the file containing the algorithm used to control the motors (can be modified to communicate with the other parts)
"""

"""
Information from the BallMazeAlgorithm class:

Motor outputs:

Motor in the y axis (moves the ball in x):

Method                       | Motor angle (absolute)
self.ball.motor_zero_x()     | 0
self.ball.motor_pos_x()      | +theta
self.ball.motor_neg_x()      | -theta

Motor in the x axis (moves the ball in y):

Method                       | Motor angle (absolute)
self.ball.motor_zero_y()     | 0
self.ball.motor_pos_y()      | +theta
self.ball.motor_neg_y()      | -theta

where theta is a very small angle (small acceleration)

User interface outputs:

Attribute                    | Information
self.ball.position           | Ball position
self.ball.velocity           | Ball velocity
self.ball.next_node          | Ball destination
self.motor_state             | Motor position
"""
import math
from itertools import count
from turtle import distance, position
import cv2
import numpy
import time

# used for real motor implementation
import serial
from time import sleep
arduino = serial.Serial('COM3', 115200, timeout=0.5)
sleep(1)

class Ball:
    def __init__(self, position):
        self.position = position
        self.velocity = [0.0, 0.0]
        self.acceleration = [0.0, 0.0] # only used for simulation

        self.max_speed = 0.1 # units/frame
        self.min_speed = 0.01 # units/frame

        self.moving_x = True
        self.progress = 0
        self.moving_data ={}

        self.count = 0 
        self.cam = cv2.VideoCapture(0)


        self.s = numpy.ones((5 ,5), numpy.uint8)
        self.rangomax = numpy.array([110, 60, 25])  # BGR color 
        self.rangomin = numpy.array([30, 30, 0])  # BGR color 
        self.T1 = time.time()   
    
    # the board is not tilting  
    
    def motor_zero_x(self):
        self.motor_state = "ZERO_X"
        
        if self.simulated:
            self.acceleration[0] = 0.0 # acceleration is set manually, only used for simulation
        else:
            arduino.write(b'b') # the real motor is triggered here
            #print('x motor return to 0 degree')

    def motor_zero_y(self):
        self.motor_state = "ZERO_Y"

        if self.simulated:
            self.acceleration[1] = 0.0 # acceleration is set manually, only used for simulation
        else:
            arduino.write(b'e') # the real motor is triggered here
            #print('y motor return to 0 degree')
    # the ball moves in the x axis

    def motor_pos_x(self):
        self.motor_state = "POS_X"

        if self.simulated:
            self.acceleration[0] = 0.007 # units/(frame^2) acceleration is set manually, only used for simulation
        else:
            arduino.write(b'a')
            #print('x motor clockwise rotate 36 degrees') # the real motor is triggered here

    def motor_neg_x(self):
        self.motor_state = "NEG_X"

        if self.simulated:
            self.acceleration[0] = -0.007 # units/(frame^2) acceleration is set manually, only used for simulation
        else:
            arduino.write(b'c')
            #print('x motor anti-clockwise rotate 36 degrees') # the real motor is triggered here
    
    # the ball moves in the y axis

    def motor_pos_y(self):
        self.motor_state = "POS_Y"

        if self.simulated:
            self.acceleration[1] = 0.007 # units/(frame^2) acceleration is set manually, only used for simulation
        else:
            arduino.write(b'f')
            #print('y motor clockwise rotate 36 degrees')# the real motor is triggered here

    def motor_neg_y(self):
        self.motor_state = "NEG_Y"

        if self.simulated:
            self.acceleration[1] = -0.007 # units/(frame^2) acceleration is set manually, only used for simulation
        else:
            arduino.write(b'd')
            #print('y motor anti-clockwise rotate 36 degrees') # the real motor is triggered here

    # the ball is balanced as it moves in the x axis

    def balance_x(self):

        # once the ball reaches an approximately zero speed, the board stops tilting

        if self.velocity[0] > self.min_speed:
            self.motor_neg_x()
        elif self.velocity[0] < -1 * self.min_speed:
            self.motor_pos_x()
        else:
            self.motor_zero_x()

            self.stop_x()

    # the ball is balanced as it moves in the y axis

    def balance_y(self):

        # once the ball reaches an approximately zero speed, the board stops tilting

        if self.velocity[1] > self.min_speed:
            self.motor_neg_y()
        elif self.velocity[1] < -1 * self.min_speed:
            self.motor_pos_y()
        else:
            self.motor_zero_y()
            
            self.stop_y()

    # the ball is successfully stopped in the x axis

    def stop_x(self):
        self.moving_x = False

    # the ball is successfully stopped in the y axis

    def stop_y(self):
        self.moving_x = True
        self.progress += 1

    def cal_speed(self):
            self.count+=1
            ball_data = [self.position[0],self.position[1],self.time]
            self.moving_data[self.count] = ball_data
            if self.count >= 10: # calculate the speed 
                x_Distance = abs(self.moving_data[self.count][0]-self.moving_data[self.count-9][0])
                y_Distance = abs(self.moving_data[self.count][1]-self.moving_data[self.count-9][1])
                self.velocity[0] = x_Distance / (self.moving_data[self.count][2]-self.moving_data[self.count-9][2])
                self.velocity[1] = y_Distance / (self.moving_data[self.count][2]-self.moving_data[self.count-9][2])
                del self.moving_data[self.count-9]
            if self.velocity[0]<0.3:
                self.velocity[0]=0
            elif self.velocity[1]<0.3:
                self.velocity[1]=0
            elif  self.velocity[0] > 15 or self.velocity[1] >15:
                self.velocity = [0,0]
                

            return self.velocity
    def cal_position(self): 
            ret, frame = self.cam.read()
                                 # image read 
            mask = cv2.inRange(frame, self.rangomin, self.rangomax)               # get blue pixel on the image 
            blue = cv2.morphologyEx(mask, cv2.MORPH_OPEN, self.s)            # creat a image of blue-pixel only 
            x, y, w, h = cv2.boundingRect(blue)                         # get blue pixel location 
 
            position = [((x+w/2-98)/18),(23.5-(y+h/2-37)/18)]
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 3)
            if position[0] < 0:
                position[0]=0 
            if position[1] < 0:
                position[1] = 0 
            cv2.imshow('camera', frame)
            return position


class BallMazeAlgorithm:
    def __init__(self, model, simulated):
        self.ball = model.ball
        self.nodes = model.nodes
        self.holes = model.holes
        self.ball.simulated = simulated

        self.limit = len(self.nodes)
        self.node_tolerance = 1.0 # units
        self.game_won = False
        self.game_lost = False
    
    """
    The following algorithm is being run every single frame and uses the ball position
    and velocity methods, the value of which is obtained from the image processing
    """

    def run(self):

        # coordinates of the next node

        self.ball.next_node = self.nodes[self.ball.progress]
        xn, yn = self.ball.next_node

        # coordinates of the ball

        xb, yb = self.ball.position

        # the ball moves in a different axis every time

        if self.ball.moving_x:
            if xb < xn:

                # once the ball reaches a certain speed, the board stops tilting

                if self.ball.velocity[0] > self.ball.max_speed:
                    self.ball.motor_zero_x()
                else:
                    self.ball.motor_pos_x()
            else:

                # once the ball reaches a certain speed, the board stops tilting

                if self.ball.velocity[0] < -1 * self.ball.max_speed:
                    self.ball.motor_zero_x()
                else:
                    self.ball.motor_neg_x()
                
            # the ball is close to the current node and the algorithm attempts to immobilise it in the x axis

            if abs(xb - xn) < self.node_tolerance:
                    self.ball.balance_x()
        else:
            if yb < yn:

                # once the ball reaches a certain speed, the board stops tilting

                if self.ball.velocity[1] > self.ball.max_speed:
                    self.ball.motor_zero_y()
                else:
                    self.ball.motor_pos_y()
            else:

                # once the ball reaches a certain speed, the board stops tilting

                if self.ball.velocity[1] < -1 * self.ball.max_speed:
                    self.ball.motor_zero_y()
                else:
                    self.ball.motor_neg_y()
                
            # the ball is close to the current node and the algorithm attempts to immobilise it in the y axis

            if abs(yb - yn) < self.node_tolerance:
                self.ball.balance_y()

                # the game is won

                if self.ball.progress == self.limit:
                    self.game_won = True
                elif (self.nodes[-2][0] -0.5 <= self.ball.position[0] <= self.nodes[-2][0] + 0.5) and (self.nodes[-2][1] -0.5 <= self.ball.position[1] <= self.nodes[-2][1] + 0.5):
                    self.game_won = True

        # the game is lost

        if any(math.dist(self.ball.position, h) < 0.25 for h in self.holes):
            self.game_lost = True
