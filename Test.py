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
        self.string_var = tk.StringVar(value='enter text')
        self.check_var = tk.BooleanVar()
        self.radio_var = tk.StringVar()

        # Widgets
        self.label1 = ttk.Label(master=self.window,
                                text='Text',
                                textvariable=self.string_var)
        self.label1.pack()

        self.user_entry = ttk.Entry(master=self.window,
                                    textvariable=self.string_var)
        self.user_entry.pack()

        self.button1 = ttk.Button(master=self.window,
                                  text='Button 1',
                                  command=self.button_method)
        self.button1.pack()


        self.radio_button = ttk.Radiobutton(self.window,
                                            text='Radio Button1',
                                            value= 'A',
                                            command=self.button_method,
                                            variable=self.radio_var)
        self.radio_button.pack()

        self.radio_button2 = ttk.Radiobutton(self.window,
                                             text='Radio Button2',
                                             value= 'B',
                                             command=self.button_method,
                                             variable= self.radio_var)
        self.radio_button2.pack()

        # Events
        self.window.bind('<Alt-KeyPress-a>', lambda event: print('an event'))


        self.run()

    def run(self):
        self.window.mainloop()

    def button_method(self):
        print(self.check_var.get())
        self.check_var.set(False)

    def button_method2(self):
        print(self.radio_var.get())

A1 = App(200, 200, 'My window')
