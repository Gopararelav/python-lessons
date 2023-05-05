import tkinter as tk
from tkinter import ttk
window = tk.Tk()


def crypt():
    print(en.get())


tabc = ttk.Notebook(window, padding=20)
tab1 = tk.Frame(tabc)
tab2 = tk.Frame(tabc)
tabc.add(tab1, text="шифр")
tabc.add(tab2, text="режим")
tabc.pack()
en = tk.Entry(tab1)
en.grid(column=0, row=0)
but = tk.Button(tab1, text="", width=10, command=crypt).grid(column=1, row=0)

window.mainloop()
