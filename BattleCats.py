import pygame
import os
import sys
import math
import json
from logic import UnitOperations, EnemyOperations
from visuals import Draw, DrawButtons


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
UnitY = HEIGHT - 250
UnitX = [0] * UnitCount
UnitType = [0] * UnitCount
UnitAnimation = [1] * UnitCount
Cooldown = [999999999999999999] * 10
AssignedButtonTypes = [1,1,1,1,1,1,1,0,0,0]
ButtonError = [False] * 10
ErrorCooldown = [0] * 10

EnemyCount = 50
EnemyY = HEIGHT - 250
EnemyX = [WIDTH] * EnemyCount
EnemyType = [0] * EnemyCount
EnemyAnimation = [1] * EnemyCount


EnemyX[0] = WIDTH - 1

Money = 0

NextAvailableUnit = 0
NextAvailableEnemy = 0




#images

UnitButtonSetup = [pygame.transform.scale(pygame.image.load('__Pngs__/cat.png').convert_alpha(), (150, 100)),
                   pygame.transform.scale(pygame.image.load('__Pngs__/cat.png').convert_alpha(), (150, 100)),
                   pygame.transform.scale(pygame.image.load('__Pngs__/cat.png').convert_alpha(), (150, 100)),
                   pygame.transform.scale(pygame.image.load('__Pngs__/cat.png').convert_alpha(), (150, 100)),
                   pygame.transform.scale(pygame.image.load('__Pngs__/cat.png').convert_alpha(), (150, 100)),
                   pygame.transform.scale(pygame.image.load('__Pngs__/cat.png').convert_alpha(), (150, 100)),
                   pygame.transform.scale(pygame.image.load('__Pngs__/cat.png').convert_alpha(), (150, 100)),
                   pygame.transform.scale(pygame.image.load('__Pngs__/cat.png').convert_alpha(), (150, 100)),
                   pygame.transform.scale(pygame.image.load('__Pngs__/cat.png').convert_alpha(), (150, 100)),
                   pygame.transform.scale(pygame.image.load('__Pngs__/cat.png').convert_alpha(), (150, 100)),]
UnitButton = [UnitButtonSetup[0].get_rect(topleft=(100 + 25, 500 + 25)),
              UnitButtonSetup[0].get_rect(topleft=(250 + 25, 500 + 25)),
              UnitButtonSetup[0].get_rect(topleft=(400 + 25, 500 + 25)),
              UnitButtonSetup[0].get_rect(topleft=(550 + 25, 500 + 25)),
              UnitButtonSetup[0].get_rect(topleft=(700 + 25, 500 + 25)),
              UnitButtonSetup[0].get_rect(topleft=(100 + 25, 600 + 25)),
              UnitButtonSetup[0].get_rect(topleft=(250 + 25, 600 + 25)),
              UnitButtonSetup[0].get_rect(topleft=(400 + 25, 600 + 25)),
              UnitButtonSetup[0].get_rect(topleft=(550 + 25, 600 + 25)),
              UnitButtonSetup[0].get_rect(topleft=(700 + 25, 600 + 25))
              ]




def Button(position,numberclicked,unicode):
    global UnitX, NextAvailableUnit, UnitButton, Cooldown, data, AssignedButtonTypes, FrameRate, Money, ButtonError, ErrorCooldown
    for i in range(len(UnitButton)):
        if ErrorCooldown[i] <= 0 and (UnitButton[i].collidepoint(position) or (numberclicked and (unicode -1 == i or unicode + 9 == i))) and Cooldown[i] >= data["Units"][AssignedButtonTypes[i]]["UnitCooldown"] * FrameRate and UnitX[NextAvailableUnit] == 0 and Money >= data["Units"][AssignedButtonTypes[i]]["UnitPrice"]:
            UnitX[NextAvailableUnit] = 1
            UnitType[NextAvailableUnit] = AssignedButtonTypes[i]
            Cooldown[i] = 0
            NextAvailableUnit = 0
            Money -= data["Units"][AssignedButtonTypes[i]]["UnitPrice"]
            while True:
                if UnitX[NextAvailableUnit] == 0:
                    break
                else:
                    NextAvailableUnit += 1
        else:
            if (UnitButton[i].collidepoint(position) or (numberclicked and (unicode -1 == i or unicode + 9 == i))):
                ButtonError[i] = True
                ErrorCooldown[i] = 0.15 * FrameRate
                


def Cooldowns():
    global Cooldown, Money, data, AssignedButtonTypes, ButtonError, FrameRate
    Money += 200/FrameRate
    for i in range(len(Cooldown)):
        Cooldown[i] += 1
        if ButtonError[i] == True:
            ErrorCooldown[i] -= 1
            if ErrorCooldown[i] <= 0:
                ButtonError[i] = False
    

    
            

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONUP:
            Button(pygame.mouse.get_pos(),False,-1000)
        if event.type == pygame.KEYDOWN:
            if event.unicode.isdigit():
                Button((-100,-100),True,int(event.unicode))


    UnitOperations(UnitCount,UnitX,data,UnitType,UnitAnimation,FrameRate,EnemyCount,EnemyX)
    EnemyOperations(EnemyCount,EnemyX,data,EnemyType,EnemyAnimation,FrameRate,UnitCount,UnitX)
    Draw(screen,data,UnitX,UnitType,UnitAnimation,EnemyX,UnitY,EnemyY,EnemyType,UnitCount,EnemyCount)
    DrawButtons(screen,UnitButton,UnitButtonSetup,ButtonError,Cooldown,data,FrameRate,AssignedButtonTypes)
    Cooldowns()
    keys = pygame.key.get_pressed()
    pygame.display.flip()
    pygame.display.update()
    clock.tick(FrameRate)
pygame.quit()
sys.exit()