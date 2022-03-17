import time

import tkinter as tk
from tkinter import ttk, messagebox

from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from motor_control_testbench import *
from motor_control_testing.graphics import *
from src.algorithm import *
from src.node_functions import *

class Interface:
    def __init__(self, master):
        self.master = master

        # initialise window parameters

        self.master.title("Ball Maze Solver")
        self.master.geometry("1000x650")
        self.master.resizable(False, False)

        # initialise page frames

        self.main_menu_frame = ttk.Frame(self.master)
        self.puzzle_frame = ttk.Frame(self.master)

        # initialise puzzle display frame

        self.puzzle_display_frame = ttk.Frame(self.puzzle_frame)
        self.puzzle_display_frame.pack(side = "left")

        # initialise settings label

        self.settings_label = ttk.Label(self.puzzle_display_frame, text = "Algorithm Settings (on start)")
        self.settings_label.pack(fill = tk.X, pady = 5)

        # initialise settings frame

        self.settings_frame = ttk.Frame(self.puzzle_display_frame)
        self.settings_frame.pack(fill = tk.X, pady = 5)

        # initialise node tolerance frame

        self.node_tolerance_frame = ttk.Frame(self.settings_frame)
        self.node_tolerance_frame.pack(side = "left", padx = 5)

        # initialise node tolerance label

        self.node_tolerance_label = ttk.Label(self.node_tolerance_frame, text = "Node Tolerance")
        self.node_tolerance_label.pack(side = "left")

        # initialise node tolerance combobox

        self.node_tolerance_combobox = ttk.Combobox(self.node_tolerance_frame, values = (0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0), width = 5, state = "readonly")
        self.node_tolerance_combobox.pack(side = "left")
        self.node_tolerance_combobox.current(7)

        # initialise min speed frame

        self.min_speed_frame = ttk.Frame(self.settings_frame)
        self.min_speed_frame.pack(side = "left", padx = 5)

        # initialise min speed label

        self.min_speed_label = ttk.Label(self.min_speed_frame, text = "Min Speed")
        self.min_speed_label.pack(side = "left")

        # initialise min speed combobox

        self.min_speed_combobox = ttk.Combobox(self.min_speed_frame, values = (0.010, 0.011, 0.012, 0.013, 0.014, 0.015, 0.016, 0.017, 0.018, 0.019), width = 5, state = "readonly")
        self.min_speed_combobox.pack(side = "left")
        self.min_speed_combobox.current(0)

        # initialise max speed frame

        self.max_speed_frame = ttk.Frame(self.settings_frame)
        self.max_speed_frame.pack(side = "left", padx = 5)

        # initialise max speed label

        self.max_speed_label = ttk.Label(self.max_speed_frame, text = "Max Speed")
        self.max_speed_label.pack(side = "left")

        # initialise max speed combobox

        self.max_speed_combobox = ttk.Combobox(self.max_speed_frame, values = (0.10, 0.11, 0.12, 0.13, 0.14, 0.15, 0.16, 0.17, 0.18, 0.19), width = 5, state = "readonly")
        self.max_speed_combobox.pack(side = "left")
        self.max_speed_combobox.current(0)

        # initialise puzzle data frame

        self.puzzle_data_frame = ttk.Frame(self.puzzle_frame)
        self.puzzle_data_frame.pack(side = "right", padx = 15, pady = 15)

        # initialise info label

        self.info_label = ttk.Label(self.puzzle_data_frame, text = "Puzzle Information")
        self.info_label.pack()

        # initialise info frame

        self.info_frame = ttk.Frame(self.puzzle_data_frame)
        self.info_frame.pack(pady = 5)

        # initialise progressbar label

        self.progressbar_label = ttk.Label(self.puzzle_data_frame, text = "Puzzle Progress")
        self.progressbar_label.pack()

        # initialise progressbar

        self.progressbar = ttk.Progressbar(self.puzzle_data_frame, length = 250)
        self.progressbar.pack(pady = 5)

        # initialise options label

        self.options_label = ttk.Label(self.puzzle_data_frame, text = "Puzzle Options")
        self.options_label.pack()

        # initialise options frame

        self.options_frame = ttk.Frame(self.puzzle_data_frame)
        self.options_frame.pack(pady = 5)

        # initialise main menu widgets

        self.main_menu_title = ttk.Label(self.main_menu_frame, text = "Ball Maze Solver", font = ("Verdana", 24))
        self.main_menu_title.pack(pady=25)

        self.main_menu_label = ttk.Label(self.main_menu_frame, text = "Select a puzzle difficulty:", font = ("Verdana", 18))
        self.main_menu_label.pack(pady = 50)

        self.easy_difficulty_button = ttk.Button(self.main_menu_frame, text = "Easy", width = 80, command = self.load_easy_difficulty) # select easy difficulty
        self.easy_difficulty_button.pack(ipady = 25)

        self.medium_difficulty_button = ttk.Button(self.main_menu_frame, text = "Medium", width = 80, command = self.load_medium_difficulty) # select medium difficulty
        self.medium_difficulty_button.pack(pady = 30, ipady = 25)

        self.medium_difficulty_button = ttk.Button(self.main_menu_frame, text = "Hard", width = 80, command = self.load_hard_difficulty) # select hard difficulty
        self.medium_difficulty_button.pack(ipady = 25)

        # initialise general treeview

        self.general_treeview = ttk.Treeview(self.info_frame, columns = ("column1", "column2"), show = "headings", selectmode = "none") # contains general info about the puzzle
        self.general_treeview.column("column1", width = 120)
        self.general_treeview.column("column2", width = 120)
        self.difficulty_row = self.general_treeview.insert("", "end", values = ("Difficulty:", ""))
        self.x_position_row = self.general_treeview.insert("", "end", values = ("X Position:", ""))
        self.y_position_row = self.general_treeview.insert("", "end", values = ("Y Position:", ""))
        self.x_velocity_row = self.general_treeview.insert("", "end", values = ("X Velocity:", ""))
        self.y_velocity_row = self.general_treeview.insert("", "end", values = ("Y Velocity:", ""))
        self.time_row = self.general_treeview.insert("", "end", values = ("Solve Time:", ""))
        self.progress_row = self.general_treeview.insert("", "end", values = ("Progress:", ""))
        self.general_treeview.bind("<Button-1>", self.disable_treeview)
        self.general_treeview.pack()

        # initialise motor state treeview

        self.motor_state_treeview = ttk.Treeview(self.info_frame, columns = ("state", "timestamp"), show = "headings", selectmode = "none") # contains state history of the motors
        self.motor_state_treeview.heading("state", text = "State")
        self.motor_state_treeview.heading("timestamp", text = "Timestamp")
        self.motor_state_treeview.column("state", width = 120)
        self.motor_state_treeview.column("timestamp", width = 120)
        self.motor_state_treeview.bind("<Button-1>", self.disable_treeview)
        self.motor_state_treeview.pack(pady = 5)

        # initialise options buttons

        self.start_button = ttk.Button(self.options_frame, text = "Start", width = 12, command = lambda: self.start(simulated = False)) # start the real puzzle solve
        self.start_button.pack(side = "left")
        
        self.simulate_button = ttk.Button(self.options_frame, text = "Simulate", width = 12, command = lambda: self.start(simulated = True)) # start the simulated puzzle solve
        self.simulate_button.pack(side = "left")

        self.stop_button = ttk.Button(self.options_frame, text = "Leave", width = 12, command = self.leave_to_main_menu) # stop the puzzle and go back to main menu
        self.stop_button.pack(side = "left")

        # initialise timer values

        self.start_time = None
        self.timer_running = False

        # start on main menu by default

        self.load_main_menu()
    
    def animate_model(self, model, simulated):
        
        # initialise algorithm

        def init():

            self.algorithm = BallMazeAlgorithm(model, simulated)
            self.algorithm.node_tolerance = float(self.node_tolerance_combobox.get())
            self.algorithm.ball.max_speed = float(self.max_speed_combobox.get())
            self.algorithm.ball.min_speed = float(self.min_speed_combobox.get())

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
                The position and velocity of the ball are received by the image processing, one frame at a time
                They are then assigned to the ball using:
                
                self.algorithm.ball.position[0] = ...
                self.algorithm.ball.position[1] = ...

                self.algorithm.ball.velocity[0] = ...
                self.algorithm.ball.velocity[1] = ...

                Then, the algorithm is run for that frame
                """
            
            self.algorithm.run()
            
            # update table values

            self.general_treeview.set(self.x_position_row, "column2", round(self.algorithm.ball.position[0], 2))
            self.general_treeview.set(self.y_position_row, "column2", round(self.algorithm.ball.position[1], 2))
            self.general_treeview.set(self.x_velocity_row, "column2", round(self.algorithm.ball.velocity[0], 2))
            self.general_treeview.set(self.y_velocity_row, "column2", round(self.algorithm.ball.velocity[1], 2))

            # fix for full progressbar on start

            if self.algorithm.ball.progress > 0:
                progress_percentages = round(get_path_length_percentages(model.nodes)[self.algorithm.ball.progress - 1], 2)
                self.general_treeview.set(self.progress_row, "column2", f"{progress_percentages}%")
                self.progressbar['value'] = progress_percentages

            if frame_number == 0:
                self.previous_motor_state = ""
            elif frame_number > 0 and self.previous_motor_state != self.algorithm.ball.motor_state:
                self.previous_motor_state = self.algorithm.ball.motor_state
                self.insert_motor_state(self.algorithm.ball.motor_state, self.constant_time)

            # the ball reaches the end

            if self.algorithm.game_won:
                self.stop_puzzle()
                messagebox.showinfo("Success!", "The puzzle solve was successful.")
            
            # the ball falls into a hole

            elif self.algorithm.game_lost:
                self.stop_puzzle()
                messagebox.showinfo("Failure!", "The puzzle solve was not successful.")

            return model.update_ball(self.puzzle_display_axes)

        self.animation = FuncAnimation(self.puzzle_display_figure, update, init_func = init, blit = True, interval = 33) # 30fps

    def reset_animation(self):
        try:
            self.animation.event_source.stop()
        except:
            pass
    
    def reset_puzzle(self):

        # reset puzzle display figure

        try:
            self.puzzle_display_canvas.get_tk_widget().destroy()
        except:
            pass

        self.puzzle_display_figure = plt.figure()
        self.puzzle_display_axes = self.puzzle_display_figure.add_axes([0, 0, 1, 1])

        self.puzzle_display_canvas = FigureCanvasTkAgg(self.puzzle_display_figure, master = self.puzzle_display_frame)
        self.puzzle_display_canvas.get_tk_widget().pack(before = self.settings_label)

        # reset general treeview

        self.general_treeview.set(self.x_position_row, "column2", "")
        self.general_treeview.set(self.y_position_row, "column2", "")
        self.general_treeview.set(self.x_velocity_row, "column2", "")
        self.general_treeview.set(self.y_velocity_row, "column2", "")
        self.general_treeview.set(self.progress_row, "column2", "")
        self.general_treeview.set(self.time_row, "column2", "00:00:0")

        # reset motor state treeview

        self.motor_state_treeview.delete(*self.motor_state_treeview.get_children())

        # reset progressbar
        
        self.progressbar['value'] = 0
    
    def stop_puzzle(self):

        # stop timer

        self.stop_timer()

        # reset animation

        self.reset_animation()

    def load_main_menu(self):

        # stop puzzle

        self.stop_puzzle()

        # reset puzzle

        self.reset_puzzle()

        # hide puzzle page

        self.puzzle_frame.pack_forget()

        # show main menu page

        self.main_menu_frame.pack()

    def leave_to_main_menu(self):

        # warning message

        if self.timer_running:
            warning = messagebox.askyesno("Warning!", "Leaving will stop the current puzzle solve. Would you like to proceed?")

            if warning:
                self.load_main_menu()
        
        else:
            self.load_main_menu()

    def load_puzzle_menu(self, difficulty):

        # set puzzle difficulty

        self.difficulty = difficulty
        self.general_treeview.set(self.difficulty_row, "column2", self.difficulty)

        # hide main menu page

        self.main_menu_frame.pack_forget()

        # show puzzle page

        self.puzzle_frame.pack()
    
    def load_easy_difficulty(self):
        self.load_puzzle_menu("EASY")

    def load_medium_difficulty(self):
        self.load_puzzle_menu("MEDIUM")

    def load_hard_difficulty(self):
        self.load_puzzle_menu("HARD")

    def disable_treeview(self, event):
        if self.general_treeview.identify_region(event.x, event.y) == "separator" or self.motor_state_treeview.identify_region(event.x, event.y) == "separator":
            return "break"
    
    def start_puzzle(self, nodes, holes, simulated):
        x, y = nodes[0]
        ball = Ball([x, y])
        model = BallMazeModel(ball, nodes, holes)
        self.animate_model(model, simulated)

    def start(self, simulated):
        if self.timer_running:
            warning = messagebox.askyesno("Warning!", "Starting a new puzzle solve will stop the current puzzle solve. Would you like to proceed?")
        
            if warning:
                self.stop_puzzle()
                self.start(simulated)

        else:
            self.reset_puzzle()
            self.start_timer()

            if self.difficulty == "EASY":
                self.start_puzzle(easy_nodes, easy_holes, simulated)

            elif self.difficulty == "MEDIUM":
                self.start_puzzle(medium_nodes, medium_holes, simulated)

            else:
                self.start_puzzle(hard_nodes, hard_holes, simulated)

    def start_timer(self):
        self.start_time = time.time()
        self.timer()
        self.timer_running = True
    
    def timer(self):
        self.format_time(time.time() - self.start_time)
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

        # display stopwatch

        self.constant_time = "%02d:%02d:%01d" % (minutes, seconds, hseconds)
        self.general_treeview.set(self.time_row, "column2", self.constant_time)

    def insert_motor_state(self, state, time):
        self.motor_state_treeview.insert("", 0, values = (state, time))