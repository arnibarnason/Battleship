#!/usr/bin/python
# -*- coding: utf-8 -*-
from Tkinter import Tk, W, E, Label, RAISED
from ttk import Frame, Style
from ttk import Entry
from time import sleep
import Player

class Battleship(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)   

        self.parent = parent

        self.initUI()

    def initUI(self):

        self.parent.title("Battleship")

        player1 = Player()
        player2 = ComputerPlayer()

        for i in range(10):
            self.columnconfigure(i)
            self.rowconfigure(i)
        
        for i in range(11):
            self.columnconfigure(i+10)

        entry = Entry(self)
        for i in range(10):
            for j in range(10):
                k = (i,j)
                x = Label(self, relief=RAISED, width=4, height=2)
                x.bind("<Button-1>", lambda event, arg=k: self.callback(event, arg))
                x.grid(row=i, column=j)

        for i in range(10):
            x = Label(self, width=2, height=2, background="black")
            x.grid(column=10, row=i)
        
        for i in range(10):
            for j in range(11,21):
                k = (i,j)
                x = Label(self, relief=RAISED, width=4, height=2)
                #x.bind("<Button-1>", lambda event, arg=k: self.callback(event, arg))
                x.grid(row=i, column=j)

        self.pack()

    def callback(self, event, pos):
        color = "red"#player2.underAttack(pos)
        event.widget["background"] = color
        time.sleep(3)
        player1.underAttack()

def main():

    root = Tk()
    app = Battleship(root)
    root.mainloop()  


if __name__ == '__main__':
    main()  