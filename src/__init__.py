import pygame
from Kangaroo import Kangaroo
from Cactus import Cactus
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

cact = Cactus()
cactSprite = pygame.sprite.RenderPlain(cact)

done = False
clock = pygame.time.Clock()

while not done:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                kang.jump()

    if kang.rect.colliderect(cact.rect):
        #print(kang.rect.size, kang.rect.topleft, kang.rect.bottomright)
        #print(cact.rect.size, cact.rect.topleft, cact.rect.bottomright)
        kang.collide()
            
    #kang.handlekeys()
    #screen.blit(kang, (0,0))
    
    screen.blit(backGround.image, (0,0))
    screen.blit(backGround.image, backGround.rect)
    
    kang.draw(screen)
    kangSprite.update()

    cact.draw(screen)
    cactSprite.update()

    #kangSprite.draw(screen)

    pygame.display.update()
    pygame.display.flip()
