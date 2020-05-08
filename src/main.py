from config import *
from rrt import rrt
import drawing
import fsm
import pygame as pg
pg.init()

drawing.screen = pg.display.set_mode((WIDTH, HEIGHT))

gameState = 'waiting'

while True:
	event = pg.event.poll()
	mousePos = pg.mouse.get_pos()

	gameState = fsm.transition(event, gameState, mousePos)

	if gameState == 'start-positioning':
		drawing.startPos = mousePos
	elif gameState == 'goal-positioning':
		drawing.goalPos = mousePos
	elif gameState == 'drawing':
		drawing.drawObstacle(mousePos)
	elif gameState == 'erasing':
		drawing.eraseObstacle(mousePos)
	elif gameState == 'clear':
		drawing.clearObstacles()
	elif gameState == 'save':
		drawing.saveObstacles()
	elif gameState == 'load':
		drawing.loadObstacles()
	elif gameState == 'rrt':
		rrt(drawing.startPos, drawing.goalPos, drawing.obstaclesSurface)

	drawing.update()
