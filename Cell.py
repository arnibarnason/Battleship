#!/usr/bin/python
# -*- coding: utf-8 -*-
#class containing properties of each cell in ocean, initially set to False,False and gray
class Cell():

	def __init__(self, isShip, isHit, color):
		self.isShip = isShip
		self.isHit = isHit
		self.color = color
