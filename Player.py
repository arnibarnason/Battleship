#!/usr/bin/python
# -*- coding: utf-8 -*-
#from Battleship import Battleship
from Cell import Cell
from random import randint
class Player():
	
	def __init__(self):
		self.hits = 0
		self.health = 17
		self.ocean = [[] for i in range(10)]

	def addCellToOcean(self, cell, x):
		self.ocean[x].append(cell)
	
	def underAttack(self):
		x = randint(0,9)
		y = randint(0,9)
		cell = self.ocean[x][y]
		cell.isHit = True
		if cell.isShip:
			cell.color.config(background="red")
		else:
			cell.color.config(background="blue")
        
	def setUpShips(self):
                ships = [2,3,3,4,5]
                for i in ships:
                    vertical = randint(0,1)
                    if vertical:
                            y = randint(0,9-i+1)
                            x = randint(0,9)
                            for j in range(i):
                                self.ocean[x][y+j].isShip = True
                                self.ocean[x][y+j].color.config(background = "grey")
                    else:
                            x = randint(0,9-i+1)
                            y = randint(0,9)
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
		else:
			cell.color.config(background="blue")	
			
	
	def setUpShips(self):
                ships = [2,3,3,4,5]
                for i in ships:
                    vertical = randint(0,1)
                    if vertical:
                            y = randint(0,9-i+1)
                            x = randint(0,9)
                            for j in range(i):
                                self.ocean[x][y+j].isShip = True
                                self.ocean[x][y+j].color.config(background = "grey")
                    else:
                            x = randint(0,9-i+1)
                            y = randint(0,9)
                            for j in range(i):
                                self.ocean[x+j][y].isShip = True
                                self.ocean[x+j][y].color.config(background = "grey")
