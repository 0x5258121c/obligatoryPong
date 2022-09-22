import pygame as pg
import sys
import math
import time
import random
from stick import Stick
from ball import Ball
from keyInputs import processKeyUp, processKeyDown

""" this file is the main file of obligatoryPong """

font_color = pg.Color(240, 240, 240)

def showScores(bg, player_1, player_2):
	scoreFont = pg.font.Font(None, 80)
	game_window = pg.display.get_surface()
	txt = scoreFont.render(f"{player_1.score} : {player_2.score}", True, font_color)
	txtRect = txt.get_rect(center = (game_window.get_width() / 2, 60))
	game_window.blit(txt, txtRect)
	

def drawDashedLines():
	game_window = pg.display.get_surface()
	lineColor = pg.Color(240, 240, 240)
	x = game_window.get_width() / 2
	for i in range(9):
		pg.draw.line(game_window, lineColor, (x,  5 + (i * 75)), (x, 50 + (i * 75)), 3)
		
	
def gameOver(player, no):
	gameOverFont = pg.font.Font(None, 80)
	gameOver_bg_color = pg.Color(38, 109, 142)
	
	game_window = pg.display.get_surface()
	game_window.fill(gameOver_bg_color)
	
	txt = gameOverFont.render(f"Player {no} wins! Play again? (Y/N)", True, font_color)
	txtRect = txt.get_rect(center = (game_window.get_width() / 2, game_window.get_height() / 2))
	game_window.blit(txt, txtRect)
	pg.display.flip()
	
	while True:
		q = 0
		e = pg.event.wait()
		if e.type == pg.QUIT:
			q = 1
		if e.type == pg.KEYDOWN:
			if e.key == pg.K_n:
				q = 1
			elif e.key == pg.K_y:
				return
		if q:
			pg.quit()
			sys.exit()

# initialize everything
pg.init()

pg.display.set_caption("obligatoryPong")
game_window = pg.display.set_mode((1080, 640))

bg = pg.Surface(game_window.get_size())
bg_color = pg.Color(63, 178, 230)
bg.fill(bg_color)

game_window.blit(bg, (0, 0))

fps = pg.time.Clock()
game_speed = 60

player_1 = Stick(0)
player_2 = Stick(1)

ball = Ball(game_window)

scored = 0

# walls represented as (x1, y1, x2, y2) formatted tuples
walls = [
			# top wall
			(0, 0, game_window.get_width(), 0),
	
			#right wall
			(game_window.get_width(), 0, game_window.get_width(), game_window.get_height() ),
	
			# bottom wall
			(0, game_window.get_height(), game_window.get_width(), game_window.get_height()),
	
			# left wall
			(0, 0, 0, game_window.get_height())
		]

while True:
	fps.tick(game_speed)
	
	if scored:
		scored = 0
	
	# get inputs for quitting, moving sticks
	for e in pg.event.get():
		if e.type == pg.QUIT:
			pg.quit()
			sys.exit()
			
		# a stick has a max speed, so if multiple directional
		# inputs are present, we have to make it so that their vector sum
		# is equal to max speed
		if e.type == pg.KEYDOWN:
			processKeyDown(e, player_1, player_2)

		# when a player releases the key, we should calculate
		# the speed so that sum is always equal to max speed
		if e.type == pg.KEYUP:
			processKeyUp(e, player_1, player_2)

	# move sticks in their area
	player_1.move()
	player_2.move()

	# move ball and check for collision with walls / sticks, check for scores,
	# positive return value means a score has been obtained
	returnVal = ball.move(walls, [player_1, player_2])
	if returnVal:
		ball = Ball(game_window)
		scored = 1
	elif returnVal == -1:
		ball = Ball(game_window)
		
	restart = 0
	# check if game is over
	if player_1.score == 5:
		gameOver(player_1, 1)
		restart = 1
	elif player_2.score == 5:
		gameOver(player_2, 2)
		restart = 1
		
	# reinitialize scores sticks and ball to restart the game
	if restart:
		ball = Ball(game_window)
		player_1 = Stick(0)
		player_2 = Stick(1)
			
	# draw everything
	game_window.blit(bg, (0, 0));
	drawDashedLines()
	player_1.draw()
	player_2.draw()
	ball.draw()
	showScores(bg, player_1, player_2)
	pg.display.update()