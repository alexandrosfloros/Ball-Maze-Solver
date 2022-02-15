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

        xn = [n[0] for n in self.nodes]
        yn = [n[1] for n in self.nodes]
        nodes = ax.plot(xn, yn, "b-o")
        
        self.ball_pos, = ax.plot([self.ball.position[0]], [self.ball.position[1]], "go", markersize = 10)
        
        return nodes + [self.ball_pos]