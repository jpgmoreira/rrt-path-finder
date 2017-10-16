
import pygame as pg
import time
from random import randrange as rand
from math import inf, hypot

from . import classes as cl
from . constants import *

pg.init()


# - - - - - - - - 
# - Function to calculate distance between 2 points:
def dist(p1,p2):
  return hypot(p2[0]-p1[0],p2[1]-p1[1])
# - - - - - - - - 

# ---------------------------------------------------------------------------------
# - Main application class: -
class Application:
  def __init__(self):

    self.screen = pg.display.set_mode((WIDTH,HEIGHT))

    # Display's icon and caption:
    icon = pg.surface.Surface((32,32))
    icon.fill(START_COLOR)
    pg.display.set_icon(icon)
    pg.display.set_caption(CAPTION)

    # Start, goal and obstacles surface.
    self.start = cl.Block(START_COLOR,START_INIT_POS)
    self.goal = cl.Block(GOAL_COLOR,GOAL_INIT_POS)
    self.obs_surf = cl.SurfSprite()

    # Tree's surface. (Normal pygame.surface.Surface).
    self.tree_surf = pg.surface.Surface((WIDTH,HEIGHT))
    self.tree_surf.set_colorkey(BG_COLOR)
    self.tree_surf.fill(BG_COLOR)

    # Surface for testing collisions:
    self.test_surf = cl.SurfSprite();

    # Contains the start, goal and obstacles surface sprites.
    self.sprites = pg.sprite.Group(self.start,self.goal,self.obs_surf)


    # States: 'normal', 'start_drag', 'goal_drag', 'drawing', 'erasing', 'running', 'path_found'.
    self.state = 'normal'; print(self.state)

    self.mainloop()

  # - - - - - - - - - - - - - - - - - - - - - -
  def mainloop(self):
    done = False
    while not done:

      # ---------------------------
      # - Events handling:
      for e in pg.event.get():
        # If the user clicks the window's 'x', closes the app.
        if e.type == pg.QUIT:
           done = True 

        elif e.type == pg.MOUSEBUTTONDOWN:
          if e.button == 1:  # Left mouse button clicked:
            if self.start.rect.collidepoint(e.pos):
              self.state = 'start_drag'
            elif self.goal.rect.collidepoint(e.pos):
              self.state = 'goal_drag'
            else:
              self.state = 'drawing'
          elif e.button == 3:  # Right button clicked:
            self.state = 'erasing'
          print(self.state)

        elif e.type == pg.MOUSEBUTTONUP:
          self.state = 'normal'; print(self.state)

        elif e.type == pg.MOUSEMOTION:
          if e.buttons[0]:  # Left mouse button holding:
            if self.state == 'start_drag':
              self.start.rect.center = e.pos
            elif self.state == 'goal_drag':
              self.goal.rect.center = e.pos
            elif self.state == 'drawing':
              pg.draw.line(self.obs_surf.image,OBS_COLOR,(e.pos[0]-e.rel[0],e.pos[1]-e.rel[1]),e.pos,OBS_WIDTH)
          elif e.buttons[2]:  # Right mouse button holding:
            if self.state == 'erasing':
              pg.draw.line(self.obs_surf.image,0,(e.pos[0]-e.rel[0],e.pos[1]-e.rel[1]),e.pos,OBS_WIDTH)

        elif e.type == pg.KEYDOWN:
          if e.key == pg.K_c:  # Clear obstacles on screen:
            self.obs_surf.image.fill(BG_COLOR)
            print('Obstacles surface cleared.')
          elif e.key == pg.K_s:  # Save current obstacles surface:
            self.save_obstacles()
          elif e.key == pg.K_l:  # Load saved obstacles surface:
            self.load_obstacles()
          elif e.key == pg.K_RETURN:  # Enter pressed: run RRT algorithm.
            self.state = 'running'; print(self.state)
            if self.run() == 'quit':
              done = True
            self.state = 'normal'; print(self.state)
      # ---------------------------
      # Updates screen:
      self.screen.fill(BG_COLOR)
      self.sprites.draw(self.screen)
      pg.display.flip()
  # - - - - - - - - - - - - - - - - - - - - - -

  # - - - - - - - - - - - - - - - - - - - - - -
  # - Function that implements RRT algorithm:
  def run(self):
    # Clears tree surface.
    self.tree_surf.fill(BG_COLOR)
    # Additional mask variable to obs_surf, for mask collision tests.
    self.obs_surf.mask = pg.mask.from_surface(self.obs_surf.image)

    # The first added vertex (root) must be the start's position.
    newvertex = cl.Vertex(self.start.rect.center,None)
    vertices = [newvertex]
    
    # Info variables: tree's height, linear distance between start and goal,
    #  and the starting time of the agorithm.
    treeheight = 0
    lin_dist = dist(self.start.rect.center,self.goal.rect.center)
    start_time = time.perf_counter()

    # Control variables:
    showinfo = True
    done = self.goal.rect.collidepoint(self.start.rect.center)

    # - - - - - - - - - - - - - - - - - - - - - - -
    while not done:
      # Sleeps the application for tests.
      #time.sleep(0.1)

      # - Events handling:
      for e in pg.event.get():
        if e.type == pg.QUIT:
          return 'quit'
        elif e.type == pg.KEYDOWN:
          # 'h' key hides and shows
          #   information on screen:
          if e.key == pg.K_h:
            showinfo = not showinfo
            if showinfo == False:
              # Hides information:
              self.screen.fill(BG_COLOR)
              self.sprites.draw(self.screen)
              self.screen.blit(self.tree_surf,(0,0))
              pg.display.flip()
          else:
            # If any key other than 'h' is pressed during
            #  the algorithm execution, the algorithm ends.
            return

      # Show (or not) information on screen:
      if showinfo:
        self.show_info(time.perf_counter()-start_time,treeheight,len(vertices),lin_dist)

      # - - -

      # - RRT algorithm steps:

      # Chooses a random point on the screen:
      newpoint = (rand(WIDTH),rand(HEIGHT))

      # Finds tree's vertex nearest to the point chosen:
      nearest_dist = inf
      for v in vertices:
        currdist = dist(newpoint,v.pos)
        if currdist < nearest_dist:
          nearest = v
          nearest_dist = currdist

      # Tries to create and edge connecting 'nearest' to 'newpoint':
        # Draws a line connecting the points on the test surface:
      test_rect = pg.draw.line(self.test_surf.image,EDGE_COLOR,nearest.pos,newpoint)
        # Checks for mask collision between the test surface and the obstacles surface:
      collide = pg.sprite.collide_mask(self.test_surf,self.obs_surf)
        # Clear the test surface:
      self.test_surf.image.fill(BG_COLOR,test_rect)

      # If there was no collision between the created edge and obstacles:
      #  - creates a vertex on 'newpoint' and adds it to 'vertices';
      #  - paints the newly created edge on the tree's surface;
      #  - checks if newpoint is inside the 'goal':
      if not collide:
        newvertex = cl.Vertex(newpoint,nearest)
        vertices.append(newvertex)

        # Tests if the new vertex increases the height of the tree:
        if newvertex.depth > treeheight:
          treeheight = newvertex.depth

        # Drawings:
        pg.draw.line(self.tree_surf,EDGE_COLOR,nearest.pos,newpoint)
        pg.draw.circle(self.tree_surf,VERTEX_COLOR,newpoint,VERTEX_RADIUS)
        lr = pg.draw.line(self.screen,EDGE_COLOR,nearest.pos,newpoint)
        cr = pg.draw.circle(self.screen,VERTEX_COLOR,newpoint,VERTEX_RADIUS)
        pg.display.update([lr,cr])

        # If newpoint is inside goal, then a path connecting start to goal 
        #  was found, and the algorithm ends.
        if self.goal.rect.collidepoint(newpoint):
          done = True

    # - - -

    # - A path was found: paints the path, shows execution info, and waits for user to press a key:
    last_time = time.perf_counter() - start_time
    self.state = 'path_found'; print(self.state)
    # Lenght (number of edges) and total distance (sum of all path's edges) of the path found:
    path_len, path_dist = self.paint_path(newvertex)
    showinfo = True
    self.show_info(last_time,treeheight,len(vertices),lin_dist,path_dist,path_len)
    loop = True
    while loop:
      for e in pg.event.get():
        if e.type == pg.QUIT:
          return 'quit'
        elif e.type == pg.KEYDOWN:
          # If a key other than 'h' is pressed, ends the function.
          if e.key == pg.K_h:
            showinfo = not showinfo
            if showinfo == False:
              self.screen.fill(BG_COLOR)
              self.sprites.draw(self.screen)
              self.screen.blit(self.tree_surf,(0,0))
              pg.display.flip()
            else:
              self.show_info(last_time,treeheight,len(vertices),lin_dist,path_dist,path_len)                     
          else:
            loop = False
  # - - - - - - - - - - - - - - - - - - - - - -

  # - - - - - - - - - - - - - - - - - - - - - -
  # Saves the obstacle surface as 'map.png'.
  def save_obstacles(self):
    pg.image.save(self.obs_surf.image,'map'+'.png')
    print('Obstacles map saved.')
  # - - - - - - - - - - - - - - - - - - - - - -

  # - - - - - - - - - - - - - - - - - - - - - -
  # Tries to load 'map.png' to 'self.obs_surf'.
  def load_obstacles(self):
    try:
      self.obs_surf.image = pg.image.load('map.png').convert()
    except:
      print("'map.png' file was not found in the same directory.")
      return
    else:
      print('Obstacles map loaded.')
      self.obs_surf.image.set_colorkey(BG_COLOR)
  # - - - - - - - - - - - - - - - - - - - - - -

  # - - - - - - - - - - - - - - - - - - - - - -
  # Show algorithm's execution info on screen:
  def show_info(self,elapsed_time,height,vertices,lin_dist,path_dist=None,path_len=None):
    time_str = "  Elapsed time: %f s  " % elapsed_time
    height_str = "  Tree's height: %d  " % height
    vertices_str = "  Vertices: %d  " % vertices
    lin_dist_str = "  Linear distance: %f  " % lin_dist 

    time_surf = FONT.render(time_str,0,TEXT_COLOR,BG_COLOR)
    height_surf = FONT.render(height_str,0,TEXT_COLOR,BG_COLOR)
    vertices_surf = FONT.render(vertices_str,0,TEXT_COLOR,BG_COLOR)
    lin_dist_surf = FONT.render(lin_dist_str,0,TEXT_COLOR,BG_COLOR)

    r1 = self.screen.blit(time_surf,(TEXT_X,TEXT_Y))
    r2 = self.screen.blit(height_surf,(TEXT_X,TEXT_Y + TEXT_PADDING))
    r3 = self.screen.blit(vertices_surf,(TEXT_X,TEXT_Y + 2*TEXT_PADDING))
    r4 = self.screen.blit(lin_dist_surf,(TEXT_X,TEXT_Y + 3*TEXT_PADDING))

    rectsUpdate = [r1,r2,r3,r4]

    if self.state == 'path_found':
      path_dist_str = "  Path distance: %f  " % path_dist 
      path_dist_surf = FONT.render(path_dist_str,0,TEXT_COLOR,(0,0,0))
      r5 = self.screen.blit(path_dist_surf,(TEXT_X,TEXT_Y + 4*TEXT_PADDING))
      path_len_str = "  Path length: %d  " % path_len 
      path_len_surf = FONT.render(path_len_str,0,TEXT_COLOR,(0,0,0))
      r6 = self.screen.blit(path_len_surf,(TEXT_X,TEXT_Y + 5*TEXT_PADDING))
      rectsUpdate += [r5,r6]

    pg.display.update(rectsUpdate)
  # - - - - - - - - - - - - - - - - - - - - - -

  # - - - - - - - - - - - - - - - - - - - - - -
  # Paints the path connecting 'start' to 'goal', and returns its information (lenght and total path's distance):
  def paint_path(self,lastvertex):
    currvertex = lastvertex
    path_len = 0
    path_dist = 0.0

    # - Draws path on the tree's surface image, then blits it on screen:
    while currvertex.parent:
      pg.draw.line(self.tree_surf,PATH_EDGE_COLOR,currvertex.pos,currvertex.parent.pos,PATH_EDGE_WIDTH)
      pg.draw.circle(self.tree_surf,PATH_VERTEX_COLOR,currvertex.pos,PATH_VERTEX_RADIUS)
      path_len += 1
      path_dist += dist(currvertex.pos,currvertex.parent.pos)
      currvertex = currvertex.parent
    pg.draw.circle(self.tree_surf,PATH_VERTEX_COLOR,currvertex.pos,PATH_VERTEX_RADIUS)
    self.screen.blit(self.tree_surf,(0,0))
    pg.display.flip()

    return path_len, path_dist
  # - - - - - - - - - - - - - - - - - - - - - -
# ---------------------------------------------------------------------------------


