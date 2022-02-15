"""
This is the file used to simulate the maze using the algorithm independently (testing only)
"""

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

from graphics import *
from algorithm import *

def animate_model(model):
    fig = plt.figure()
    ax = fig.add_axes([0, 0, 1, 1])

    time = -1

    # initialising algorithm

    def init():
        global algorithm
        algorithm = BallMazeAlgorithm(model.ball, model.nodes)

        return model.init_path(ax)

    # updating algorithm in every frame

    def update(frame_number):
        algorithm.ball.position[0] += algorithm.ball.velocity[0]
        algorithm.ball.position[1] += algorithm.ball.velocity[1]
        
        algorithm.ball.velocity[0] += algorithm.ball.acceleration[0]
        algorithm.ball.velocity[1] += algorithm.ball.acceleration[1]
        
        algorithm.run()
        
        return model.update_ball(ax)

    animation = FuncAnimation(fig, update, init_func = init, blit = True, interval = 20) # 50fps
    plt.show()