import pygame
from Kangaroo import Kangaroo
from Cactus import Cactus
from BackGround import Background

pygame.init()
#Sets Up Screen
screen = pygame.display.set_mode((1080, 540))
pygame.display.set_caption('Kangaroo Run')
white = (255, 255, 255)

score = 0
myfont = pygame.font.SysFont("monospace", 16)

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

clock = pygame.time.Clock()

done = False
game_over = False
pause = False
pauseCount = 1

while not done:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                kang.jump()
            if event.key == pygame.K_r:
                kang.reinit()
                cact.reinit()
                score = 0
                game_over = False
            if event.key == pygame.K_q:
                done = True
            if event.key == pygame.K_p:
                pauseCount += 1
                if pauseCount % 2 == 0:
                    kang.freezeKang()
                    cact.freezeCact()
                    pause = True
                elif pauseCount % 2 == 1:
                    cact.resumeCact()
                    pause = False

    screen.blit(backGround.image, (0,0))
    screen.blit(backGround.image, backGround.rect)

    if kang.rect.colliderect(cact.rect):
        kang.collide()
        game_over = True

    if game_over:
        textgo = myfont.render("Game Over", 0, (0,0,0))
        screen.blit(textgo, (475, 150))
        kang.freezeKang()
        cact.freezeCact()
    
    if pause:
        texths = myfont.render("Press H For High Scores", 0, (0,0,0))
        screen.blit(texths, (10, 10))
        textps = myfont.render("Press P To Resume", 0, (0,0,0))
        screen.blit(textps, (425, 10))

    label = myfont.render("Score: {0}".format(score), 0, (0, 0, 0))
    screen.blit(label, (900, 10))
    if not game_over and not pause:
        score += 1
    
    kang.draw(screen)
    kangSprite.update()

    cact.draw(screen)
    cactSprite.update()

    pygame.display.update()
    pygame.display.flip()