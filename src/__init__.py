import pygame
import json
import random
from Kangaroo import Kangaroo
from Cactus import Cactus
from BackGround import Background
from Cloud import Cloud


pygame.init()

'''Font'''
myfont = pygame.font.Font("../assets/font.ttf", 20)
titlefont = pygame.font.Font("../assets/font.ttf", 50)

'''Background'''
w = 1080
h = 540
background = pygame.image.load('../assets/backdrop.png')
background_size = (w,h)
background_rect = (w,h)
screen = pygame.display.set_mode([w,h])
x = 0

pygame.display.set_caption('Kangaroo Run')
white = (255, 255, 255)

'''Score'''
score = 0
highscore = 0

scorefile = open("../assets/scores.txt","r")
highscore = int(scorefile.read())
scorefile.close()

'''Objects'''
kang = Kangaroo()
kangSprite = pygame.sprite.RenderPlain(kang)

cact = Cactus()
cactSprite = pygame.sprite.RenderPlain(cact)

cact2 = Cactus()
cactSprite2 = pygame.sprite.RenderPlain(cact2)

cact3 = Cactus()
cactSprite3 = pygame.sprite.RenderPlain(cact3)

cloud = Cloud()
cloudSprite = pygame.sprite.RenderPlain(cloud)

cloud2 = Cloud()
cloudSprite2 = pygame.sprite.RenderPlain(cloud)
cloud2.x += random.randrange(50)
cloud2.y += random.randrange(50)



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
