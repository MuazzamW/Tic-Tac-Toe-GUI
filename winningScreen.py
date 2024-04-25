# winning screen once game is done
#     - shows who won
#     - game metadata
#     - play again button
#     - quit game button
#     - return to welcome screen
import tkinter as tk
from gameEngine import gameEngine
from main import Welcome

class WinScreen(gameEngine):
    def __init__(self):
        # initialize
        self.root = tk.Tk()
        self.root.geometry('400x400')
        self.root.title('Winning Page')

        # find winner
        if self.getWinner() == None:
            self.text = tk.Label(self.root, text = 'The game has resulted in a tie.')
        else:
            self.text = tk.Label(self.root, text = f'{self.getWinnder()} has won!')

        # creating labels
        self.title = tk.Label(self.root, text = 'Congrats!', font = ('Arial', 30))

        # placing labels
        self.title.grid(row = 0, column = 1, padx= 5, pady= 5)
        self.text.grid(row = 1, column = 0, padx = 5, pady = 5)

        # creating buttons
        self.quit_button = tk.Button(self.root, text = 'Quit', command = lambda:self.root.destroy())
        self.view_log = tk.Button(self.root, text = 'Game Log', command = lambda:self.viewGameLog())
        self.new_game = tk.Button(self.root, text = 'Return', command = lambda:self.returntoStart())

        # placing buttons
        self.quit_button.grid(row = 1, column = 0, padx = 5, pady = 5)
        self.new_game.grid(row = 1, column = 1, padx = 5, pady = 5)
        self.view_log.grid(row = 1, column = 2, padx = 5, pady = 5)

        self.root.mainloop()

    def returntoStart(self):
        self.root.destroy()
        w2 = Welcome()

    def viewGameLog(self):
        # ----- have gamelog be toplevel becuase we don't want to withdraw this class
        # instantiate gameLogScreen
        pass

w2 = WinScreen()