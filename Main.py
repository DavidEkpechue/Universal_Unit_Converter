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
        self.window.resizable(False, False)
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


        # Widgets

        self.label1 = ttk.Label(self.window, text='Enter distance:')
        self.label1.pack()

        self.user_entry = ttk.Entry(self.window, textvariable=self.int_var)
        self.user_entry.pack()

        self.dropdown_from = ttk.Combobox(self.window, textvariable=self.unit_string_from, values=self.units)
        self.dropdown_from.pack()

        self.dropdown_to = ttk.Combobox(self.window, textvariable=self.unit_string_to, values=self.units)
        self.dropdown_to.pack()

        self.button1 = ttk.Button(self.window, text='Convert', command=self.convert_units)
        self.button1.pack()

        self.result_label = ttk.Label(self.window, text="Conversion Result:")
        self.result_label.pack()

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
A1 = App(400, 600, 'Distance Converter')
