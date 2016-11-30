import pygame

class Score:
  def __init__(self):
        '''Initializes score'''
        pygame.sprite.Sprite.__init__(self)
        self.x = 0
        self.y = 0
        self.v = 0
        self.g = 0
