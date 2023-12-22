import tkinter as tk
from tkinter import ttk


class App:
    def __init__(self, window_x, window_y, window_name):
        # Window
        self.window_x = window_x
        self.window_y = window_y
        self.window_name = window_name
        self.window = tk.Tk()
        self.window.title(f'{self.window_name}')
        self.window.geometry(f'{self.window_x}x{self.window_y}')
        self.Numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
                        11, 12, 13, 14, 15, 16, 17,
                        18, 19, 20, 21, 22, 23, 24,
                        25, 26, 27, 28, 29, 30, ]

        # tk variables

        self.text_var = tk.StringVar(value='Howdy')

        # Widgets


        self.notebook = ttk.Notebook(self.window)
        self.tab1 = ttk.Frame(self.notebook)
        self.scale = ttk.Scale(self.tab1)
        self.dropdown = ttk.Combobox(self.tab1,
                                     values=self.Numbers)
        self.scale.pack()
        self.dropdown.pack()

        self.tab2 = ttk.Frame(self.notebook)

        self.label = ttk.Label(self.tab2,
                               textvariable= self.text_var)
        self.entry = ttk.Entry(self.tab2,
                               textvariable= self.text_var)
        self.label.pack()
        self.entry.pack()


        self.notebook.pack()
        self.notebook.add(self.tab1, text='tab 1')
        self.notebook.add(self.tab2, text='tab 2')

        # Events

        self.run()

    def run(self):
        self.window.mainloop()


A1 = App(600, 400, 'My window')
