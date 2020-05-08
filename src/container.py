from utils import dist
class pointsContainer:
	def __init__(self):
		self._points = []
	
	def insert(self, point):
		self._points.append(point)
	
	def NNS(self, point):
		best = self._points[0]
		bestDist = dist(best, point)
		for p in self._points:
			if dist(p, point) < bestDist:
				best = p
				bestDist = dist(p, point)
		return best
