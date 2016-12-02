import pygame
import math
import random

class Score():
  def __init__(self):
    pygame.sprite.Sprite.__init__(self)
    self.score = 0

  def changeScore(self, current_score):
      self.score = math.floor(current_score + (random.randrange(75, 105) + (current_score * .0005)))
      return self.score
