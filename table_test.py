import customtkinter


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # configure grid system (3x2 grid)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure((0, 1, 2), weight=1)

        # create multiple pages (frames)
        self.page_1 = customtkinter.CTkFrame(master=self, fg_color=None, corner_radius=0)
        self.page_2 = customtkinter.CTkFrame(master=self, fg_color=None, corner_radius=0)
        self.page_3 = customtkinter.CTkFrame(master=self, fg_color=None, corner_radius=0)

        # save all pages in list and add them to the window with grid manager
        self.all_pages = [self.page_1, self.page_2, self.page_3]
        for page in self.all_pages:
            page.grid(row=0, column=0, columnspan=3, sticky="nsew")

        # add widgets to pages
        self.label_1 = customtkinter.CTkLabel(master=self.page_1, text="page 1")
        self.label_1.grid(row=0, column=0)
        self.label_2 = customtkinter.CTkLabel(master=self.page_2, text="page 2")
        self.label_2.grid(row=0, column=0)
        self.label_3 = customtkinter.CTkLabel(master=self.page_3, text="page 3")
        self.label_3.grid(row=0, column=0)

        # create buttons to select a page
        self.button_1 = customtkinter.CTkButton(master=self, text="page 1", command=lambda: self.select_page(self.page_1))
        self.button_1.grid(row=1, column=0, pady=10)
        self.button_2 = customtkinter.CTkButton(master=self, text="page 2", command=lambda: self.select_page(self.page_2))
        self.button_2.grid(row=1, column=1, pady=10)
        self.button_3 = customtkinter.CTkButton(master=self, text="page 3", command=lambda: self.select_page(self.page_3))
        self.button_3.grid(row=1, column=2, pady=10)

        # select initial page
        self.select_page(self.page_1)

    def select_page(self, selected_page: customtkinter.CTkFrame):
        # make selected page visible
        selected_page.grid(row=0, column=0, columnspan=3, sticky="nsew")

        # remove all other pages
        for page in self.all_pages:
            if page is not selected_page:
                page.grid_forget()


if __name__ == "__main__":
    app = App()
    app.mainloop()