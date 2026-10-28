import pygame
import json
import os

with open("CharacterDataSheet.json", "r") as file:
    data = json.load(file)

if not pygame.get_init():
    pygame.init()
WIDTH,HEIGHT = 1250,750
screen = pygame.display.set_mode((WIDTH,HEIGHT))


class Enemy:
    
    DogTroopWalk = [pygame.transform.scale(pygame.image.load('__Pngs__/cat.png').convert_alpha(), (data["Enemy"][0]["EnemySize"], 2 * data["Enemy"][0]["EnemySize"])),
                    pygame.transform.scale(pygame.image.load('__Pngs__/cat.png').convert_alpha(), (data["Enemy"][0]["EnemySize"], 2 * data["Enemy"][0]["EnemySize"]))]
    DogTroopAtk = [pygame.transform.scale(pygame.image.load('__Pngs__/cat.png').convert_alpha(), (data["Enemy"][0]["EnemySize"], 2 * data["Enemy"][0]["EnemySize"])),
                    pygame.transform.scale(pygame.image.load('__Pngs__/cat.png').convert_alpha(), (data["Enemy"][0]["EnemySize"], 2 * data["Enemy"][0]["EnemySize"]))]

    EnemyWalkAnimations = [DogTroopWalk]
    EnemyAtkAnimations = [DogTroopAtk]
    
    
    def __init__(self):
        self.EnemyX = WIDTH
        self.EnemyType = 0
        self.EnemyAnimation = 0
        self.EnemyAtkAnimation = 0
        self.EnemyCooldown = 0
        self.EnemyHealth = 0

    def drawWalk(self):
        return self.EnemyWalkAnimation[self.EnemyType][self.EnemyAnimation]
    def drawAtk(self):
        return self.EnemyAtkAnimation[self.EnemyType][self.EnemyAnimation]
    def drawStand(self):
        return self.EnemyAtkAnimation[self.EnemyType][0]