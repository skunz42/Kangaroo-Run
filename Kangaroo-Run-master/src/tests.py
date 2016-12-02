import pygame
from Score import Score
from Kangaroo import Kangaroo
from Cactus import Cactus
from BackGround import Background
from Login import Login


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
mediumText = pygame.font.Font("yoshi.ttf",48)
smallText = pygame.font.Font("yoshi.ttf",18)
pause = False

done = False
clock = pygame.time.Clock()
def text_objects(text, font, color = white):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()
def loginScreen():
    print("aaaaa")
    login_screen = True
    print("aaaaa")
    while(login_screen == True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                login_screen == False
                pygame.quit()
                quit()
        button("[USERNAME]",420,300,240,39,black,button_light,"user")
        button("[PASSWORD]",860,440,140,40,black,button_light,"pass")
def button(msg,x,y,w,h,i_color,a_color,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if(x + w > mouse[0] > x and y + h > mouse[1] > y):
        pygame.draw.rect(screen, a_color,(x,y, w,h))
        if(click[0] == 1 and action != None):
            if(action == "user"):
                login.loginLoop()
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

def main():
    test_login_screen = loginScreen()
main()
