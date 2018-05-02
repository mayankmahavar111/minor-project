import os
import tkinter as tk
from assistant import assist
from reminder import checkReminder

def hello():
    print("Hello World")


if __name__ == '__main__':
    root = tk.Tk()
    root.minsize(width=100,height=20)
    root.resizable(width=False,height=False)
    helloCommand= lambda : assist()
    panel = tk.Label(root)
    panel.pack(side="top", fill="both", expand="yes")

    play = tk.Button(root,command=helloCommand,text="speak",width=20)
    checkReminder()

    play.pack()

    root.mainloop()