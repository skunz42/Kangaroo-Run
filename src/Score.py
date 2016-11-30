import pygame
import __init__.py  

clock = pygame.time.Clock()

class Score:
  def __init__(self):
    self.score = 1
    self.x = 0
    self.y = 0
    self.v = 0
    self.g = 0
  def changeScore(score):
    while(done == False):
      clock.tick(60)
      score = 100 + (score * .002)
      print(score)
