import pygame as pg
import math
""" this file deals with key inputs and modifies the speed of sticks in the game """

def processKeyDown(e, player_1, player_2):
	match e.key:
		
		# every keydown is basically just this but their player, directional sign 
		# and vector index taken into consideration
		case pg.K_w:
			
			# if no keys are currently pressed, stick goes in this direction with max speed
			if not player_1.pressedKeys:
				player_1.speed[1] = -player_1.maxSpeed
				
			# if only one key pressed other than this one
			# the stick is given a speed in this direction
			# so when both speed vectors are summed it equals to max speed
			# to achieve that, the size of the other vector is modified to sin45 * maxspeed
			elif player_1.pressedKeys == 1:
				if player_1.speed[1] > 0:
					player_1.speed[1] -= player_1.maxSpeed
				else:
					player_1.speed[1] -= player_1.maxSpeed / math.sqrt(2)

				if player_1.speed[0] < 0:
					player_1.speed[0] = -player_1.maxSpeed / math.sqrt(2)
				elif player_1.speed[0] > 0:
					player_1.speed[0] = player_1.maxSpeed / math.sqrt(2)
			else:
				player_1.speed[1] -= player_1.maxSpeed / math.sqrt(2)
			player_1.pressedKeys += 1

		case pg.K_d:
			if not player_1.pressedKeys:
				player_1.speed[0] = +player_1.maxSpeed
			elif player_1.pressedKeys == 1:
				if player_1.speed[0] < 0:
					player_1.speed[0] += player_1.maxSpeed
				else:
					player_1.speed[0] += player_1.maxSpeed / math.sqrt(2)

				if player_1.speed[1] < 0:
					player_1.speed[1] = -player_1.maxSpeed / math.sqrt(2)
				elif player_1.speed[1] > 0:
					player_1.speed[1] = player_1.maxSpeed / math.sqrt(2)
			else:
				player_1.speed[0] += player_1.maxSpeed / math.sqrt(2)
			player_1.pressedKeys += 1

		case pg.K_s:
			if not player_1.pressedKeys:
				player_1.speed[1] = +player_1.maxSpeed
			elif player_1.pressedKeys == 1:
				if player_1.speed[1] < 0:
					player_1.speed[1] += player_1.maxSpeed
				else:
					player_1.speed[1] += player_1.maxSpeed / math.sqrt(2)

				if player_1.speed[0] < 0:
					player_1.speed[0] = -player_1.maxSpeed / math.sqrt(2)
				elif player_1.speed[0] > 0:
					player_1.speed[0] = player_1.maxSpeed / math.sqrt(2)
			else:
				player_1.speed[1] += player_1.maxSpeed / math.sqrt(2)
			player_1.pressedKeys += 1

		case pg.K_a:
			if not player_1.pressedKeys:
				player_1.speed[0] = -player_1.maxSpeed
			elif player_1.pressedKeys == 1:
				if player_1.speed[0] > 0:
					player_1.speed[0] -= player_1.maxSpeed
				else:
					player_1.speed[0] -= player_1.maxSpeed / math.sqrt(2)

				if player_1.speed[1] < 0:
					player_1.speed[1] = -player_1.maxSpeed / math.sqrt(2)
				elif player_1.speed[1] > 0:
					player_1.speed[1] = player_1.maxSpeed / math.sqrt(2)
			else:
				player_1.speed[0] -= player_1.maxSpeed / math.sqrt(2)
			player_1.pressedKeys += 1

		case pg.K_UP:
			if not player_2.pressedKeys:
				player_2.speed[1] = -player_2.maxSpeed
			elif player_2.pressedKeys == 1:
				if player_2.speed[1] > 0:
					player_2.speed[1] -= player_2.maxSpeed
				else:
					player_2.speed[1] -= player_2.maxSpeed / math.sqrt(2)

				if player_2.speed[0] < 0:
					player_2.speed[0] = -player_2.maxSpeed / math.sqrt(2)
				elif player_2.speed[0] > 0:
					player_2.speed[0] = player_2.maxSpeed / math.sqrt(2)
			else:
				player_2.speed[1] -= player_2.maxSpeed / math.sqrt(2)
			player_2.pressedKeys += 1

		case pg.K_RIGHT:
			if not player_2.pressedKeys:
				player_2.speed[0] = player_2.maxSpeed
			elif player_2.pressedKeys == 1:
				if player_2.speed[0] < 0:
					player_2.speed[0] += player_2.maxSpeed
				else:
					player_2.speed[0] += player_2.maxSpeed / math.sqrt(2)

				if player_2.speed[1] < 0:
					player_2.speed[1] = -player_2.maxSpeed / math.sqrt(2)
				elif player_2.speed[1] > 0:
					player_2.speed[1] = player_2.maxSpeed / math.sqrt(2)
			else:
				player_2.speed[0] += player_2.maxSpeed / math.sqrt(2)
			player_2.pressedKeys += 1

		case pg.K_DOWN:
			if not player_2.pressedKeys:
				player_2.speed[1] = player_2.maxSpeed
			elif player_2.pressedKeys == 1:
				if player_2.speed[1] < 0:
					player_2.speed[1] += player_2.maxSpeed
				else:
					player_2.speed[1] += player_2.maxSpeed / math.sqrt(2)

				if player_2.speed[0] < 0:
					player_2.speed[0] = -player_2.maxSpeed / math.sqrt(2)
				elif player_2.speed[0] > 0:
					player_2.speed[0] = player_2.maxSpeed / math.sqrt(2)
			else:
				player_2.speed[1] += player_2.maxSpeed / math.sqrt(2)
			player_2.pressedKeys += 1

		case pg.K_LEFT:
			if not player_2.pressedKeys:
				player_2.speed[0] = -player_2.maxSpeed
			elif player_2.pressedKeys == 1:
				if player_2.speed[0] > 0:
					player_2.speed[0] -= player_2.maxSpeed
				else:
					player_2.speed[0] -= player_2.maxSpeed / math.sqrt(2)

				if player_2.speed[1] < 0:
					player_2.speed[1] = -player_2.maxSpeed / math.sqrt(2)
				elif player_2.speed[1] > 0:
					player_2.speed[1] = player_2.maxSpeed / math.sqrt(2)
			else:
				player_2.speed[0] -= player_2.maxSpeed / math.sqrt(2)
			player_2.pressedKeys += 1
					
					
def processKeyUp(e, player_1, player_2):
	match e.key:
		
		# what is done for this key is basically the same with the others,
		# except player and negativity of the speed, and the index of it.
		case pg.K_w:
			player_1.pressedKeys -= 1
			
			# if no keys other than the just released one were pressed,
			# it means that the stick isn't moving anymore
			if not player_1.pressedKeys:
				player_1.speed = [0, 0]
				
			# if just another one was pressed, we add the stick a speed
			# in the opposite direction so that the effect of the key
			# is removed, and if the stick has a speed in the other axis,
			# we increase it to have the value of maxspeed as it is the only
			# pressed key
			elif player_1.pressedKeys == 1:
				player_1.speed[1] += player_1.maxSpeed / math.sqrt(2)
				if player_1.speed[0] > 0:
					player_1.speed[0] = player_1.maxSpeed
				elif player_1.speed[0] < 0:
					player_1.speed[0] = -player_1.maxSpeed
					
			# if more keys are pressed, don't adjust the speed of the other axis
			# and just add a speed in the opposite direction
			else:
				player_1.speed[1] += player_1.maxSpeed / math.sqrt(2)

		case pg.K_d:
			player_1.pressedKeys -= 1
			if not player_1.pressedKeys:
				player_1.speed = [0, 0]
			elif player_1.pressedKeys == 1:
				player_1.speed[0] -= player_1.maxSpeed / math.sqrt(2)
				if player_1.speed[1] > 0:
					player_1.speed[1] = player_1.maxSpeed
				elif player_1.speed[1] < 0:
					player_1.speed[1] = -player_1.maxSpeed
			else:
				player_1.speed[0] -= player_1.maxSpeed / math.sqrt(2)

		case pg.K_s:
			player_1.pressedKeys -= 1
			if not player_1.pressedKeys:
				player_1.speed = [0, 0]
			elif player_1.pressedKeys == 1:
				player_1.speed[1] -= player_1.maxSpeed / math.sqrt(2)
				if player_1.speed[0] > 0:
					player_1.speed[0] = player_1.maxSpeed
				elif player_1.speed[0] < 0:
					player_1.speed[0] = -player_1.maxSpeed
			else:
				player_1.speed[1] -= player_1.maxSpeed / math.sqrt(2)

		case pg.K_a:
			player_1.pressedKeys -= 1
			if not player_1.pressedKeys:
				player_1.speed = [0, 0]
			elif player_1.pressedKeys == 1:
				player_1.speed[0] += player_1.maxSpeed / math.sqrt(2)
				if player_1.speed[1] > 0:
					player_1.speed[1] = player_1.maxSpeed
				elif player_1.speed[1] < 0:
					player_1.speed[1] = -player_1.maxSpeed
			else:
				player_1.speed[0] += player_1.maxSpeed / math.sqrt(2)

		case pg.K_UP:
			player_2.pressedKeys -= 1
			if not player_2.pressedKeys:
				player_2.speed = [0, 0]
			elif player_2.pressedKeys == 1:
				player_2.speed[1] += player_2.maxSpeed / math.sqrt(2)
				if player_2.speed[0] > 0:
					player_2.speed[0] = player_2.maxSpeed
				elif player_2.speed[0] < 0:
					player_2.speed[0] = -player_2.maxSpeed
			else:
				player_2.speed[1] += player_2.maxSpeed / math.sqrt(2)

		case pg.K_RIGHT:
			player_2.pressedKeys -= 1
			if not player_2.pressedKeys:
				player_2.speed = [0, 0]
			elif player_2.pressedKeys == 1:
				player_2.speed[0] -= player_2.maxSpeed / math.sqrt(2)
				if player_2.speed[1] > 0:
					player_2.speed[1] = player_2.maxSpeed
				elif player_2.speed[1] < 0:
					player_2.speed[1] = -player_2.maxSpeed
			else:
				player_2.speed[0] -= player_2.maxSpeed / math.sqrt(2)

		case pg.K_DOWN:
			player_2.pressedKeys -= 1
			if not player_2.pressedKeys:
				player_2.speed = [0, 0]
			elif player_2.pressedKeys == 1:
				player_2.speed[1] -= player_2.maxSpeed / math.sqrt(2)
				if player_2.speed[0] > 0:
					player_2.speed[0] = player_2.maxSpeed
				elif player_2.speed[0] < 0:
					player_2.speed[0] = -player_2.maxSpeed
			else:
				player_2.speed[1] -= player_2.maxSpeed / math.sqrt(2)

		case pg.K_LEFT:
			player_2.pressedKeys -= 1
			if not player_2.pressedKeys:
				player_2.speed = [0, 0]
			elif player_2.pressedKeys == 1:
				player_2.speed[0] += player_2.maxSpeed / math.sqrt(2)
				if player_2.speed[1] > 0:
					player_2.speed[1] = player_2.maxSpeed
				elif player_2.speed[1] < 0:
					player_2.speed[1] = -player_2.maxSpeed
			else:
				player_2.speed[0] += player_2.maxSpeed / math.sqrt(2)