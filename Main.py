import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
import Colours
from NavBar import *
from Conversions import *


def create_small_layout():
    print('small_layout')


def create_medium_layout():
    print('medium_layout')


class App(ctk.CTk):
    def __init__(self, window_x, window_y, window_name):
        super().__init__()

        # Window setup
        self.geometry(f"{window_x}x{window_y}")
        self.title(window_name)
        self.attributes('-topmost', True)
        self.wm_minsize(window_x, window_y)

        self.size_notifier = SizeNotifier(self, {
            720: self.create_small_layout,
            1000: self.create_medium_layout
        })

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
            page.grid(row=0, column=0, columnspan=4, sticky="nsew")
            page.grid_remove()

        self.navbar = NavigationBar(self, self.pages)
        self.navbar.grid(row=1, column=0, columnspan=10, sticky="nsew")

        self.sidebar()

        self.mainloop()

    def sidebar(self):
        button_colour = Colours.Matte.purple
        hover_button_colour = Colours.Matte.purple_hover

        button_colour_light = Colours.Pastel.blue
        hover_button_colour_light = Colours.Pastel.blue_hover

        self.animated_panel = SideBar(self, 1.0, 0.7)

        button = ctk.CTkButton(self, text='options', command=self.animated_panel.animate,
                               fg_color=(button_colour_light, button_colour),
                               hover_color=(hover_button_colour_light, hover_button_colour),
                               font=('', 7),
                               text_color=('black', 'white'))
        button.grid(column=9, row=1, pady=10, padx=5, sticky="nsew")

    @staticmethod
    def create_small_layout():
        print('Current size: Small')
        # Here, define what happens when the layout is small
        # For example, adjust the columnspan of pages, change the size of widgets, etc.

    @staticmethod
    def create_medium_layout():
        print('Current size: Medium')
        # Here, define what happens when the layout is medium
        # Similar to above, adjust the layout as needed for medium size


class SideBar(ctk.CTkFrame):
    def __init__(self, parent, start_pos, end_pos):
        super().__init__(master=parent)

        # General attributes
        self.start_pos = start_pos
        self.end_pos = end_pos
        self.width = abs(start_pos - end_pos)

        # Animation logic
        self.pos = self.start_pos
        self.in_start_pos = True

        # Variables
        self.is_on = ctk.BooleanVar(value=ctk.get_appearance_mode() == 'dark')

        # Layout
        self.place(relx=self.start_pos, rely=0.05, relwidth=self.width, relheight=0.755)

        # Label for the switch
        self.theme_label = ctk.CTkLabel(self, text='Toggle Light/Dark Mode')
        self.theme_label.pack(pady=(10, 0))

        # Switch for toggling light mode
        self.theme_switch = ctk.CTkSwitch(self, text='', variable=self.is_on, command=self.toggle_theme)
        self.theme_switch.pack(pady=10)

    def toggle_theme(self):
        # Change appearance mode based on the switch state
        new_mode = 'light' if self.is_on.get() else 'dark'
        ctk.set_appearance_mode(new_mode)

    def animate(self):
        if self.in_start_pos:
            self.animate_forward()
        else:
            self.animate_backwards()

    def animate_forward(self):
        if self.pos > self.end_pos:
            self.pos -= 0.008
            self.place(relx=self.pos, rely=0.05, relwidth=self.width, relheight=0.755)
            self.after(10, self.animate_forward)
        else:
            self.in_start_pos = False

    def animate_backwards(self):
        if self.pos < self.start_pos:
            self.pos += 0.008
            self.place(relx=self.pos, rely=0.05, relwidth=self.width, relheight=0.755)
            self.after(10, self.animate_backwards)
        else:
            self.in_start_pos = True


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
