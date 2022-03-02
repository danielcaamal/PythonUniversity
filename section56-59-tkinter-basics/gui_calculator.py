import tkinter as tk
from tkinter import ttk, messagebox

class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry('400x350')
        self.resizable(0,0)
        self.title('Calculator')
        self.iconbitmap('./section56-59-tkinter-basics/calculadora.ico')

        # Variables
        self.expression = ''
        self.entry = None
        self.entry_text = tk.StringVar()

        self._create_components()

    def _create_components(self):
        # Creating the frame text
        entry_frame = tk.Frame(self, width=50, height=50, bg='grey')
        entry_frame.pack(side=tk.TOP)

        entry = tk.Entry(
            entry_frame, 
            font=('arial', 18, 'bold'), 
            textvariable=self.entry_text, 
            width=30,
            justify=tk.RIGHT
        ).grid(row=0, column=0, ipady=10)

        # Creating the frame buttons
        button_frame = tk.Frame(self, width=400, height=450, bg='grey')
        button_frame.pack()

        # Clean button
        clean_button = tk.Button(
            button_frame,text='C',
            width=32, 
            command=self._clean_event,
            height=3,
            bd=0,
            bg='#eee',
            cursor='hand2',
        ).grid(row=0, column=0, columnspan=3, padx=1, pady=1)

        # Division button
        division_button = tk.Button(
            button_frame,
            text='/',
            width=10,
            command=lambda: self._click_event('/'),
            height=3,
            bd=0,
            bg='#eee',
            cursor='hand2',
        ).grid(row=0, column=3, padx=1, pady=1)

        # Numeric buttons
        button_map = (
            ('7',1,0,lambda: self._click_event('7')),('8',1,1,lambda: self._click_event('8')),('9',1,2,lambda: self._click_event('9')),('*',1,3,lambda: self._click_event('*')),
            ('4',2,0,lambda: self._click_event('4')),('5',2,1,lambda: self._click_event('5')),('6',2,2,lambda: self._click_event('6')),('-',2,3,lambda: self._click_event('-')),
            ('1',3,0,lambda: self._click_event('1')),('2',3,1,lambda: self._click_event('2')),('3',3,2,lambda: self._click_event('3')),('+',3,3,lambda: self._click_event('+')),
            (',',4,0,lambda: self._click_event(',')),('0',4,1,lambda: self._click_event('0')),('.',4,2,lambda: self._click_event('.')), ('=',4,3,lambda: self._evaluate_event())
        )
        
        buttons = [x for x in range(21)]
        for index, button in enumerate(button_map):
            buttons[index] = tk.Button(
                button_frame,
                text=button[0],
                width=10,
                command=button[3],
                height=3,
                bd=0,
                bg='#eee',
                cursor='hand2',
            ).grid(row=button[1], column=button[2], padx=1, pady=1)

    

    def _clean_event(self):
        self.expression = ''
        self.entry_text.set(self.expression)

    def _click_event(self, element):
        self.expression = f'{self.expression}{element}'
        self.entry_text.set(self.expression)

    def _evaluate_event(self):
        try:
            resultado = str(eval(self.expression))
            self.entry_text.set(resultado)
        except Exception as e:
            messagebox.showerror('Error', f'Ha ocurrido un error: {e}')
            self.entry_text.set('')
        self.expression = ''



if __name__ == '__main__':
    calc = Calculator()
    calc.mainloop()