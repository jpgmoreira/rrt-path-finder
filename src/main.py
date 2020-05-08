from rrt import rrt
import drawing
import events
import pygame as pg
pg.init()

gameState = 'waiting'

while True:
	event = pg.event.poll()
	mousePos = pg.mouse.get_pos()

	gameState = events.handle(event, gameState)

	if gameState == 'start-positioning':
		drawing.startPos = mousePos
	elif gameState == 'goal-positioning':
		drawing.goalPos = mousePos
	elif gameState == 'drawing':
		drawing.drawObstacle(mousePos)
	elif gameState == 'erasing':
		drawing.eraseObstacle(mousePos)
	elif gameState == 'rrt':
		rrt(drawing.startPos, drawing.goalPos, drawing.obstaclesSurface)

	drawing.update()
