"""
This is the module responsible for handling drawings to the screen.
All pygame.draw commands must be executed inside this module.
It also contains important variables related to drawing and other uses,
  that are accessible by other modules, such as startPos and goalPos. 
"""
from config import *
import pygame as pg

# Reference to the application's screen:
screen = None

# Initialize start and goal positions:
startPos = START_INIT_POS
goalPos = GOAL_INIT_POS

# Surfaces drawn to the screen:
obstaclesSurface = pg.Surface((WIDTH, HEIGHT))
treeSurface = pg.Surface((WIDTH, HEIGHT))
infoSurface = pg.Surface((WIDTH, HEIGHT))

treeSurface.set_colorkey((0, 0, 0))
infoSurface.set_colorkey((0, 0, 0))

# Edges pool to avoid updating the screen every time a new edge is added:
edgesPool = []

# Show or not the information about the algorithm:
showInfo = False

def drawObstacle(position):
	pg.draw.circle(obstaclesSurface, OBSTACLES_COLOR, position, OBSTACLES_RADIUS)	

def eraseObstacle(position):
	pg.draw.circle(obstaclesSurface, (0, 0, 0), position, OBSTACLES_RADIUS)	

def clearObstacles():
	obstaclesSurface.fill(0)

def clearTree():
	treeSurface.fill(0)

def saveObstacles():
	pg.image.save(obstaclesSurface, MAP_FILENAME)

def loadObstacles():
	global obstaclesSurface
	obstaclesSurface = pg.image.load(MAP_FILENAME)

def addEdge(edge):
	global edgesPool
	edgesPool.append(edge)
	if len(edgesPool) >= MAX_EDGES_POOL:
		for e in edgesPool:
			pg.draw.circle(treeSurface, (255, 128, 0), e[1], 2)
			pg.draw.line(treeSurface, (255, 255, 255), e[0], e[1])
		edgesPool = []
		update()

def clearEdgesPool():
	global edgesPool
	edgesPool = []

def toggleInfo():
	global showInfo
	showInfo = not showInfo

def updateInfo(elapsed, nodes, height, length = None):
	infoSurface.fill(0)
	elapsed = format(elapsed, '.4f')
	lines = [
		f'Time: {elapsed}s',
		f'Nodes: {nodes}',
		f'Height: {height}'
	]
	if length:
		lines.append(f'Path length: {length}')
	for i in range(len(lines)):
		temp = FONT.render(lines[i], 0, (255, 255, 0), (0, 0, 1))
		infoSurface.blit(temp, (WIDTH - temp.get_width(), i * FONT.get_height()))

def drawPath(parent):
	global showInfo
	showInfo = True
	current = goalPos
	while parent[current]:
		pg.draw.line(treeSurface, (0, 0, 255), current, parent[current], 4)
		pg.draw.circle(treeSurface, (0, 191, 255), current, 4)
		current = parent[current]
	pg.draw.circle(treeSurface, (0, 191, 255), current, 4)

def update():
	"""Update the screen."""
	screen.fill(0)
	screen.blit(obstaclesSurface, (0, 0))
	pg.draw.circle(screen, GOAL_COLOR, goalPos, RADIUS)
	pg.draw.circle(screen, START_COLOR, startPos, RADIUS)
	screen.blit(treeSurface, (0, 0))
	if showInfo:
		screen.blit(infoSurface, (0, 0))
	pg.display.flip()
