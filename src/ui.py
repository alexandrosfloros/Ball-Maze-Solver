import time

import tkinter as tk
from tkinter import ttk, messagebox

from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from motor_control_testbench import *
from motor_control_testing.graphics import BallMazeModel
from motor_control_testing.algorithm import *

class Interface:
    def __init__(self, master):
        self.master = master

        ### initialising window parameters

        self.master.title("Ball Maze Solver")
        self.master.geometry("1000x600")
        self.master.resizable(False, False)

        ### initialising page frames

        self.main_menu_frame = ttk.Frame(self.master)
        self.puzzle_frame = ttk.Frame(self.master)

        ### initialising puzzle display canvas

        self.puzzle_display_figure = plt.figure()
        self.puzzle_display_axes = self.puzzle_display_figure.add_axes([0, 0, 1, 1])

        self.puzzle_display_canvas = FigureCanvasTkAgg(self.puzzle_display_figure, master = self.puzzle_frame)
        self.puzzle_display_canvas.get_tk_widget().pack(side = "left")

        ### initialising puzzle data frame

        self.puzzle_data_frame = ttk.Frame(self.puzzle_frame)
        self.puzzle_data_frame.pack(side = "right", padx = 15, pady = 15)

        ### initialising info label

        self.info_label = ttk.Label(self.puzzle_data_frame, text = "Puzzle Information")
        self.info_label.pack()

        ### initialising info frame

        self.info_frame = ttk.Frame(self.puzzle_data_frame)
        self.info_frame.pack()

        ### initialising settings label

        self.settings_label = ttk.Label(self.puzzle_data_frame, text = "Puzzle Settings")
        self.settings_label.pack()

        ### initialising settings frame

        self.settings_frame = ttk.Frame(self.puzzle_data_frame)
        self.settings_frame.pack()

        ### initialising main menu widgets

        self.main_menu_title = ttk.Label(self.main_menu_frame, text = "Autonomously Operated Maze", font = ("Verdana", 24))
        self.main_menu_title.pack(pady=25)

        self.main_menu_label = ttk.Label(self.main_menu_frame, text = "Select a maze difficulty:", font = ("Verdana", 18))
        self.main_menu_label.pack(pady = 50)

        self.easy_difficulty_button = ttk.Button(self.main_menu_frame, text = "Easy", width = 80, command = self.load_easy_difficulty) # select easy difficulty
        self.easy_difficulty_button.pack(ipady = 25)

        self.medium_difficulty_button = ttk.Button(self.main_menu_frame, text = "Medium", width = 80, command = self.load_medium_difficulty) # select medium difficulty
        self.medium_difficulty_button.pack(pady = 30, ipady = 25)

        self.medium_difficulty_button = ttk.Button(self.main_menu_frame, text = "Hard", width = 80, command = self.load_hard_difficulty) # select hard difficulty
        self.medium_difficulty_button.pack(ipady = 25)

        ### initialising info widgets

        self.general_treeview = ttk.Treeview(self.info_frame, columns = ("column1", "column2"), show = "headings", selectmode = "none") # contains general info about the puzzle
        self.general_treeview.column("column1", width = 140)
        self.general_treeview.column("column2", width = 100)

        self.difficulty_row = self.general_treeview.insert("", "end", values = ("Difficulty:", ""))
        self.current_position_row = self.general_treeview.insert("", "end", values = ("Current Position:", ""))
        self.next_position_row = self.general_treeview.insert("", "end", values = ("Next Position:", ""))
        self.x_velocity_row = self.general_treeview.insert("", "end", values = ("X Velocity:", ""))
        self.y_velocity_row = self.general_treeview.insert("", "end", values = ("Y Velocity:", ""))
        self.time_row = self.general_treeview.insert("", "end", values = ("Solved Time:", ""))
        self.average_time = self.general_treeview.insert("","end", values = ("Average Solve Time", ""))
        self.progress_row = self.general_treeview.insert("", "end", values = ("Progress:", ""))


        self.general_treeview.bind("<Button-1>", self.disable_treeview)
        self.general_treeview.pack()

        self.state_treeview = ttk.Treeview(self.info_frame, columns = ("state", "time"), show = "headings", selectmode = "none") # contains state history of the motors
        self.state_treeview.heading("state", text = "State")
        self.state_treeview.heading("time", text = "Time")
        self.state_treeview.column("state", width = 120)
        self.state_treeview.column("time", width = 120)
        self.state_treeview.bind("<Button-1>", self.disable_treeview)
        self.state_treeview.pack(pady = 15)

        ### initialising settings widgets

        self.start_button = ttk.Button(self.settings_frame, text = "Start", width = 12, command = lambda: self.start(simulated = False)) # start the real puzzle solve
        self.start_button.pack(side = "left")
        
        self.simulate_button = ttk.Button(self.settings_frame, text = "Simulate", width = 12, command = lambda: self.start(simulated = True)) # start the simulated puzzle solve
        self.simulate_button.pack(side = "left")

        self.stop_button = ttk.Button(self.settings_frame, text = "Leave", width = 12, command = self.leave_to_main_menu) # stop the puzzle and go back to main menu
        self.stop_button.pack(side = "right")

        ### initialising timer values

        self.start_time = None
        self.timer_running = False
        self.timer_value = tk.StringVar()

        ### starting on main menu by default

        self.load_main_menu()
    
    def animate_model(self, model, simulated):
        
        # initialising algorithm

        def init():
            self.algorithm = BallMazeAlgorithm(model.ball, model.nodes, model.holes)

            return model.init_path(self.puzzle_display_axes)

        # updating algorithm in every frame

        def update(frame_number):
            if simulated:
                self.algorithm.ball.position[0] += self.algorithm.ball.velocity[0]
                self.algorithm.ball.position[1] += self.algorithm.ball.velocity[1]
            
                self.algorithm.ball.velocity[0] += self.algorithm.ball.acceleration[0]
                self.algorithm.ball.velocity[1] += self.algorithm.ball.acceleration[1]
            
            else:

                """
                This is the loop for the real puzzle solve
                The position of the ball is received by the image processing, one frame at a time
                It is then assigned to the ball using:
                
                self.algorithm.ball.position[0] = ...
                self.algorithm.ball.position[1] = ...

                Then, the algorithm is run for that frame
                """
            
            self.algorithm.run()
            
            ### the ball reaches the end

            if self.algorithm.game_won:
                self.animation.event_source.stop()
            
            ### the ball falls into a hole

            elif self.algorithm.game_lost:
                self.animation.event_source.stop()

            return model.update_ball(self.puzzle_display_axes)

        self.animation = FuncAnimation(self.puzzle_display_figure, update, init_func = init, blit = True, interval = 33) # 30fps

    def load_main_menu(self):

        ### hide puzzle page

        self.puzzle_frame.pack_forget()

        ### reset value for solve time

        self.constant_time = "00:00:0"
        self.general_treeview.set(self.time_row, "column2", self.constant_time)

        ### stop the timer when returning back to the main menu

        self.stop_timer()

        ### stop the animation when returning back to the main menu

        try:
            self.animation.event_source.stop()
        except:
            pass

        ### show main menu page

        self.main_menu_frame.pack()

    def leave_to_main_menu(self):

        ### warning message

        warning = messagebox.askyesno("Warning", "Leaving will stop the current maze solving. Would you like to leave?")

        if warning:
            self.load_main_menu()       

    def load_puzzle_menu(self, difficulty):

        ### hide main menu page

        self.main_menu_frame.pack_forget()

        ### show puzzle page

        self.puzzle_frame.pack()

        ### set puzzle difficulty

        self.difficulty = difficulty
        self.general_treeview.set(self.difficulty_row, "column2", self.difficulty)
    
    def load_easy_difficulty(self):
        self.load_puzzle_menu("EASY")

    def load_medium_difficulty(self):
        self.load_puzzle_menu("MEDIUM")

    def load_hard_difficulty(self):
        self.load_puzzle_menu("HARD")

    def disable_treeview(self, event):
        if self.general_treeview.identify_region(event.x, event.y) == "separator" or self.state_treeview.identify_region(event.x, event.y) == "separator":
            return "break"
    
    def start_animation(self, nodes, holes, simulated):
        x, y = nodes[0]
        ball = Ball([x, y])
        model = BallMazeModel(ball, nodes, holes)
        self.animate_model(model, simulated)

    def start(self, simulated):
        if not self.timer_running:
            
            self.start_timer()

            if self.difficulty == "EASY":
                self.start_animation(easy_nodes, easy_holes, simulated)

            elif self.difficulty == "MEDIUM":
                self.start_animation(medium_nodes, medium_holes, simulated)

            else:
                self.start_animation(hard_nodes, hard_holes, simulated)

    def start_timer(self):
        self.start_time = time.time()
        self.timer()
        self.timer_running = True
    
    def timer(self):
        self.timer_value.set(self.format_time(time.time() - self.start_time))
        self.after_loop = self.puzzle_frame.after(50, self.timer)

    def stop_timer(self):
        if self.timer_running:
            self.puzzle_frame.after_cancel(self.after_loop)
            self.timer_running = False

    def format_time(self, elap):
        hours = int(elap / 3600)
        minutes = int(elap / 60 - hours * 60.0)
        seconds = int(elap - hours * 3600.0 - minutes * 60.0)
        hseconds = int((elap - hours * 3600.0 - minutes * 60.0 - seconds) * 10)

        ### display the stop watch

        self.constant_time = "%02d:%02d:%01d" % (minutes, seconds, hseconds)
        self.general_treeview.set(self.time_row, "column2", self.constant_time)