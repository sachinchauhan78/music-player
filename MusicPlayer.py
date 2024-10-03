import pygame
import tkinter as tkr
from tkinter import ttk
from tkinter.filedialog import askdirectory
import os

class MusicPlayer:
    def __init__(self, master):
        self.master = master
        self.master.title("Music Player")
        self.master.geometry("500x400")
        self.master.configure(bg="black")

        self.directory = askdirectory()
        os.chdir(self.directory)
        self.song_list = os.listdir()

        self.play_list = tkr.Listbox(self.master, font=("Arial", 12), bg='white', selectmode=tkr.SINGLE, bd=0, selectbackground='#4CAF50')
        for item in self.song_list:
            self.play_list.insert(tkr.END, item)

        pygame.init()
        pygame.mixer.init()

        self.var = tkr.StringVar() 
        self.song_title = tkr.Label(self.master, font=("Arial", 16, "bold"), textvariable=self.var, bg="#333333", fg="#ffffff")

        self.create_widgets()

    def create_widgets(self):
        ttk.Separator(self.master, orient='horizontal').pack(fill='x', pady=10)

        tkr.Label(self.master, text="Music Player", font=("Arial", 20, "bold"), bg="dark blue", fg="white").pack(pady=10)

        tkr.Frame(self.master, bg="black").pack()

        tkr.Button(self.master, text="PLAY", command=self.play, bg="red", fg="white", font=("Arial", 12, "bold")).pack(side=tkr.LEFT, padx=10)
        tkr.Button(self.master, text="STOP", command=self.stop, bg="green", fg="white", font=("Arial", 12, "bold")).pack(side=tkr.LEFT, padx=10)
        tkr.Button(self.master, text="PAUSE", command=self.pause, bg="orange", fg="white", font=("Arial", 12, "bold")).pack(side=tkr.LEFT, padx=10)
        tkr.Button(self.master, text="UNPAUSE", command=self.unpause, bg="yellow", fg="white", font=("Arial", 12, "bold")).pack(side=tkr.LEFT, padx=10)

        ttk.Separator(self.master, orient='horizontal').pack(fill='x', pady=10)

        self.song_title.pack(pady=10)

        self.play_list.pack(fill="both", expand="yes", padx=10, pady=10)

    def play(self):
        try:
            selected_song = self.play_list.get(tkr.ACTIVE)
            pygame.mixer.music.load(selected_song)
            self.var.set(selected_song)
            pygame.mixer.music.play()
        except pygame.error:
            print("Error: Unable to play the selected song.")

    def stop(self):
        pygame.mixer.music.stop()

    def pause(self):
        pygame.mixer.music.pause()

    def unpause(self):
        pygame.mixer.music.unpause()

if __name__ == "__main__":
    root = tkr.Tk()
    app = MusicPlayer(root)
    root.mainloop()
