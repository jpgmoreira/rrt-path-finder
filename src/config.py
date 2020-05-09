from pygame import font
font.init()

# Screen size:
WIDTH = 800
HEIGHT = 600

# Radius of the start and goal circles:
RADIUS = 20

START_INIT_POS = (30, 30)
GOAL_INIT_POS = (WIDTH - 30, HEIGHT - 30)

START_COLOR = (0, 255, 0)
GOAL_COLOR = (255, 0, 0)

OBSTACLES_COLOR = (77, 135, 181)
OBSTACLES_RADIUS = 10

# During RRT, update the screen every MAX_EDGES_POOL new edges created.
MAX_EDGES_POOL = 10

# Filename to save and load obstacles map:
MAP_FILENAME = 'map.png'

# Font used to display information about the algorithm:
FONT = font.SysFont('Tahoma', 25, bold = True)
