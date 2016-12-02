import pygame
from Score import Score
from Kangaroo import Kangaroo
from Cactus import Cactus
from BackGround import Background

#test 2

pygame.init()
#Sets Up Screen
screen = pygame.display.set_mode((1080, 540))
pygame.display.set_caption('Kangaroo Run')
white = (255, 255, 255)
black = (0, 0, 0)
button_light = (205, 200, 177)

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

score = Score()
starting_score = 0

largeText = pygame.font.Font("yoshi.ttf",60)
mediumText = pygame.font.Font("yoshi.ttf",48)
smallText = pygame.font.Font("yoshi.ttf",18)
pause = False

done = False
clock = pygame.time.Clock()

def game_loop():
    done = False
    global pause
    current_score = score.changeScore(starting_score + 1)
    while not done:
        clock.tick(60)
        current_score = score.changeScore(current_score)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    kang.jump()
                    if event.key == pygame.K_p:
                        pause = True
                        paused()

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

        scoreSurf, scoreRect = text_objects(str(current_score), mediumText, black)
        scoreRect.center = (970, 35)
        screen.blit(scoreSurf, scoreRect)

        #kangSprite.draw(screen)

        pygame.display.update()
        pygame.display.flip()

def text_objects(text, font, color = white):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()

def button(msg,x,y,w,h,i_color,a_color,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if(x + w > mouse[0] > x and y + h > mouse[1] > y):
        pygame.draw.rect(screen, a_color,(x,y, w,h))
        if(click[0] == 1 and action != None):
            if(action == "play"):
                game_loop()
                if(action == "quit"):
                    pygame.quit()
                    quit()
    else:
        pygame.draw.rect(screen, i_color,(x,y, w,h))


    TextSurf, TextRect = text_objects(msg,smallText)
    TextRect.center = ((x+(w/2)),(y+(h/2)))
    screen.blit(TextSurf, TextRect)

def paused():
    while(pause):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        TextSurf, TextRect = text_objects("PAUSED", largeText)
        TextRect.center = ((1080/2),(540/2))
        screen.blit(TextSurf, TextRect)

        button("[CONTINUE]",420,300,240,39,black,button_light,"play")
        button("[QUIT]",860,440,140,40,black,button_light,"quit")

        pygame.display.update()
        clock.tick(15)

def game_intro():
    intro = True

    while(intro):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        TextSurf, TextRect = text_objects("Kangaroo Run", largeText)
        TextRect.center = ((1080/2),(540/2))
        screen.blit(TextSurf, TextRect)

        button("[CLICK HERE TO BEGIN]",420,300,240,39,black,button_light,"play")
        button("[QUIT]",860,440,140,40,black,button_light,"quit")

        pygame.display.update()
        clock.tick(15)

game_intro()
