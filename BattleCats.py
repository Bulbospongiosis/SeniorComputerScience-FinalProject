import pygame
import os
import sys
import math
import json
from logic import UnitOperations, EnemyOperations
from visuals import Draw, DrawButtons, textplacement


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
UnitY = HEIGHT - 275
UnitX = [0] * UnitCount
UnitType = [0] * UnitCount
UnitAnimation = [0] * UnitCount
UnitAtkAnimation = [0] * UnitCount
UnitCooldown = [0] * UnitCount
UnitHealth = [0] * UnitCount
Cooldown = [999999999999999999] * 10
AssignedButtonTypes = [0,0,0,0,0,0,0,0,0,0]
ButtonError = [False] * 10
ErrorCooldown = [0] * 10
JewButtonError = False
JewErrorCooldown = 0

EnemyCount = 50
EnemyY = HEIGHT - 275
EnemyX = [WIDTH] * EnemyCount
EnemyType = [0] * EnemyCount
EnemyAnimation = [1] * EnemyCount
EnemyAtkAnimation = [0] * EnemyCount
EnemyCooldown = [0] * EnemyCount
EnemyHealth = [0] * EnemyCount


EnemyX[0] = WIDTH - 10
EnemyHealth[0] = 100

Money = 0
BaseMoneySpeed = 170
MoneyLimit = 4500
JewButtonLevel = 1

NextAvailableUnit = 0
NextAvailableEnemy = 0




#images
DogHouse = pygame.transform.scale(pygame.image.load('__Pngs__/doghouse.png').convert_alpha(), (HEIGHT/1.5, HEIGHT/1.5))

JewButtonSetup = pygame.transform.scale(pygame.image.load('__Pngs__/JewButton.png').convert_alpha(), (240, 240))
JewButton = JewButtonSetup.get_rect(topleft=(900,500))
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
UnitButton = [UnitButtonSetup[AssignedButtonTypes[0]].get_rect(topleft=(100 + 25, 500 + 25)),
              UnitButtonSetup[AssignedButtonTypes[1]].get_rect(topleft=(250 + 25, 500 + 25)),
              UnitButtonSetup[AssignedButtonTypes[2]].get_rect(topleft=(400 + 25, 500 + 25)),
              UnitButtonSetup[AssignedButtonTypes[3]].get_rect(topleft=(550 + 25, 500 + 25)),
              UnitButtonSetup[AssignedButtonTypes[4]].get_rect(topleft=(700 + 25, 500 + 25)),
              UnitButtonSetup[AssignedButtonTypes[5]].get_rect(topleft=(100 + 25, 600 + 25)),
              UnitButtonSetup[AssignedButtonTypes[6]].get_rect(topleft=(250 + 25, 600 + 25)),
              UnitButtonSetup[AssignedButtonTypes[7]].get_rect(topleft=(400 + 25, 600 + 25)),
              UnitButtonSetup[AssignedButtonTypes[8]].get_rect(topleft=(550 + 25, 600 + 25)),
              UnitButtonSetup[AssignedButtonTypes[9]].get_rect(topleft=(700 + 25, 600 + 25))
              ]

JohnWalk = [pygame.transform.scale(pygame.image.load('__Pngs__/cat.png').convert_alpha(), (data["Units"][0]["UnitSize"], 2 * data["Units"][0]["UnitSize"])),
            pygame.transform.scale(pygame.image.load('__Pngs__/cat.png').convert_alpha(), (data["Units"][0]["UnitSize"], 2 * data["Units"][0]["UnitSize"]))]
JohnAtk = [pygame.transform.scale(pygame.image.load('__Pngs__/cat.png').convert_alpha(), (data["Units"][0]["UnitSize"], 2 * data["Units"][0]["UnitSize"])),
           pygame.transform.scale(pygame.image.load('__Pngs__/cat.png').convert_alpha(), (data["Units"][0]["UnitSize"], 2 * data["Units"][0]["UnitSize"]))]

WalkAnimations = [JohnWalk]
AtkAnimations = [JohnAtk]




DogTroopWalk = [pygame.transform.scale(pygame.image.load('__Pngs__/cat.png').convert_alpha(), (data["Enemy"][0]["EnemySize"], 2 * data["Enemy"][0]["EnemySize"])),
            pygame.transform.scale(pygame.image.load('__Pngs__/cat.png').convert_alpha(), (data["Enemy"][0]["EnemySize"], 2 * data["Enemy"][0]["EnemySize"]))]
DogTroopAtk = [pygame.transform.scale(pygame.image.load('__Pngs__/cat.png').convert_alpha(), (data["Enemy"][0]["EnemySize"], 2 * data["Enemy"][0]["EnemySize"])),
           pygame.transform.scale(pygame.image.load('__Pngs__/cat.png').convert_alpha(), (data["Enemy"][0]["EnemySize"], 2 * data["Enemy"][0]["EnemySize"]))]

EnemyWalkAnimations = [DogTroopWalk]
EnemyAtkAnimations = [DogTroopAtk]



def Button(position,numberclicked,unicode):
    global JewButtonError, JewButtonLevel, JewButton, JewErrorCooldown, UnitX, NextAvailableUnit, UnitButton, Cooldown, data, AssignedButtonTypes, FrameRate, Money, ButtonError, ErrorCooldown, MoneyLimit
    for i in range(len(UnitButton)):
        if ErrorCooldown[i] <= 0 and (UnitButton[i].collidepoint(position) or (numberclicked and (unicode -1 == i or unicode + 9 == i))) and Cooldown[i] >= data["Units"][AssignedButtonTypes[i]]["UnitCooldown"] * FrameRate and UnitX[NextAvailableUnit] == 0 and Money >= data["Units"][AssignedButtonTypes[i]]["UnitPrice"]:
            UnitX[NextAvailableUnit] = 1
            UnitType[NextAvailableUnit] = AssignedButtonTypes[i]
            Cooldown[i] = 0
            
            Money -= data["Units"][AssignedButtonTypes[i]]["UnitPrice"]
            UnitHealth[NextAvailableUnit] = data["Units"][AssignedButtonTypes[i]]["UnitHealth"]
            UnitCooldown[NextAvailableUnit] = 0
            NextAvailableUnit += 1
            while True:
                if UnitX[NextAvailableUnit] == 0:
                    break
                else:
                    if NextAvailableUnit != UnitCount -1:
                        NextAvailableUnit += 1
                    else:
                        break
        else:
            if (UnitButton[i].collidepoint(position) or (numberclicked and (unicode -1 == i or unicode + 9 == i))):
                ButtonError[i] = True
                ErrorCooldown[i] = 0.15 * FrameRate
    if JewButton.collidepoint(position) and Money >= MoneyLimit - 1500 and JewButtonLevel < 8:
        Money -= MoneyLimit - 1500
        MoneyLimit += 1500
        JewButtonLevel += 1
    else:
        if JewButton.collidepoint(position):
            JewButtonError = True
            JewErrorCooldown = 0.15 * FrameRate


                


def Cooldowns():
    global Cooldown, Money, data, AssignedButtonTypes, ButtonError, FrameRate, JewButtonError, JewErrorCooldown
    if Money < MoneyLimit:
        Money += (BaseMoneySpeed*MoneyLimit)/(FrameRate*4500)
    else:
        Money = MoneyLimit
    for i in range(len(Cooldown)):
        Cooldown[i] += 1
        if ButtonError[i] == True:
            ErrorCooldown[i] -= 1
            if ErrorCooldown[i] <= 0:
                ButtonError[i] = False
    if JewButtonError == True:
        JewErrorCooldown -= 1
        if JewErrorCooldown <= 0:
            JewButtonError = False
    

    
           

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


    UnitOperations(UnitCount,UnitX,data,UnitType,UnitAnimation,FrameRate,EnemyCount,EnemyX,UnitCooldown,UnitAtkAnimation,UnitHealth,EnemyHealth,WalkAnimations,AtkAnimations)
    EnemyOperations(EnemyCount,EnemyX,data,EnemyType,EnemyAnimation,FrameRate,UnitCount,UnitX,UnitHealth,EnemyHealth,EnemyCooldown,EnemyAtkAnimation,EnemyWalkAnimations,EnemyAtkAnimations)
    Draw(screen,data,UnitX,UnitType,UnitAnimation,EnemyX,UnitY,EnemyY,EnemyType,UnitCount,EnemyCount,DogHouse)
    DrawButtons(screen,UnitButton,UnitButtonSetup,ButtonError,Cooldown,data,FrameRate,AssignedButtonTypes,JewButtonError,JewButtonSetup)
    Cooldowns()
    textplacement(screen,data,Money,MoneyLimit,JewButtonLevel)
    keys = pygame.key.get_pressed()
    pygame.display.flip()
    pygame.display.update()
    clock.tick(FrameRate)
pygame.quit()
sys.exit()