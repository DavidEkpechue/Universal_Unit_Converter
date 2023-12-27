import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
import math
from Conversions import *


def create_small_layout():
    print('small_layout')


def create_medium_layout():
    print('medium_layout')


class NavigationBar(ctk.CTkFrame):
    def __init__(self, parent, pages):
        super().__init__(parent)
        self.pages = pages
        self.select_page(next(iter(self.pages.values())))  # Selects the first converter as default
        self.create_widget()
        self.create_layout()

    def create_widget(self):
        for i, (name, page) in enumerate(self.pages.items()):
            button = ctk.CTkButton(master=self,
                                   font=('', 7),
                                   text=name,
                                   command=lambda page=page: self.select_page(page),
                                   fg_color='#473d4d')
            button.grid(row=0, column=i, pady=10, padx=10, sticky="ew")  # Place buttons in row 0

    def create_layout(self):
        self.grid_rowconfigure(0, weight=1, uniform='a')  # Give weight to the row containing buttons
        self.grid_columnconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8, 9), weight=1, uniform='a')  # Adjust according to the number of buttons

    def select_page(self, selected_page):
        # Remove the current page from the grid (if there's one)
        current_page = next((page for page in self.pages.values() if page.grid_info()), None)
        if current_page:
            current_page.grid_remove()

        # Make the selected page visible
        selected_page.grid()


class App(ctk.CTk):
    def __init__(self, window_x, window_y, window_name):
        super().__init__()

        # Window setup
        self.geometry(f"{window_x}x{window_y}")
        self.title(window_name)
        self.attributes('-topmost', True)
        self.wm_minsize(window_x, window_y)

        # Create multiple pages (frames)
        self.pages = {
            'Distance': DistanceConverter(self),
            'Temperature': TemperatureConverter(self),
            'Mass': MassConverter(self),
            'Area': AreaConverter(self),
            'Time': TimeConverter(self),
            'Speed': SpeedConverter(self),
            'Volume': VolumeConverter(self),
            'Pressure': PressureConverter(self),
            'Energy': EnergyConverter(self)
            # Add other converter classes here if necessary
        }

        # Configure grid system for the app
        self.grid_rowconfigure(0, weight=6, uniform='a')  # Give weight to the row that contains the pages
        self.grid_rowconfigure(1, weight=1, uniform='a')  # Give weight to the row that contains the pages
        self.grid_columnconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8, 9), weight=1,
                                  uniform='a')


        # Add pages to the window
        for name, page in self.pages.items():
            page.grid(row=0, column=0, columnspan=1, sticky="nsew")
            page.grid_remove()

        self.navbar = NavigationBar(self, self.pages)
        self.navbar.grid(row=1, column=0, columnspan=2, sticky="nsew")

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

    def check_size(self, event):
        if event.widget == self.window:
            window_width = self.window.winfo_width()
            checked_size = None

            for min_size in self.size_dict:
                if window_width >= min_size:
                    checked_size = min_size
                    break  # Exit loop once the appropriate size is found

            if checked_size != self.current_min_size:
                self.current_min_size = checked_size
                self.size_dict[self.current_min_size]()


if __name__ == "__main__":
    # Create app instance and run it
    app = App(720, 500, 'Unit Converter')
