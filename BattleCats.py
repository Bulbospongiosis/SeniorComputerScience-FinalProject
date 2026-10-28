import pygame
import os
import sys
import math
import json
from logic import UnitOperations, EnemyOperations
from visuals import Draw, DrawButtons, textplacement
from menu import menuappear
from Unit import Unit
from Enemy import Enemy


with open("CharacterDataSheet.json", "r") as file:
    data = json.load(file)

pygame.init()
pygame.mixer.init()

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
UnitBaseHealth = 5000
UnitY = HEIGHT - 275
Units = []
for i in range(UnitCount):
    Units.append(Unit())

Cooldown = [999999999999999999] * 10
AssignedButtonTypes = [0,0,0,0,0,0,0,0,0,0]
ButtonError = [False] * 10
ErrorCooldown = [0] * 10
JewButtonError = False
JewErrorCooldown = 0

EnemyCount = 50
EnemyBaseHealth = 5000
EnemyY = HEIGHT - 275
Enemies = []
for i in range(EnemyCount):
    Enemies.append(Enemy())



Money = 0
BaseMoneySpeed = 170
MoneyLimit = 4500
JewButtonLevel = 1

NextAvailableUnit = 0
NextAvailableEnemy = 0


menu = True

Level = "Hell"


#sounds


#images
background = pygame.transform.scale(pygame.image.load('__Pngs__/cat.png').convert_alpha(), (WIDTH,HEIGHT))
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









def Button(position,numberclicked,unicode):
    global JewButtonError, JewButtonLevel, JewButton, JewErrorCooldown, NextAvailableUnit, UnitButton, Cooldown, data, AssignedButtonTypes, FrameRate, Money, ButtonError, ErrorCooldown, MoneyLimit
    for i in range(len(UnitButton)):
        if ErrorCooldown[i] <= 0 and (UnitButton[i].collidepoint(position) or (numberclicked and (unicode -1 == i or unicode + 9 == i))) and Cooldown[i] >= data["Units"][AssignedButtonTypes[i]]["UnitCooldown"] * FrameRate and Units[NextAvailableUnit].UnitX == 0 and Money >= data["Units"][AssignedButtonTypes[i]]["UnitPrice"]:
            Units[NextAvailableUnit].UnitX = 1
            Units[NextAvailableUnit].UnitType = AssignedButtonTypes[i]
            Cooldown[i] = 0

            Money -= data["Units"][AssignedButtonTypes[i]]["UnitPrice"]
            Units[NextAvailableUnit].UnitHealth = data["Units"][AssignedButtonTypes[i]]["UnitHealth"]
            Units[NextAvailableUnit].UnitCooldown = 0
            NextAvailableUnit += 1
            while True:
                if Units[NextAvailableUnit].UnitX == 0:
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

def PlayMusic():
    if Level == "Hell":
        pygame.mixer.music.load('__SFX__/theme.mp3')

    pygame.mixer.music.play(-1)

def StatReset():
    global Cooldown, ButtonError, ErrorCooldown, Money, BaseMoneySpeed, MoneyLimit, JewButtonLevel, NextAvailableUnit, NextAvailableEnemy
    for i in range(UnitCount):
        Units[i].UnitX = 0
        Units[i].UnitHealth = 0
        Units[i].UnitType = 0
        Units[i].UnitAnimation = 0
        Units[i].UnitAtkAnimation = 0
        Units[i].UnitCooldown = 0
    Cooldown = [999999999999999999] * 10
    ButtonError = [False] * 10
    ErrorCooldown = [0] * 10

    for i in range(EnemyCount):
        Enemies[i].EnemyX = WIDTH
        Enemies[i].EnemyCooldown = 0
        Enemies[i].EnemyHealth = 0
        Enemies[i].EnemyType = 0
        Enemies[i].EnemyAnimation = 0
        Enemies[i].EnemyAtkAnimation = 0

    Money = 0
    BaseMoneySpeed = 170
    MoneyLimit = 4500
    JewButtonLevel = 1

    NextAvailableUnit = 0
    NextAvailableEnemy = 0

    Enemies[0].EnemyX = WIDTH - 10
    Enemies[0].EnemyHealth = data["Enemy"][Enemies[i].EnemyType]["EnemyHealth"]
    Enemies[0].EnemyType = 0


PlayMusic()
StatReset()       
menu = False
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


    if not menu:
        pygame.mixer.music.unpause()
        UnitOperations(UnitCount,Units,data,FrameRate,EnemyCount,Enemies,EnemyBaseHealth)
        Money = EnemyOperations(EnemyCount,Enemies,data,FrameRate,UnitCount,Units,UnitBaseHealth,Money)
        Draw(screen,data,Units,Enemies,UnitY,EnemyY,UnitCount,EnemyCount,DogHouse)
        DrawButtons(screen,UnitButton,UnitButtonSetup,ButtonError,Cooldown,data,FrameRate,AssignedButtonTypes,JewButtonError,JewButtonSetup)
        Cooldowns()
        textplacement(screen,data,Money,MoneyLimit,JewButtonLevel)

    else:
        pygame.mixer.music.pause()
        StatReset()
        menuappear(AssignedButtonTypes,data,screen,background)
    keys = pygame.key.get_pressed()
    pygame.display.flip()
    pygame.display.update()
    clock.tick(FrameRate)
pygame.quit()
pygame.mixer.quit()
sys.exit()