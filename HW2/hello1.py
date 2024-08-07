import tkinter as tk
from tkinter import *


def on_click():
    lbs = thb.get() * 0.03
    exchange.set(f'{lbs:.2f} US')
    


root = Tk()
root.option_add("*Font", "impact 20")
thb = DoubleVar()
exchange = StringVar()


Entry(root, textvariable=thb, width=50 , justify="right").pack(side=LEFT, padx=50)
Label(root, text="THB").pack(side=LEFT, padx=10)
Button(root, text=" = ", bg="gray", command=on_click).pack(side=LEFT)
Label(root, textvariable=exchange , padx=10).pack(side=LEFT)

root.mainloop()
