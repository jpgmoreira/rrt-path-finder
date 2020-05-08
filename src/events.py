from config import *
from utils import dist
import drawing
import pygame as pg

def rrtHandler():
	"""Handle user events during RRT execution."""
	event = pg.event.poll()
	if event.type == pg.KEYDOWN:
		if event.key == pg.K_h:
			drawing.toggleInfo()
		else:
			drawing.clearTree()
			drawing.showInfo = False
			return False
	return True

def mainHandler(event, state, mousePos):
	"""State transitions when executing the main function."""
	overStart = dist(drawing.startPos, mousePos) < RADIUS
	overGoal = dist(drawing.goalPos, mousePos) < RADIUS

	if state == 'waiting':
		if event.type == pg.MOUSEBUTTONDOWN:
			if overStart: return 'start-positioning'
			elif overGoal: return 'goal-positioning'
			elif event.button == 1: return 'drawing'
			elif event.button == 3: return 'erasing'		
		elif event.type == pg.KEYDOWN:
			if event.key == pg.K_RETURN: return 'rrt'
			elif event.key == pg.K_s: return 'save'
			elif event.key == pg.K_l: return 'load'		
			elif event.key == pg.K_c: return 'clear'		

	elif state in ['drawing', 'erasing', 'start-positioning', 'goal-positioning']:
		if event.type == pg.MOUSEBUTTONUP:
			return 'waiting'

	elif state in ['save', 'load', 'clear']:
		return 'waiting'

	elif state == 'path-found':
		if event.type == pg.KEYDOWN:
			if event.key == pg.K_h:
				drawing.toggleInfo()
			else:
				drawing.clearTree()
				drawing.showInfo = False
				return 'waiting'

	return state
