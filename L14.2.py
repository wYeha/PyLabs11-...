import sys
import tkinter
import random
import os

d={'Птица':'bird', 'Кот':'cat', 'Пес':'dog', 'Машина':'car', 'Голова':'head'}
window = tkinter.Tk()
window.geometry('200x300')
frame = tkinter.Frame(window)
frame.pack()
label = tkinter.Label(frame)
answer = tkinter.Label(frame)
label.pack()
entry = tkinter.Entry(frame, width=10)
entry.pack()
answer.pack()


def random_word():
    word = random.choice(list(d.keys()))
    label.configure(text=word)
    answer.configure(text="")
    entry.delete(0, tkinter.END)
    return word


random_word()


def restart():
    python = sys.executable
    os.execl(python, python, *sys.argv)


def recognize():
    a = entry.get()
    if d[label.cget('text')] == a:
        result = 'Да'
    else:
        result = 'Нет'
        recognize.invocations -=1
        if recognize.invocations == 0:
            result = 'Проиграли, играем заново'
            restart()
    answer.configure(text=result)


recognize.invocations = 3


btn1 = tkinter.Button(frame, text="Проверка", command=recognize)
btn1.pack()
btn2 = tkinter.Button(frame, text="Следующее слово", command=random_word)
btn2.pack()
window.mainloop()
