import pygame
import sys
import math
import json

with open("CharacterDataSheet.json", "r") as file:
    data = json.load(file)

pygame.init()

WIDTH,HEIGHT = 1250,750

screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Battle Class")
clock = pygame.time.Clock()

#Colors
WHITE = (255,255,255)
BLACK = (0,0,0)
BLUE = (50,150,255)
GREEN = (50,200,50)
RED = (255,0,0)
PURPLE = (128,0,128)
ORANGE = (255, 165, 0)

#Variables
FrameRate = 60

UnitCount = 50
UnitY = HEIGHT - 25
UnitX = [0] * UnitCount
UnitType = [0] * UnitCount
UnitAnimation = [1] * UnitCount

EnemyCount = 50
EnemyY = HEIGHT - 25
EnemyX = [WIDTH] * EnemyCount
EnemyType = [0] * EnemyCount
EnemyAnimation = [1] * EnemyCount

UnitX[0] = 1 #temp
EnemyX[0] = WIDTH - 1


#Defs
def Draw():
    global data, UnitX, UnitType, UnitAnimation
    screen.fill(WHITE)
    #pygame.draw.rect(screen,BLACK,(0,0,100,100))
    
    for i in range(UnitCount):
        if UnitX[i] > 0:
            
            pygame.draw.rect(screen,BLACK,(UnitX[i] - data["Units"][UnitType[i]]["UnitSize"],UnitY - data["Units"][UnitType[i]]["UnitSize"],data["Units"][UnitType[i]]["UnitSize"],data["Units"][UnitType[i]]["UnitSize"]))
    for i in range(EnemyCount):
        if EnemyX[i] < WIDTH:
            
            pygame.draw.rect(screen,BLACK,(EnemyX[i],EnemyY - data["Enemy"][EnemyType[i]]["EnemySize"],data["Enemy"][EnemyType[i]]["EnemySize"],data["Enemy"][EnemyType[i]]["EnemySize"]))
            

def UnitOperations():
    global data, UnitX, UnitType, UnitAnimation
    for i in range(UnitCount):
        if abs(UnitX[i] - FrontmostEnemy()) > data["Units"][UnitType[i]]["UnitRange"] and UnitX[i] > 0:
            
            UnitX[i] += data["Units"][UnitType[i]]["UnitSpeed"]*24/FrameRate
            UnitAnimation[i] += 1 if UnitAnimation[i] == data["Units"][UnitType[i]]["UnitWalkFrames"] else 1 - data["Units"][UnitType[i]]["UnitWalkFrames"]

def EnemyOperations():   
    global data, EnemyX, EnemyType, EnemyAnimation
    for i in range(EnemyCount):
        if abs(EnemyX[i] - FrontmostUnit()) > data["Enemy"][EnemyType[i]]["EnemyRange"] and EnemyX[i] < WIDTH:
            EnemyX[i] -= data["Enemy"][EnemyType[i]]["EnemySpeed"]*24/FrameRate
            EnemyAnimation[i] += 1 if EnemyAnimation[i] == data["Enemy"][EnemyType[i]]["EnemyWalkFrames"] else 1 - data["Enemy"][EnemyType[i]]["EnemyWalkFrames"]
def FrontmostUnit():
    global UnitX
    FrontmostX = UnitX[0]
    for i in range(UnitCount):
        if UnitX[i] > FrontmostX:
            FrontmostX = UnitX[i]
    return FrontmostX

def FrontmostEnemy():
    global EnemyX
    FrontmostEnemyX = EnemyX[0]
    for i in range(EnemyCount):
        if EnemyX[i] < FrontmostEnemyX:
            FrontmostEnemyX = EnemyX[i]
    return FrontmostEnemyX





running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    UnitOperations()
    EnemyOperations()
    Draw()
    keys = pygame.key.get_pressed()
    pygame.display.flip()
    pygame.display.update()
    clock.tick(FrameRate)
pygame.quit()
sys.exit()