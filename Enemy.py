import pygame
import json
import os
import random

with open("CharacterDataSheet.json", "r") as file:
    data = json.load(file)

if not pygame.get_init():
    pygame.init()
WIDTH,HEIGHT = 1250,750
screen = pygame.display.set_mode((WIDTH,HEIGHT))


class Enemy:
    
    DogTroopWalk = [pygame.transform.scale(pygame.image.load('__Pngs__/cat.png').convert_alpha(), (data["Enemy"][0]["EnemySize"], data["Enemy"][0]["EnemySize"])),
                    pygame.transform.scale(pygame.image.load('__Pngs__/cat.png').convert_alpha(), (data["Enemy"][0]["EnemySize"], data["Enemy"][0]["EnemySize"]))]
    DogTroopAtk = [pygame.transform.scale(pygame.image.load('__Pngs__/cat.png').convert_alpha(), (data["Enemy"][0]["EnemySize"], data["Enemy"][0]["EnemySize"])),
                    pygame.transform.scale(pygame.image.load('__Pngs__/cat.png').convert_alpha(), (data["Enemy"][0]["EnemySize"], data["Enemy"][0]["EnemySize"]))]
    DogTroopPost = [pygame.transform.scale(pygame.image.load('__Pngs__/cat.png').convert_alpha(), (data["Enemy"][0]["EnemySize"], data["Enemy"][0]["EnemySize"])),
                    pygame.transform.scale(pygame.image.load('__Pngs__/cat.png').convert_alpha(), (data["Enemy"][0]["EnemySize"], data["Enemy"][0]["EnemySize"]))]

    
    EnemyWalkAnimations = [DogTroopWalk]
    EnemyAtkAnimations = [DogTroopAtk]
    EnemyPostAnimations = [DogTroopPost]

    def __init__(self,data):
        self.EnemyX = WIDTH
        self.EnemyType = 0
        self.EnemyAnimation = 0
        self.EnemyAtkAnimation = 0
        self.EnemyPostAnimation = 99999999
        self.EnemyCooldown = 0
        self.EnemyHealth = 0
        self.FrameRate = 60
        self.Range = data["Enemy"][self.EnemyType]["EnemyRange"] + random.randint(-2, 2)

    def drawWalk(self):
        frame_idx = int(self.EnemyAnimation * 12 / self.FrameRate) % len(self.EnemyWalkAnimations[self.EnemyType])
        return self.EnemyWalkAnimations[self.EnemyType][frame_idx]

    def drawAtk(self):
        frame_idx = int(self.EnemyAtkAnimation * 12 / self.FrameRate) % len(self.EnemyAtkAnimations[self.EnemyType])
        return self.EnemyAtkAnimations[self.EnemyType][frame_idx]

    def drawPost(self):
        frame_idx = int(self.EnemyPostAnimation * 12 / self.FrameRate) % len(self.EnemyPostAnimations[self.EnemyType])
        return self.EnemyPostAnimations[self.EnemyType][frame_idx]

    def drawStand(self):
        return self.EnemyAtkAnimations[self.EnemyType][0]

    def spawn(self):
        self.Range = data["Enemy"][self.EnemyType]["EnemyRange"] + random.randint(-2, 2)
