import tkinter as tk
from tkinter import ttk, messagebox


class Login(tk.Tk):
    def __init__(self):
        super().__init__()

        # Main window
        self.geometry('300x130')
        self.title('Login')
        self.resizable(0,0)

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=3)

        self._create_components()
    
    def _create_components(self):
        # User
        label_user = ttk.Label(text='User:')
        label_user.grid(row=0, column=0, sticky=tk.E, padx=5, pady=5)

        self.entry_user = ttk.Entry(self)
        self.entry_user.grid(row=0, column=1, sticky=tk.W, padx=5, pady=5)

        # Password
        label_pwd = ttk.Label(text='Password:')
        label_pwd.grid(row=1, column=0, sticky=tk.E, padx=5, pady=5)

        self.entry_pwd = ttk.Entry(self, show='*')
        self.entry_pwd.grid(row=1, column=1, sticky=tk.W, padx=5, pady=5)

        # Login 
        login_button = ttk.Button(self, text='Login', command=self._login)
        login_button.grid(row=3, column=0, padx=5, pady=5, columnspan=2)

    def _login(self):
        messagebox.showinfo('Login', f'user: {self.entry_user.get()}, password: {self.entry_pwd.get()}')


if __name__ == '__main__':
    login = Login()
    login.mainloop()



