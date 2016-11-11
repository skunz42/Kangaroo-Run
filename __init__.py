import pygame
from Kangaroo import Kangaroo
from BackGround import Background

#life is a never ending struggle

pygame.init()
#Sets Up Screen
screen = pygame.display.set_mode((1080, 540))
pygame.display.set_caption('Kangaroo Run')
white = (255, 255, 255)

background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill(white)

backGround = Background('../assets/background.png')


screen.blit(background, (0,0))
pygame.display.flip()
screen.blit(backGround.image, backGround.rect)


kang = Kangaroo()
kangSprite = pygame.sprite.RenderPlain(kang)

done = False
clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    
    #screen.blit(background, (0,0))
    screen.blit(backGround.image, backGround.rect)
    kangSprite.update()
    kangSprite.draw(screen)
    pygame.display.flip()
    clock.tick(60)
