import tkinter as tk
from tkinter import ttk
from random import randint, choice


class App:
    def __init__(self, window_x, window_y, window_name):
        # Window
        self.window_x = window_x
        self.window_y = window_y
        self.window_name = window_name
        self.window = tk.Tk()
        self.window.title(f'{self.window_name}')
        self.window.geometry(f'{self.window_x}x{self.window_y}')

        self.canvas = tk.Canvas(self.window, bg='white',
                                scrollregion=(0, 0, 2000, 5000))

        self.canvas.create_line((0, 0, 2000, 5000), fill='black', width=10)

        for i in range(100):
            l = randint(0, 2000)
            t = randint(0, 5000)
            r = l + randint(10, 500)
            b = t + randint(10, 200)
            colour = choice(['black', 'white', 'red',
                             'green', 'yellow', 'blue'])
            self.canvas.create_rectangle(l, t, r, b, fill=colour)

        self.canvas.pack(expand=True, fill='both')

        self.scrollbar = ttk.Scrollbar(self.window,
                                       orient='vertical',
                                       command=self.canvas.yview)
        self.canvas.config(yscrollcommand=self.scrollbar.set)

        self.h_scrollbar = ttk.Scrollbar(self.window,
                                         orient='horizontal',
                                         command=self.canvas.xview)
        self.canvas.config(xscrollcommand=self.h_scrollbar.set)

        self.h_scrollbar.place(relx=0, rely=1, relwidth=1, anchor='sw')

        self.scrollbar.place(relx=1, rely=0, relheight=1, anchor='ne')

        # Events

        self.canvas.bind('<MouseWheel>',
                         lambda event: self.canvas.yview_scroll(-int(event.delta / 60), 'units'))
        self.canvas.bind('<Control MouseWheel>',
                         lambda event: self.canvas.xview_scroll(-int(event.delta / 60), 'units'))

        self.run()

    def run(self):
        self.window.mainloop()


A1 = App(600, 400, 'My window')
