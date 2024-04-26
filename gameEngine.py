import random
import json

#class gameEngine
# Description: This class is the main engine for the game, makes all decisions

#init function:
#variables
#internal game grid
#internal game state
#the turn of the player -> turn variable
#move counter
#boolean to check if the game is over


#functions:
# - check winner
# - make move (accepts coordinates from the gui class)
# - reset game function sets all parameters to zero
# - write to game log

class gameEngine:
    
    def __init__(self,xPlayer, oPlayer):
        self.__xPlayer = xPlayer
        self.__oPlayer = oPlayer
        self.reset()
    
    def getPlayerX(self):
        return self.__xPlayer
    
    def getPlayerO(self):
        return self.__oPlayer
    
    def getTurn(self):
        return self.__turn

    def reset(self):
        self.__grid = [[None, None, None], [None, None, None], [None, None, None]]
        self.__turn = random.choice(['X', 'O'])
        self.__move_counter = 0
        self.__game_over = False
    
    def makeMove(self,xPos, yPos):
        if self.__grid[yPos][xPos] is None:
            self.__grid[yPos][xPos] = self.__turn
        else:
            raise LocationError("Invalid location, please try again.") 
        self.__move_counter += 1
    
    def changeTurn(self):
        self.__turn = "X" if self.__turn == "O" else "O"
    
    def checkWinner(self):
        #check rows
        for row in self.__grid:
            if row[0] == row[1] == row[2] and row[0] is not None:
                self.__game_over = True
                return (row[0],self.__game_over)
        
        #check columns
        for i in range(3):
            if self.__grid[0][i] == self.__grid[1][i] == self.__grid[2][i] and self.__grid[0][i] is not None:
                self.__game_over = True
                return (self.__grid[0][i], self.__game_over)
        
        #check diagonals
        if self.__grid[0][0] == self.__grid[1][1] == self.__grid[2][2] and self.__grid[0][0] is not None:
            self.__game_over = True
            return (self.__grid[0][0],self.__game_over)
        
        if self.__grid[0][2] == self.__grid[1][1] == self.__grid[2][0] and self.__grid[0][2] is not None:
            self.__game_over = True
            return (self.__grid[0][2],self.__game_over)
        
        if self.__move_counter == 9:
            self.__game_over = True
            return ("Tie",self.__game_over)
        
        return None
    
    def writeToLog(self):
        data = {
            #format grid as 3x3 grid
            "grid": f"""
                    {self.__grid[0]}
                    {self.__grid[1]}
                    {self.__grid[2]} 
                    """,
            "winner": self.checkWinner()[0],
            "turns": self.__move_counter,
            "Player X": self.__xPlayer,
            "Player O": self.__oPlayer
        }
        with open('data.json', 'a', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)



class LocationError(Exception):
    def __init__(self,msg):
        super().__init__(msg)

