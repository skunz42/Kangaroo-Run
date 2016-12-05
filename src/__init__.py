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
titlefont = pygame.font.SysFont("monospace", 32)

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
start = False
game_over = False
pause = False
pauseCount = 1

while not done:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            '''Jump'''
            if event.key == pygame.K_UP:
                kang.jump()
            '''Restart'''
            if event.key == pygame.K_r:
                kang.reinit()
                cact.reinit()
                score = 0
                pause = False
                pauseCount = 1
                game_over = False
            '''Quit'''
            if event.key == pygame.K_q:
                done = True
            '''Pause'''
            if event.key == pygame.K_p:
                pauseCount += 1
                if pauseCount % 2 == 0:
                    kang.freezeKang()
                    cact.freezeCact()
                    pause = True
                elif pauseCount % 2 == 1:
                    cact.resumeCact()
                    pause = False
            '''Start'''
            if event.key == pygame.K_s:
                start = True

    screen.blit(backGround.image, (0,0))
    screen.blit(backGround.image, backGround.rect)

    if not start:
        textstart = myfont.render("Press S to Start", 0, (0,0,0))
        screen.blit(textstart, (435, 120))
        texttitle = titlefont.render("Kangaroo Run", 0, (240, 0, 0))
        screen.blit(texttitle, (400, 75))

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
    if not game_over and not pause and start:
        score += 1
    
    if start:
        kang.draw(screen)
        kangSprite.update()

        cact.draw(screen)
        cactSprite.update()

    pygame.display.update()
    pygame.display.flip()