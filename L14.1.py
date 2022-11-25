import tkinter
def click():
    res=(float(entry.get())-32)/1.8
    label.config(text=res)
window = tkinter.Tk()
frame = tkinter.Frame(window)
frame.pack()
label=tkinter.Label(frame)
label.pack()
entry = tkinter.Entry(frame)
entry.pack()
label = tkinter.Label(frame)
label.pack()
button = tkinter.Button(frame, command=click, width=10, text="Перевести")
button.pack()
window.mainloop()