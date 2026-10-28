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

    JohnWalk = [pygame.transform.scale(pygame.image.load('__Pngs__/cat.png').convert_alpha(), (data["Units"][0]["UnitSize"], 2 * data["Units"][0]["UnitSize"])),
                pygame.transform.scale(pygame.image.load('__Pngs__/cat.png').convert_alpha(), (data["Units"][0]["UnitSize"], 2 * data["Units"][0]["UnitSize"]))]
    JohnAtk = [pygame.transform.scale(pygame.image.load('__Pngs__/cat.png').convert_alpha(), (data["Units"][0]["UnitSize"], 2 * data["Units"][0]["UnitSize"]))]

    WalkAnimations = [JohnWalk]
    AtkAnimations = [JohnAtk]


    def __init__(self):
        self.UnitX = 0
        self.UnitType = 0
        self.UnitAnimation = 0
        self.UnitAtkAnimation = 0
        self.UnitCooldown = 0
        self.UnitHealth = 0