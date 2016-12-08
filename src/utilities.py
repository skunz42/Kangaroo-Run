import os
import sys
import pygame

def load_png(name):
        """ Load image and return image object"""
        try:
                image = pygame.image.load(name)
                if image.get_alpha is None:
                        image = image.convert()
                else:
                        image = image.convert_alpha()
        except pygame.error as message:
                print('Cannot load image:' + name)
                raise SystemExit(message)
        return image, image.get_rect()
def getText(event):
        word = []
        while(True):
                if event.type == pygame.KEYDOWN:
                    if event == pygame.K_RETURN:
                        newword = ""
                        for i in self.word:
                            newword = newword + i
                        print(newword)
                        return newword
                    else:
                        key = pygame.key.name(event.key)
                        word.append(key)
