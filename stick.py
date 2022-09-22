import pygame as pg

class Stick:
	def __init__(self, player): # player -> 0 or 1, 0 is left side 1 is right side
		""" initialize color, rectangles, speed """
		w = pg.display.get_surface().get_width()
		h = pg.display.get_surface().get_height()
		self.color = pg.Color(240, 240, 240)
		self.rect = pg.Rect(0, 0, 20, 180)
		self.score = 0
		
		if(player == 1):
			self.rect.center = 3 * (w / 4), h / 2
		else:
			self.rect.center = w / 4, h / 2
			
		self.playArea = pg.Rect(player * (w / 2), 0, w / 2, h)
		self.speed = [0, 0] # speed on the axises
		self.maxSpeed = 8 # radius of the speed circle
		self.pressedKeys = 0 # directional keys being held down
	
	def move(self):
		""" move the current rectangles position in place (without returning a copy of it) """
		if self.playArea.contains(self.rect.move(self.speed)):
			self.rect.move_ip(self.speed)
			
		self.top_side = (self.rect.left, self.rect.top, self.rect.left + 20, self.rect.top)
		self.right_side = (self.rect.left + 20, self.rect.top, self.rect.left + 20, self.rect.top + 180)
		self.bottom_side = (self.rect.left, self.rect.top + 180, self.rect.left + 20, self.rect.top + 180)
		self.left_side = (self.rect.left, self.rect.top, self.rect.left, self.rect.top + 180)
	
	def draw(self):
		""" draw stick to game window """
		game_window = pg.display.get_surface()
		pg.draw.rect(game_window, self.color, self.rect)