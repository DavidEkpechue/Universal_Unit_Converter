import customtkinter as ctk

# window

window = ctk.CTk()
window.geometry('600x400')

#widgets

label = ctk.CTkLabel(window, text='Label')
button = ctk.CTkButton(window, text='Button', height= 10)

if button.cget('hover'):
    print('hover')
    button.configure(require_redraw= True,
                     height= 200)

button.pack()
label.pack()

#run
window.mainloop()
