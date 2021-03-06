"""
This is the file containing the algorithm used to control the motors (testing only)
"""

import math

class Ball:
    def __init__(self, position):
        self.position = position
        self.velocity = [0.0, 0.0]
        self.acceleration = [0.0, 0.0] # only used for simulation

        self.max_speed = 0.1 # units/frame
        self.min_speed = 0.01 # units/frame

        self.moving_x = True
        self.progress = 0
    
    # the board is not tilting
    
    def motor_zero_x(self):
        self.acceleration[0] = 0.0 # acceleration is set manually, only used for simulation

    def motor_zero_y(self):
        self.acceleration[1] = 0.0 # acceleration is set manually, only used for simulation

    # the ball moves in the x axis

    def motor_pos_x(self):
        self.acceleration[0] = 0.007 # units/(frame^2) acceleration is set manually, only used for simulation

    def motor_neg_x(self):
        self.acceleration[0] = -0.007 # units/(frame^2) acceleration is set manually, only used for simulation
    
    # the ball moves in the y axis

    def motor_pos_y(self):
        self.acceleration[1] = 0.007 # units/(frame^2) acceleration is set manually, only used for simulation

    def motor_neg_y(self):
        self.acceleration[1] = -0.007 # units/(frame^2) acceleration is set manually, only used for simulation

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

class BallMazeAlgorithm:
    def __init__(self, model):
        self.ball = model.ball
        self.nodes = model.nodes
        self.holes = model.holes
        
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

        # the game is lost

        if any(math.dist(self.ball.position, h) < 0.75 for h in self.holes):
            self.game_lost = True