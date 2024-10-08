import os
import pygame
import tkinter as tk
from tkinter import filedialog

pygame.mixer.init()

root = tk.Tk()
root.title("Music Player")
root.geometry("600x500")
root.configure(bg="darkslateblue")  # Closest name for #1a1a2e

playlist = []
current_song_index = 0
is_playing = False

def add_song():
    song_path = filedialog.askopenfilename(filetypes=[("Music Files", "*.mp3")])
    if song_path:
        playlist.append(song_path)
        song_list.insert(tk.END, os.path.basename(song_path))

def play_pause_song():
    global current_song_index, is_playing
    if is_playing:
        pygame.mixer.music.pause()
        play_pause_button.config(text="Play")
        is_playing = False
    else:
        if not pygame.mixer.music.get_busy():
            selected_song = song_list.curselection()
            if selected_song:
                current_song_index = selected_song[0]
                song_path = playlist[current_song_index]
                pygame.mixer.music.load(song_path)
                pygame.mixer.music.play()
            else:
                return
        else:
            pygame.mixer.music.unpause()
        play_pause_button.config(text="Pause")
        is_playing = True

def forward_song():
    global current_song_index
    if current_song_index < len(playlist) - 1:
        current_song_index += 1
        update_song_selection()
        pygame.mixer.music.load(playlist[current_song_index])
        pygame.mixer.music.play()
        play_pause_button.config(text="Pause")
        is_playing = True

def backward_song():
    global current_song_index
    if current_song_index > 0:
        current_song_index -= 1
        update_song_selection()
        pygame.mixer.music.load(playlist[current_song_index])
        pygame.mixer.music.play()
        play_pause_button.config(text="Pause")
        is_playing = True

def update_song_selection():
    song_list.select_clear(0, tk.END)
    song_list.activate(current_song_index)
    song_list.select_set(current_song_index)

button_style = {"bg": "crimson", "fg": "white", "font": ("Arial", 12), "activebackground": "midnightblue"}  # Closest names for #e94560 and #0f3460
label_style = {"bg": "darkslateblue", "fg": "ghostwhite", "font": ("Arial", 16, "bold")}  # Closest names for #1a1a2e and #f7f7f7

title_label = tk.Label(root, text="Music Player", **label_style)
title_label.grid(row=0, column=0, columnspan=4, pady=20)

song_list = tk.Listbox(root, bg="midnightblue", fg="white", font=("Arial", 12), width=60, height=15, selectbackground="crimson")  # Closest names for #16213e and #e94560
song_list.grid(row=1, column=0, columnspan=4, padx=20, pady=20)

add_button = tk.Button(root, text="Add Song", command=add_song, **button_style)
add_button.grid(row=2, column=0, padx=10, pady=20)

backward_button = tk.Button(root, text="Previous", command=backward_song, **button_style)
backward_button.grid(row=2, column=1, padx=10, pady=20)

play_pause_button = tk.Button(root, text="Play", command=play_pause_song, **button_style)
play_pause_button.grid(row=2, column=2, padx=10, pady=20)

forward_button = tk.Button(root, text="Next", command=forward_song, **button_style)
forward_button.grid(row=2, column=3, padx=10, pady=20)

root.mainloop()
