import tkinter as tk
from tkinter import ttk
import math as math


def create_small_layout():
    print('small_layout')


def create_medium_layout():
    print('medium_layout')


class App(tk.Tk):
    def __init__(self, window_x, window_y, window_name):
        super().__init__()
        # Window setup
        self.geometry(f"{window_x}x{window_y}")
        self.title(window_name)
        self.attributes('-topmost', True)

        # Store tabs and notebook as instance variables
        self.notebook = ttk.Notebook(self)
        self.notebook.grid(row=0, column=0, sticky='nsew', padx=10, pady=10)

        self.tabs = {
            'Distance': DistanceConverter(self.notebook),
            'Temperature': TemperatureConverter(self.notebook),
            'Mass': MassConverter(self.notebook),
            'Area': AreaConverter(self.notebook),
            'Time': TimeConverter(self.notebook),
            'Speed': SpeedConverter(self.notebook),
            'Volume': VolumeConverter(self.notebook),
            'Pressure': PressureConverter(self.notebook),
            'Energy': EnergyConverter(self.notebook)
        }

        # Add tabs to the notebook
        for name, tab in self.tabs.items():
            self.notebook.add(tab, text=name)

        size_dict = {
            300: self.small_size_test,  # Width threshold for 'small' layout
            600: self.medium_size_test  # Width threshold for 'medium' layout
        }

        # Initialize the SizeNotifier with the size dictionary
        self.size_notifier = SizeNotifier(self, size_dict)

        self.grid_rowconfigure(0, weight=1, uniform='a')
        self.grid_columnconfigure((0, 1), weight=1, uniform='a')

        self.mainloop()

    def small_size_test(self):
        print('Current size: Small')

    def medium_size_test(self):
        print('Current size: Medium')



class SizeNotifier:
    def __init__(self, window, size_dict):
        self.window = window
        self.size_dict = {key: value for key, value in sorted(size_dict.items(), reverse=True)}
        self.current_min_size = None

        self.window.bind('<Configure>', self.check_size)
        self.check_size(None)  # Initial check to set up the correct size on start

    def check_size(self, event):
        window_width = self.window.winfo_width()
        checked_size = None

        for min_size in self.size_dict:
            if window_width >= min_size:
                checked_size = min_size
                break  # Exit loop once the appropriate size is found

        if checked_size != self.current_min_size:
            self.current_min_size = checked_size
            self.size_dict[self.current_min_size]()

class BaseConverter(ttk.Frame):
    def __init__(self, parent, units, conversions, label_text):
        super().__init__(parent)
        self.units = units
        self.conversions = conversions

        self.unit_string_from = tk.StringVar(value=self.units[0])
        self.unit_string_to = tk.StringVar(value=self.units[0])
        self.value_var = tk.DoubleVar()

        self.create_widget(label_text)
        self.create_layout()

    def create_widget(self, label_text):
        self.label1 = ttk.Label(self, text=f'Enter {label_text}:', anchor='center', font=50)
        self.label2 = ttk.Label(self, text='TO', font=50, padding=30)
        self.user_entry = ttk.Entry(self, textvariable=self.value_var)
        self.dropdown_from = ttk.Combobox(self, textvariable=self.unit_string_from, values=self.units)
        self.dropdown_to = ttk.Combobox(self, textvariable=self.unit_string_to, values=self.units)
        self.button1 = ttk.Button(self, text='Convert', command=self.convert_units)
        self.result_label = ttk.Label(self, text="Conversion Result:", anchor='center', font=20)

    def create_layout(self):
        self.grid_rowconfigure((0, 1, 2, 3, 4), weight=1, uniform='a')
        self.grid_columnconfigure((0, 1, 2), weight=1, uniform='a')

        self.label1.grid(row=0, column=0, columnspan=3, sticky='news')
        self.label2.grid(row=2, column=1, columnspan=3, sticky='news')
        self.user_entry.grid(row=1, column=0, columnspan=3, sticky='news', pady=5)
        self.dropdown_from.grid(row=2, column=0, sticky='news')
        self.dropdown_to.grid(row=2, column=2, sticky='news')
        self.button1.grid(row=3, column=0, columnspan=3, sticky='news')
        self.result_label.grid(row=4, column=0, columnspan=3, sticky='news')

    def convert_units(self):
        value = self.value_var.get()
        unit_from = self.unit_string_from.get()
        unit_to = self.unit_string_to.get()

        # Convert the input to the base unit first
        base_unit_value = value * self.conversions[unit_from]

        # Then convert from the base unit to the target unit
        result = base_unit_value / self.conversions[unit_to]

        self.result_label["text"] = f"Result: {result:.2f} {unit_to}"


class DistanceConverter(BaseConverter):
    def __init__(self, parent):
        units = ['Feet', 'Miles', 'Yards', 'Inches', 'Light Years', 'Meters', 'Centimeters', 'Kilometers']
        conversions = {'Feet': 0.3048, 'Miles': 1609.34, 'Yards': 0.9144, 'Inches': 0.0254, 'Meters': 1,
                       'Centimeters': 0.01, 'Kilometers': 1000, 'Light Years': 9460660000000000}
        super().__init__(parent, units, conversions, 'distance')


class TemperatureConverter(BaseConverter):
    def __init__(self, parent):
        units = ['Celsius', 'Fahrenheit', 'Kelvin']
        conversions = {'Celsius': 1, 'Fahrenheit': 1, 'Kelvin': 1}  # Placeholder as conversion is non-linear
        super().__init__(parent, units, conversions, 'temperature')

    def convert_units(self):
        temp = self.value_var.get()
        unit_from = self.unit_string_from.get()
        unit_to = self.unit_string_to.get()

        # Convert the input to Celsius first
        if unit_from == 'Fahrenheit':
            temp = (temp - 32) * 5 / 9
        elif unit_from == 'Kelvin':
            temp = temp - 273.15

        # Then convert from Celsius to the target unit
        if unit_to == 'Fahrenheit':
            result = (temp * 9 / 5) + 32
        elif unit_to == 'Kelvin':
            result = temp + 273.15
        else:
            result = temp

        self.result_label["text"] = f"Result: {result:.2f} {unit_to}"


class MassConverter(BaseConverter):
    def __init__(self, parent):
        units = ['Kilograms', 'Grams', 'Pounds', 'Ounces', 'Stones', 'Metric Tons', 'Carats']
        conversions = {
            'Kilograms': 1, 'Grams': 0.001, 'Pounds': 0.453592, 'Ounces': 0.0283495,
            'Stones': 6.35029, 'Metric Tons': 1000, 'Carats': 0.0002
        }
        super().__init__(parent, units, conversions, 'mass')


class AreaConverter(BaseConverter):
    def __init__(self, parent):
        units = ['Square Meters', 'Square Kilometers', 'Square Feet', 'Acres', 'Hectares']
        conversions = {'Square Meters': 1, 'Square Kilometers': 1000000, 'Square Feet': 0.092903, 'Acres': 4046.86,
                       'Hectares': 10000}
        super().__init__(parent, units, conversions, 'area')


class TimeConverter(BaseConverter):
    def __init__(self, parent):
        units = ['Seconds', 'Minutes', 'Hours', 'Days', 'Weeks', 'Years']
        conversions = {
            'Seconds': 1, 'Minutes': 60, 'Hours': 3600,
            'Days': 86400, 'Weeks': 604800, 'Years': 31536000
        }
        super().__init__(parent, units, conversions, 'time')


class SpeedConverter(BaseConverter):
    def __init__(self, parent):
        units = ['Kilometers per Hour', 'Miles per Hour', 'Meters per Second', 'Feet per Second', 'Knots', 'Mach']
        conversions = {
            'Kilometers per Hour': 0.277778,
            'Miles per Hour': 0.44704,
            'Meters per Second': 1,
            'Feet per Second': 0.3048,
            'Knots': 0.514444,
            'Mach': 343
        }
        super().__init__(parent, units, conversions, 'speed')


class VolumeConverter(BaseConverter):
    def __init__(self, parent):
        units = ['Liters', 'Milliliters', 'Cubic Meters', 'Gallons', 'Cubic Feet', 'Imperial Gallons', 'Cubic Inches']
        conversions = {
            'Liters': 1,
            'Milliliters': 1000,
            'Cubic Meters': 0.001,
            'Gallons': 0.264172,
            'Cubic Feet': 0.0353147,
            'Imperial Gallons': 0.219969,
            'Cubic Inches': 61.0237
        }
        super().__init__(parent, units, conversions, 'volume')


class PressureConverter(BaseConverter):
    def __init__(self, parent):
        units = ['Pascals', 'Bar', 'PSI', 'Atmospheres', 'Torr', 'Millibar']
        conversions = {
            'Pascals': 1,
            'Bar': 0.00001,
            'PSI': 0.000145038,
            'Atmospheres': 0.00000986923,
            'Torr': 0.00750062,
            'Millibar': 0.01
        }
        super().__init__(parent, units, conversions, 'pressure')


class EnergyConverter(BaseConverter):
    def __init__(self, parent):
        units = ['Joules', 'Kilojoules', 'Calories', 'Kilocalories', 'Watt-hours', 'BTU', 'Electronvolts']
        conversions = {
            'Joules': 1,
            'Kilojoules': 0.001,
            'Calories': 0.239006,
            'Kilocalories': 0.000239006,
            'Watt-hours': 0.000277778,
            'BTU': 0.000947817,
            'Electronvolts': 6.242e+18
        }
        super().__init__(parent, units, conversions, 'energy')


# Create app instance
A1 = App(400, 400, 'Distance Converter')
