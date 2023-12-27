import customtkinter as ctk
import Colours


class NavigationBar(ctk.CTkFrame):
    def __init__(self, parent, pages):
        super().__init__(parent)
        self.pages = pages
        self.select_page(next(iter(self.pages.values())))  # Selects the first converter as default
        self.create_widget()
        self.create_layout()

    def create_widget(self):
        for i, (name, page) in enumerate(self.pages.items()):
            button_colour = Colours.Matte.purple
            hover_button_colour = Colours.Matte.purple_hover
            button = ctk.CTkButton(master=self,
                                   font=('', 7),
                                   text=name,
                                   command=lambda page=page: self.select_page(page),
                                   fg_color=button_colour,
                                   hover_color=hover_button_colour)
            button.grid(row=0, column=i, pady=10, padx=5, sticky="nsew")  # Place buttons in row 0

    def create_layout(self):
        self.grid_rowconfigure(0, weight=1, uniform='a')  # Give weight to the row containing buttons
        self.grid_columnconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8, 9), weight=1,
                                  uniform='a')  # Adjust according to the number of buttons

    def select_page(self, selected_page):
        # Remove the current page from the grid (if there's one)
        current_page = next((page for page in self.pages.values() if page.grid_info()), None)
        if current_page:
            current_page.grid_remove()

        # Make the selected page visible
        selected_page.grid()
