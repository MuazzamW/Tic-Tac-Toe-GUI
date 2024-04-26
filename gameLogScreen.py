import tkinter as tk

class gameLogScreen():
    
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry('400x400')
        self.root.title('Game Logs')

        
        # creating two frames -> top frame is for the title and bottom is to show all the game logs
        self.topframe = tk.Frame(self.root)
        self.bottomframe = tk.Frame(self.root)
