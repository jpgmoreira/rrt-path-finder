from random import randrange as rand
from config import *
import math

def dist(p1, p2):
	return math.hypot(p2[0] - p1[0], p2[1] - p1[1])

def randomPoint():
	return rand(WIDTH), rand(HEIGHT)

def inside(point, center):
	return dist(point, center) < RADIUS

def normalize(vx, vy):
	norm = math.sqrt(vx * vx + vy * vy)
	if (norm > 1e-6):
		vx /= norm
		vy /= norm
	return (vx, vy)
