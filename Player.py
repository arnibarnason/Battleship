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
			
	
