#!/usr/bin/python
# -*- coding: utf-8 -*-
from Tkinter import Tk, W, E, S, N, Label, Button, RAISED
from ttk import Frame, Style
from ttk import Entry
import tkMessageBox
from time import sleep
from Player import Player, ComputerPlayer
from Cell import Cell

class Battleship(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)   
        self.parent = parent
        self.player1 = Player()
        self.player2 = ComputerPlayer()
        self.isOver = True
        self.initUI()

    def initUI(self):

        self.parent.title("Battleship")
		#initialize players cells 
        for i in range(11):
            self.columnconfigure(i, weight=1)
            self.rowconfigure(i, weight=1)
		#initialize computers cells
        for i in range(10):
            self.columnconfigure(i+11, weight=1)
        
        entry = Entry(self)
        self.setup()       
        
        x = Button(self, text="Reset", command=self.setup)
        x.grid(row=11,column=14, columnspan=3, sticky=N+S+E+W)
        self.pack()

    def setup(self):
        self.isOver = False
        self.player1.resetPlayer()
        self.player2.resetPlayer()
		#setup ocean and link left mouse button (button-1) to callback function
        for i in range(10):
            for j in range(10):
                x = Label(self, relief=RAISED, width=4, height=2)
                x.bind("<Button-1>", lambda event, arg=(i,j): self.callback(event, arg))
                x.grid(row=i, column=j)
				#initialize cell with isShip=isHit=false and label	
                cell = Cell(False, False, x)
                self.player2.addCellToOcean(cell, i)

        Label(self, text="Attack here!").grid(column=4, row=11, columnspan=3)
		#init section between oceans
        for i in range(10):
            x = Label(self, width=2, height=2, background="black")
            x.grid(column=10, row=i)
		#init computers attack ocean
        for i in range(10):
            for j in range(11,21):
                x = Label(self, relief=RAISED, width=4, height=2)
                x.grid(row=i, column=j)
                cell = Cell(False, False, x)
                self.player1.addCellToOcean(cell, i)

        self.player1.setUpShips()
        self.player2.setUpShips()

	#callback is called when left mouse button clicks onto a cell in players attack ocean
    def callback(self, event, pos):
        self.parent.wm_title("Computers turn!")
        if not self.isOver:
			#underAttack returns true when health is zero	
            if self.player2.underAttack(pos):
                tkMessageBox.showinfo("VICTORY", "Congratulations, you WON!")
                self.isOver = True
			#post attack
            self.parent.update()
            self.parent.wm_title("Your turn!")
			#sleep for 1 second between turns, as if computer was thinking
            sleep(1)
            if self.player1.underAttack():
                tkMessageBox.showinfo("LOOOOSER", "All of your ships have been ruined!")
                for i in range(10):
                    for j in range(10):
                        cell = self.player2.ocean[i][j]
                        if cell.isShip and not cell.isHit:
                            cell.color.config(background="green")

                self.isOver = True
        else:
            tkMessageBox.showinfo("Reset", "The game is finished, you need to reset the game to continue")


def main():

    root = Tk()
    app = Battleship(root)
    root.mainloop()  


if __name__ == '__main__':
    main()  
