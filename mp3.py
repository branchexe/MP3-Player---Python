import tkinter as tk
from tkinter import filedialog
import pygame
import os


#       -- ONLY MP3, OGG, AND WAV ARE SUPPORTED, CHECK PYGAME FOR MORE --
def play_audio():
    global songtitle
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()
    songtitle = os.path.basename(filename)
    songtitle_label.config(text=songtitle)
    seek_bar.config(to=pygame.mixer.music.get_pos())
    update_seek_bar()

def pause_audio():
    pygame.mixer.music.pause()

def stop_audio():
    pygame.mixer.music.stop()

def open_file():
    global filename
    filename = filedialog.askopenfilename()

def update_seek_bar():
    progress = pygame.mixer.music.get_pos()/1000
    seek_bar.set(pygame.mixer.music.get_pos()/1000)
    progress_label.config(text=f'{int(progress)}/{int(seek_bar.cget("to"))}')
    seek_bar.set(progress)
    root.after(100, update_seek_bar)

def seek(val):
    pygame.mixer.music.play()
    pygame.mixer.music.set_pos(float(val)*1000)

root = tk.Tk()
root.title("MP3 Player")

play_button = tk.Button(root, text="Play", command=play_audio)
play_button.pack()

pause_button = tk.Button(root, text="Pause", command=pause_audio)
pause_button.pack()

stop_button = tk.Button(root, text="Stop", command=stop_audio)
stop_button.pack()

open_file_button = tk.Button(root, text="Open File", command=open_file)
open_file_button.pack()

seek_bar = tk.Scale(root, from_=0, orient=tk.HORIZONTAL, command=seek, sliderlength=20)
seek_bar.pack()

songtitle_label = tk.Label(root, text="")
songtitle_label.pack()

progress_label = tk.Label(root, text="")
progress_label.pack()

pygame.init()
root.mainloop()
