#!/usr/bin/python
# -*- coding: utf-8 -*-
#from Battleship import Battleship
from Cell import Cell
from random import randint
class Player():
	
	def __init__(self):
		self.lastHits = []
                # Represents the direction the ship is placed (i.e. vertical or horizontal)
                self.foundDirection = 0
		self.health = 17
		self.ocean = [[] for i in range(10)]

        def resetOcean(self):
		self.ocean = [[] for i in range(10)]

	def addCellToOcean(self, cell, x):
		self.ocean[x].append(cell)
	
	def underAttack(self):
                (x, y, direction) = self.nextShot()
		cell = self.ocean[x][y]
                cell.isHit = True
		if cell.isShip:
                        self.foundDirection = direction
			cell.color.config(background="red")
                        self.health -= 1
                        self.lastHits.append((x, y))
                        if self.health == 0:
                            return True
		else:
			cell.color.config(background="blue")
                        return False

        def nextShot(self):
            for i, j in self.lastHits:
                if self.foundDirection == 1 or self.foundDirection == 0:
                    if i != 9 and not self.ocean[i+1][j].isHit:
                        print("infirst")
                        return (i+1,j, 1)
                if self.foundDirection == 1 or self.foundDirection == 0:
                    if i != 0 and not self.ocean[i-1][j].isHit:
                        print("insecond")
                        return (i-1,j, 1)
                if self.foundDirection == 2 or self.foundDirection == 0:
                    if j != 9 and not self.ocean[i][j+1].isHit:
                        print("inthird")
                        return (i,j+1, 2)
                if self.foundDirection == 2 or self.foundDirection == 0:
                    if j != 0 and not self.ocean[i][j-1].isHit:
                        print("infirst")
                        return (i,j-1, 2)
            x = randint(0,9)
            y = randint(0,9)
            print("hallo")
            while self.ocean[x][y].isHit:
                x = randint(0,9)
                y = randint(0,9)
            self.foundDirection = 0
            self.lastHits = []
            return (x, y, 0) 

	def setUpShips(self):
                ships = [2,3,3,4,5]
                for i in ships:
                    vertical = randint(0,1)
                    overlap = True
                    while overlap:
                        overlap = False
                        if vertical:
                                y = randint(0,9-i+1)
                                x = randint(0,9)
                                for j in range(i): 
                                    if self.ocean[x][y+j].isShip == True:
                                        overlap = True
                                if not overlap:
                                    for j in range(i):
                                        self.ocean[x][y+j].isShip = True
                                        self.ocean[x][y+j].color.config(background = "grey")
                        else:
                                x = randint(0,9-i+1)
                                y = randint(0,9)
                                for j in range(i):
                                    if self.ocean[x+j][y].isShip == True:
                                        overlap = True
                                if not overlap:
                                    for j in range(i):
                                        self.ocean[x+j][y].isShip = True
                                        self.ocean[x+j][y].color.config(background = "grey")

	
class ComputerPlayer(Player):
	
	def __init__(self):
		Player.__init__(self)

	def underAttack(self, coordinates):
		x = coordinates[0]
		y = coordinates[1]
		cell = self.ocean[x][y]
		cell.isHit = True
		if cell.isShip:
			cell.color.config(background="red")	
                        self.health -= 1
                        if self.health == 0:
                            return True
		else:
			cell.color.config(background="blue")	
                        return False
			
	
	def setUpShips(self):
                ships = [2,3,3,4,5]
                for i in ships:
                    vertical = randint(0,1)
                    overlap = True
                    while overlap:
                        overlap = False
                        if vertical:
                                y = randint(0,9-i+1)
                                x = randint(0,9)
                                for j in range(i): 
                                    if self.ocean[x][y+j].isShip == True:
                                        overlap = True
                                if not overlap:
                                    for j in range(i):
                                        self.ocean[x][y+j].isShip = True
                        else:
                                x = randint(0,9-i+1)
                                y = randint(0,9)
                                for j in range(i):
                                    if self.ocean[x+j][y].isShip == True:
                                        overlap = True
                                if not overlap:
                                    for j in range(i):
                                        self.ocean[x+j][y].isShip = True
