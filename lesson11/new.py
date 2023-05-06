import tkinter as tk
from tkinter import messagebox
import tkinter.ttk as ttk
from stegano import lsb
from tkinter import filedialog as fd
import string
window = tk.Tk()
window.title("Шифромас")
window.geometry("500x500+400+100")
window.resizable(False, False)
window.attributes("-topmost", True)
window["bg"] = "#381A51"


def crypt():
    if ch.get() == "cesar":
        text = en.get()
        shift = int(shiftbox.get())
        shifr = ""
        alphabet = string.ascii_lowercase
        shifted_alphabet = alphabet[shift:] + alphabet[:shift]
        for x in text:
            for y in alphabet:
                if x == y:
                    ind = alphabet.find(y)
                    cha = shifted_alphabet[ind+(shift-2)]
                    shifr += cha
        en.delete(0, tk.END)
        en.insert(1, shifr)
    elif ch.get() == "image":
        file = fd.askopenfilename(filetypes=[('Images', '*.png')])
        secret = lsb.hide(file, en.get())
        file = fd.asksaveasfilename(filetypes=[('Images', '*.png')], initialfile="Secret.png")
        secret.save(file)
    else:
        messagebox.showerror("ERROR", "введено некоректное значение")


def decrypt():
    if ch.get() == "cesar":
        shifr = en.get()
        shift = int(shiftbox.get())
        text = ""
        alphabet = string.ascii_lowercase
        shifted_alphabet = alphabet[shift:] + alphabet[:shift]
        for x in shifr:
            for y in shifted_alphabet:
                if x == y:
                    ind = shifted_alphabet.find(y)
                    cha = alphabet[ind+(shift-2)]
                    text += cha
        en.delete(0, tk.END)
        en.insert(1, text)
    elif ch.get() == "image":
        file = fd.askopenfilename(filetypes=[('Images', '*.png')])
        secret = lsb.reveal(file)
        print(secret)
    else:
        messagebox.showerror("ERROR", "введено некоректное значение")


tb_con = ttk.Notebook(window)
tab1 = tk.Frame(tb_con, bg="#33AD11")
tab2 = tk.Frame(tb_con)
tb_con.add(tab1, text="шифр")
tb_con.add(tab2, text="режим")
tb_con.pack(expand=1, fill="both", padx=20, pady=20)
lb = tk.Label(tab1, text="Введите шифруемое сообщение", font=50, bg="#33AD11")
lb.grid(column=0, row=0)
en = tk.Entry(tab1, bg="#33AD11")
en.grid(column=0, row=1, sticky="NSEW")
en.insert(1, "abc")
button = tk.Button(tab1, command=crypt, text="crypt", bg="#33AD11")
button.grid(column=2, row=0)
lb2 = tk.Label(tab2, text="Выберите режим").grid(column=0, row=0)
button2 = tk.Button(tab1, command=decrypt, text="decrypt", bg="#33AD11")
button2.grid(column=3, row=0)
ch = ttk.Combobox(tab2)
ch['values'] = ("cesar", "image")
ch.grid(column=1, row=0)
shiftbox = ttk.Spinbox(tab2, from_=0, to=36)
shiftbox.grid(column=2, row=0)
window.mainloop()
