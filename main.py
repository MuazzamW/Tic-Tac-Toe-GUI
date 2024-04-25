#main driver code here

#init function:

# - create welcome screen
# - view log button -> open log screen and show game history
# - new game button -> istantiate gameEngine object
# - quit game button -> closes screen
# - create a gameEngine object
import tkinter as tk
from gameScreen import gameScreen

class Welcome:
    def __init__(self):
        # initialize
        self.root = tk.Tk()
        self.root.geometry('400x400')
        self.root.title('Welcome Page')

        # creating labels
        self.title = tk.Label(self.root, text = 'Tic Tac Toe', font = ('Arial', 30))

        # placing labels
        self.title.grid(row = 0, column = 1, padx= 0, pady= 0)

        # creating buttons
        self.quit_button = tk.Button(self.root, text = 'Quit', command = lambda:self.root.destroy())
        self.view_log = tk.Button(self.root, text = 'Game Log', command = lambda:self.viewGameLog())
        self.new_game = tk.Button(self.root, text = 'Start Game', command = lambda:self.startGame())

        # placing buttons
        self.quit_button.grid(row = 1, column = 0, padx = 5, pady = 5)
        self.new_game.grid(row = 1, column = 1, padx = 5, pady = 5)
        self.view_log.grid(row = 1, column = 2, padx = 5, pady = 5)

        self.root.mainloop()

    def startGame(self):
        
        self.root.destroy()
        g1 = gameScreen()

    def viewGameLog(self):
        # ----- have gamelog be toplevel becuase we don't want to withdraw this class
        # instantiate gameLogScreen
        pass


w1 = Welcome()