from . constants import *
import pygame as pg
pg.init()

# Start and target blocks class:
class Block(pg.sprite.Sprite):
  def __init__(self, color, pos):
    pg.sprite.Sprite.__init__(self)

    self.image = pg.Surface((SIDE, SIDE))
    self.rect = self.image.get_rect(topleft=pos)

    self.image.fill(color)

# ----------------------------------------------------------

# - SurfsSprite:
#  Used to test sprite mask collision between the drawn edges
#   on 'test_surf' and the obstacles on 'obs_surf'.
class SurfSprite(pg.sprite.Sprite):
  def __init__(self):
    pg.sprite.Sprite.__init__(self)

    self.image = pg.surface.Surface((WIDTH, HEIGHT))
    self.rect = self.image.get_rect()

    self.image.set_colorkey(BG_COLOR)
    self.image.fill(BG_COLOR)

# ----------------------------------------------------------

# - Vertex class:
class Vertex:
  def __init__(self, pos, parent):
    self.pos = pos
    self.parent = parent
    if parent:
      self.depth = parent.depth + 1
    else:
      self.depth = 0
