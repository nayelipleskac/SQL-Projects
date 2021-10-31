#Snake Pygame

import pygame, random, time 
from pygame.locals import *
import sqlite3
conn = sqlite3.connect('myDatabase.db')
c = conn.cursor()

pygame.init() #start pygame
screen = pygame.display.set_mode((600,600))
pygame.display.set_caption("Snake!!")
clock = pygame.time.Clock()


red = (255,0,0)
green = (0, 255,0)
white = (255,255,255)
black = (0,0,0)

foodx =(random.randint(20,580) // 10 ) * 10
foody =(random.randint (20,580) // 10 ) * 10

snakex = (random.randint(0,600) // 10 ) * 10
snakey = (random.randint(0,600) // 10 ) * 10

xMotion = 0
yMotion = 0

snakelist = []
snakelist.append([snakex,snakey])
userScore = len(snakelist)

#showtext

def showtext(msg,x,y,color):
    font = pygame.font.SysFont("freesans", 32)
    msgobj = font.render(msg,False,white)
    screen.blit(msgobj,(x,y))

def scoreTracker(userScore):
    c.execute(" SELECT count(userScore) FROM sqlite_master WHERE type='table' AND name='scoreTracker' ")

    #if the count is 1, then table exists
    if c.fetchone()[0]==1 : {
	print('Table exists.')
    } 
    else:
        c.execute('CREATE TABLE scoreTracker(name text, userName text, password text)') #creates table scoreTracker
    c.execute("INSERT INTO scoreTracker(score) VALUES (?)",(userScore)) #inserts one row
    conn.commit()

def showMenu():
    showtext('SNAKE WORLD', 250, 150, white)
    showtext('select an option: ', 250, 200, white)
    showtext('1. start 2. highscore 3. exit')

def startGame():
    pass

def showHighScores():
    showtext('HIGH SCORES')
    c.execute('SELECT * FROM signUpUser WHERE userName = ? and password = ?', (userScore)) #verifies userName / password in signUpUser



while True:
   
    pygame.display.update()
    screen.fill(black)
    # create Menu

    pygame.draw.rect(screen,red,(foodx,foody,10,10),0)
    
    snakelist.insert(0,([snakelist[0][0],snakelist[0][1]]))
    
    for each in snakelist:
        pygame.draw.rect(screen,green,(each[0],each[1],10,10),0)
    snakelist.pop()
    snakelist[0][0]+=xMotion
    snakelist[0][1]+=yMotion

    #Game over condition
    if snakelist[0] in snakelist[1:]:
        print('snakelist:', snakelist)
        print('snakelist[1:]', snakelist[1:])
        showtext("GAME OVER.", 250,100, white)
        print('head co. were already in list')
        break

    clock.tick(10)

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


    #eating food
    if snakelist[0][0] in range (foodx,foodx + 10) and snakelist[0][1] in range (foody,foody + 10):
        
          snakelist.insert(0,[foodx,foody])
          foodx = (random.randint(20,580) // 10 ) * 10
          foody = (random.randint(20,580) // 10 ) * 10

     
    for event in pygame.event.get():
        
        if event.type == QUIT:
            pygame.quit()
            exit()
            
        #movement
        elif event.type == KEYDOWN:
            if event.key == K_DOWN:
                yMotion = 10
                xMotion = 0
               

            if event.key == K_UP:
                yMotion = -10
                xMotion = 0

        
            if event.key == K_LEFT:
                xMotion = -10
                yMotion = 0

       
            if event.key == K_RIGHT:
                xMotion = 10
                yMotion=0
            if event.key == K_1:
                pass
                #start
            if event.key == K_2:
                showtext()
            if event.key == K_3:
                break


           
