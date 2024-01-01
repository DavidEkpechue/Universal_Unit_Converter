import tkinter as tk
import customtkinter as ctk
import Colours
import requests


class BaseConverter(ctk.CTkFrame):
    def __init__(self, parent, units, conversions, label_text):
        super().__init__(parent)
        self.units = units
        self.conversions = conversions

        self.unit_string_from = ctk.StringVar(value=self.units[0])
        self.unit_string_to = ctk.StringVar(value=self.units[0])
        self.value_var = tk.StringVar(value='0')


        self.create_widget(label_text)
        self.create_layout()

    def create_widget(self, label_text):
        button_colour = Colours.Matte.purple
        button_colour2 = Colours.Matte.purple_hover
        button_colour3 = Colours.Matte.purple_hover_hover
        button_colour_light = Colours.Pastel.blue
        button2_colour_light = Colours.Pastel.blue_hover
        button3_colour_light = Colours.Pastel.blue_hover_hover
        font = ('Ebrima', 10.01)
        big_font = ('Ebrima', 14)

        self.label1 = ctk.CTkLabel(self,
                                   text=f'Enter {label_text}:',
                                   font=big_font)

        self.label2 = ctk.CTkLabel(self,
                                   text='TO',
                                   anchor='center',
                                   font=font
                                   )

        self.user_entry = ctk.CTkEntry(self,
                                       textvariable=self.value_var,
                                       font=big_font)

        self.dropdown_from = ctk.CTkOptionMenu(self,
                                               values=self.units,
                                               variable=self.unit_string_from,
                                               font=font,
                                               dropdown_font=font,
                                               button_color=(button2_colour_light, button_colour2),
                                               button_hover_color=(button3_colour_light, button_colour3),
                                               fg_color=(button_colour_light, button_colour),
                                               text_color=('black', 'white'))

        self.dropdown_to = ctk.CTkOptionMenu(self,
                                             values=self.units,
                                             variable=self.unit_string_to,
                                             font=font,
                                             dropdown_font=font,
                                             button_color=(button2_colour_light, button_colour2),
                                             button_hover_color=(button3_colour_light, button_colour3),
                                             fg_color=(button_colour_light, button_colour),
                                             text_color=('black', 'white'))

        self.button1 = ctk.CTkButton(self,
                                     text='Convert',
                                     font=big_font,
                                     command=lambda: self.convert_units(),
                                     fg_color=(button_colour_light, button_colour),
                                     hover_color=(button2_colour_light, button_colour2),
                                     text_color=('black', 'white'))
        self.result_label = ctk.CTkLabel(self,
                                         text="Conversion Result:",
                                         text_color=('black', 'white'),
                                         font=big_font)

    def create_layout(self):
        self.grid_rowconfigure((0, 1, 2, 3, 4), weight=5, uniform='a')
        self.grid_columnconfigure((0, 2), weight=5, uniform='a')
        self.grid_columnconfigure(1, weight=1, uniform='a')

        self.label1.grid(row=0, column=0, columnspan=3, sticky='news')
        self.label2.grid(row=2, column=0, columnspan=3, sticky='ew')
        self.user_entry.grid(row=1, column=0, columnspan=3, sticky='news', pady=20,padx=10)
        self.dropdown_from.grid(row=2, column=0, sticky='ew', pady=10,padx=10)
        self.dropdown_to.grid(row=2, column=2, sticky='ew', pady=10,padx=10)
        self.button1.grid(row=3, column=0, columnspan=3, sticky='news',
                          padx=30, pady=10)
        self.result_label.grid(row=4, column=0, columnspan=3, sticky='news')

    def convert_units(self):

        print('clicked')
        try:
            value = float(self.value_var.get())
        except ValueError:
            self.result_label["text"] = "Invalid input"
            return

        unit_from = self.unit_string_from.get()
        print('got unit from')
        unit_to = self.unit_string_to.get()

        # Convert the input to the base unit first
        base_unit_value = value * self.conversions[unit_from]

        # Then convert from the base unit to the target unit
        result = base_unit_value / self.conversions[unit_to]

        self.result_label.configure(text=f"{result:.2f} {unit_to}")
        print(result)


class DistanceConverter(BaseConverter):
    def __init__(self, parent):
        units = ['Feet', 'Miles', 'Yards', 'Inches', 'Light Years', 'Meters', 'Centimeters', 'Kilometers']
        conversions = {'Feet': 0.3048, 'Miles': 1609.34, 'Yards': 0.9144, 'Inches': 0.0254, 'Meters': 1,
                       'Centimeters': 0.01, 'Kilometers': 1000, 'Light Years': 9460660000000000}
        super().__init__(parent, units, conversions, 'distance')


class TemperatureConverter(BaseConverter):
    def __init__(self, parent):
        units = ['Celsius', 'Fahrenheit', 'Kelvin']
        # The conversion functions convert from the unit to Celsius
        conversions = {
            'Celsius': lambda t: t,
            'Fahrenheit': lambda t: (t - 32) * 5 / 9,
            'Kelvin': lambda t: t - 273.15
        }
        super().__init__(parent, units, conversions, 'temperature')

    def convert_units(self):
        print("convert_units called")  # Debugging print
        try:
            temp = float(self.value_var.get())
            print(f"Input value: {temp}")  # Debugging print
        except ValueError:
            self.result_label["text"] = "Invalid input"
            print("Invalid input")  # Debugging print
            return

        # Rest of your conversion logic...

        unit_from = self.unit_string_from.get()
        unit_to = self.unit_string_to.get()

        # Convert the input to Celsius
        temp_in_celsius = self.conversions[unit_from](temp)

        # Convert from Celsius to the target unit
        result = temp_in_celsius
        if unit_to == 'Fahrenheit':
            result = (temp_in_celsius * 9 / 5) + 32
        elif unit_to == 'Kelvin':
            result = temp_in_celsius + 273.15

        self.result_label.configure(text=f"Result: {result:.2f} {unit_to}")
        print(f"Result set to label: {result:.2f} {unit_to}")  # Debugging print


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


class CurrencyConverter(BaseConverter):
    def __init__(self, parent):
        self.rates = {}
        self.common_currencies = ['USD', 'EUR', 'GBP', 'JPY', 'CAD', 'AUD', 'CHF', 'CNY', 'SEK', 'NZD']
        self.update_rates()

        super().__init__(parent, self.common_currencies, self.rates, 'currency')

    def update_rates(self):
        # Fetch the latest currency rates from an API
        url = 'https://api.exchangerate-api.com/v4/latest/EUR'  # Example API endpoint
        try:
            response = requests.get(url)
            data = response.json()
            all_rates = data['rates']

            # Filter rates to include only common currencies
            self.rates = {currency: all_rates[currency] for currency in self.common_currencies if currency in all_rates}
        except Exception as e:
            print(f"Error updating rates: {e}")
            # Handle error (e.g., set default rates, show a message, etc.)

    def convert_units(self):
        try:
            value = float(self.value_var.get())
        except ValueError:
            self.result_label["text"] = "Invalid input"
            return

        self.update_rates()  # Update rates every time a conversion is made

        unit_from = self.unit_string_from.get()
        unit_to = self.unit_string_to.get()

        # Convert the input to the base currency (e.g., EUR)
        base_currency_value = value / self.rates[unit_from]

        # Then convert from the base currency to the target unit
        result = base_currency_value * self.rates[unit_to]

        self.result_label.configure(text=f"{result:.2f} {unit_to}")