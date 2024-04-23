#main driver code here

#init function:

# - create welcome screen
# - view log button -> open log screen and show game history
# - new game button -> istantiate gameEngine object
# - quit game button -> closes screen
# - create a gameEngine object
import tkinter as tk

class Welcome:
    def __init__(self):
        # initialize
        self.root = tk.Tk()
        self.root.geometry('500x500')
        self.root.configure(bg = 'white')
        self.root.title('Welcome Page')

        # creating labels
        self.title = tk.Label(self.root, text = 'Tic Tac Toe', font = ('Arial', 30))

        # placing labels
        self.title.grid(row = 0, column = 0, padx= 0, pady= 0)

        self.root.mainloop()


w1 = Welcome()