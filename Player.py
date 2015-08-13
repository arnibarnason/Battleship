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
                self.guessList = self.generateGuessList()

        def resetPlayer(self):
            self.ocean = [[] for i in range(10)]
            self.health = 17
            self.health = 17
            self.foundDirection = 0
            self.lastHits = []
			#guessList contains cells where there might be a ship
            self.guessList = self.generateGuessList()
	#cell is each square in grid and ocean is the grid
	def addCellToOcean(self, cell, x):
		self.ocean[x].append(cell)
	#generate attack on players ships from computer	
	def underAttack(self):
	#next shot returns an educated guess where ship might be and if lies vertically or horizontally
                (x, y, direction) = self.nextShot()
		cell = self.ocean[x][y]
                cell.isHit = True
		if cell.isShip:
			#the computer hit a ship
                        self.foundDirection = direction
			cell.color.config(background="red")
                        self.health -= 1
                        self.lastHits.append((x, y))
                        if self.health == 0:
                            return True
		else:
			#the computer missed
			cell.color.config(background="blue")
                        return False
		#AI function for computer
        def nextShot(self):
            for i, j in self.lastHits:
                if self.foundDirection == 1 or self.foundDirection == 0:
                    if i != 9 and not self.ocean[i+1][j].isHit:
                        return (i+1,j, 1)
                if self.foundDirection == 1 or self.foundDirection == 0:
                    if i != 0 and not self.ocean[i-1][j].isHit:
                        return (i-1,j, 1)
                if self.foundDirection == 2 or self.foundDirection == 0:
                    if j != 9 and not self.ocean[i][j+1].isHit:
                        return (i,j+1, 2)
                if self.foundDirection == 2 or self.foundDirection == 0:
                    if j != 0 and not self.ocean[i][j-1].isHit:
                        return (i,j-1, 2)

            lenGuessList = len(self.guessList)
            if not lenGuessList is 0:
				#guessList is not empty, so computer can make an educated guess
                (x, y) = self.guessList.pop(randint(0, lenGuessList - 1))
                while self.ocean[x][y].isHit:
                    lenGuessList = len(self.guessList)
                    (x, y) = self.guessList.pop(randint(0, lenGuessList - 1))
            else:
				#guesslist is empty so computer attacks a random non-hit cell in ocean
                x = randint(0,9)
                y = randint(0,9)
                while self.ocean[x][y].isHit:
                    x = randint(0,9)
                    y = randint(0,9)
            self.foundDirection = 0
            self.lastHits = []
            return (x, y, 0) 

        def generateGuessList(self):
            guessList = []
            for i in range(10):
                guessList.append((i,i))

            guessList.append(zip(range(0, 5), range(5, 10)))
            guessList.append(zip(range(5, 10), range(0, 5)))
            
            guessList.append(zip(range(0, 3), range(7, 10)))
            guessList.append(zip(range(7, 10), range(0, 3)))

            guessList.append(zip(range(0, 8), range(2, 10)))
            guessList.append(zip(range(2, 10), range(0, 8)))

            guessList.append((0,9))
            guessList.append((9,0))

            returnList = []
            for i in guessList:
                if type(i) is list:
                    for j in i:
                        returnList.append(j)
                else:
                    returnList.append(i)

            return returnList

	#place ships on ocean, unfortunately it is random for both player and computer
	def setUpShips(self):
                ships = [2,3,3,4,5]
                for i in ships:
                    vertical = randint(0,1)
					#overlap variable helps to make ships non-overlapping
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
									#place ship in position
                                    for j in range(i):
                                        self.ocean[x][y+j].isShip = True
                                        self.ocean[x][y+j].color.config(background = "grey")
                        else:
								#ship will lie horizontally
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
	#place attack on players attack ocean according to selected cell with coordinates
	def underAttack(self, coordinates):
		x = coordinates[0]
		y = coordinates[1]
		cell = self.ocean[x][y]
		cell.isHit = True
		#change color to red if there is a ship there and to blue if not
		if cell.isShip:
			cell.color.config(background="red")	
                        self.health -= 1
                        if self.health == 0:
                            return True
		else:
			cell.color.config(background="blue")	
                        return False
			
	#same as setupShips for player except they are not visible on players attack ocean	
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
