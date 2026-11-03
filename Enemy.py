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
    
    DogTroopWalk = [pygame.transform.scale(pygame.image.load('__Pngs__/cat.png').convert_alpha(), (data["Enemy"][0]["EnemySize"], data["Enemy"][0]["EnemySize"])),
                    pygame.transform.scale(pygame.image.load('__Pngs__/cat.png').convert_alpha(), (data["Enemy"][0]["EnemySize"], data["Enemy"][0]["EnemySize"]))]
    DogTroopAtk = [pygame.transform.scale(pygame.image.load('__Pngs__/cat.png').convert_alpha(), (data["Enemy"][0]["EnemySize"], data["Enemy"][0]["EnemySize"])),
                    pygame.transform.scale(pygame.image.load('__Pngs__/cat.png').convert_alpha(), (data["Enemy"][0]["EnemySize"], data["Enemy"][0]["EnemySize"]))]

    EnemyWalkAnimations = [DogTroopWalk]
    EnemyAtkAnimations = [DogTroopAtk]
    
    
    def __init__(self):
        self.EnemyX = WIDTH
        self.EnemyType = 0
        self.EnemyAnimation = 0
        self.EnemyAtkAnimation = 0
        self.EnemyCooldown = 0
        self.EnemyHealth = 0
        self.FrameRate = 60

    def drawWalk(self):
        frame_idx = int(self.EnemyAnimation * 12 / self.FrameRate) % len(self.EnemyWalkAnimations[self.EnemyType])
        return self.EnemyWalkAnimations[self.EnemyType][frame_idx]

    def drawAtk(self):
        frame_idx = int(self.EnemyAtkAnimation * 12 / self.FrameRate) % len(self.EnemyAtkAnimations[self.EnemyType])
        return self.EnemyAtkAnimations[self.EnemyType][frame_idx]

    def drawStand(self):
        return self.EnemyAtkAnimations[self.EnemyType][0]