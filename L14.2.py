import tkinter
import random

d={'Птица':'bird', 'Кот':'cat', 'Пес':'dog', 'Машина':'car', 'Голова':'head'}
window = tkinter.Tk()
window.geometry('200x300')
frame = tkinter.Frame(window)
frame.grid()
label = tkinter.Label(frame)
label.grid(row=0, column=0)
entry = tkinter.Entry(frame)
entry.grid(row=0,column=2)
label2=tkinter.Label(frame, text="на английском")
label2.grid(row=0, column=1)
label3=tkinter.Label(frame)
label3.grid(row=0, column=3, text=" ")

def random_word():
    word=random.choice(list(d.keys()))
    label.configure(text=word)
    return word
random_word()

def recognize():
    l=entry.get()
    if d[label.get()]==l :
        label3.configure(text="да")
    else:
        label3.configure(text="нет")
recognize()

window.mainloop()