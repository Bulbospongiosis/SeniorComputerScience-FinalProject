import pygame
import sys
import math
import json
from logic import UnitOperations, EnemyOperations
from visuals import Draw
from spawn import Button

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

Money = 0


#images
UnitButton = pygame.image.load('__Pngs__/cat.png').convert_alpha()





running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    UnitOperations(UnitCount,UnitX,data,UnitType,UnitAnimation,FrameRate,EnemyCount,EnemyX)
    EnemyOperations(EnemyCount,EnemyX,data,EnemyType,EnemyAnimation,FrameRate,UnitCount,UnitX)
    Draw(screen,data,UnitX,UnitType,UnitAnimation,EnemyX,UnitY,EnemyY,EnemyType,UnitCount,EnemyCount)
    Button(screen,UnitButton)
    keys = pygame.key.get_pressed()
    pygame.display.flip()
    pygame.display.update()
    clock.tick(FrameRate)
pygame.quit()
sys.exit()