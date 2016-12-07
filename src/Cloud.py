import pygame
from utilities import load_png
import random

class Cloud(pygame.sprite.Sprite):

	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image, self.rect = load_png('../assets/Cloud.png')

		self.x = 1080
		self.y = 140

		self.v = 1 #Velocity
		self.move = True

		screen = pygame.display.get_surface()
		self.area = screen.get_rect()

	def reinit(self):
		'''Moves Cloud to position'''
		self.x = 1200
		self.y = 140
		self.v = 1
		self.move = True

	def freezeCloud(self):
		'''Stops cloud in collision'''
		self.move = False

	def draw(self, screen):
		'''Speeds up cloud'''
		if self.move:
			if self.rect.x < -50:
				self.rect.x = 1080 + random.randrange(0,500)
				self.rect.y = 50 + random.randrange(0,100)
			self.rect.x -= self.v

		screen.blit(self.image, (self.rect.x, self.rect.y))