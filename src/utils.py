from random import randrange as rand
from config import *
import math

def dist(p1, p2):
	"""
	Compute the euclidean distance between p1 and p2.

	p1 -- point (x, y)
	p2 -- point (x, y)
	"""
	return math.hypot(p2[0] - p1[0], p2[1] - p1[1])

def randomPoint():
	"""
	Returns coordinates of a random point on the screen.
	"""
	return rand(WIDTH), rand(HEIGHT)

def inside(point, center):
	"""
	Determine if point is inside the circle centered at
	  center and with radius equal config.RADIUS.
	"""
	return dist(point, center) < RADIUS

def normalize(vx, vy):
	"""
	Normalizes the input vector and returns its coordinates.
	"""
	norm = math.sqrt(vx * vx + vy * vy)
	if (norm > 1e-6):
		vx /= norm
		vy /= norm
	return (vx, vy)
