from ui import *
from ui import Interface
import tkinter as tk

def main():
    root = tk.Tk()
    app = Interface(root)
    root.mainloop()

if __name__ == "__main__":
    main()