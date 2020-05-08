from utils import dist

class pointsContainer:
	"""
	An ADT to store 2D points and find a point's nearest neighbor.

	To solve the Nearest Neighbor Search problem (NNS), I chose to
	  do a linear search, since it is much simpler than other
	  approaches and produces a reasonably good result here.
	"""
	def __init__(self):
		self._points = []
	
	def insert(self, point):
		self._points.append(point)
	
	def NNS(self, point):
		best = self._points[0] # will throw IndexError if self._points is empty.
		bestDist = dist(best, point)
		for p in self._points:
			pDist = dist(p, point)
			if pDist < bestDist:
				best = p
				bestDist = pDist
		return best
