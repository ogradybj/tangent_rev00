import pygame, sys
from pygame.locals import *
import random
import math
from time import sleep



pygame.init()
FPS = 30
fpsClock = pygame.time.Clock()


DISPLAYSURF = pygame.display.set_mode((800,400), 0, 32)
pygame.display.set_caption('TANGENT')

#set up colors
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255, 0, 0)
GREEN = (0,255,50)
BLUE = (0,0,255)
speed = 5
bluex = 100
bluey = 10
speed = 3
xdir = 1
ydir = 1

B1 = 700
B2 = 500
B3 = 400
B4 = 200
B5 = 50
B6 = 320
counter = 0
ii = 0
xx = 0


class blueguy(pygame.sprite.Sprite):

    def __init__(self):
        self.x = random.randint(200,400)
        self.y = random.randint(100,200)
        self.dx = speed
        self.dy = speed
        self.on = False

    def update(self):

        if self.on == False:    

            if self.x >= 800:
                self.xdir = -1
            elif self.x <= 0:
                self.xdir = 1
            if self.y >= 400:
                self.ydir = -1
            elif self.y <= 0:
                self.ydir = 1


            self.x = self.x+(self.xdir*self.dx)
            self.y = self.y+(self.ydir*self.dy)
        elif self.on == True:
            self.x = self.x-speed/2
            
            
        pygame.draw.circle(DISPLAYSURF, BLUE, (self.x,self.y), 8, 6)
        pygame.draw.circle(DISPLAYSURF, BLACK, (self.x,self.y), 10, 3)

    def checkends(self):
        if self.x <=5:
            print 'left end'
        elif self.x >= 800:
            print 'right end'


    def moveoff(self):
        self.on = False

    def guyEnd(self):
        imp = 0

        for ee in range(1,9):
            imp = imp+1
            if imp == 1:
                pygame.draw.circle(DISPLAYSURF, RED, (guy.x,guy.y), 25, 0)
                sleep(0.2)
            elif imp == 2:
                pygame.draw.circle(DISPLAYSURF, RED, (guy.x,guy.y), 35, 0)
                sleep(0.2)
            elif imp == 3:
                pygame.draw.circle(DISPLAYSURF, RED, (guy.x,guy.y), 50, 0)
                sleep(0.2)
            elif imp == 4:
                pygame.draw.circle(DISPLAYSURF, RED, (guy.x,guy.y), 70, 0)
                sleep(0.2)
            elif imp >= 5:
                pygame.draw.circle(DISPLAYSURF, RED, (guy.x,guy.y), 100, 0)
                sleep(0.2)

                
    def updateguySpeed(self):
        self.dx = speed*2
        

class ball:
    global speed
    global counter
    x = 800
    #y = 200
    '''x = random.randint(150,650)
    y = 0'''
    dx = speed
    good = 1


    def __init__(self):
        self.X = 800 #random.randint(150,650)
        self.y = random.randrange(35, 365, 11)
        self.dx = speed
        self.good = random.randint(0,5)

    def update(self):
        self.x = self.x-self.dx
        if self.x <= 5:
            self.x = 800
            self.y = random.randint(20, 380)
            self.good = random.randint(0,5)

        if self.good <1:
            pygame.draw.circle(DISPLAYSURF, RED, (self.x,self.y), 28, 0)
        pygame.draw.circle(DISPLAYSURF, BLACK, (self.x,self.y), 28, 4)

    def checkimpact(self):
        
        dis = math.sqrt((self.x-guy.x)**2 + (self.y-guy.y)**2)

        if dis < 28 and self.good < 1:
            print 'boom'
            guy.guyEnd()
            
        elif dis < 28 and self.good >= 1:
            guy.on = True
            guy.x = self.x-20
            
            
    def updatebSpeed(self):
        self.dx = speed
        self.dy = speed


guy = blueguy()
balls = [ball()]



'''
#draw on the surface object
DISPLAYSURF.fill(WHITE)

pygame.draw.line(DISPLAYSURF, RED, (0,0), (0, 400), 10)
pygame.draw.line(DISPLAYSURF, RED, (800,0), (800, 400), 10)
pygame.draw.line(DISPLAYSURF, BLACK, (0,0), (800, 0), 10)
pygame.draw.line(DISPLAYSURF, BLACK, (0,400), (800, 400), 10)

'''


def updateballSpeed():
    for b in balls:
        b.updatebSpeed()


while True:
    DISPLAYSURF.fill(WHITE)
    ii = ii + 1
    if ii == 18*2:
        ii = 0
        counter = counter+1
        if counter < 11:
            balls.append(ball())
        elif counter > 19:
            xx = xx+1
            if xx == 25:
                speed = speed+1
                guy.updateguySpeed()
                updateballSpeed()
                xx = 0
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONUP:# & guy.on == True:
            
            guy.moveoff()
    guy.update()
    guy.checkends()
    for b in balls:
        b.update()
        b.checkimpact()
    
    pygame.display.update()
    fpsClock.tick(FPS)


