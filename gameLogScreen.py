import tkinter as tk
from tkinter import ttk, Y, LEFT, RIGHT, BOTH, VERTICAL
from gameEngine import gameEngine
from gameScreen import logButton 
from gameLogHandler import gameLogHandler

class logButton(tk.Button):
    def __init__(self, index, text, command, master):
        super().__init__(text = text, command = command, master = master)
        self.__index = index
    
    def getIndex(self):
        return self.__index

class gameLogScreen():
    
    def __init__(self,fileName):
        self.__fileName = fileName
        # creating logscreen as a toplevel that can be shown without destroying the previous screen (everything else about it is the same)
        self.root = tk.Tk()
        self.root.geometry('400x400')
        self.root.title('Game Logs')
        self.__gameLogHandler = gameLogHandler(fileName)

        
        # creating two frames -> top frame is for the title and bottom is to show all the game logs
        self.topframe = tk.Frame(self.root)
        self.bottomframe = tk.Frame(self.root)

        # packing the frames
        self.topframe.pack()
        self.bottomframe.pack(fill = BOTH, expand = 1)

        #create canvas
        self.canvas = tk.Canvas(self.bottomframe)
        self.canvas.pack(side = LEFT, fill = BOTH, expand = 1)

        #create scrollbar
        self.scrollbar = ttk.Scrollbar(self.bottomframe, orient=VERTICAL, command = self.canvas.yview)
        self.scrollbar.pack(side = RIGHT, fill = Y)

        #configure canvas
        self.canvas.configure(yscrollcommand = self.scrollbar.set)
        self.canvas.bind('<Configure>', lambda e: self.canvas.configure(scrollregion = self.canvas.bbox("all")))

        #create another frame inside the canvas
        self.frame = tk.Frame(self.canvas)
        self.canvas.create_window((0,0), window = self.frame, anchor = 'nw')


        # creating labels for the title and the game logs
        self.title = tk.Label(self.topframe, text = 'Game Logs', font = ('Arial', 30))

        #adding buttons to bottom frame
        for i in range(len(self.__gameLogHandler.returnLogs())):
            log = self.__gameLogHandler.returnLogs()[i]
            logButton(i, text = log["date"], command = lambda i = i:self.showLog(log), master = self.frame).grid(row = i, column = 0, padx = 5, pady = 5)


        # placing labels
        self.title.grid(row = 0, column = 1, padx= 0, pady= 0)
        

        self.root.mainloop()
    
    def showLog(self,log):
        # open on top of the current window
        self.top = tk.Toplevel(self.root)
        self.top.geometry('400x400')
        self.top.title('Game Log')
        self.topframe = tk.Frame(self.top)
        self.bottomframe = tk.Frame(self.top)
        self.topframe.pack()
        self.bottomframe.pack()
        # creating labels for the title and the game logs
        self.title = tk.Label(self.topframe, text = 'Game Log', font = ('Arial', 30))
        self.title.grid(row = 0, column = 1, padx= 0, pady= 0)
        # adding labels to the top frame
        tk.Label(self.topframe, text = "Date: " + log["date"]).grid(row = 1, column = 1, padx= 0, pady= 0)
        tk.Label(self.topframe, text = "Player X: " + log["Player X"]).grid(row = 2, column = 1, padx= 0, pady= 0)
        tk.Label(self.topframe, text = "Player O: " + log["Player O"]).grid(row = 3, column = 1, padx= 0, pady= 0)
        tk.Label(self.topframe, text = "Winner: " + log["winner"]).grid(row = 4, column = 1, padx= 0, pady= 0)
        tk.Label(self.topframe, text = "Turns: " + str(log["turns"])).grid(row = 5, column = 1, padx= 0, pady= 0)
        tk.Label(self.topframe, text = "Grid:").grid(row = 6, column = 1, padx= 0, pady= 0)
        # adding labels to the bottom frame
        tk.Label(self.bottomframe, text = log["grid"]).grid(row = 0, column = 0, padx= 0, pady= 0)
        # creating a back button
        tk.Button(self.bottomframe, text = 'Back', command = lambda:self.top.destroy()).grid(row = 1, column = 1, padx= 0, pady= 0)
        self.top.mainloop()
# gl

s1 = gameLogScreen("GameLog/data.json")
