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
		#t is what will be returned
		t = []
		#if this is the first time we hit this particular ship:
		if len(self.hits) == 1:
			x = self.hits[0][0]
			y = self.hits[0][1]
			self.boundaryCheck()
			#initialize target to surrounding coordinates that are not already hit:
			self.target = [t for t in [(x+1,y),(x-1,y), (x,y+1), (x,y-1)] if not self.ocean[t[0]][t[1]].isHit]
			t = self.target[0]
			print("t line 55:",t)
			self.target.remove(t)
			return t
		#here we have hit ship more than once
		else:
			#ship lies vertically:
			if self.hits[0][0] == self.hits[1][0]:
			#set target to opposite ends of previous hit-line
				firstHit = self.hits[0]
				lastHit = self.hits[-1]
				if firstHit > lastHit:
					self.target = [(firstHit[0],firstHit[1]+1), (lastHit[0],lastHit[1]-1)]
				else:
					self.target = [(firstHit[0],firstHit[1]-1), (lastHit[0],lastHit[1]+1)]
			else:
				#ship lies horizontally
				firstHit = self.hits[0]
				lastHit = self.hits[-1]
				if firstHit > lastHit:
					self.target = [(firstHit[0]+1,firstHit[1]), (lastHit[0]-1,lastHit[1])]
				else: 
					self.target = [(firstHit[0]-1,firstHit[1]), (lastHit[0]+1,lastHit[1])]
			self.boundaryCheck()
			#remove targets that have already been hit, might be unnecessary
			self.target = [t for t in self.target if not self.ocean[t[0]][t[1]].isHit]
			if not self.target:
			#we have already tried all potential targets 
				self.hits = []
				return (randint(0,9),randint(0,9))
			t = self.target[0]
			self.target.remove(t)
		return t
				
	def boundaryCheck(self):
		#check if target is inside of ocean, if it is a valid index
		for t in self.target:
			if t[0] not in range(10):
				self.target.remove(t)


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
