import customtkinter as ctk
from random import choice


class SlidePanel(ctk.CTkFrame):
    def __init__(self, parent, start_pos, end_pos):
        super().__init__(master=parent)

        # general attributes
        self.start_pos = start_pos + 0.04
        self.end_pos = end_pos - 0.03
        self.width = abs(start_pos - end_pos)

        # animation logic
        self.pos = self.start_pos
        self.in_start_pos = True

        # layout
        self.place(relx=self.start_pos, rely=0.05, relwidth=self.width, relheight=0.9)

    def animate(self):
        if self.in_start_pos:
            self.animate_forward()
        else:
            self.animate_backwards()

    def animate_forward(self):
        if self.pos > self.end_pos:
            self.pos -= 0.008
            self.place(relx=self.pos, rely=0.05, relwidth=self.width, relheight=0.9)
            self.after(10, self.animate_forward)
        else:
            self.in_start_pos = False

    def animate_backwards(self):
        if self.pos < self.start_pos:
            self.pos += 0.008
            self.place(relx=self.pos, rely=0.05, relwidth=self.width, relheight=0.9)
            self.after(10, self.animate_backwards)
        else:
            self.in_start_pos = True

class App:
    def __init__(self):
        self.window = ctk.CTk()
        self.window.title('Animated Widgets')
        self.window.geometry('600x400')

        self.create_widgets()

    def create_widgets(self):
        self.animated_panel = SlidePanel(self.window, 1.0, 0.7)
        ctk.CTkLabel(self.animated_panel, text='Label 1').pack(expand=True, fill='both', padx=2, pady=10)
        ctk.CTkLabel(self.animated_panel, text='Label 2').pack(expand=True, fill='both', padx=2, pady=10)
        ctk.CTkButton(self.animated_panel, text='Button', corner_radius=0).pack(expand=True, fill='both', pady=10)
        ctk.CTkTextbox(self.animated_panel, fg_color=('#dbdbdb', '#2b2b2b')).pack(expand=True, fill='both', pady=10)

        button_x = 0.5
        button = ctk.CTkButton(self.window, text='Toggle Sidebar', command=self.animated_panel.animate)
        button.place(relx=button_x, rely=0.5, anchor='center')

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    app = App()
    app.run()