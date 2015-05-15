#!/usr/bin/python
# -*- coding: utf-8 -*-
from Battleship import Battleship
from Cell import Cell

class Player():
	
	def __init__(self):
		self.hits = 0
		self.health = 17
		self.grid = initGrid()

	def initGrid(self):
		grid = [[] for i in range(10)]
		for i in range(10):
			for j in range(10):
				grid.append(Cell(False, False))
		return grid
	
class ComputerPlayer(Player):
	
	def __init__(self):
		Player.__init__(self)

	def underAttack(coordinates):
		x = coordinates[0]
		y = coordinates[1]
		grid[x][y].isHit = True
		print(grid[x][y].isShip)
			
	
