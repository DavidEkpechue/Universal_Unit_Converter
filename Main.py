import tkinter as tk
from tkinter import ttk


class App:
    def __init__(self, window_x, window_y, window_name):
        # Window setup
        self.window = tk.Tk()
        self.window.geometry(f"{window_x}x{window_y}")
        self.window.title(window_name)

        # tk variables
        self.int_var = tk.IntVar()
        self.radio_var = tk.IntVar()  # Default value set to "1"

        # Widgets
        self.label1 = ttk.Label(self.window, text='Enter distance:')
        self.label1.pack()

        self.user_entry = ttk.Entry(self.window, textvariable=self.int_var)
        self.user_entry.pack()

        self.button1 = ttk.Button(self.window, text='Convert', command=self.convert_to_meters)
        self.button1.pack()

        self.radio_button = ttk.Radiobutton(self.window, text='Feet', value="1", variable=self.radio_var)
        self.radio_button.pack()

        self.radio_button2 = ttk.Radiobutton(self.window, text='Miles', value="2", variable=self.radio_var)
        self.radio_button2.pack()

        self.result_label = ttk.Label(self.window, text="Conversion Result:")
        self.result_label.pack()

        self.run()

    def run(self):
        self.window.mainloop()

    def convert_to_meters(self):
        distance = self.int_var.get()
        conversion_type = self.radio_var.get()

        if conversion_type == 1:
            result = distance * 0.3048
        elif conversion_type == 2:
            result = distance * 1609.34
        else:
            result = "Invalid selection"

        if isinstance(result, float):
            self.result_label["text"] = f"Result: {result:.2f} meters"
        else:
            self.result_label["text"] = "Invalid selection"


# Create app instance
A1 = App(800, 600, 'Distance Converter')
