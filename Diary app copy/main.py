from tkinter import *
from tkinter import ttk
from tkinter.colorchooser import askcolor
from time import *

from calendarik import *
from diary import *
from text_redactor import *

import random,os

play_from_start()

list_of_hints = ['What a nice day!...','I learned smt new today...','Had an interesting day!...','Got usefull skills...']
# folder_path = 'C:\\Users\\Turanch0X\\Desktop\\видео_фото_аудио\\Заметки'
# settings = ['1','2','3']

def update_time():
    current_time = strftime('%H:%M:%S') #function from time module
    timing.config(text=current_time)
    timing.after(1000,update_time)

def past():
    back()
    fill(info_label)

def future():
    next()
    fill(info_label)

window = Tk()
window.title('My Diary')
window.iconbitmap('C:\\Users\\Turanch0X\\Desktop\\IT\\Python\\TKinter\\Diary app\\logo.ico')
window.resizable(True,True)
window.geometry('467x474+800+100')
frame = Frame(window,bg='indigo')
frame.pack(fill=BOTH, expand=True)
timing = Label(frame,text='0',font=('Helvetica',20),fg='orange',bg='indigo')
timing.grid(row=0,column=7,columnspan=4,sticky='NSEW')
update_time()

back_button = Button(frame,text='<',command=past,borderwidth=0,relief="flat",fg='orange',bg='indigo')
next_button = Button(frame,text='>',command=future,borderwidth=0,relief="flat",fg='orange',bg='indigo')
info_label = Label(frame,width=3,height=1,font='Arial 16 bold',fg='orange',bg='indigo')

info_label.grid(row=0,column=1,columnspan=5,sticky='NSEW')
back_button.grid(row=0,column=0,sticky='NSEW')
next_button.grid(row=0,column=6,sticky='NSEW')

# def click(day):
    # message.delete('1.0', END)
    # selected_date = int(info_label.cget("text").split(", ")[1])
    # for file in os.listdir(folder_path):
    #     if file.endswith('.txt'):
    #         full_path = os.path.join(folder_path,file)
    #         creation = os.path.getctime(full_path)
    #         creation_datetime = date.fromtimestamp(creation)

    #         creation_day = creation_datetime.day
    #         creation_month = creation_datetime.month
    #         creation_year = creation_datetime.year
    

    #         if day == creation_day and month == creation_month and year == creation_year:
    #             formatted_date = creation_datetime.strftime('%d.%m.%Y')
    #             # message.insert(END, os.path.splitext(os.path.basename(file))[0] + '\n')
    #             message.insert(END, f'{os.path.splitext(os.path.basename(file))[0]}, Date: {formatted_date}\n')
    #         else:
    #             print('Nothing here')

for day in range(7):
    labl = Label(frame,text=calendar.day_abbr[day], width=3,height=2, font='Arial 10 bold', fg='black', borderwidth=0, relief="flat")
    labl.grid(row=1,column=day,sticky='NSEW') #ошибка автора. row=1, а не 2

for row in range(6):
    for col in range(7):
        day = (row * 7 + col + 1)-6
        butn = Button(frame,text=str(day),width=4,height=4,borderwidth=0,relief="flat") #command=lambda day=day: click(day)
        butn.grid(row=row+2,column=col,sticky='NSEW')
        days.append(butn)
fill(info_label)

message = Text(frame,bg='lightgray',width=26,height=22,wrap=WORD,fg='#b95028')
message.insert(END, random.choice(list_of_hints))
message.grid(row=2,rowspan=6,column=7,columnspan=3,sticky='NSEW') #с listboxom rowspan=7g

save_button = Button(frame, text = 'Save',command=lambda: save_text(message),borderwidth=0,relief="flat")
load_button = Button(frame, text = 'Load',command=lambda: load_text(message),borderwidth=0,relief="flat")

options = Button(frame, text = '⚙️', borderwidth=0, relief='flat', command=lambda: open_new_window(options)) #timing,info_label,back_button,next_button,labl

scrollbar = Scrollbar(frame, orient=VERTICAL, command=message.yview)
message['yscrollcommand'] = scrollbar.set
scrollbar.grid(row=2, rowspan=6, column=10, sticky='NSW')

save_button.grid(row=1,column=7,sticky='NSEW')
load_button.grid(row=1,column=9,columnspan=2,sticky='NSEW')
options.grid(row=1,column=8,sticky='NSEW')

window.mainloop()