
# @Author: Xinyi li
# @File: snake.py
# @Time: 2019/9/19
# @Contact: lixinyi2019uk@163.com
# @Description: Gluttonous Snake
# @Python Version: 3.7.5


import pygame
import sys
import time
import random
from pygame.locals import *

# Define needed colors
blackcolor = pygame.Color(0,0,0)
whitecolor = pygame.Color(255,255,255) 
redcolor = pygame.Color(255,0,0)

# Initiate variables
totaltime = pygame.time.Clock()
gameNum = 0
#mode = 0

# Define interface while gameover
def gameover(playSurf):
    gameoverFont = pygame.font.SysFont('microsoftsansserif',50)
    gameoverSurf = gameoverFont.render('Game is over',True,redcolor)
    gameoverRect = gameoverSurf.get_rect()
    gameoverRect.center = (400,300)
    playSurf.blit(gameoverSurf,gameoverRect)
    pygame.display.flip()
    time.sleep(1)
    menu(gameNum,totaltime)

# Define difficulties-including easy, middle and hard modes
def difficulty(totaltime): 
    capFont = pygame.font.SysFont('microsoftsansserif',40)
    capSurf = capFont.render('Gluttonous Snake',True,whitecolor)
    capRect = capSurf.get_rect()
    capRect.center = (400,150)
    
    mode_easyFont = pygame.font.SysFont('microsoftsansserif',30)
    mode_easySurf = mode_easyFont.render('Easy',True,whitecolor)
    mode_easyRect = mode_easySurf.get_rect()
    mode_easyRect.center = (200,300)
    mode_midFont = pygame.font.SysFont('microsoftsansserif',30)
    mode_midSurf = mode_midFont.render('Middle',True,whitecolor)
    mode_midRect = mode_midSurf.get_rect()
    mode_midRect.center = (400,300)
    mode_hardFont = pygame.font.SysFont('microsoftsansserif',30)
    mode_hardSurf = mode_hardFont.render('Hard',True,whitecolor)
    mode_hardRect = mode_hardSurf.get_rect()
    mode_hardRect.center = (600,300)

    backFont = pygame.font.SysFont('microsoftsansserif',30)
    backSurf = backFont.render('Back',True,whitecolor)
    backRect = backSurf.get_rect()
    backRect.center = (400,400)
    
    modeSurf = pygame.display.set_mode((800,600))
    pygame.display.set_caption('Gluttonous Snake')
    
    #global mode

    while True:
        modeSurf.blit(capSurf,capRect)
        modeSurf.blit(mode_easySurf,mode_easyRect)
        modeSurf.blit(mode_midSurf,mode_midRect)
        modeSurf.blit(mode_hardSurf,mode_hardRect)
        modeSurf.blit(backSurf,backRect)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONDOWN:
                if event.button == 1 and mode_easyRect.collidepoint(event.pos):
                    #mode = 5
                    main(5)
                elif event.button == 1 and mode_midRect.collidepoint(event.pos):
                    #mode = 10
                    main(10)
                elif event.button == 1 and mode_hardRect.collidepoint(event.pos):
                    #mode = 15
                    main(15)
                elif event.button == 1 and backRect.collidepoint(event.pos):
                    menu(gameNum,totaltime)                  

        totaltime.tick(10)
        
        
# Define interface while entering the game or while restarting the game 
def menu(gameNum,totaltime):
    pygame.init()
    capFont = pygame.font.SysFont('microsoftsansserif',40)
    capSurf = capFont.render('Gluttonous Snake',True,whitecolor)
    capRect = capSurf.get_rect()
    capRect.center = (400,150)
    
    startFont = pygame.font.SysFont('microsoftsansserif',30)
    startSurf = startFont.render('Start game',True,whitecolor)
    startRect = startSurf.get_rect()
    startRect.center = (400,300)
    restartFont = pygame.font.SysFont('microsoftsansserif',30)
    restartSurf = restartFont.render('Restart',True,whitecolor)
    restartRect = restartSurf.get_rect()
    restartRect.center = (400,300)
    endFont = pygame.font.SysFont('microsoftsansserif',30)
    endSurf = endFont.render('Exit',True,whitecolor)
    endRect = endSurf.get_rect()
    endRect.center = (400,400)
           
    menuSurf = pygame.display.set_mode((800,600))
    pygame.display.set_caption('Gluttonous Snake')
    #print(gameNum)
    

    while True:
        if gameNum > 0:
            menuSurf.blit(capSurf,capRect)
            menuSurf.blit(restartSurf,restartRect)
            menuSurf.blit(endSurf,endRect)
            pygame.display.flip()
        else:
            menuSurf.blit(capSurf,capRect)
            menuSurf.blit(startSurf,startRect)
            menuSurf.blit(endSurf,endRect)
            pygame.display.flip()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONDOWN:
                if event.button == 1 and (startRect.collidepoint(event.pos) or restartRect.collidepoint(event.pos)):
                    #print(mode)
                    difficulty(totaltime)                   
                elif event.button == 1 and endRect.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()

        totaltime.tick(10)





# Define "pause" button to pause the game in the process of playing
# Offer two choices: exit and return
def pause(playSurf,internaltime,paused,paused_rect):
    largeText = pygame.font.SysFont('microsoftsansserif',115)
    textSurf = largeText.render('Paused',True,redcolor)
    textRect = textSurf.get_rect()
    textRect.center = (400,200)
    playSurf.blit(textSurf,textRect)

    back_to_menuFont = pygame.font.SysFont('microsoftsansserif',60)
    back_to_menuSurf = back_to_menuFont.render('Back to Menu?',True,redcolor)
    back_to_menuRect = back_to_menuSurf.get_rect()
    back_to_menuRect.center = (400,350)
    playSurf.blit(back_to_menuSurf,back_to_menuRect)

    exitFont = pygame.font.SysFont('microsoftsansserif',60)
    exitSurf = exitFont.render('or Exit?',True,redcolor)
    exitRect = exitSurf.get_rect()
    exitRect.center = (400,450)
    playSurf.blit(exitSurf,exitRect)
 
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONDOWN:
                if event.button == 1 and paused_rect.collidepoint(event.pos):
                    paused = not paused  
                    #print(paused)
                    break   
                elif event.button == 1 and back_to_menuRect.collidepoint(event.pos):
                    menu(gameNum,totaltime)
                elif event.button == 1 and exitRect.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()

        pygame.display.flip()
        internaltime.tick(10)
        
# Define the whole game process-basic rules and control.
def main(mode):
    pygame.init()
    internaltime = pygame.time.Clock()
    playSurf = pygame.display.set_mode((800,600))
    pygame.display.set_caption('Gluttonous Snake')
    global gameNum
    gameNum = 1
    

    snakePos = [400,300]
    snakeSeg = [[400,300],[380,300],[360,300]]
    foodPos = [500,500]
    flag = 1
    direction = 'right'
    changedir = direction

    paused = False
    paused_image = pygame.image.load('pause_resume.png').convert_alpha()
    paused_rect = paused_image.get_rect()
    paused_rect.midtop = (775,0)

          
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONDOWN:
                if event.button == 1 and paused_rect.collidepoint(event.pos):
                    paused = not paused
                    #print(paused)
                    pause(playSurf,internaltime,paused,paused_rect) 
                    paused = not paused  
                                         
                else:
                    playSurf.fill(blackcolor)
                    playSurf.blit(paused_image,paused_rect)

                       
            elif event.type == KEYDOWN:
                if event.key == K_RIGHT or event.key == ord('d'):
                    changedir = 'right'
                elif event.key == K_LEFT or event.key == ord('a'):
                    changedir = 'left'
                elif event.key == K_UP or event.key == ord('w'):
                    changedir = 'up'
                elif event.key == K_DOWN or event.key == ord('s'):
                    changedir = 'down'
                elif event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
        if direction == 'right' and changedir != 'left':
            direction = changedir
        elif direction == 'left' and changedir != 'right':
            direction = changedir
        elif direction == 'up' and changedir != 'down':
            direction = changedir
        elif direction == 'down' and changedir != 'up':
            direction = changedir

        if direction == 'right':
            snakePos[0] += 20
        elif direction == 'left':
            snakePos[0] -= 20
        elif direction == 'up':
            snakePos[1] -= 20
        elif direction == 'down':
            snakePos[1] += 20

        snakeSeg.insert(0,list(snakePos))
        if snakePos[0] == foodPos[0] and  snakePos[1] == foodPos[1]:
            flag = 0
        else:
            snakeSeg.pop()

        if flag == 0:
            while foodPos in snakeSeg:
                x = random.randrange(1,40)
                y = random.randrange(1,30)
                foodPos = [int(x*20),int(y*20)]
            
        flag = 1
        playSurf.fill(blackcolor)
        playSurf.blit(paused_image,paused_rect)
        for position in snakeSeg:
            pygame.draw.rect(playSurf,whitecolor,Rect(position[0],position[1],20,20))
        pygame.draw.rect(playSurf,redcolor,Rect(snakePos[0],snakePos[1],20,20))
        pygame.draw.rect(playSurf,whitecolor,Rect(foodPos[0],foodPos[1],20,20))

        pygame.display.flip()
        if snakePos[0] > 780 or snakePos[0] < 0:
            gameover(playSurf)
            menu(gameNum,totaltime)
        elif snakePos[1] > 580 or snakePos[1] < 0:
            gameover(playSurf)
            menu(gameNum,totaltime)

        for body in snakeSeg[1:]:
            if snakePos[0] == body[0] and snakePos[1] == body[1]:
                gameover(playSurf)
                menu(gameNum,totaltime)

        internaltime.tick(mode)

if True:
    menu(gameNum,totaltime)
