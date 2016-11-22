import pygame
from utilities import load_png

class Kangaroo(pygame.sprite.Sprite):

    def __init__(self):
        '''Initializes kangaroo sprite'''
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_png('../assets/kangaroo-frame-0.png')
        self.jumpup = False
        self.x = 0
        self.y = 415
        self.v = -20
        self.g = 1

        screen = pygame.display.get_surface()
        self.area = screen.get_rect()
        self.state = "still"

        self.imageCounter = 0
        self.counter = 10

        #self.reinit()

    #def reinit(self):
        '''Moves kangaroo to position'''
        #self.state = "still"
        #self.movepos = [0,0]
        #self.rect.bottomleft = self.area.bottomleft

    def update(self):
        '''Cycles through kangaroo images'''
        self.counter = self.counter + 1
        self.image = pygame.image.load("../assets/kangaroo-frame-" + str(self.imageCounter) + ".png")
        if self.counter % 10 == 0:
            self.imageCounter = self.imageCounter + 1
        if(self.imageCounter == 4):
            self.imageCounter = 0

    def jump(self):
        self.jumpup = True
        #self.v += self.g #Increments velocity
        #self.y += self.v #Changes y position
            
        #if(self.y > 415):
         #   self.y = 415
          #  self.v = -20
           # self.jump = False

    #def handlekeys(self):
     #   key = pygame.key.get_pressed()
      #  if key[pygame.K_UP]:
       #     self.jump()

    def draw(self, screen):
        if self.jumpup:
            self.v += self.g #Increments velocity
            self.y += self.v #Changes y position
            
            if(self.y > 415):
                self.y = 415
                self.v = -20
                self.jumpup = False
            
        screen.blit(self.image, (self.x, self.y))