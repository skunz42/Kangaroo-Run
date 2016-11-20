import pygame
from Kangaroo import Kangaroo
from BackGround import Background

#test 2

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
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            
    kang.handlekeys()
    #screen.blit(kang, (0,0))
    
    screen.blit(backGround.image, (0,0))
    screen.blit(backGround.image, backGround.rect)
    kang.draw(screen)

    kangSprite.update()
    #kangSprite.draw(screen)
    pygame.display.update()
    pygame.display.flip()