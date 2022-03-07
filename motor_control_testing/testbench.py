"""
This is the file used to run the algorithm independently (testing only)
"""

from simulation import *

# initialising path nodes

easy_nodes = [
    [12.5, 22.0], # starting node
    [1.5, 22.0],
    [1.0, 12.5],
    [3.0, 12.5],
    [3.0, 16.0],
    [3.0, 16.0],
    [10.0, 16.0],
    [10.0, 9.5],
    [4.0, 9.5],
    [1.5, 7.0],
    [1.5, 3.0],
    [6.5, 3.0],
    [6.5, 6.0],
    [9.0, 6.0],
    [9.0, 3.5],
    [12.5, 3.5],
    [12.5, 6.0],
    [17.0, 6.0],
    [17.0, 9.0],
    [13.0, 9.0],
    [13.0, 14.0],
    [20.5, 14.0],
    [20.5, 19.0],
    [17.5, 19.0],
    [17.5, 21.5],
    [25.0, 21.5],
    [25.0, 17.0],
    [26.5, 14.5],
    [25.0, 12.5],
    [24.0, 11.0],
    [24.0, 8.5],
    [26.5, 8.5],
    [26.0, 1.5],
    [22.0, 1.5],
    [22.0, 4.5],
    [20.0, 5.5],
    [20.0, 1.0],
    [10.5, 1.0] # ending node
]

medium_nodes = [

]

hard_nodes = [
    
]

# initialising holes

easy_holes = [
    [3.1, 18.4],
    [5.5, 12.7],
    [3.1, 6.4],
    [17.2, 3.5],
    [14.9, 11.0],
    [17.2, 16.9],
    [23.9, 14.2],
    [23.9, 5.6]
]

medium_holes = [

]

hard_holes = [

]

# initialising ball position

ball = Ball([12.5, 22.0])

# initialising graphics

model = BallMazeModel(ball, easy_nodes, easy_holes)

# initialising simulation

animate_model(model)