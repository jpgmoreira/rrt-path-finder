from config import OBSTACLES_COLOR
from utils import dist, normalize

def collision(src, dst, obstacles):
	vx, vy = normalize(dst[0] - src[0], dst[1] - src[1])
	curr = list(src)
	while dist(curr, dst) > 1:
		intCurr = int(curr[0]), int(curr[1])
		if obstacles.get_at(intCurr) == OBSTACLES_COLOR:
			return True
		curr[0] += vx
		curr[1] += vy
	return False
