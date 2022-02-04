# GUI - Graphical User Interface
from cgitb import text
import tkinter as tk
from tkinter import ttk

# Creating the window
window = tk.Tk()

# Window size
window.geometry('600x400')

# Window title
window.title('Grid view')


# Labels
label1 = tk.Label(window, text='This is a label', justify=tk.LEFT)

# Variable associated to entry

entry1_var = tk.StringVar(value='Default value')

# Callbacks

def on_click():
    entry1.config(state=tk.NORMAL)
    button2.config(state=tk.NORMAL)

def on_click_2():
    entry1.config(state=tk.NORMAL)
    password.config(text=entry1.get())
    print(f'Reading string: {entry1.get()}')
    print(f'Reading string using variable: {entry1_var.get()}')
    print(f'Writing string using variable: {entry1_var.set("Changing")}')

    entry1.select_range(0 ,tk.END)
    entry1.focus()
    # entry1.delete(0, tk.END)

# Widgets
entry1 = ttk.Entry(window, width=30, justify=tk.CENTER, textvariable=entry1_var)
password = ttk.Entry(window, width=30, justify=tk.CENTER, show='*')

# Disable widgets
button1 = ttk.Button(window, text='Enable string and button', command=on_click, state=tk.NORMAL)
button2 = ttk.Button(window, text='Send', command=on_click_2, state=tk.DISABLED)


# Grid
entry1.grid(row=0, column=0)
password.grid(row=1, column=0)
button1.grid(row=0, column=1)
button2.grid(row=0, column=2)
label1.grid(row=2, column=0)


# Insert text
# entry1.insert(0, 'Insert one string')
# entry1.insert(tk.END, '.')

# entry1.config(state='readonly')

# Main loop
window.mainloop()