from tkinter import *
import tkinter as tk

one= tk.Tk ()
one['bg'] = 'black'
one.title("Fuel Track ")
#root.geometry('1400x900')
screen_width = one.winfo_screenwidth()
screen_height = one.winfo_screenheight()
one.resizable(width=False, height=False)
screen_width = one.winfo_screenwidth()
screen_height = one.winfo_screenheight()
window_width = 1400
window_height = 900
x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)
one.geometry(f"{window_width}x{window_height}+{x}+{y}")
label1 = tk.Label(one, text="Это пример использования place()")
label1.place(x=5, y=50)

button1 = tk.Button(one, text="Нажми кнопку")
button1.place(x=50, y=100)
#Canvas = Canvas(root, height=300, width=250)
#Canvas.pack()

#frame = Frame(root, bg='red')
#frame.place(relx=0.15)

#title=Label(frame, text="ntrc")
#title.pack
one.mainloop()
