import tkinter as tk
from tkinter import ttk
import math as math


class App:
    def __init__(self, window_x, window_y, window_name):
        # Window setup
        self.window = tk.Tk()
        self.window.geometry(f"{window_x}x{window_y}")
        self.window.title(window_name)
        self.window.attributes('-topmost', True)
        self.units = ['Feet', 'Miles', 'Yards',
                      'Inches', 'Light Years', 'Meters',
                      'Centimeters', 'Kilometers']

        self.conversions = {'Feet': 0.3048, 'Miles': 1609.34, 'Yards': 0.9144,
                            'Inches': 0.0254, 'Meters': 1, 'Centimeters': 0.01,
                            'Kilometers': 1000, 'Light Years': 9460660000000000}

        # tk variables
        self.int_var = tk.IntVar()
        self.unit_string_from = tk.StringVar(value=self.units[0])
        self.unit_string_to = tk.StringVar(value=self.units[0])

        # frames

        self.frame1 = ttk.Frame(self.window)
        self.frame2 = ttk.Frame(self.window)
        self.frame3 = ttk.Frame(self.frame1)

        self.frame1.place(x=0,
                          y=0,
                          relwidth=0.3,
                          relheight=1)
        self.frame2.place(relx=0.3,
                          y=0,
                          relwidth=0.7,
                          relheight=1)
        self.frame3.grid(row=4,
                         column=0,
                         columnspan= 3)

        self.frame1.columnconfigure((0, 1, 2),
                                    weight=1,
                                    uniform='a')
        self.frame1.rowconfigure((0, 1, 2, 3, 4),
                                 weight=1,
                                 uniform='a')

        # Widgets

        self.scale_var = tk.IntVar()

        self.scale = ttk.Scale(self.frame1,
                               command=lambda value: print(self.scale_var.get()),
                               from_=0,
                               to=100,
                               length=200,
                               variable=self.scale_var,
                               orient='vertical')
        self.scale.grid(row=0,
                        column=0,
                        sticky='ns',
                        rowspan=2)

        self.progress = ttk.Progressbar(self.frame1,
                                        variable=self.scale_var,
                                        maximum=100,
                                        orient='vertical')
        self.progress.start()
        self.progress.grid(row=0,
                           column=1,
                           sticky='ns',
                           rowspan=2)

        self.label = ttk.Label(self.frame1,
                               textvariable=self.scale_var,
                               font=50,
                               background='#A9A9A9')

        self.label['anchor'] = 'center'

        self.label.grid(row=2,
                        column=0,
                        sticky='nsew',
                        columnspan=3,
                        padx=15,
                        pady=15)

        # frame 2
        self.label1 = ttk.Label(self.frame2,
                                text='Enter distance:', )
        self.label1.pack()

        self.user_entry = ttk.Entry(self.frame2, textvariable=self.int_var)
        self.user_entry.pack()

        self.dropdown_from = ttk.Combobox(self.frame2, textvariable=self.unit_string_from, values=self.units)
        self.dropdown_from.pack()

        self.dropdown_to = ttk.Combobox(self.frame2, textvariable=self.unit_string_to, values=self.units)
        self.dropdown_to.pack()

        self.button1 = ttk.Button(self.frame2, text='Convert', command=self.convert_units)
        self.button1.pack()

        self.result_label = ttk.Label(self.frame2, text="Conversion Result:")
        self.result_label.pack()

        #frame 3

        self.checkbutton = ttk.Checkbutton(self.frame3,
                                           text="Check")

        self.checkbutton.pack(side="left")




        self.label['anchor'] = 'center'

        self.run()

    def run(self):
        self.window.mainloop()

    def convert_units(self):
        distance = self.int_var.get()
        unit_from = self.unit_string_from.get()
        unit_to = self.unit_string_to.get()

        # Convert the input to meters first
        meters = distance * self.conversions[unit_from]

        # Then convert from meters to the target unit
        result = meters / self.conversions[unit_to]

        self.result_label["text"] = f"Result: {result:.2f} {unit_to}"


# Create app instance
A1 = App(800, 600, 'Distance Converter')
