import pygame
import random
import time
from pygame.locals import *
import sqlite3
conn = sqlite3.connect('snakeDatabase.db')
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

start = False


def showtext(msg,x,y,color):
    font = pygame.font.SysFont("freesans", 32)
    msgobj = font.render(msg,False,color)
    screen.blit(msgobj,(x,y))

def showMenu():
    # screen.fill(black)
    pygame.display.update()
    showtext('SNAKE WORLD', 230, 100, white)
    showtext('Select an option:', 230, 160, white)
    showtext('1. Start', 250, 220, white)
    showtext('2. HighScore', 250, 270, white)
    showtext('3. Exit', 250, 320, white)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            if event.key == K_1:
                startGame()
            if event.key == K_2:
                print('user pressed high scores')
                showHighScores()
            if event.key == K_3:
                pygame.quit()
                exit()

def startGame():
    start = True
    while True:
    
        pygame.display.update()
        showMenu()
        screen.fill(black)
        clock.tick(10)
        
        # print(snake.snakelist)
        snake.moveSnake()

        if snake.snakelist[0] in snake.snakelist[1:]: 
            print(snake.snakelist, len(snake.snakelist))
            print('you ran into yourself')
            showtext(f'Your Score: {len(snake.snakelist)}!', 230, 30, white)
            insertIntoTable(len(snake.snakelist))
            showMenu()
            break

        snake.eatFood()
        snake.updateSnake()
        food.drawFood()

        #wall condition
        if snake.snakelist[0][0] >= 600:
            snake.snakelist[0][0] = 590
            print(snake.snakelist, len(snake.snakelist))

            showtext(f'Your Score: {len(snake.snakelist)}!', 230, 30, white)

            showMenu()
            break


        if snake.snakelist[0][0] <= 0:
            snake.snakelist[0][0] = 10
            print(snake.snakelist, len(snake.snakelist))

            showtext(f'Your Score: {len(snake.snakelist)}!', 230, 30, white)

            showMenu()

            break

        if snake.snakelist[0][1] <= 0:
            snake.snakelist[0][1] = 10
            print(snake.snakelist, len(snake.snakelist))

            showtext(f'Your Score: {len(snake.snakelist)}!', 230, 30, white)

            showMenu()

            break

        if snake.snakelist[0][1] >= 600:
            snake.snakelist[0][1] = 590
            print(snake.snakelist, len(snake.snakelist))

            showtext(f'Your Score: {len(snake.snakelist)}!', 230, 30, white)

            showMenu()

            break
        
            

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print('user quit')
                pygame.quit()
                exit()
            if event.type == KEYDOWN:
                
                if event.key == K_DOWN:
                    snake.xMotion = 0
                    snake.yMotion = 10

                if event.key == K_UP:
                    snake.xMotion = 0
                    snake.yMotion = -10

                if event.key == K_LEFT:
                    snake.xMotion = -10
                    snake.yMotion = 0

                if event.key == K_RIGHT:
                    snake.xMotion = 10
                    snake.yMotion=0

def showHighScores():
    screen.fill(black)
    pygame.display.update()
    showtext('HIGH SCORES', 30, 100, red)
    showtext('1. '+ 'hs', 30, 140, red)
    showtext('2. ', 30, 170, red)
    showtext('3. ', 30, 200, red)
    showtext('4. ', 30, 230, red)
    showtext('5. ', 30, 260, red)

    #displays highest 5 scores
    c.execute('SELECT * FROM highScores WHERE score')
    getRows = c.fetchall()
    for row in getRows: 
        print(row)


# def createTable():
#     c.execute("SELECT count(scores) FROM sqlite_master WHERE type='table' AND name='highScores'")

#     #if the count is 1, then table exists
#     if c.fetchone()[0]==1 : {
# 	    print('Table exists.')
#     } 
#     else:
#         c.execute('CREATE TABLE highScores(scores integer)')

def insertIntoTable(playerScore):
    c.execute("SELECT count(scores) FROM sqlite_master WHERE type='table' AND name='highScores'")

    #if the count is 1, then table exists
    if c.fetchone()[0]==1 : {
	    print('Table exists.')
    } 
    else:
        c.execute('CREATE TABLE highScores(scores integer)')
    #inserts scores into table
    c.execute("INSERT INTO highScores(scores integer) VALUES (?)",(playerScore))
    
    rows = c.fetchall()
    print(rows)
        

class Snake():
    def __init__(self):
        self.x = (random.randint(0, 600) // 10) * 10
        self.y = (random.randint(0, 600) // 10) * 10
        self.color = green
        self.xMotion = 0
        self.yMotion = 0
        self.snakelist = [[self.x, self.y]]
        self.playerScore = len(self.snakelist)

    def moveSnake(self):
        self.snakelist[0][0] += self.xMotion
        self.snakelist[0][1] += self.yMotion

    def eatFood(self):
        if self.snakelist[0][0] in range (food.x, food.x + 10) and self.snakelist[0][1] in range (food.y, food.y + 10):
            self.snakelist.insert(0,[food.x, food.y])

            print('food in contact with snake')
            print(self.snakelist)

            food.updateFoodPosition()
           
    def updateSnake(self):
        for each in self.snakelist:
            pygame.draw.rect(screen,self.color,(each[0],each[1],10,10),0)
        self.snakelist.insert(0,([self.snakelist[0][0],self.snakelist[0][1]]))
        self.snakelist.pop()
            

snake = Snake()

class Food():
    def __init__(self):
        self.x = (random.randint(20, 580) // 10) * 10
        self.y = (random.randint(20, 580) // 10) * 10
        self.color = red

    def drawFood(self):
        pygame.draw.rect(screen, self.color, (self.x, self.y, 10, 10), 0)

    def updateFoodPosition(self):
        self.x = (random.randint(20,580) // 10 ) * 10
        self.y = (random.randint(20,580) // 10 ) * 10


food = Food()

while True:
    if start == False:
        showMenu()
        
    if start == True:
        startGame()
       



