import pygame
from utilities import load_png

class Kangaroo(pygame.sprite.Sprite):

    def __init__(self):
        '''Initializes kangaroo sprite'''
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_png('../assets/kangaroo-frame-0.png')
        screen = pygame.display.get_surface()
        self.area = screen.get_rect()
        self.imageCounter = 0
        self.counter = 10
        self.reinit()

    def reinit(self):
        '''Moves kangaroo to position'''
        self.state = "still"
        self.movepos = [0,0]
        self.rect.bottomleft = self.area.bottomleft

    def update(self):
        '''Cycles through kangaroo images'''
        self.counter = self.counter + 1
        self.image = pygame.image.load("../assets/kangaroo-frame-" + str(self.imageCounter) + ".png")
        if self.counter % 10 == 0:
            self.imageCounter = self.imageCounter + 1
        if(self.imageCounter == 4):
            self.imageCounter = 0
