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
		self.hits = []
		self.target = []

        def resetOcean(self):
		self.ocean = [[] for i in range(10)]

	def addCellToOcean(self, cell, x):
		self.ocean[x].append(cell)
	
	def underAttack(self):
		if not self.hits:
			x = randint(0,9)
			y = randint(0,9)
		else:
			guess = self.aI()
			x = guess[0]
			y = guess[1]
		cell = self.ocean[x][y]
                while cell.isHit == True:
					x = randint(0,9)
					y = randint(0,9)
					cell = self.ocean[x][y]
                cell.isHit = True
		if cell.isShip:
			self.hits.append((x,y))
			cell.color.config(background="red")
                        self.health -= 1
                        if self.health == 0:
                            return True
		else:
			cell.color.config(background="blue")
                        return False
    
	#try to make a smart move based on previous hits:
	def aI(self):
		print("inside ai")	
		#if this is the first time we hit this particular ship:
		if len(self.hits) == 1 and not self.target:
			x = self.hits[0][0]
			y = self.hits[0][1]
			#initialize target to surrounding coordinates:
			self.target = [(x+1,y),(x-1,y), (x,y+1), (x,y-1)]
			print("clean target:",[t for t in [(x+1,y),(x-1,y), (x,y+1), (x,y-1)] if not self.ocean[t[0]][t[1]].isHit])
	
			for t in self.target:
				print("t line 54:",t)
				self.target.remove(t)
				if self.ocean[t[0]][t[1]].isShip:
					print("t inside if: ",t)
					return t
		#here we have hit ship more than once
		else:
			'''if we still have targets:
			if self.target:
				for i in self.target:
					if 
			return (x,y)'''
			#ship lies vertically:
			#if hits[0][0] == hits[1][0]
				
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
