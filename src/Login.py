import pygame

class Login():
    def __init__(self):
        self.password = str
        self.username = str
        self.word = []
    def loginLoop(self):
        done = False
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done == True
                else:
                    word = Login.getText()
    def getText():
        done = False
        while(done == False):
            for event in pygame.event.get():
                if event == pygame.KEYDOWN:
                    print(event)
                    if event == pygame.K_SPACE:
                        done = True
                    else:
                        key = event
                        self.word.append(key)
        print('Done')
    









#m
