"""
This is the file used to display the algorithm simulation independently (testing only)
"""

class BallMazeModel:
    def __init__(self, ball, nodes):
        self.ball = ball
        self.nodes = nodes
    
    def update_ball(self, ax):
        patches = self.init_path(ax)

        self.ball_pos.set_data([self.ball.position[0]], [self.ball.position[1]])

        return patches

    def init_path(self, ax):
        ax.set_xlim([0, 5])
        ax.set_ylim([0, 5])

        xp = [n[0] for n in self.nodes]
        yp = [n[1] for n in self.nodes]
        path = ax.plot(xp, yp, "b-o")
        
        self.ball_pos, = ax.plot([self.ball.position[0]], [self.ball.position[1]], "go", markersize = 10)
        
        return path + [self.ball_pos]