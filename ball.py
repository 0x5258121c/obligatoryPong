import pygame as pg
import random
import math

""" this file contains the Ball class file """

class Ball:
	def __init__(self, game_window):
		w = pg.display.get_surface().get_width()
		h = pg.display.get_surface().get_height()
		self.color = pg.Color(255, 127, 39)
		self.rect = pg.Rect(0, 0, 20, 20) # might change size
		self.rect.center = w / 2, h / 2
		self.game_window = game_window
		self.maxSpeed = 13
		self.speed = self.randomInitialspeed()
	
	def randomInitialspeed(self):
		""" returns a random speed from 4 diagonal vectors """
		randVal = random.randrange(0, 4)
		
		# a value that is used to provide smooth, stable movement
		# which doesn't exceed a maximum speed
		tmp = self.maxSpeed / math.sqrt(2) 
		match randVal:
			case 0: # up-right
				return [tmp, -tmp]
			case 1: # up-left
				return [-tmp, -tmp]
			case 2: # bottom-right
				return [tmp, tmp]
			case 3: # bottom-left
				return [-tmp, tmp]
			
	def move(self, walls, players):
		self.rect.move_ip(self.speed)
		scoreObtained = 0
		for i, wall in enumerate(walls):
			if self.rect.clipline(wall):
				match i:
					case 0:
						self.speed[1] = -self.speed[1]
						self.rect.top = 1
					case 2:
						self.speed[1] = -self.speed[1]
						self.rect.top = self.game_window.get_height() - 21
					case 1: # right wall, score goes to player 1
						players[0].score += 1
						scoreObtained = 1
					case 3: # left wall, score goes to player 2
						players[1].score += 1
						scoreObtained = 1
						
		for player in players:
			if self.rect.clipline(player.top_side):
				self.rect.top = player.rect.top + 21
				self.speed[1] = -self.speed[1]
			if self.rect.clipline(player.right_side):
				self.rect.left = player.rect.left + 21
				self.speed[0] = -self.speed[0]
			if self.rect.clipline(player.bottom_side):
				self.rect.top = player.rect.top + 201
				self.speed[1] = -self.speed[1]
			if self.rect.clipline(player.left_side):
				self.rect.left = player.rect.left - 21
				self.speed[0] = -self.speed[0]
		
		if self.rect.top < 0 or self.rect.top > 630 or self.rect.left < 0 or self.rect.left > 1070:
			return -1
			
		if scoreObtained:
			return True
			
	def draw(self):
		""" draws the ball to the game window """
		self.game_window = pg.display.get_surface()
		pg.draw.rect(self.game_window, self.color, self.rect)