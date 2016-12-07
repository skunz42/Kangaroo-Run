import pygame
import json
from Kangaroo import Kangaroo
from Cactus import Cactus
from Cloud import Cloud
from BackGround import Background

pygame.init()
#Sets Up Screen
screen = pygame.display.set_mode((1080, 540))
pygame.display.set_caption('Kangaroo Run')
white = (255, 255, 255)

score = 0
highscore = 0

scorefile = open("../assets/scores.txt", "r")
highscore = int(scorefile.read())
scorefile.close()

'''Fonts'''

myfont = pygame.font.SysFont("monospace", 16)
titlefont = pygame.font.SysFont("monospace", 32)

'''Text'''

textstart = myfont.render("Press S to Start", 0, (0,0,0))
texttitle = titlefont.render("Kangaroo Run", 0, (0, 0, 0))
textre = myfont.render("Press R to Restart", 0, (0,0,0))
textqu = myfont.render("Press Q to Quit", 0, (0,0,0))
textps = myfont.render("Press P To Resume", 0, (0,0,0))
textgo = myfont.render("Game Over", 0, (0,0,0))

'''Background'''

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

cact2 = Cactus()
cact2Sprite = pygame.sprite.RenderPlain(cact2)

cloud = Cloud()
cloudSprite = pygame.sprite.RenderPlain(cloud)

cloud2 = Cloud()
cloud2Sprite = pygame.sprite.RenderPlain(cloud)

'''Music'''

pygame.mixer.init(22050,-16,2,4096)
pygame.mixer.music.load("../assets/song.mp3")
pygame.mixer.music.set_volume(.5)
pygame.mixer.music.play(-1)

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
                cact2.reinit()
                cloud.reinit()
                cloud2.reinit()
                score = 0
                pause = False
                pauseCount = 1
                game_over = False
            '''Quit'''
            if event.key == pygame.K_q:
                done = True
            '''Pause'''
            if event.key == pygame.K_p and start:
                pauseCount += 1
                if pauseCount % 2 == 0:
                    kang.freezeKang()
                    cact.freezeCact()
                    cact2.freezeCact()
                    pause = True
                elif pauseCount % 2 == 1:
                    cact.resumeCact()
                    cact2.resumeCact()
                    pause = False
            
            '''Start'''
            if event.key == pygame.K_s:
                start = True

    screen.blit(backGround.image, (0,0))
    screen.blit(backGround.image, backGround.rect)

    '''Title Screen'''
    if not start:
        screen.blit(textstart, (435, 120))
        screen.blit(texttitle, (400, 75))

    '''Collision'''
    if kang.rect.colliderect(cact.rect) or kang.rect.colliderect(cact2.rect):
        kang.collide()
        game_over = True
    
    '''Game Over Screen'''
    if game_over:
        screen.blit(textgo, (475, 150))
        screen.blit(textre, (430, 180))
        screen.blit(textqu, (440, 210))
        kang.freezeKang()
        cact.freezeCact()
        cact2.freezeCact()
        '''Sets new highscore'''
        if score > highscore:
            highscore = score
            scorefile = open("../assets/scores.txt", "w")
            scorefile.write(str(highscore))
            scorefile.close()
    
    '''Pause Screen'''
    if pause and start:
        screen.blit(textps, (425, 10))

    '''Displays Score'''
    if start:
        label = myfont.render("Score: {0}".format(score), 0, (0, 0, 0))
        texths = myfont.render("High Score: {0}".format(highscore), 0, (0,0,0))
        screen.blit(label, (900, 10))
        screen.blit(texths, (850, 40))
        if not game_over and not pause and start:
            score += 1    
        '''Loads cactus and kangaroo after start'''
        kang.draw(screen)
        kangSprite.update()

        cact.draw(screen)
        cactSprite.update()

        if score > 1000:
            cact2.v = cact.v
            cact2.draw(screen)
            cact2Sprite.update()

        cloud.draw(screen)
        cloudSprite.update()

        cloud2.draw(screen)
        cloud2Sprite.update()

    pygame.display.update()
    pygame.display.flip()