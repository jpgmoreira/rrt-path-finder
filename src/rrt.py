from container import pointsContainer
from collision import collision
from utils import randomPoint, inside
import pygame as pg
import drawing
import time

def rrt(start, goal, obstacles):
	parent = { start: None }
	depth = { start: 0 }

	container = pointsContainer()
	container.insert(start)
	
	height = 0
	nodes = 1

	current = start

	startTime = time.perf_counter()

	while not False:#inside(current, goal):
		event = pg.event.poll()

		sample = randomPoint()
		nearest = container.NNS(sample)

		if (sample == nearest):
			continue
		
		if not collision(sample, nearest, obstacles):
			container.insert(sample)
			parent[sample] = nearest
			depth[sample] = depth[nearest] + 1

			height = max(height, depth[sample])
			nodes += 1

			drawing.addEdge( (nearest, sample) )

			current = sample
