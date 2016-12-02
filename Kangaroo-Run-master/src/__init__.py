import pygame
from Score import Score
from Kangaroo import Kangaroo
from Cactus import Cactus
from BackGround import Background
from Login import Login
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

login = Login()

score = Score()
starting_score = 0

largeText = pygame.font.Font("yoshi.ttf",60)
mediumText = pygame.font.Font("yoshi.ttf",36)
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

def button(msg,x,y,w,h,i_color,a_color,text_size, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if(x + w > mouse[0] > x and y + h > mouse[1] > y):
        pygame.draw.rect(screen, a_color,(x,y, w,h))
        if(click[0] == 1 and action != None):
            if(action == "login"):
                login_screen = loginScreen()
            if(action == "user"):
                login.loginLoop()
            if(action == "play"):
                game_loop()
                if(action == "quit"):
                    pygame.quit()
                    quit()
    else:
        pygame.draw.rect(screen, i_color,(x,y, w,h))


    TextSurf, TextRect = text_objects(msg,text_size)
    TextRect.center = ((x+(w/2)),(y+(h/2)))
    screen.blit(TextSurf, TextRect)
def loginScreen():
    login_screen = True
    screen.blit(backGround.image, backGround.rect)
    while(login_screen == True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                login_screen == False
                pygame.quit()
                quit()
        pygame.display.update()
        clock.tick(15)
        button("[USERNAME]",420,250,240,39,black,button_light,mediumText)
        button("[PASSWORD]",420,350,240,39,black,button_light,mediumText)
        writeText("Username",420,100,240,39,largeText,black)
        writeText("Note, Click the button then type.", 420,200,240,39, mediumText, black)
def writeText(text,x,y,w,h,size,color):
    TextSurf, TextRect = text_objects(text, size, color)
    TextRect.center = (x + (w/2)),(y + (h/2))
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

        button("[CONTINUE]",420,300,240,39,black,button_light,smallText,"play")
        button("[QUIT]",860,440,140,40,black,button_light,smallText,"quit")

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


        button("[CLICK HERE TO LOGIN]",420,300,240,39,black,button_light,smallText,"login")
        button("[QUIT]",860,440,140,40,black,button_light,smallText,"quit")

        pygame.display.update()
        clock.tick(15)

game_intro()
