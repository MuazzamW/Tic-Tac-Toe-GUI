import tkinter as tk

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