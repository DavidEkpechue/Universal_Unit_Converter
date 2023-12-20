import tkinter as tk
from tkinter import ttk
from random import choice


class App:
    def __init__(self, window_x, window_y, window_name):
        # Window
        self.window_x = window_x
        self.window_y = window_y
        self.window_name = window_name
        self.window = tk.Tk()
        self.window.title(f'{self.window_name}')
        self.window.geometry(f'{self.window_x}x{self.window_y}')
        self.first_names = ['David', 'John', 'Daniel',
                            'Emmanuel', 'Mohamed', 'Jennifer',
                            'Anthony', 'Lucy', 'Bernhard',
                            'Mortimer', 'Sophia', 'Niamh',
                            'Denis', 'Patryk', 'Reuben',
                            'Paul', 'Mia', 'Maia',
                            'Niggard', 'Chris', 'Jesus',
                            'Valentine', 'Yvonne', 'Linus',
                            'Johannes', 'Samuel', 'Sadie',
                            'Vincent', 'Ling-Ling', 'Raheem'
                            ]

        self.second_names = ['Ekpechue', 'Johannes', 'Davis',
                             'Brown', 'White', 'Black',
                             'Smith', 'Bishop', 'O\' Reilly',
                             'Cook', 'Taylor', 'Walker',
                             'Kent', 'Wayne', 'Itadori',
                             'Andrews', 'Ferris', 'Tolkein',
                             'Zach', 'Jaeger', 'Potter',
                             'Farrell', 'Gill', 'Moore',
                             'Lee', 'Peerson', 'Bander',
                             'Adeniranye', 'Abourass', 'Awode',
                             'Adekunle', 'Tinubu', 'Niggerson', 'Benyounis']

        # tk variables

        # Widgets
        self.table = ttk.Treeview(self.window,
                                  columns=('first', 'last', 'email'),
                                  show='headings')
        self.table.heading('first',
                           text='First Name')
        self.table.heading('last',
                           text='Surname')
        self.table.heading('email',
                           text='Email Address')
        self.table.pack(fill='both',
                        expand=True)

        for i in range(100):
            first = choice(self.first_names)
            last = choice(self.second_names)
            email = f'{first}{last}@example.com'
            data = (first, last, email)
            self.table.insert(parent='',
                              index=0,
                              values=data)
        self.table.insert(parent='',
                          index=tk.END,
                          values=('XXXX', 'YYYY', 'ZZZZ'))

        # Events
        self.table.bind('<<TreeviewSelect>>',
                        self.item_select)
        self.table.bind('<Delete>', self.delete_items)

        self.run()

    def run(self):
        self.window.mainloop()

    def item_select(self, _):
        for i in self.table.selection():
            print(self.table.item(i)['values'])
    def delete_items(self, _):
        for i in self.table.selection():
            self.table.delete(i)



A1 = App(600, 400, 'My window')
