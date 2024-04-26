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
    
    def getX(self):
        return self.__x

    def getY(self):
        return self.__y

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
        self.photoimageBlank = tk.PhotoImage(file = 'Images/blankimage.png')
        
        self.__buttonGrid = []

        for row in range(3):
            for column in range(3):
               self.__buttonGrid.append(Button(column, row, image = self.photoimageBlank, command = lambda row = row, column = column:self.checkWinner(row, column), master = self.topframe))
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
    
    def checkWinner(self, row, column):
        # check for winner and switch player image, update in gameengine
        print('button clicked')
        print(column, row)

        # check if move can be made, and update grid in gameengine
        self.__gameEngine.makeMove(column, row)

        # update grid in gamescreen
        tempimage = tk.PhotoImage(file = 'Images/Xicon.png')
        self.__buttonGrid[column*3+row].configure(image = tempimage)
        self.__buttonGrid[column*3+row].photo = tempimage

        print(self.__buttonGrid[column*3+row].getX(), self.__buttonGrid[column*3+row].getY())
        print(row*3+column)

        

        if not self.__gameEngine.checkWinner() is None:
            pass
    
    def resetGame(self):
        self.root2.destroy()
        g1 = gameScreen(self.__gameEngine.getPlayerX(), self.__gameEngine.getPlayerO())

