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

        # tk variables
        self.scale_var = tk.IntVar()

        # Widgets
        self.scale = ttk.Scale(self.window,
                               command=lambda value: print(self.scale_var.get()),
                               from_=0,
                               to=100,
                               length= 200,
                               variable= self.scale_var)
        self.scale.pack()


        self.progress = ttk.Progressbar(self.window,
                                        variable= self.scale_var,
                                        maximum= 100,
                                        orient= 'vertical')
        self.progress.start()
        self.progress.pack()

        self.label = ttk.Label(self.window,
                               textvariable= self.scale_var)
        self.label.pack()



        # Events

        self.run()

    def run(self):
        self.window.mainloop()


A1 = App(600, 400, 'My window')
