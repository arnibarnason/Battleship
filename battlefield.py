#!/usr/bin/python
# -*- coding: utf-8 -*-
from Tkinter import Tk, W, E, PhotoImage, Label, RAISED
from ttk import Frame, Style
from ttk import Entry

class Battleship(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)   

        self.parent = parent

        self.initUI()

    def initUI(self):

        self.parent.title("Battleship")

        for i in range(10):
            self.columnconfigure(i)
            self.rowconfigure(i)

        entry = Entry(self)
        for i in range(10):
            for j in range(10):
                k = (i,j)
                x = Label(self, relief=RAISED, width=8, height=3, padx=3, pady=3)
                x.bind("<Button-1>", self.callback)
                x.grid(row=i, column=j)
        self.pack()

    def callback(self, event):
        event.widget["background"] = "red"

def main():

    root = Tk()
    app = Battleship(root)
    root.mainloop()  


if __name__ == '__main__':
    main()  
