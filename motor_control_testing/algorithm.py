"""
This is the file containing the algorithm used to control the motors (testing only)
"""

"""
Information from the Ball class:

Motor outputs:

Motor in the y axis (moves the ball in x):

Method           | Motor angle (absolute)
self.equal_x()   | 0
self.move_xpos() | +theta
self.move_xneg() | -theta

Motor in the x axis (moves the ball in y):

Method           | Motor angle (absolute)
self.equal_y()   | 0
self.move_xpos() | +theta
self.move_xneg() | -theta

where theta is a very small angle (small acceleration)

Display outputs:

Attribute        | Information
self.position    | Ball position
self.next_node   | Ball destination
"""

class Ball:
    def __init__(self, position):
        self.position = position
        self.velocity = [0.0, 0.0]
        self.acceleration = [0.0, 0.0] # only used for simulation

        self.max_speed = 0.02 # units/frame
        self.min_speed = 0.002 # units/frame

        self.moving_x = True
        self.progress = 0
    
    # the board is not tilting
    
    def equal_x(self):
        self.acceleration[0] = 0.0 # acceleration is set manually, only used for simulation

    def equal_y(self):
        self.acceleration[1] = 0.0 # acceleration is set manually, only used for simulation

    # the ball moves in the x axis

    def move_xpos(self):
        self.acceleration[0] = 0.0008 # acceleration is set manually, only used for simulation

    def move_xneg(self):
        self.acceleration[0] = -0.0008 # acceleration is set manually, only used for simulation
    
    # the ball moves in the y axis

    def move_ypos(self):
        self.acceleration[1] = 0.0008 # acceleration is set manually, only used for simulation

    def move_yneg(self):
        self.acceleration[1] = -0.0008 # acceleration is set manually, only used for simulation

    # the ball is balanced as it moves in the x axis

    def balance_x(self):

        # once the ball reaches an approximately zero speed, the board stops tilting

        if self.velocity[0] > self.min_speed:
            self.move_xneg()
        elif self.velocity[0] < -1 * self.min_speed:
            self.move_xpos()
        else:
            self.equal_x()

            self.stop_x()

    # the ball is balanced as it moves in the y axis

    def balance_y(self):

        # once the ball reaches an approximately zero speed, the board stops tilting

        if self.velocity[1] > self.min_speed:
            self.move_yneg()
        elif self.velocity[1] < -1 * self.min_speed:
            self.move_ypos()
        else:
            self.equal_y()
            
            self.stop_y()

    # the ball is successfully stopped in the x axis

    def stop_x(self):
        self.moving_x = False

    # the ball is successfully stopped in the y axis

    def stop_y(self):
        self.moving_x = True
        self.progress += 1

class BallMazeAlgorithm:
    def __init__(self, ball, nodes):
        self.ball = ball
        self.nodes = nodes
        self.limit = len(self.nodes)
        self.node_tolerance = 0.2 # units
    
    """
    The following algorithm is being run every single frame and uses the ball position
    and velocity methods, the value of which is obtained from the image processing
    """

    def run(self):
        if self.ball.progress < self.limit:

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
                        self.ball.equal_x()
                    else:
                        self.ball.move_xpos()
                else:

                    # once the ball reaches a certain speed, the board stops tilting

                    if self.ball.velocity[0] < -1 * self.ball.max_speed:
                        self.ball.equal_x()
                    else:
                        self.ball.move_xneg()
                
                # the ball is close to the current node and the algorithm attempts to immobilise it in the x axis

                if abs(xb - xn) < self.node_tolerance:
                    self.ball.balance_x()
            else:
                if yb < yn:

                    # once the ball reaches a certain speed, the board stops tilting

                    if self.ball.velocity[1] > self.ball.max_speed:
                        self.ball.equal_y()
                    else:
                        self.ball.move_ypos()
                else:

                    # once the ball reaches a certain speed, the board stops tilting

                    if self.ball.velocity[1] < -1 * self.ball.max_speed:
                        self.ball.equal_y()
                    else:
                        self.ball.move_yneg()
                
                # the ball is close to the current node and the algorithm attempts to immobilise it in the y axis

                if abs(yb - yn) < self.node_tolerance:
                    self.ball.balance_y()

                    # the ball moves back to the starting node, only used for simulation

                    if self.ball.progress == self.limit:
                        self.ball.progress = 0