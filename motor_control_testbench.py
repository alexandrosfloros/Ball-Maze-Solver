"""
This is the file used to run the algorithm independently (testing only)
"""

from motor_control_testing.simulation import *
from motor_control_testing.graphics import *

# initialising path nodes

easy_nodes = [
    [14.50, 23.00],
    [0.50, 23.00],
    [0.50, 13.00],
    [2.50, 13.00],
    [2.50, 16.50],
    [10.00, 16.50],
    [10.00, 9.00],
    [5.50, 9.00],
    [5.50, 10.50],
    [3.00, 10.50],
    [0.50, 7.50],
    [0.50, 0.50],
    [6.50, 0.50],
    [6.50, 6.50],
    [9.00, 6.50],
    [9.00, 3.50],
    [12.50, 3.50],
    [12.50, 6.00],
    [17.00, 6.00],
    [17.50, 9.50],
    [12.00, 9.50],
    [12.00, 15.00],#2
    [22.00, 15.00],
    [22.00, 19.00],
    [17.00, 23.00],
    [27.50, 23.00],
    [27.50, 19.00],
    [25.00, 17.50],
    [27.50, 12.50],
    [24.00, 8.50],
    [27.50, 0.50],
    [23.00, 0.50],
    [19.50, 6.00],
    [20.50, 0.50],
    [10.50, 0.50],
]

medium_nodes = [
    [16.00, 21.50],
    [5.50, 21.50],
    [5.50, 16.00],
    [7.00, 16.00],
    [7.00, 10.50],
    [1.00, 10.50],
    [1.00, 5.00],
    [8.00, 5.00],
    [8.00, 8.50],
    [11.50, 8.50],
    [11.50, 4.00],
    [13.50, 4.00],
    [13.50, 10.50],
    [11.00, 10.50],
    [11.00, 13.00],
    [9.50, 13.00],
    [9.50, 19.50],
    [12.50, 19.50],
    [12.50, 17.50],
    [19.00, 17.50],
    [19.00, 20.00],
    [26.50, 20.00],
    [26.50, 16.00],
    [21.50, 16.00],
    [21.50, 14.00],
    [19.00, 14.00],
    [19.00, 12.50],
    [17.50, 12.50],
    [17.50, 9.50],
    [20.00, 9.50],
    [20.00, 4.00],
    [21.50, 4.00],
    [21.50, 1.00],
    [10.50, 1.00]
]

hard_nodes = [
    [14.50, 22.00],
    [8.00, 22.00],
    [8.00, 20.50],
    [6.00, 20.50],
    [6.00, 22.00],
    [3.50, 22.00],
    [3.50, 20.00],
    [1.00, 20.00],
    [1.00, 17.00],
    [3.50, 17.00],
    [3.50, 15.00],
    [1.00, 15.00],
    [1.00, 13.00],
    [3.50, 13.00],
    [3.50, 9.00],
    [0.50, 9.00],
    [0.50, 7.00],
    [2.00, 7.00],
    [2.00, 4.50],
    [2.00, 0.50],
    [5.50, 0.50],
    [5.50, 2.50],
    [8.50, 2.50],
    [8.50, 5.50],
    [6.75, 5.50],
    [6.75, 8.50],
    [10.50, 8.50],
    [10.50, 12.50],
    [7.50, 12.50],
    [7.50, 14.50],
    [5.50, 14.50],
    [5.50, 17.00],
    [10.50, 17.00],
    [10.50, 19.50],
    [13.00, 19.50],
    [13.00, 16.50],
    [15.00, 16.50],
    [15.00, 12.50],
    [13.00, 12.50],
    [13.00, 9.00],
    [15.00, 9.00],
    [15.00, 7.00],
    [13.00, 7.00],
    [13.00, 5.00],
    [10.50, 5.00],
    [10.50, 1.00],
    [15.00, 1.00],
    [15.00, 4.50],
    [16.5, 4.50],
    [16.5, 5.75],
    [19.50, 5.75],
    [19.50, 1.00],
    [22.00, 1.00],
    [22.00, 4.50],
    [23.00, 4.50],
    [25.25, 4.50],
    [25.25, 7.50],
    [24.00, 7.50],
    [24.00, 11.50],
    [22.00, 11.50],
    [22.00, 8.50],
    [19.50, 8.50],
    [19.50, 9.75],
    [17.50, 9.75],
    [17.50, 12.75],
    [18.75, 12.75],
    [18.75, 14.50],
    [22.00, 14.50],
    [22.00, 16.50],
    [19.50, 16.50],
    [19.50, 20.00],
    [24.50, 20.00],
    [24.50, 16.00],
    [26.50, 16.00],
    [26.50, 13.00]
]

# initialising holes

easy_holes = [
    [3.1, 18.4],
    [5.50, 12.7],
    [3.1, 6.4],
    [17.2, 3.50],
    [14.9, 11.00],
    [17.2, 16.9],
    [23.9, 14.2],
    [23.9, 5.6]
]

medium_holes = [
    [3.00, 18.3],
    [7.9, 15.7],
    [5.50, 12.7],
    [5.50, 8.6],
    [3.1, 6.3],
    [5.6, 3.4],
    [10.3, 6.8],
    [17.2, 6.8],
    [14.9, 11.00],
    [12.50, 14.2],
    [7.9, 18.4],
    [15.00, 19.00],
    [21.6, 17.50],
    [17.2, 14.2],
    [23.9, 14.2],
    [23.9, 5.6]
]

hard_holes = [
    [1.00, 21.8],
    [1.00, 10.7],
    [1.00, 5.00],
    [3.4, 6.7],
    [3.4, 2.00],
    [3.4, 18.50],
    [5.7, 12.9],
    [5.7, 8.8],
    [5.7, 3.7],
    [5.7, 18.50],
    [8.00, 18.50],
    [8.00, 15.7],
    [8.00, 10.7],
    [8.00, 7.00],
    [8.00, 1.3],
    [10.3, 14.3],
    [10.3, 7.1],
    [12.6, 14.6],
    [12.6, 3.00],
    [15.00, 19.2],
    [15.00, 11.1],
    [15.00, 5.7],
    [17.3, 21.6],
    [17.3, 17.00],
    [17.3, 14.3],
    [17.3, 7.00],
    [17.3, 3.7],
    [17.3, 1.2],
    [19.6, 12.00],
    [21.9, 21.6],
    [21.9, 17.8],
    [21.9, 13.2],
    [21.9, 5.8],
    [24.2, 21.50],
    [24.2, 14.2],
    [24.2, 5.7],
    [24.2, 1.3],
    [26.50, 19.9],
    [26.50, 8.8],
    [26.50, 4.2]
]

if __name__ == "__main__":

    # initialising ball position

    x, y = hard_nodes[0]
    ball = Ball([x, y])

    # initialising graphics

    model = BallMazeModel(ball, hard_nodes, hard_holes)

    # initialising simulation

    animate_model(model)