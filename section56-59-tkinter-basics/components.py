from time import sleep
import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext



class Components(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry('650x400+450+200')
        self.title('Components')
        self._create_tabs()

    def _create_components_tab1(self, tab):
        # Adding entries
        label1 = ttk.Label(tab, text='Name:')
        label1.grid(row=0, column=0, sticky=tk.E)
        entry1 = ttk.Entry(tab, width=30)
        entry1.grid(row=0, column=1, padx=5, pady=5)

        # Adding button
        def send():
            messagebox.showinfo('Message', f'Name: {entry1.get()}')
        
        button1 = ttk.Button(tab, text='Send', command=send)
        button1.grid(row=1, column=0, columnspan=2)

    def _create_components_tab2(self, tab):
        # Adding Scrolled Text
        content = 'This is a text'
        scroll_text1 = scrolledtext.ScrolledText(tab, width=50, height=10, wrap=tk.WORD)
        scroll_text1.insert(tk.INSERT, content)

        scroll_text1.grid(row=0, column=0)

    def _create_components_tab3(self, tab):
        # Addding DataList o Combobox
        data = [ x + 1 for x in range(10) ]
        combobox = ttk.Combobox(tab, width=15, values=data)
        combobox.grid(row=0, column=0, padx=10, pady=10)

        # Default value
        combobox.current(5)

        # Read value
        def show_value():
            messagebox.showinfo('Message',f'Value: {combobox.get()}')

        button1 = ttk.Button(tab, text='Show selected value', command=show_value)
        button1.grid(row=0, column=0, padx=10, pady=10)

    def _create_components_tab4(self, tab):
        # Handling images
        image = tk.PhotoImage(file='./section56-59-tkinter-basics/python-logo.png')

        def show_route():
            messagebox.showinfo('Information', f'Route: {image.cget("file")}')
        imagebutton = ttk.Button(tab, image=image, command=show_route)
        imagebutton.grid(row=0, column=0, padx=10, pady=10)

    def _create_components_tab5(self, tab):
        # Creating progress bar
        progress_bar = ttk.Progressbar(tab, orient='horizontal', length=550)
        progress_bar.grid(row=0, column=0, padx=10, pady=10, columnspan=4)

        def init_button():
            progress_bar['maximum'] = 100
            for i in range(101):
                sleep(0.05)
                progress_bar['value'] = i
                progress_bar.update()

            progress_bar['value'] = 0
            progress_bar.update()

        def loop_button():
            progress_bar.start()
        
        def stop_button():
            progress_bar.stop()
        
        def after_button():
            wait_ms = 1000
            self.after(wait_ms, progress_bar.stop)

        # Button controllers
        button1 = ttk.Button(tab, text='Init Button', command=init_button)
        button1.grid(row=1, column=0)

        button2 = ttk.Button(tab, text='Loop Button', command=loop_button)
        button2.grid(row=1, column=1)

        button3 = ttk.Button(tab, text='Stop Button', command=stop_button)
        button3.grid(row=1, column=2)

        button4 = ttk.Button(tab, text='After Button', command=after_button)
        button4.grid(row=1, column=3)


    def _create_tabs(self):
        # Creating tab controller
        control_tab = ttk.Notebook()

        # Create the frame tabs
        tab1 = ttk.Frame(control_tab)
        tab2 = ttk.LabelFrame(control_tab, text='Content')
        tab3 = ttk.Label(control_tab)
        tab4 = ttk.LabelFrame(control_tab, text='Image')
        tab5 = ttk.LabelFrame(control_tab, text='Progress Bar')

        # Adding tabs
        control_tab.add(tab1, text='Tab 1')
        control_tab.add(tab2, text='Tab 2')
        control_tab.add(tab3, text='Tab 3')
        control_tab.add(tab4, text='Tab 4')
        control_tab.add(tab5, text='Tab 5')

        control_tab.pack(fill='both')

        # Create components tab1
        self._create_components_tab1(tab1)

        # Create components tab2
        self._create_components_tab2(tab2)

        # Create components tab3
        self._create_components_tab3(tab3)

        # Create components tab4
        self._create_components_tab4(tab4)

        # Create components tab4
        self._create_components_tab5(tab5)

if __name__ == '__main__':
    components = Components()
    components.mainloop()
