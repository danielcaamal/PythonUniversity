# GUI - Graphical User Interface
import tkinter as tk
from tkinter import ttk

# Creating the window
window = tk.Tk()

# Window size
window.geometry('600x400')

# Window title
window.title('Grid view')


# Grid configuration ROW
window.rowconfigure(0, weight=1)
window.rowconfigure(1, weight=5)
window.rowconfigure(2, weight=2)

# Grid configuration COLUMN
window.columnconfigure(0, weight=2)
window.columnconfigure(1, weight=1)

# Events
def event1():
    button1.config(text='Button 1 Pressed')


def event2():
    button2.config(text='Button 2 Pressed')

def event3():
    button3.config(text='Button 3 Pressed')

def event4():
    button4.config(text='Button 4 Pressed')

def event5():
    button5.config(text='Button 5 Pressed', fg='blue', relief=tk.GROOVE, bg='yellow')

# Widgets
button1 = ttk.Button(window, text='Button 1', command=event1)
button2 = ttk.Button(window, text='Button 2', command=event2)
button3 = ttk.Button(window, text='Button 3', command=event3)
button4 = ttk.Button(window, text='Button 4', command=event4)


# Grid view
button1.grid(row=0, column=0, sticky=tk.NSEW)
# Sticky N, S, E, W
button2.grid(row=1, column=0, sticky=tk.NSEW)

# Using paddings and columnspans, rowspans
button3.grid(row=2, column=0, sticky=tk.NSEW, padx=20, columnspan=2)
button4.grid(row=0, column=1, sticky=tk.NSEW, ipadx=20)

# Using tk functions
button5 = tk.Button(window, text='Button 5', command=event5)
button5.grid(row=1, column=1, sticky=tk.NSEW)

# Main loop
window.mainloop()
