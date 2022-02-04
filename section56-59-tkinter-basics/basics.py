# GUI - Graphical User Interface
import tkinter as tk
from tkinter import ttk

# Creating the window
window = tk.Tk()

# Window size
window.geometry('600x400')

# Window title
window.title('New window')

# Window icon
window.iconbitmap('section56-59-tkinter-basics/icono.ico')


# Listing events
def on_click():
    # Changing properties
    button1.config(text='Button pressed')
    button2 = ttk.Button(window, text='New button')
    button2.pack()
    print('Clicked')

# Adding elements or widgets
button1 = ttk.Button(window, text='Click me', command=on_click)

# Layout Manager to deploy widgets
button1.pack()

# Main loop
window.mainloop()
