"""
This is the file used to run the algorithm independently (testing only)
"""

from simulation import *
from graphics import *

# initialising path nodes

easy_nodes = [
    [12.5, 22.0],
    [1.0, 22.0],
    [1.0, 16.0],
    [6.0, 16.0],
    [10.0, 16.0],
    [10.0, 9.5],
    [3.0, 9.5],
    [3.0, 7.5],
    [1.5, 7.5],
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
    [25.0, 14.5],
    [25.0, 12.5],
    [23.5, 12.5],
    [23.5, 8.5],
    [26.5, 8.5],
    [26.5, 1.5],
    [22.0, 1.5],
    [22.0, 4.5],
    [20.0, 4.5],
    [20.0, 1.0],
    [10.5, 1.0]
]

medium_nodes = [
    [16.0, 21.5],
    [5.5, 21.5],
    [5.5, 16.0],
    [7.0, 16.0],
    [7.0, 10.5],
    [1.0, 10.5],
    [1.0, 5.0],
    [8.0, 5.0],
    [8.0, 8.5],
    [11.5, 8.5],
    [11.5, 4.0],
    [13.5, 4.0],
    [13.5, 10.5],
    [11.0, 10.5],
    [11.0, 13.0],
    [9.5, 13.0],
    [9.5, 19.5],
    [12.5, 19.5],
    [12.5, 17.5],
    [19.0, 17.5],
    [19.0, 20.0],
    [26.5, 20.0],
    [26.5, 16.0],
    [21.5, 16.0],
    [21.5, 14.0],
    [19.0, 14.0],
    [19.0, 12.5],
    [17.5, 12.5],
    [17.5, 9.5],
    [20.0, 9.5],
    [20.0, 4.0],
    [21.5, 4.0],
    [21.5, 1.0],
    [10.5, 1.0]
]

hard_nodes = [
    [14.5, 22.0],
    [8.0, 22.0],
    [8.0, 20.5],
    [6.0, 20.5],
    [6.0, 22.0],
    [3.5, 22.0],
    [3.5, 20.0],
    [1.0, 20.0],
    [1.0, 17.0],
    [3.5, 17.0],
    [3.5, 15.0],
    [1.0, 15.0],
    [1.0, 13.0],
    [3.5, 13.0],
    [3.5, 9.0],
    [2.5, 9.0],
    [0.5, 7.0],
    [3.0, 4.5],
    [1.5, 2.5],
    [2.0, 1.0],
    [5.0, 1.0],
    [7.0, 2.5],
    [8.5, 4.0],
    [8.5, 6.0],
    [6.5, 6.0],
    [6.5, 7.5],
    [7.5, 8.5],
    [10.5, 9.0],
    [10.5, 12.5],
    [8.0, 13.0],
    [5.5, 14.5],
    [5.5, 17.0],
    [10.5, 17.0],
    [10.5, 19.5],
    [13.0, 19.5],
    [13.0, 16.5],
    [15.0, 16.5],
    [15.0, 12.5],
    [13.0, 12.5],
    [13.0, 9.0],
    [15.0, 9.0],
    [15.0, 7.0],
    [13.0, 7.0],
    [13.0, 5.0],
    [10.5, 5.0],
    [10.5, 1.0],
    [15.0, 1.0],
    [15.0, 4.0],
    [17.0, 5.0],
    [19.5, 5.5],
    [19.5, 1.0],
    [22.0, 1.0],
    [22.0, 4.0],
    [23.0, 4.5],
    [24.5, 4.5],
    [26.0, 6.0],
    [26.0, 7.5],
    [24.0, 7.5],
    [24.0, 11.5],
    [22.0, 11.5],
    [22.0, 8.5],
    [19.5, 8.5],
    [19.5, 9.5],
    [17.5, 9.5],
    [17.5, 12.0],
    [19.5, 14.5],
    [22.0, 14.5],
    [22.0, 16.5],
    [19.5, 16.5],
    [19.5, 20.0],
    [24.5, 20.0],
    [24.5, 16.0],
    [26.5, 16.0],
    [26.5, 13.0]
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
    [3.0, 18.3],
    [7.9, 15.7],
    [5.5, 12.7],
    [5.5, 8.6],
    [3.1, 6.3],
    [5.6, 3.4],
    [10.3, 6.8],
    [17.2, 6.8],
    [14.9, 11.0],
    [12.5, 14.2],
    [7.9, 18.4],
    [15.0, 19.0],
    [21.6, 17.5],
    [17.2, 14.2],
    [23.9, 14.2],
    [23.9, 5.6]
]

hard_holes = [
    [1.0, 21.8],
    [1.0, 10.7],
    [1.0, 5.0],
    [3.4, 6.7],
    [3.4, 2.0],
    [3.4, 18.5],
    [5.7, 12.9],
    [5.7, 8.8],
    [5.7, 3.7],
    [5.7, 18.5],
    [8.0, 18.5],
    [8.0, 15.7],
    [8.0, 10.7],
    [8.0, 7.0],
    [8.0, 1.3],
    [10.3, 14.3],
    [10.3, 7.1],
    [12.6, 14.6],
    [12.6, 3.0],
    [15.0, 19.2],
    [15.0, 11.1],
    [15.0, 5.7],
    [17.3, 21.6],
    [17.3, 17.0],
    [17.3, 14.3],
    [17.3, 7.0],
    [17.3, 3.7],
    [17.3, 1.2],
    [19.6, 12.0],
    [21.9, 21.6],
    [21.9, 17.8],
    [21.9, 13.2],
    [21.9, 5.8],
    [24.2, 21.5],
    [24.2, 14.2],
    [24.2, 5.7],
    [24.2, 1.3],
    [26.5, 19.9],
    [26.5, 8.8],
    [26.5, 4.2]
]

# initialising ball position

x, y = medium_nodes[0]
ball = Ball([x, y])

# initialising graphics

model = BallMazeModel(ball, medium_nodes, medium_holes)

# initialising simulation

animate_model(model)