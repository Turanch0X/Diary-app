from tkinter import *
import pygame

pygame.mixer.init()
assistent = pygame.mixer.music
count = 1
dark_font_color = '#d5875a'

def open_new_window(menu): #timer,infa,nazad,vpered,weekdays
    def on_close():
        menu['state'] = ACTIVE
        root.destroy()

    root = Toplevel()
    root.title('Option Menu')
    root.geometry('+980+180')
    root.protocol("WM_DELETE_WINDOW", on_close)

    music = Button(root, text='Play music ⏸️', pady=10, borderwidth=0, command=manage_music).pack()
    dark_theme = Button(root, text='Dark color theme 🌙', pady=10, borderwidth=0).pack() #command=lambda: set_dark(timer,infa,nazad,vpered)
    light_theme = Button(root, text='Light color theme ☀️', pady=10, borderwidth=0).pack() #command=lambda: set_light(timer,infa,nazad,vpered,weekdays)
    default_theme = Button(root, text='Default color theme 🔙', pady=10, borderwidth=0).pack() #command=lambda: set_default(timer,infa,nazad,vpered)

    menu['state'] = DISABLED  # Set the gear button to disabled

def play_from_start():
    assistent.load('C:\\Users\\Turanch0X\\Desktop\\IT\\Python\\TKinter\\Diary app\\Suite.mp3')
    assistent.set_volume(0.4)
    assistent.play()

def manage_music():
    global count
    if count%2!=0:
        assistent.stop()
    else:
        assistent.play()
    count+=1

# def set_dark(timer,infa,nazad,vpered):
#     timer.config(bg='black',fg=dark_font_color)
#     infa.config(bg='black',fg=dark_font_color)
#     nazad.config(bg='black',fg=dark_font_color)
#     vpered.config(bg='black',fg=dark_font_color)

# def set_light(timer,infa,nazad,vpered,weekdays):
#     timer.config(bg='lightgrey',fg='grey')
#     infa.config(bg='lightgrey',fg='grey')
#     nazad.config(bg='lightgrey',fg='grey')
#     vpered.config(bg='lightgrey',fg='grey')
#     weekdays.config(bg='white', fg='black')

# def set_default(timer,infa,nazad,vpered):
#     timer.config(bg='indigo',fg='orange')
#     infa.config(bg='indigo',fg='orange')
#     nazad.config(bg='indigo',fg='orange')
#     vpered.config(bg='indigo',fg='orange')