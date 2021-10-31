import pygame
import random
import time
from pygame.locals import *
import sqlite3
conn = sqlite3.connect('myDatabase.db')
c = conn.cursor()

pygame.init()  # start pygame
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Snake!!")
clock = pygame.time.Clock()

black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
white = (255, 255, 255)
yellow = (200, 200, 0)

snakelist = []

def showtext(msg,x,y,color):
    font = pygame.font.SysFont("freesans", 32)
    msgobj = font.render(msg,False,white)
    screen.blit(msgobj,(x,y))


class Snake():
    def __init__(self):
        self.x = (random.randint(0, 600) // 10) * 10
        self.y = (random.randint(0, 600) // 10) * 10
        self.color = green
        self.xMotion = 0
        self.yMotion = 0

    def drawSnake(self):
        snakelist.insert(0,([snakelist[0][0],snakelist[0][1]]))
        for each in snakelist:
            pygame.draw.rect(screen,self.color,(each[0],each[1],10,10),0)
        snakelist.pop()

    def moveSnake(self):
        snakelist.append([self.x, self.y])
        snakelist[0][0] += self.xMotion
        snakelist[0][1] += self.yMotion

    def eatFood(self):
        if snakelist[0][0] in range (self.x, self.x + 10) and snakelist[0][1] in range (self.y, self.y + 10):
            
          snakelist.insert(0,[self.x, self.y])
          self.x = (random.randint(20,580) // 10 ) * 10
          self.y = (random.randint(20,580) // 10 ) * 10

snake = Snake()

class Food():
    def __init__(self):
        self.x = (random.randint(20, 580) // 10) * 10
        self.y = (random.randint(20, 580) // 10) * 10
        self.color = red

    def drawFood(self):
        pygame.draw.rect(screen, self.color, (self.x, self.y, 10, 10), 0)

food = Food()

while True:

    screen.fill(black)
    clock.tick(10)
    snake.drawSnake()
    snake.moveSnake()
    snake.eatFood()
    food.drawFood()

    #wall condition
    if snakelist[0][0] >= 600:
        snakelist[0][0] = 590
        break

    if snakelist[0][0] <= 0:
        snakelist[0][0] = 10
        break

    if snakelist[0][1] <= 0:
        snakelist[0][1] = 10
        break

    if snakelist[0][1] >= 600:
        snakelist[0][1] = 590
        break

    #Game over condition
    if snakelist[0] in snakelist[1:]:
        print('snakelist:', snakelist)
        print('snakelist[1:]', snakelist[1:])
        showtext("GAME OVER.", 250,100, white)
        print('head co. were already in list')
        break

