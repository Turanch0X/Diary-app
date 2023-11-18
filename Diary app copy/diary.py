from tkinter import *
from tkinter import filedialog

def save_text(text_widget):
    text = text_widget.get('1.0',END).strip()
    if len(text)>0:
        file_path = filedialog.asksaveasfilename(defaultextension='.txt', filetypes=[("Text Files", "*.txt")])
        if file_path:
            with open(file_path,'w') as file:
                file.write(text)
    else:
        text_widget.delete('1.0', END)
        text_widget.insert(END, 'А вот ХУЙ тебе!')

def load_text(text_widget):
    file_path = filedialog.askopenfilename(filetypes=[('Text Files', '*.txt')])
    if file_path:
        with open(file_path, 'r') as file:
            text_widget.delete('1.0',END)
            text_widget.insert(END,file.read())