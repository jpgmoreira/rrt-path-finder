from points_container import pointsContainer
from collision import collision
from utils import randomPoint, inside
import pygame as pg
import drawing
import events
import time

def rrt(start, goal, obstacles):
	"""
	start -- point (x, y)
	goal  -- point (x, y)
	obstacles: pygame.Surface
	"""
	parent = { start: None }
	depth = { start: 0 }

	container = pointsContainer()
	container.insert(start)
	
	height = 0
	nodes = 1

	current = start

	startTime = time.perf_counter()

	while not inside(current, goal):
		if not events.rrtHandler():  # handle user events.
			return None

		if drawing.showInfo:  # drawing-related.
			elapsed = time.perf_counter() - startTime
			drawing.updateInfo(elapsed, nodes, height)
			drawing.update()

		sample = randomPoint()
		nearest = container.NNS(sample)

		if (sample == nearest):  # do not allow two identical points.
			continue
		
		if not collision(sample, nearest, obstacles):
			container.insert(sample)
			parent[sample] = nearest
			depth[sample] = depth[nearest] + 1

			height = max(height, depth[sample])
			nodes += 1

			drawing.addEdge( (nearest, sample) )

			current = sample
	
	if not goal in parent:
		parent[goal] = current
		depth[goal] = depth[current] + 1
		height = max(height, depth[goal])
		nodes += 1
		drawing.addEdge( (current, goal) )

	elapsed = time.perf_counter() - startTime
	drawing.updateInfo(elapsed, nodes, height, depth[goal])

	return parent
