import pygame

class Background(pygame.sprite.Sprite):
    def __init__(self, name):
        pygame.sprite.Sprite.__init__(self)  #call Sprite initializer

        """ Load image and return image object"""
        try:
                self.image = pygame.image.load(name)
                if self.image.get_alpha is None:
                        self.image = self.image.convert()
                else:
                        self.image = self.image.convert_alpha()
        except pygame.error as message:
                print('Cannot load image:' + name)
                raise SystemExit(message)

        self.rect = self.image.get_rect()