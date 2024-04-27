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

        # creating labels for the title and the game logs
        self.title = tk.Label(self.topframe, text = 'Game Logs', font = ('Arial', 30))
        

        # placing labels
        self.title.grid(row = 0, column = 1, padx= 0, pady= 0)
        self.logs.grid(row = 0, column = 0, padx= 0, pady= 0)


