#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
ZetCode Tkinter tutorial

This script shows a simple window
on the screen.

author: Jan Bodnar
last modified: January 2011
website: www.zetcode.com
"""

from Tkinter import Tk, W, E
from ttk import Frame, Label, Style
from ttk import Entry

class Battleship(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)   

        self.parent = parent

        self.initUI()

    def initUI(self):

        self.parent.title("Battleship")

        Style().configure("TCheckbutton", padding=(2, 2, 2, 2), font='serif 10')

        for i in range(10):
            self.columnconfigure(i)
            self.rowconfigure(i)

        entry = Entry(self)
        for i in range(10):
            for j in range(10):
                x = Label(self, text="  iii  ")
                x.bind("<Button-1>", self.callback)
                x.grid(row=i, column=j)
        self.pack()

    def callback(self, event):
        #x = Label(self, text="  jee  ", background="red")
        #x.grid(row=i, column=j)
        event.widget["foreground"] = "red"#.config(background='red')
        event.widget["text"] = "haaaaaaalo"
        print("hallo")

def main():

    root = Tk()
    #root.geometry("250x150+300+300")
    app = Battleship(root)
    root.mainloop()  


if __name__ == '__main__':
    main()  
