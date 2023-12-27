import customtkinter as ctk

# window

window = ctk.CTk()
window.geometry('600x400')

#widgets

label = ctk.CTkLabel(window, text='Label')
label.pack()

#run
window.mainloop()
