import tkinter as tk
# from tkinter import *

sheet = tk.Tk()

sheet.geometry("800x500")
sheet.title("Character Sheet")

label = tk.Label(sheet, text="Hello World", font=('Arial', 18))
label.pack(padx=20,pady=20)

textbox = tk.Text(sheet, height=3, font=('Arial', 16))
textbox.pack(padx=20,pady=10)

button = tk.Button(sheet, text="Click", font=('Arial', 18))
button.pack(padx=10,pady=10)

myentry = tk.Entry(sheet)
myentry.pack()

sheet.mainloop()

