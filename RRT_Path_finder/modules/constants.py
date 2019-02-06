
from pygame import font
font.init()

SIDE = 30  # Start and goal squares side.
START_COLOR = (0,255,0)  # Start color = green.
GOAL_COLOR = (255,0,0)  # Goal color = red.
START_INIT_POS = (100,100)  # Start initial position.
GOAL_INIT_POS = (30,30)  # Goal initial position.

OBS_WIDTH = 10  # Drawing obstacle width.
OBS_COLOR = (77,135,181) # Obstacles color.

WIDTH = 800  # Display's width.
HEIGHT = 600  # Display's height.

CAPTION = 'RRT path finder'  # Window's caption.

BG_COLOR = (0,0,0)  # Background color.

EDGE_COLOR = (255,255,255)  # Tree's edge color.
EDGE_WIDTH = 1              # Tree's edge width.
VERTEX_COLOR = (255,128,0)  # Tree's vertex color.
VERTEX_RADIUS = 2           # Tree's vertex radius.

PATH_EDGE_COLOR = (0,0,255) # Path's edge color.
PATH_EDGE_WIDTH = 4         # Path's edge width.
PATH_VERTEX_COLOR = (0,191,255)  # Path's vertex color.
PATH_VERTEX_RADIUS = 4      # Path's vertex radius.

TEXT_X = WIDTH - 200  # 'x' coordinate where to display text info.
TEXT_Y = 15           # 'y' initial coordinate of text info.
TEXT_PADDING = 18     # Text padding between lines.
TEXT_COLOR = (255,255,0)  # Text color.
FONT = font.SysFont('Tahoma',15)  # Text font.
