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
class Unit:

    JohnWalk = [pygame.transform.scale(pygame.image.load('__Pngs__/cat.png').convert_alpha(), (data["Units"][0]["UnitSize"], data["Units"][0]["UnitSize"])),
                pygame.transform.scale(pygame.image.load('__Pngs__/cat.png').convert_alpha(), (data["Units"][0]["UnitSize"], data["Units"][0]["UnitSize"]))]
    JohnAtk = [pygame.transform.scale(pygame.image.load('__Pngs__/cat.png').convert_alpha(), (data["Units"][0]["UnitSize"], data["Units"][0]["UnitSize"]))]
    JohnPost = [pygame.transform.scale(pygame.image.load('__Pngs__/cat.png').convert_alpha(), (data["Units"][0]["UnitSize"], data["Units"][0]["UnitSize"]))]
    
##############################################################
    CatWalk = [pygame.transform.scale(pygame.image.load('Cat/cat0.png').convert_alpha(), (data["Units"][1]["UnitSize"], data["Units"][1]["UnitSize"])),
                    pygame.transform.scale(pygame.image.load('Cat/cat1.png').convert_alpha(), (data["Units"][1]["UnitSize"], data["Units"][1]["UnitSize"])),
                    pygame.transform.scale(pygame.image.load('Cat/cat2.png').convert_alpha(), (data["Units"][1]["UnitSize"], data["Units"][1]["UnitSize"])),
                    pygame.transform.scale(pygame.image.load('Cat/cat3.png').convert_alpha(), (data["Units"][1]["UnitSize"], data["Units"][1]["UnitSize"])),
                    pygame.transform.scale(pygame.image.load('Cat/cat4.png').convert_alpha(), (data["Units"][1]["UnitSize"], data["Units"][1]["UnitSize"])),
                    pygame.transform.scale(pygame.image.load('Cat/cat5.png').convert_alpha(), (data["Units"][1]["UnitSize"], data["Units"][1]["UnitSize"])),
                    pygame.transform.scale(pygame.image.load('Cat/cat6.png').convert_alpha(), (data["Units"][1]["UnitSize"], data["Units"][1]["UnitSize"]))]
                        
    CatAtk = [pygame.transform.scale(pygame.image.load('Cat/cattack0.png').convert_alpha(), (data["Units"][1]["UnitSize"], data["Units"][1]["UnitSize"])),
              pygame.transform.scale(pygame.image.load('Cat/cattack1.png').convert_alpha(), (data["Units"][1]["UnitSize"], data["Units"][1]["UnitSize"])),
              pygame.transform.scale(pygame.image.load('Cat/cattack2.png').convert_alpha(), (data["Units"][1]["UnitSize"], data["Units"][1]["UnitSize"])),
              pygame.transform.scale(pygame.image.load('Cat/cattack3.png').convert_alpha(), (data["Units"][1]["UnitSize"], data["Units"][1]["UnitSize"])),
              pygame.transform.scale(pygame.image.load('Cat/cattack4.png').convert_alpha(), (data["Units"][1]["UnitSize"], data["Units"][1]["UnitSize"]))
              ]
    CatPost = [pygame.transform.scale(pygame.image.load('Cat/cattack5.png').convert_alpha(), (data["Units"][1]["UnitSize"], data["Units"][1]["UnitSize"])),
                pygame.transform.scale(pygame.image.load('Cat/cattack6.png').convert_alpha(), (data["Units"][1]["UnitSize"], data["Units"][1]["UnitSize"]))]
##########################################################
    TankWalk = [pygame.transform.scale(pygame.image.load('Tank/tank0.png').convert_alpha(), (data["Units"][2]["UnitSize"], data["Units"][2]["UnitSize"])),
                    pygame.transform.scale(pygame.image.load('Tank/tank1.png').convert_alpha(), (data["Units"][2]["UnitSize"], data["Units"][2]["UnitSize"])),
                    pygame.transform.scale(pygame.image.load('Tank/tank2.png').convert_alpha(), (data["Units"][2]["UnitSize"], data["Units"][2]["UnitSize"])),
                    pygame.transform.scale(pygame.image.load('Tank/tank3.png').convert_alpha(), (data["Units"][2]["UnitSize"], data["Units"][2]["UnitSize"])),
                    pygame.transform.scale(pygame.image.load('Tank/tank4.png').convert_alpha(), (data["Units"][2]["UnitSize"], data["Units"][2]["UnitSize"])),
                    pygame.transform.scale(pygame.image.load('Tank/tank5.png').convert_alpha(), (data["Units"][2]["UnitSize"], data["Units"][2]["UnitSize"])),
                    pygame.transform.scale(pygame.image.load('Tank/tank6.png').convert_alpha(), (data["Units"][2]["UnitSize"], data["Units"][2]["UnitSize"])),
                    pygame.transform.scale(pygame.image.load('Tank/tank7.png').convert_alpha(), (data["Units"][2]["UnitSize"], data["Units"][2]["UnitSize"]))]
                        
    TankAtk = [pygame.transform.scale(pygame.image.load('Tank/tankatk0.png').convert_alpha(), (data["Units"][2]["UnitSize"], data["Units"][2]["UnitSize"])),
                pygame.transform.scale(pygame.image.load('Tank/tankatk1.png').convert_alpha(), (data["Units"][2]["UnitSize"], data["Units"][2]["UnitSize"])),
                pygame.transform.scale(pygame.image.load('Tank/tankatk2.png').convert_alpha(), (data["Units"][2]["UnitSize"], data["Units"][2]["UnitSize"])),
                pygame.transform.scale(pygame.image.load('Tank/tankatk3.png').convert_alpha(), (data["Units"][2]["UnitSize"], data["Units"][2]["UnitSize"])),
                pygame.transform.scale(pygame.image.load('Tank/tankatk4.png').convert_alpha(), (data["Units"][2]["UnitSize"], data["Units"][2]["UnitSize"]))
                ]
                
    TankPost = [pygame.transform.scale(pygame.image.load('Tank/tankatk5.png').convert_alpha(), (data["Units"][2]["UnitSize"], data["Units"][2]["UnitSize"])),
                pygame.transform.scale(pygame.image.load('Tank/tankatk6.png').convert_alpha(), (data["Units"][2]["UnitSize"], data["Units"][2]["UnitSize"])),
                pygame.transform.scale(pygame.image.load('Tank/tankatk6.png').convert_alpha(), (data["Units"][2]["UnitSize"], data["Units"][2]["UnitSize"])),
                pygame.transform.scale(pygame.image.load('Tank/tankatk6.png').convert_alpha(), (data["Units"][2]["UnitSize"], data["Units"][2]["UnitSize"])),
                pygame.transform.scale(pygame.image.load('Tank/tankatk6.png').convert_alpha(), (data["Units"][2]["UnitSize"], data["Units"][2]["UnitSize"])),
                pygame.transform.scale(pygame.image.load('Tank/tankatk7.png').convert_alpha(), (data["Units"][2]["UnitSize"], data["Units"][2]["UnitSize"]))]


    WalkAnimations = [JohnWalk,CatWalk,TankWalk]
    AtkAnimations = [JohnAtk,CatAtk,TankAtk]
    PostAnimations = [JohnPost,CatPost,TankPost]

    def __init__(self,data):
        self.UnitX = 0
        self.UnitType = 0
        self.UnitAnimation = 0
        self.UnitAtkAnimation = 0
        self.UnitPostAnimation = 99999999
        self.UnitCooldown = 0
        self.UnitHealth = 0
        self.FrameRate = 60
        self.Range = data["Units"][self.UnitType]["UnitRange"] + random.randint(-2, 2)

    def drawWalk(self):
        frame_idx = int(self.UnitAnimation * 12 / self.FrameRate) % len(self.WalkAnimations[self.UnitType])
        return self.WalkAnimations[self.UnitType][frame_idx]

    def drawAtk(self):
        frame_idx = int(self.UnitAtkAnimation * 12 / self.FrameRate) % len(self.AtkAnimations[self.UnitType])
        return self.AtkAnimations[self.UnitType][frame_idx]

    def drawPost(self):
            frame_idx = int(self.UnitPostAnimation * 12 / self.FrameRate) % len(self.PostAnimations[self.UnitType])
            return self.PostAnimations[self.UnitType][frame_idx]

    def drawStand(self):
        return self.AtkAnimations[self.UnitType][0]