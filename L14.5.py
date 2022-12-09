from tkinter import *
from tkinter import messagebox

from math import pi

result = .0


def clear():
    edit.delete(0, last=END)


def calc():
    global result
    try:
        r = float(radius.get())
        result = 4 / 3 * pi * r ** 3
        messagebox.showinfo("Объем сферы", "{:.4f}".format(result))
    except ValueError:
        messagebox.showerror("Чел ты...", "Некорректный ввод!")


def save_txt():
    if result:
        with open("out.txt", 'w') as f:
            f.write('Объем сферы с радиусом {} равен {}'.format(radius.get(), str(result)))
        messagebox.showinfo("Объем сферы", "Сохранено в файл 'out.txt'")
    else:
        messagebox.showwarning("Чел ты...", "Нечего сохранять!")


def save_html():
    if result:
        s = """ <!DOCTYPE html> <html lang="en"> <head> <meta charset="UTF-8"> <title>Tkinter</title>
        </head> <body> <h2> Объем сферы с радиусом {} равен {}
         </h2> </body> </html> """.format(radius.get(), str(result))

        with open("output.html", 'w') as f:
            f.write(s)
        messagebox.showinfo("Объем сферы", "Сохранено в файл 'output.html'")
    else:
        messagebox.showwarning("Косяк, батенька!", "Нечего сохранять!")


root = Tk()
root.title('Sphere')
root.resizable(False, False)
radius = StringVar()

Label(root, text='Radius:').grid(row=0, column=0, sticky=E, padx=10, pady=10)

edit = Entry(root, width=10, text='0', textvariable=radius)
edit.grid(row=0, column=1, padx=10, pady=10)

btn_calc = Button(root, text='Calculate', command=calc)
btn_calc.grid(row=0, column=2, padx=10, pady=10)

btn_save_txt = Button(root, text='Save to txt', command=save_txt)
btn_clear = Button(root, text='Clear', command=clear)
btn_save_htm = Button(root, text='Save to html', command=save_html)

btn_save_txt.grid(row=2, column=0, padx=10, pady=10)
btn_clear.grid(row=2, column=1, padx=10, pady=10)
btn_save_htm.grid(row=2, column=2, padx=10, pady=10)

root.mainloop()