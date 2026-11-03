import pygame
import json
import os

with open("CharacterDataSheet.json", "r") as file:
    data = json.load(file)

if not pygame.get_init():
    pygame.init()
WIDTH,HEIGHT = 1250,750
screen = pygame.display.set_mode((WIDTH,HEIGHT))
class Unit:

    JohnWalk = [pygame.transform.scale(pygame.image.load('__Pngs__/cat.png').convert_alpha(), (data["Units"][0]["UnitSize"], data["Units"][0]["UnitSize"])),
                pygame.transform.scale(pygame.image.load('__Pngs__/cat.png').convert_alpha(), (data["Units"][0]["UnitSize"], data["Units"][0]["UnitSize"]))]
    JohnAtk = [pygame.transform.scale(pygame.image.load('__Pngs__/cat.png').convert_alpha(), (data["Units"][0]["UnitSize"], data["Units"][0]["UnitSize"]))]

    PatrickWalk = [pygame.transform.scale(pygame.image.load('Patrick/stand.png').convert_alpha(), (data["Units"][1]["UnitSize"], data["Units"][1]["UnitSize"])),
                    pygame.transform.scale(pygame.image.load('Patrick/stand.png').convert_alpha(), (data["Units"][1]["UnitSize"], data["Units"][1]["UnitSize"]))]
    PatrickAtk = [pygame.transform.scale(pygame.image.load('Patrick/stand.png').convert_alpha(), (data["Units"][1]["UnitSize"], data["Units"][1]["UnitSize"]))]
    

    WalkAnimations = [JohnWalk,PatrickWalk]
    AtkAnimations = [JohnAtk,PatrickAtk]


    def __init__(self):
        self.UnitX = 0
        self.UnitType = 0
        self.UnitAnimation = 0
        self.UnitAtkAnimation = 0
        self.UnitCooldown = 0
        self.UnitHealth = 0
        self.FrameRate = 60

    def drawWalk(self):
        frame_idx = int(self.UnitAnimation * 12 / self.FrameRate) % len(self.WalkAnimations[self.UnitType])
        return self.WalkAnimations[self.UnitType][frame_idx]

    def drawAtk(self):
        frame_idx = int(self.UnitAtkAnimation * 12 / self.FrameRate) % len(self.AtkAnimations[self.UnitType])
        return self.AtkAnimations[self.UnitType][frame_idx]

    def drawStand(self):
        return self.AtkAnimations[self.UnitType][0]