import openpyxl as xl
import tkinter as tk
window = tk.Tk()
window.geometry("400x400")
window["bg"] = "Gray"
icon = tk.PhotoImage(file="lesson12\icon.png")
window.iconphoto(True, icon)
wb = xl.load_workbook("lesson12\Книга2.xlsx")
page = wb.get_sheet_by_name("Book")
penum = 1
max = 6


class new():
    def __init__(self, penum: int, max: int) -> None:
        self.penum = penum
        self.min = 2
        self.max = max

    def next(self):
        if self.penum == self.max:
            pass
        else:
            penum = self.penum + 1
            lbl1["text"] = "название: " + str(page[f"A{penum}"].value)
            lbl2["text"] = "цена: " + str(page[f"B{penum}"].value)
            lbl3["text"] = "количество: " + str(page[f"C{penum}"].value)
            self.penum = penum

    def behind(self):
        if self.penum == self.min:
            pass
        else:
            penum = self.penum - 1
            lbl1["text"] = "название: " + str(page[f"A{penum}"].value)
            lbl2["text"] = "цена: " + str(page[f"B{penum}"].value)
            lbl3["text"] = "количество: " + str(page[f"C{penum}"].value)
            self.penum = penum

    def add(self, name: None, price: None, count: None):
        print("in progress!!!")


book = new(penum, max)
main = tk.Frame(window, bg="Gray")
main.place(x=140, y=150)
lbl1 = tk.Label(main, text="", bg="Gray")
lbl1.pack()
lbl2 = tk.Label(main, text="", bg="Gray")
lbl2.pack()
lbl3 = tk.Label(main, text="", bg="Gray")
lbl3.pack()
book.next()
but1 = tk.Button(window, text="next-->", command=lambda: book.next(), bg="Gray")
but1.place(x=345, y=360)
but2 = tk.Button(window, text="<--behind", command=lambda: book.behind(), bg="Gray")
but2.place(x=5, y=360)
but3 = tk.Button(window, text="add", bg="Gray", command=lambda: book.add("", 0, 0))
but3.place(x=190, y=360)

window.mainloop()
