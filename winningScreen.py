# winning screen once game is done
#     - shows who won
#     - game metadata
#     - play again button
#     - quit game button
#     - return to welcome screen
import tkinter as tk

class WinScreen():
    def __init__(self, winner, parent):
        # initialize
        self.parent = parent
        self.root = tk.Toplevel()
        self.root.geometry('400x400')
        self.root.title('Winning Page')

        self.winner = winner

        # find winner
        if self.winner == None:
            self.text = tk.Label(self.root, text = 'The game has resulted in a tie.')
        else:
            self.text = tk.Label(self.root, text = f'{self.winner} has won!')

        # creating labels
        self.title = tk.Label(self.root, text = 'Game Over!', font = ('Arial', 30))

        # placing labels
        self.title.grid(row = 0, column = 1, padx= 5, pady= 5)
        self.text.grid(row = 1, column = 0, padx = 5, pady = 5)

        # creating buttons
        self.quit_button = tk.Button(self.root, text = 'Quit', command = lambda:self.parent.destroy())
        self.view_log = tk.Button(self.root, text = 'Game Log', command = lambda:self.viewGameLog())
        self.return_button = tk.Button(self.root, text = 'Play Again', command = lambda:self.replayGame())

        # placing buttons
        self.quit_button.grid(row = 2, column = 0, padx = 5, pady = 5)
        self.view_log.grid(row = 2, column = 2, padx = 5, pady = 5)
        self.return_button.grid(row = 2, column = 1, padx = 5, pady = 5)

        self.root.mainloop()

    def replayGame(self):
        self.root.destroy()
        self.parent.deiconify()

    def viewGameLog(self):
        # ----- have gamelog be toplevel becuase we don't want to withdraw this class
        # instantiate gameLogScreen
        pass