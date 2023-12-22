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

        self.text_var = tk.StringVar(value= 'Howdy')

        # Widgets
        self.frame1 = ttk.Frame(self.window,
                                width=200,
                                height=200,
                                borderwidth=10,
                                relief=tk.GROOVE)
        self.frame1.pack(side= 'left')

        self.label1 = ttk.Label(self.frame1,
                                textvariable=self.text_var)
        self.label1.pack()


        self.button1 = ttk.Button(self.frame1,
                                  textvariable= self.text_var)
        self.button1.pack()

        self.frame2 = ttk.Frame(self.window)
        self.frame2.pack(side="left")

        self.entry = ttk.Entry(self.frame2,
                               textvariable= self.text_var)
        self.entry.pack()

        self.label2 = ttk.Label(self.frame2,
                                textvariable=self.text_var)
        self.label2.pack()

        self.button2 = ttk.Button(self.frame2,
                                  textvariable=self.text_var)
        self.button2.pack()



        # Events

        self.run()

    def run(self):
        self.window.mainloop()


A1 = App(600, 400, 'My window')
