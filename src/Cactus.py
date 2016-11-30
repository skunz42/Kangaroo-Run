#Insert Cactus Code Here

import pygame
from utilities import load_png

class Cactus(pygame.sprite.Sprite):

	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image, self.rect = load_png('../assets/Cactus.png')
		self.x = 1080
		self.y = 425
		self.v = 2

		screen = pygame.display.get_surface()
		self.area = screen.get_rect()
		self.state = "moving"

		self.imageCounter = 0
		self.counter = 10

	def draw(self, screen):
		if self.x < -50:
			self.x = 1080
		self.x -= self.v
		self.v += 1/500

		screen.blit(self.image, (self.x, self.y))