import pygame
import json
import utilities
from Kangaroo import Kangaroo
from Cactus import Cactus
from BackGround import Background
from Highscore import Highscore

pygame.init()
#Sets Up Screen
screen = pygame.display.set_mode((1080, 540))
pygame.display.set_caption('Kangaroo Run')
white = (255, 255, 255)

score = 0
myfont = pygame.font.SysFont("monospace", 16)
biggerfont = pygame.font.SysFont("monospace", 24)
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

highscoreClass = Highscore()
hslist = highscoreClass.getScores()
lowest = hslist[0]

clock = pygame.time.Clock()

username = str

done = False
highscore = False
start = False
game_over = False
pause = False
login_screen = False
logged_in = False
pauseCount = 1
initialstring = str((open("highscore.txt", "r")).read())
initialdict = json.loads(initialstring)

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
            # if event.key == pygame.K_l:
            #     login_screen = True
            if event.key == pygame.K_h:
                highscore = True

    screen.blit(backGround.image, (0,0))
    screen.blit(backGround.image, backGround.rect)

    '''Title Screen'''
    if not start:
        textstart = biggerfont.render("Press S to Start", 0, (0,0,0))
        screen.blit(textstart, (400, 200))
        texttitle = titlefont.render("Kangaroo Run", 0, (240, 0, 0))
        screen.blit(texttitle, (400, 65))
        # if not logged_in:
        #     textlogin = myfont.render("Press L to Login", 0, (0,0,0))
        #     screen.blit(textlogin, (435, 110))
        # else:
        #     textlogin = myfont.render(username, 0, (0, 0, 0))
        #     screen.blit(textlogin, (435, 110))

    '''Collision'''
    if kang.rect.colliderect(cact.rect):
        kang.collide()
        game_over = True
    
    '''Game Over Screen'''
    if game_over:
        textgo = myfont.render("Game Over", 0, (0,0,0))
        screen.blit(textgo, (475, 150))
        kang.freezeKang()
        cact.freezeCact()
        if(score > lowest):
            textNewHigh = myfont.render("Enter Name", 0, white)
            screen.blit(textNewHigh, (475, 250))
            dictToWriteOut = highscoreClass.updateList(score)
            highscoreClass.writeToFile(dictToWriteOut)
        game_over = False
        pause = True
    
    '''Pause Screen'''
    if pause:
        texths = myfont.render("Press H For High Scores", 0, (0,0,0))
        screen.blit(texths, (10, 10))
        textps = myfont.render("Press P To Resume", 0, (0,0,0))
        screen.blit(textps, (425, 10))
        '''High Score'''
        if highscore:
            screen.blit(backGround.image, (0, 0))
            texthstitle = titlefont.render("High Scores:", 0, white)
            name = highscoreClass.getNames(initialdict)
            hslist = highscoreClass.getScores()
            text1 = biggerfont.render("1: " + name[0] + ": " + str(hslist[4]), 0, white)
            text2 = biggerfont.render("2: " + name[1] + ": " + str(hslist[3]), 0, white)
            text3 = biggerfont.render("3: " + name[2] + ": " + str(hslist[2]), 0, white)
            text4 = biggerfont.render("4: " + name[3] + ": " + str(hslist[1]), 0, white)
            text5 = biggerfont.render("5: " + name[4] + ": " + str(hslist[0]), 0, white)
            screen.blit(texthstitle, (420, 100))
            screen.blit(text1, (450, 150))
            screen.blit(text2, (450, 175))
            screen.blit(text3, (450, 200))
            screen.blit(text4, (450, 225))
            screen.blit(text5, (450, 250))

    '''Displays Score'''
    label = myfont.render("Score: {0}".format(score), 0, (0, 0, 0))
    screen.blit(label, (900, 10))
    if not game_over and not pause and start:
        score += 1


    '''Loads cactus and kangaroo after start'''
    if start:
        kang.draw(screen)
        kangSprite.update()

        cact.draw(screen)
        cactSprite.update()

    # '''Login'''
    # if login_screen:
    #     screen.blit(backGround.image, backGround.rect)
    #     username_text = myfont.render("Enter your username: ", 0, (0, 0, 0))
    #     screen.blit(username_text, (400, 75))
    #     password_text = myfont.render("Enter your password: ", 0, (0, 0, 0))
    #     screen.blit(password_text, (400, 100))
    #     while(login_screen == True):
    #         login.loginLoop()




    pygame.display.update()
    pygame.display.flip()
