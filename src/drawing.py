from config import *
import pygame as pg

screen = None

startPos = START_INIT_POS
goalPos = GOAL_INIT_POS

obstaclesSurface = pg.Surface((WIDTH, HEIGHT))
treeSurface = pg.Surface((WIDTH, HEIGHT))

obstaclesSurface.set_colorkey((0, 0, 0))
treeSurface.set_colorkey((0, 0, 0))

def drawObstacle(position):
	pg.draw.circle(obstaclesSurface, OBSTACLES_COLOR, position, OBSTACLES_RADIUS)	

def eraseObstacle(position):
	pg.draw.circle(obstaclesSurface, (0, 0, 0), position, OBSTACLES_RADIUS)	

def saveObstacles():
	pg.image.save(obstaclesSurface, MAP_FILENAME)

def loadObstacles():
	try:
		obstaclesSurface = pg.image.load(MAP_FILENAME)
	except:
		pass

def update():
	screen.fill(0)
	screen.blit(obstaclesSurface, (0, 0))
	pg.draw.circle(screen, GOAL_COLOR, goalPos, RADIUS)
	pg.draw.circle(screen, START_COLOR, startPos, RADIUS)
	screen.blit(treeSurface, (0, 0))
	pg.display.flip()
