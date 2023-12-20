import tkinter as tk
from tkinter import ttk


class App:
    def __init__(self, window_x, window_y, window_name):
        # Window setup
        self.window = tk.Tk()
        self.window.geometry(f"{window_x}x{window_y}")
        self.window.title(window_name)
        self.units = ['Feet', 'Miles', 'Yards', 'Inches', 'Light Years', 'Centimeters', 'Kilometers', '']
        self.feet_conversion = 0.3048
        self.miles_conversion = 1609.34
        self.yards_conversion = 0.9144
        self.inches_conversion = 0.0254
        self.centimeters_conversion = 0.01
        self.Kilometers_conversion = 1000
        self.lightyear_conversion = 9460660000000000

        # tk variables
        self.int_var = tk.IntVar()
        self.radio_var = tk.IntVar()
        self.unit_sting = tk.StringVar(value=self.units[0])

        # Widgets
        self.label1 = ttk.Label(self.window,
                                text='Enter distance:')
        self.label1.pack()

        self.user_entry = ttk.Entry(self.window,
                                    textvariable=self.int_var)
        self.user_entry.pack()

        self.button1 = ttk.Button(self.window, text='Convert',
                                  command=self.convert_to_meters)
        self.button1.pack()

        self.result_label = ttk.Label(self.window,
                                      text="Conversion Result:")
        self.result_label.pack()

        self.dropdown = ttk.Combobox(self.window,
                                     textvariable=self.unit_sting,
                                     values=self.units)
        self.dropdown.pack()

        self.run()

    def run(self):
        self.window.mainloop()

    def convert_to_meters(self):
        distance = self.int_var.get()
        conversion_type = self.unit_sting.get()

        if conversion_type == 'Feet':
            result = distance * self.feet_conversion
        elif conversion_type == 'Miles':
            result = distance * self.miles_conversion
        elif conversion_type == 'Yards':
            result = distance * self.yards_conversion
        elif conversion_type == 'Inches':
            result = distance * self.inches_conversion
        elif conversion_type == 'Centimeters':
            result = distance * self.centimeters_conversion
        elif conversion_type == 'Kilometers':
            result = distance * self.Kilometers_conversion
        elif conversion_type == 'Light Years':
            result = distance * self.lightyear_conversion
        else:
            result = "Invalid selection"

        if isinstance(result, (float, int)):
            self.result_label["text"] = f"Result: {result:.2f} meters"
        else:
            self.result_label["text"] = "Invalid selection"


# Create app instance
A1 = App(800, 600, 'Distance Converter')
