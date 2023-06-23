import pygame
import random
from settings import *

class Generator:
    def __init__(self, screen):
        self.x = random.randint(50, 350)
        self.y = random.randint(50, 350)
        self.bonusTime = random.randint(1, 5)
        self.screen = screen
        self.ticks=0
        self.tickSpeed=1
        self.bonusTick = 0
        self.score = 0
        self.bonusGen = False
        self.circleRect = None

    def gen(self):
        self.circleRect = pygame.draw.circle(self.screen, 'red', (self.x, self.y), POINT_SIZE)

    def genBonus(self):
        self.circleRect = pygame.draw.circle(self.screen, 'green', (self.x, self.y), BONUS_SIZE)


    def main(self):
        self.tickSpeedController()

        if self.bonusGen:
            self.genBonus()
        else:
            self.gen()

        if self.ticks<120:
            self.ticks+=self.tickSpeed

        if self.ticks==120:
            if self.bonusGen==True:
                self.bonusGen=False
            
            self.x, self.y = random.randint(50, 350), random.randint(50, 350)
            self.ticks=0
            self.bonusTick+=1

        if self.bonusTick==self.bonusTime:
            self.bonusGen=True
            self.x, self.y = random.randint(50, 350), random.randint(50, 350)
            self.ticks=0
            self.bonusTick=0
            self.bonusTime=random.randint(1, 5)

    def clickEvent(self, x, y):
        left, right, top, bottom = self.circleRect.left, self.circleRect.right, self.circleRect.top, self.circleRect.bottom
        if (x>=left and x<=right) and (y>=top and y<=bottom):
            if(self.bonusGen):
                self.score+=10
            else:
                self.score+=10
            self.ticks=120
            self.checkScore(self.score)
        
        

    def checkScore(self, score):
        if score!=0 and score%10==0:
            self.tickSpeed+=1

    def tickSpeedController(self):
        if self.tickSpeed>2:
            self.tickSpeed=2

        


