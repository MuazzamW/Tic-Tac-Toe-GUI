#game screen logic
# create labels for the images
# - image 1 = x
# - image 2 = o
# - image 3 = blank
# - create the grid of buttons
# - add a reset button at the bottom
# - quit game button
import tkinter as tk
from gameEngine import gameEngine

class Button(tk.Button):
    def __init__(self, x, y, image,command,master):
        super().__init__(image = image, command = command,master = master)
        self.__x = x
        self.__y = y
        self.__image = image

class gameScreen:
    def __init__(self, xPlayer, oPlayer):

        self.__gameEngine = gameEngine(xPlayer, oPlayer)

        # initialize
        self.root2 = tk.Tk()
        self.root2.geometry('400x400')
        self.root2.title('Game Screen')

        # creating two frames
        self.topframe = tk.Frame(self.root2)
        self.bottomframe = tk.Frame(self.root2)

        # creating photoimages
        self.photoimage0 = tk.PhotoImage(file = 'Images/blankimage.png').subsample(2,2)
        self.photoimage1 = tk.PhotoImage(file = 'Images/oicon.png')
        self.photoimage2 = tk.PhotoImage(file = 'Images/xicon.png')

        # creating lists for images and for grid
        self.images = [self.photoimage0, self.photoimage1, self.photoimage2]
        
        # (TEMPORARY) creating game buttons 
        # self.button1 = tk.Button(self.topframe, image = self.photoimage0, command = lambda:self.root2.destroy)
        # self.button1.grid(row = 0, column = 0, padx = 5, pady = 5)
        # self.button2 = tk.Button(self.topframe, image = self.photoimage1, command = lambda:self.root2.destroy)
        # self.button2.grid(row = 1, column = 0, padx = 5, pady = 5)
        
        self.__buttonGrid = []

        for row in range(3):
            for column in range(3):
               self.__buttonGrid.append(Button(row, column, image = self.photoimage1, command = lambda:self.checkWinner(),master = self.topframe))
               self.__buttonGrid[-1].grid(row = row, column = column, padx = 5, pady = 5) 
        

        # create quit and reset buttons
        self.quit_button = tk.Button(self.bottomframe, text = 'Quit', command = lambda:self.root2.destroy())
        self.reset_button = tk.Button(self.bottomframe, text = 'Reset', command = lambda:self.resetGame())

        # grid quit and reset buttons
        self.quit_button.grid(row = 0, column = 0, padx = 5, pady = 5)
        self.reset_button.grid(row = 0, column = 1, padx = 5, pady = 5)

        # pack frames
        self.topframe.pack()
        self.bottomframe.pack()

        self.root2.mainloop()
    
    def checkWinner(self):
        print('button clicked')
        if not self.__gameEngine.checkWinner() is None:
            pass
    
    def resetGame(self):
        self.root2.destroy()
        g1 = gameScreen()

g1=gameScreen("Jeff","bob")

