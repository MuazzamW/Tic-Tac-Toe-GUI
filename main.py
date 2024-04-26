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
        # initialize window that asks for user names
        self.top = tk.Toplevel(self.root)
        
        # variables for entries
        self.player1 = tk.StringVar()
        self.player2 = tk.StringVar()

        # creating labels, entries, button
        self.prompt1 = tk.Label(self.top, text = "Enter player 1's name: ")
        self.prompt2 = tk.Label(self.top, text = "Enter player 2's name: ")
        self.entry1 = tk.Entry(self.top, bd = 2)
        self.entry2 = tk.Entry(self.top, bd = 2)
        self.button1 = tk.Button(self.top, text = 'Continue', command = lambda:self.continueGame())

        # grid labels, entries, buttons
        self.prompt1.grid(row = 0, column = 0, padx = 5, pady = 5)
        self.prompt2.grid(row = 1, column = 0, padx = 5, pady = 5)
        self.entry1.grid(row = 0, column = 1, padx = 5, pady = 5)
        self.entry2.grid(row = 1, column = 1, padx = 5, pady = 5)
        self.button1.grid(row = 2, column = 1, padx = 5, pady = 5)


    def continueGame(self):
        # assign player names to variables
        self.player1 = self.entry1.get()
        self.player2 = self.entry2.get()

        # close current screen and open game
        self.root.destroy()
        g1 = gameScreen(self.player1, self.player2)

    def viewGameLog(self):
        # ----- have gamelog be toplevel becuase we don't want to withdraw this class
        # instantiate gameLogScreen
        pass


w1 = Welcome()