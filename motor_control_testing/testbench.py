"""
This is the file used to run the algorithm independently (testing only)
"""

from simulation import *

# initialising path nodes

nodes = [
    [0.5, 1.0], # starting point
    [1.0, 1.25],
    [1.5, 1.25],
    [2, 1.0],
    [2.5, 0.75],
    [3.0, 1.0],
    [3.75, 1.25],
    [4.0, 2.0],
    [3.75, 2.75],
    [3.0, 3.0],
    [2.5, 2.75],
    [2.0, 3.0],
    [1.5, 2.75],
    [1.0, 2.75],
    [0.5, 3.0],
    [0.5, 4.0],
    [1.0, 4.5],
    [1.5, 4.5],
    [1.75, 4.25],
    [2.0, 4.0],
    [2.5, 3.75],
    [3.0, 4.0],
    [3.5, 4.5],
    [4.0, 4.5],
    [4.5, 4.0],
    [4.5, 3.5],
    [4.25, 3.0],
    [4.25, 2.25] # ending point
]

# initialising ball position

ball = Ball([1.25, 0.5])

# initialising graphics

model = BallMazeModel(ball, nodes)

# initialising simulation

animate_model(model)