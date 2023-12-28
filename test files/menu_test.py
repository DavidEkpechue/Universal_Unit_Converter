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
        self.menu = tk.Menu(self.window)

        self.window['menu'] = self.menu
        self.file_menu = tk.Menu(self.menu,
                                 tearoff=False)
        self.menu.add_cascade(label='File',
                              menu=self.file_menu)
        self.file_menu.add_command(label='new',
                                   command=lambda: print('New File'))
        self.file_menu.add_command(label='open',
                                   command=lambda: print('open File'))
        self.file_menu.add_command(label='save',
                                   command=lambda: print('Save File'))

        self.help_menu = tk.Menu(self.menu,
                                 tearoff=False)
        self.menu.add_cascade(label='Help',
                              menu=self.help_menu)
        self.help_menu.add_command(label='help',
                                   command=lambda: print('Helped'))

        self.menu3 = tk.Menu(self.menu,
                             tearoff= False)
        self.menu.add_cascade(label='menu3',
                              menu=self.menu3)
        self.menu3.add_command(label='test')

        self.menu3_submenu = tk.Menu(self.menu3,
                                     tearoff= False)
        self.menu3.add_cascade(label='test2',
                               menu= self.menu3_submenu)

        self.men_but = ttk.Menubutton(self.window,
                                      textvariable=self.text_var)
        self.men_but.pack()
        self.sub_men_but = tk.Menu(self.men_but,
                                   tearoff= False)
        self.sub_men_but.add_command(label= 'hii',
                                     command= lambda : print('test'))
        self.men_but['menu'] = self.sub_men_but
        # Events

        self.run()

    def run(self):
        self.window.mainloop()


A1 = App(600, 400, 'My window')
