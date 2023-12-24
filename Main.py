import tkinter as tk
from tkinter import ttk
import math as math


class App(tk.Tk):
    def __init__(self, window_x, window_y, window_name):
        super().__init__()
        # Window setup
        self.geometry(f"{window_x}x{window_y}")
        self.title(window_name)
        self.attributes('-topmost', True)
        self.resizable(False, False)

        self.grid_rowconfigure(0, weight=1, uniform='a')  # Configure row 0 to take available space
        self.grid_columnconfigure(0, weight=1, uniform='a')  # Configure column 0 to take available space
        self.grid_columnconfigure(1, weight=1, uniform='a')  # Configure column 0 to take available space

        # Notebook (Tabbed interface)
        notebook = ttk.Notebook(self)
        notebook.grid(row=0, column=0, sticky='nsew', padx=10, pady=10)  # Placed in row 0, column 0

        # Notebook (Tabbed interface)
        notebook = ttk.Notebook(self)
        notebook.grid(row=0, column=0, sticky='ew', padx=10, pady=10)

        # Tabs
        distance_tab = Distance_Converter(notebook, 0)
        mass_tab = MassConverter(notebook)
        # currency_tab = CurrencyConverter(notebook)
        temperature_tab = TemperatureConverter(notebook)
        time_tab = TimeConverter(notebook)
        # area_tab = AreaConverter(notebook)
        # speed_tab = SpeedConverter(notebook)

        # Add tabs to the notebook
        notebook.add(distance_tab, text='Distance')
        notebook.add(mass_tab, text='Mass')
        # notebook.add(currency_tab, text='Currency')
        notebook.add(temperature_tab, text='Temperature')
        notebook.add(time_tab, text='Time')
        # notebook.add(area_tab, text='Area')
        # notebook.add(speed_tab, text='Speed')

        # Run app
        self.mainloop()


class Distance_Converter(ttk.Frame):
    def __init__(self, parent, x_padding):
        super().__init__(parent)

        self.units = ['Feet', 'Miles', 'Yards',
                      'Inches', 'Light Years', 'Meters',
                      'Centimeters', 'Kilometers']
        self.conversions = {'Feet': 0.3048, 'Miles': 1609.34, 'Yards': 0.9144,
                            'Inches': 0.0254, 'Meters': 1, 'Centimeters': 0.01,
                            'Kilometers': 1000, 'Light Years': 9460660000000000}

        self.unit_string_from = tk.StringVar(value=self.units[0])
        self.unit_string_to = tk.StringVar(value=self.units[0])
        self.int_var = tk.IntVar()

        self.x_padding = x_padding

        self.create_widget()
        self.create_layout()

    def create_widget(self):
        self.label1 = ttk.Label(self, text='Enter distance:', anchor='center', font=50)
        self.label2 = ttk.Label(self, text='TO', font=50, padding= 30)
        self.user_entry = ttk.Entry(self, textvariable=self.int_var)
        self.dropdown_from = ttk.Combobox(self, textvariable=self.unit_string_from, values=self.units)
        self.dropdown_to = ttk.Combobox(self, textvariable=self.unit_string_to, values=self.units)
        self.button1 = ttk.Button(self, text='Convert', command=self.convert_units)
        self.result_label = ttk.Label(self, text="Conversion Result:", anchor='center', font=20)

    def create_layout(self):
        self.grid_rowconfigure((0, 1, 2, 3, 4), weight=1, uniform='a')
        self.grid_columnconfigure((0, 1, 2), weight=1, uniform='a')

        self.label1.grid(row=0, column=0, columnspan=3, sticky='news', padx=self.x_padding)
        self.label2.grid(row=2, column=1, columnspan=3, sticky='news')
        self.user_entry.grid(row=1, column=0, columnspan=3, sticky='news', padx=self.x_padding)
        self.dropdown_from.grid(row=2, column=0, sticky='news', padx=self.x_padding)
        self.dropdown_to.grid(row=2, column=2, sticky='news', padx=self.x_padding)
        self.button1.grid(row=3, column=0, columnspan=3, sticky='news', padx=self.x_padding)
        self.result_label.grid(row=4, column=0, columnspan=3, sticky='news', padx=self.x_padding)

    def convert_units(self):
        distance = self.int_var.get()
        unit_from = self.unit_string_from.get()
        unit_to = self.unit_string_to.get()

        # Convert the input to meters first
        meters = distance * self.conversions[unit_from]

        # Then convert from meters to the target unit
        result = meters / self.conversions[unit_to]

        self.result_label["text"] = f"Result: {result:.2f} {unit_to}"


class TemperatureConverter(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        # Temperature units
        self.units = ['Celsius', 'Fahrenheit', 'Kelvin']

        # Variables
        self.temp_string_from = tk.StringVar(value=self.units[0])
        self.temp_string_to = tk.StringVar(value=self.units[0])
        self.temp_value = tk.DoubleVar()

        # Create widgets
        self.create_widget()
        self.create_layout()

    def create_widget(self):
        self.label1 = ttk.Label(self, text='Enter temperature:', anchor='center', font=50)
        self.label2 = ttk.Label(self, text='TO', font=50, padding= 30)
        self.user_entry = ttk.Entry(self, textvariable=self.temp_value)
        self.dropdown_from = ttk.Combobox(self, textvariable=self.temp_string_from, values=self.units)
        self.dropdown_to = ttk.Combobox(self, textvariable=self.temp_string_to, values=self.units)
        self.button1 = ttk.Button(self, text='Convert', command=self.convert_temperature)
        self.result_label = ttk.Label(self, text="Conversion Result:", anchor='center', font=20)

    def create_layout(self):
        self.grid_rowconfigure((0, 1, 2, 3, 4), weight=1, uniform='a')
        self.grid_columnconfigure((0, 1, 2), weight=1, uniform='a')

        self.label1.grid(row=0, column=0, columnspan=3, sticky='news')
        self.label2.grid(row=2, column=1, columnspan=3, sticky='news')
        self.user_entry.grid(row=1, column=0, columnspan=3, sticky='news')
        self.dropdown_from.grid(row=2, column=0, sticky='news')
        self.dropdown_to.grid(row=2, column=2, sticky='news')
        self.button1.grid(row=3, column=0, columnspan=3, sticky='news')
        self.result_label.grid(row=4, column=0, columnspan=3, sticky='news')

    def convert_temperature(self):
        temp = self.temp_value.get()
        unit_from = self.temp_string_from.get()
        unit_to = self.temp_string_to.get()

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


class MassConverter(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        # Mass units
        self.units = ['Kilograms', 'Grams', 'Pounds', 'Ounces']
        self.conversions = {
            'Kilograms': 1,
            'Grams': 1000,
            'Pounds': 2.20462,
            'Ounces': 35.274
        }

        # Variables
        self.mass_string_from = tk.StringVar(value=self.units[0])
        self.mass_string_to = tk.StringVar(value=self.units[0])
        self.mass_value = tk.DoubleVar()

        # Create widgets
        self.create_widget()
        self.create_layout()

    def create_widget(self):
        self.label1 = ttk.Label(self, text='Enter mass:', anchor='center', font=50)
        self.label2 = ttk.Label(self, text='TO', font=50, padding= 30)
        self.user_entry = ttk.Entry(self, textvariable=self.mass_value)
        self.dropdown_from = ttk.Combobox(self, textvariable=self.mass_string_from, values=self.units)
        self.dropdown_to = ttk.Combobox(self, textvariable=self.mass_string_to, values=self.units)
        self.button1 = ttk.Button(self, text='Convert', command=self.convert_mass)
        self.result_label = ttk.Label(self, text="Conversion Result:", anchor='center', font=20)

    def create_layout(self):
        self.grid_rowconfigure((0, 1, 2, 3, 4), weight=1, uniform='a')
        self.grid_columnconfigure((0, 1, 2), weight=1, uniform='a')

        self.label1.grid(row=0, column=0, columnspan=3, sticky='news')
        self.label2.grid(row=2, column=1, columnspan=3, sticky='news')
        self.user_entry.grid(row=1, column=0, columnspan=3, sticky='news')
        self.dropdown_from.grid(row=2, column=0, sticky='news')
        self.dropdown_to.grid(row=2, column=2, sticky='news')
        self.button1.grid(row=3, column=0, columnspan=3, sticky='news')
        self.result_label.grid(row=4, column=0, columnspan=3, sticky='news')

    def convert_mass(self):
        mass = self.mass_value.get()
        unit_from = self.mass_string_from.get()
        unit_to = self.mass_string_to.get()

        # Convert the input to kilograms first
        kilograms = mass / self.conversions[unit_from]

        # Then convert from kilograms to the target unit
        result = kilograms * self.conversions[unit_to]

        self.result_label["text"] = f"Result: {result:.2f} {unit_to}"


class AreaConverter(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        # Area units
        self.units = ['Square Meters', 'Square Kilometers', 'Square Feet', 'Acres', 'Hectares']
        self.conversions = {
            'Square Meters': 1,
            'Square Kilometers': 0.000001,
            'Square Feet': 10.7639,
            'Acres': 0.000247105,
            'Hectares': 0.0001
        }

        # Variables
        self.area_string_from = tk.StringVar(value=self.units[0])
        self.area_string_to = tk.StringVar(value=self.units[0])
        self.area_value = tk.DoubleVar()

        # Create widgets
        self.create_widget()
        self.create_layout()

    def create_widget(self):
        self.label1 = ttk.Label(self, text='Enter area:', anchor='center', font=50)
        self.label2 = ttk.Label(self, text='TO', font=50, padding= 30)
        self.user_entry = ttk.Entry(self, textvariable=self.area_value)
        self.dropdown_from = ttk.Combobox(self, textvariable=self.area_string_from, values=self.units)
        self.dropdown_to = ttk.Combobox(self, textvariable=self.area_string_to, values=self.units)
        self.button1 = ttk.Button(self, text='Convert', command=self.convert_area)
        self.result_label = ttk.Label(self, text="Conversion Result:", anchor='center', font=20)

    def create_layout(self):
        self.grid_rowconfigure((0, 1, 2, 3, 4), weight=1, uniform='a')
        self.grid_columnconfigure((0, 1, 2), weight=1, uniform='a')

        self.label1.grid(row=0, column=0, columnspan=3, sticky='news')
        self.label2.grid(row=2, column=1, columnspan=3, sticky='news')
        self.user_entry.grid(row=1, column=0, columnspan=3, sticky='news')
        self.dropdown_from.grid(row=2, column=0, sticky='news')
        self.dropdown_to.grid(row=2, column=2, sticky='news')
        self.button1.grid(row=3, column=0, columnspan=3, sticky='news')
        self.result_label.grid(row=4, column=0, columnspan=3, sticky='news')

    def convert_area(self):
        area = self.area_value.get()
        unit_from = self.area_string_from.get()
        unit_to = self.area_string_to.get()

        # Convert the input to square meters first
        square_meters = area / self.conversions[unit_from]

        # Then convert from square meters to the target unit
        result = square_meters * self.conversions[unit_to]

        self.result_label["text"] = f"Result: {result:.2f} {unit_to}"


class TimeConverter(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        # Time units
        self.units = ['Seconds', 'Minutes', 'Hours', 'Days']
        self.conversions = {
            'Seconds': 1,
            'Minutes': 60,
            'Hours': 3600,
            'Days': 86400
        }

        # Variables
        self.time_string_from = tk.StringVar(value=self.units[0])
        self.time_string_to = tk.StringVar(value=self.units[0])
        self.time_value = tk.DoubleVar()

        # Create widgets
        self.create_widget()
        self.create_layout()

    def create_widget(self):
        self.label1 = ttk.Label(self, text='Enter time:', anchor='center', font=50)
        self.label2 = ttk.Label(self, text='TO', font=50, padding= 30)
        self.user_entry = ttk.Entry(self, textvariable=self.time_value)
        self.dropdown_from = ttk.Combobox(self, textvariable=self.time_string_from, values=self.units)
        self.dropdown_to = ttk.Combobox(self, textvariable=self.time_string_to, values=self.units)
        self.button1 = ttk.Button(self, text='Convert', command=self.convert_time)
        self.result_label = ttk.Label(self, text="Conversion Result:", anchor='center', font=20)

    def create_layout(self):
        self.grid_rowconfigure((0, 1, 2, 3, 4), weight=1, uniform='a')
        self.grid_columnconfigure((0, 1, 2), weight=1, uniform='a')

        self.label1.grid(row=0, column=0, columnspan=3, sticky='news')
        self.label2.grid(row=2, column=1, columnspan=3, sticky='news')
        self.user_entry.grid(row=1, column=0, columnspan=3, sticky='news')
        self.dropdown_from.grid(row=2, column=0, sticky='news')
        self.dropdown_to.grid(row=2, column=2, sticky='news')
        self.button1.grid(row=3, column=0, columnspan=3, sticky='news')
        self.result_label.grid(row=4, column=0, columnspan=3, sticky='news')

    def convert_time(self):
        time = self.time_value.get()
        unit_from = self.time_string_from.get()
        unit_to = self.time_string_to.get()

        # Convert the input to seconds first
        seconds = time * self.conversions[unit_from]

        # Then convert from seconds to the target unit
        result = seconds / self.conversions[unit_to]

        self.result_label["text"] = f"Result: {result:.2f} {unit_to}"


# Create app instance
A1 = App(600, 400, 'Distance Converter')
