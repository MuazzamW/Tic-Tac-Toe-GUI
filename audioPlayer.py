import pygame
import tkinter as tk
from os import listdir
from os.path import isfile, join
from tkinter import ttk, Y, LEFT, RIGHT, BOTH, VERTICAL

class AudioPlayer:
    def __init__(self):
        self.__playlistPath = "Aasees_Playlist"
        self.root = tk.Tk()
        self.root.title("Audio Player")
        self.root.geometry("400x400")
        self.root.resizable(False, False)

        self.__playlist = [f for f in listdir(self.__playlistPath) if isfile(join(self.__playlistPath, f))]
        self.__currentSong = 0
        self.__isPlaying = False

         # creting three frames
        self.topframe = tk.Frame(self.root)
        self.middleframe = tk.Frame(self.root)
        self.bottomframe = tk.Frame(self.root)

        # packing the frames
        self.topframe.pack()
        self.middleframe.pack(fill = BOTH, expand = 1)
        self.bottomframe.pack(fill = BOTH, expand = 1)
        

        #create canvas
        self.canvas = tk.Canvas(self.middleframe)
        self.canvas.pack(side = LEFT, fill = BOTH, expand = 1)

        #create scrollbar
        self.scrollbar = ttk.Scrollbar(self.middleframe, orient=VERTICAL, command = self.canvas.yview)
        self.scrollbar.pack(side = RIGHT, fill = Y)

        #configure canvas
        self.canvas.configure(yscrollcommand = self.scrollbar.set)
        self.canvas.bind('<Configure>', lambda e: self.canvas.configure(scrollregion = self.canvas.bbox("all")))

        #create another frame inside the canvas
        self.frame = tk.Frame(self.canvas)
        self.canvas.create_window((0,0), window = self.frame, anchor = 'nw')

        #add buttons for each song
        for i in range(len(self.__playlist)):
            tk.Button(self.frame, text = self.__playlist[i], command = lambda i = i:self.playSong(i)).grid(row = i, column = 0, padx = 5, pady = 5)

        #create pause and play buttons
        self.play_button = tk.Button(self.bottomframe, text = 'Play', command = lambda:self.play())
        self.pause_button = tk.Button(self.bottomframe, text = 'Pause', command = lambda:self.pause())

        # grid play and pause buttons
        self.play_button.grid(row = 1, column = 0, padx = 5, pady = 5)
        self.pause_button.grid(row = 1, column = 1, padx = 5, pady = 5)


        # creating labels for the title and the game logs
        self.title = tk.Label(self.topframe, text = "Aasees's Playlist", font = ('Arial', 30))

        # placing labels
        self.title.grid(row = 0, column = 1, padx= 0, pady= 0)

        self.root.mainloop()
    
    def playSong(self, index):
        pygame.mixer.init()
        pygame.mixer.music.load(f"{self.__playlistPath}/{self.__playlist[index]}")
        pygame.mixer.music.play()
        self.__currentSong = index
        self.__isPlaying = True

    def play(self):
        if not self.__isPlaying:
            pygame.mixer.music.unpause()
            self.__isPlaying = True
    
    def pause(self):
        if self.__isPlaying:
            pygame.mixer.music.pause()
            self.__isPlaying = False
    

a1 = AudioPlayer()