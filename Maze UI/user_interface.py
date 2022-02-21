# from tkinter import *
# from tkinter.ttk import *

import tkinter as tk
from PIL import Image, ImageTk

from tkinter import ttk
# window = Tk() #create the window
# window.title("Autonomously Operated Maze") #Set window title
# window.geometry("1200x750")

root = tk.Tk()
root.title("Autonomously Operated Maze") #Set window title
# root.geometry("1200x750")
root.attributes('-fullscreen', True)

root.configure(background='grey')

Instructions = ttk.Label(root, text = "Select maze difficulty:", font="Verdana")
##Instructions.grid(column=2, row=4)
Instructions.pack(pady=20)
Frame = tk.Frame(root)
Frame.configure(background='grey')
Frame.pack()

#main menu buttons 

#Easy Button Characteristics
easy_text = tk.StringVar()
easy_btn = ttk.Button(Frame, textvariable=easy_text)
easy_text.set("Easy")
easy_btn.pack(anchor='center')
##easy_btn.grid(column=10, row=4)

#Medium Button Characteristics
medium_text = tk.StringVar()
medium_btn = ttk.Button(Frame, textvariable=medium_text)
medium_text.set("Medium")
medium_btn.pack(anchor='center')
##medium_btn.grid(column=10, row=6)

#Hard Button Characteristics
hard_text = tk.StringVar()
hard_btn = ttk.Button(Frame, textvariable=hard_text)
hard_text.set("Hard")
hard_btn.pack(anchor='center')
##hard_btn.grid(column=10, row=8)

root.mainloop()

#main menu 