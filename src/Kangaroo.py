import pygame
from utilities import load_png

class Kangaroo(pygame.sprite.Sprite):

    def __init__(self):
        '''Initializes kangaroo sprite'''
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_png('../assets/kangaroo-frame-0.png')
        self.rect = self.rect.inflate(-64, -64)

        self.jumpup = False
        self.colliding = False

        self.x = 0
        self.y = 415
        self.rect.x = 0
        self.rect.y = 415
        self.v = -20 #Velocity
        self.g = 1 #Gravity constant

        screen = pygame.display.get_surface()
        self.area = screen.get_rect()

        self.imageCounter = 0 #For images
        self.counter = 10

    def reinit(self):
        '''Moves kangaroo to position'''
        self.x = 0
        self.y = 415
        self.v = -20
        self.rect.x = 0
        self.rect.y = 415

    def freezeKang(self):
        '''Freezes kangaroo in place if collision occurs'''
        self.jumpup = False
        self.counter = 0
    
    def resumeKang(self):
        self.jumpup = True
        
    def update(self):
        '''Cycles through kangaroo images'''
        self.counter = self.counter + 1
        self.image = pygame.image.load("../assets/kangaroo-frame-" + str(self.imageCounter) + ".png")
        if self.counter % 10 == 0:
            self.imageCounter = self.imageCounter + 1
        if(self.imageCounter == 4):
            self.imageCounter = 0

    def jump(self):
        '''Sets jump to true'''
        self.jumpup = True

    def collide(self):
        '''Sets collision to true'''
        self.colliding = True

    def draw(self, screen):
        '''Jump equation'''
        if self.jumpup:
            self.v += self.g #Increments velocity
            self.rect.y += self.v #Changes y position
            
            if(self.rect.y > 415):
                self.rect.y = 415
                self.v = -20
                self.jumpup = False

        if self.colliding:
            self.colliding = False
            
        screen.blit(self.image, (self.rect.x, self.rect.y))