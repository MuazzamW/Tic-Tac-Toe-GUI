import tkinter as tk

class gameLogScreen():
    
    def __init__(self):
        # creating logscreen as a toplevel that can be shown without destroying the previous screen (everything else about it is the same)
        self.root = tk.Toplevel()
        self.root.geometry('400x400')
        self.root.title('Game Logs')

        
        # creating two frames -> top frame is for the title and bottom is to show all the game logs
        self.topframe = tk.Frame(self.root)
        self.bottomframe = tk.Frame(self.root)
