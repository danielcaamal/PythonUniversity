import tkinter as tk
from tkinter import ttk
from tkinter.filedialog import askopenfile, asksaveasfilename

class Editor(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Text Editor')
        self.rowconfigure(0, minsize=600, weight=1)
        self.columnconfigure(1, minsize=600, weight=1)
        self.text_field = tk.Text(self, wrap=tk.WORD)
        self.file = None
        self.open_file = False

        self._create_components()
        self._create_menu()
    
    def _create_components(self):
        button_frame = tk.Frame(self,relief=tk.RAISED, bg='grey')

        open_button = tk.Button(button_frame, text='Open', command=self._open_file)
        save_button = tk.Button(button_frame, text='Save', command=self._save_file)
        save_as_button = tk.Button(button_frame, text='Save As', command=self._save_as_file)

        open_button.grid(row=0, column=0, sticky=tk.EW, padx=5, pady=5)
        save_button.grid(row=1, column=0, sticky=tk.EW, padx=5, pady=5)
        save_as_button.grid(row=2, column=0, sticky=tk.EW, padx=5, pady=5)

        button_frame.grid(row=0, column=0, sticky=tk.NS)
        self.text_field.grid(row=0, column=1, sticky=tk.NSEW)

    def _create_menu(self):
        app_menu = tk.Menu(self)
        self.config(menu=app_menu)
        file_menu = tk.Menu(app_menu, tearoff=False)
        app_menu.add_cascade(label='File', menu=file_menu)
        file_menu.add_command(label='Open', command=self._open_file)
        file_menu.add_command(label='Save', command=self._save_file)
        file_menu.add_command(label='Save As', command=self._save_as_file)
        file_menu.add_separator()
        file_menu.add_command(label='Exit', command=self._exit)
    
    def _open_file(self):
        self.open_file = askopenfile(mode='r+')
        self.text_field.delete(1.0, tk.END)
        if not self.open_file:
            return
        
        with open(self.open_file.name, 'r+') as self.file:
            text = self.file.read()
            self.text_field.insert(1.0, text)
            self.title(f'*Text Editor - {self.file.name}')
        


    def _save_file(self):
        if self.open_file:
            with open(self.open_file.name, 'w') as self.file:
                text = self.text_field.get(1.0, tk.END)
                self.file.write(text)
                self.title(f'Text Editor - {self.file.name}')
        else:
            self._save_as_file()


    def _save_as_file(self):
        self.file = asksaveasfilename(
            defaultextension='txt',
            filetypes=[('Text Files', '*.txt'),('All files', '*.*')]
        )
        if not self.file:
            return
        
        with open(self.file, 'w') as self.file:
            text = self.text_field.get(1.0, tk.END)
            self.file.write(text)
            self.title(f'Text Editor - {self.file.name}')
            self.open_file = self.file
    
    
    def _exit(self):
        self.quit()










if __name__ == '__main__':
    edit = Editor()
    edit.mainloop()
