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

##########################################################
    DivaWalk = [pygame.transform.scale(pygame.image.load('Diva/diva0.png').convert_alpha(), (data["Units"][3]["UnitSize"], data["Units"][3]["UnitSize"])),
                    pygame.transform.scale(pygame.image.load('Diva/diva1.png').convert_alpha(), (data["Units"][3]["UnitSize"], data["Units"][3]["UnitSize"])),
                    pygame.transform.scale(pygame.image.load('Diva/diva2.png').convert_alpha(), (data["Units"][3]["UnitSize"], data["Units"][3]["UnitSize"])),
                    pygame.transform.scale(pygame.image.load('Diva/diva3.png').convert_alpha(), (data["Units"][3]["UnitSize"], data["Units"][3]["UnitSize"])),
                    pygame.transform.scale(pygame.image.load('Diva/diva4.png').convert_alpha(), (data["Units"][3]["UnitSize"], data["Units"][3]["UnitSize"])),
                    pygame.transform.scale(pygame.image.load('Diva/diva5.png').convert_alpha(), (data["Units"][3]["UnitSize"], data["Units"][3]["UnitSize"])),
                    pygame.transform.scale(pygame.image.load('Diva/diva6.png').convert_alpha(), (data["Units"][3]["UnitSize"], data["Units"][3]["UnitSize"])),
                    pygame.transform.scale(pygame.image.load('Diva/diva7.png').convert_alpha(), (data["Units"][3]["UnitSize"], data["Units"][3]["UnitSize"]))]
                        
    DivaAtk = [pygame.transform.scale(pygame.image.load('Diva/divaatk00.png').convert_alpha(), (data["Units"][3]["UnitSize"], data["Units"][3]["UnitSize"])),
                pygame.transform.scale(pygame.image.load('Diva/divaatk01.png').convert_alpha(), (data["Units"][3]["UnitSize"], data["Units"][3]["UnitSize"])),
                pygame.transform.scale(pygame.image.load('Diva/divaatk02.png').convert_alpha(), (data["Units"][3]["UnitSize"], data["Units"][3]["UnitSize"])),
                pygame.transform.scale(pygame.image.load('Diva/divaatk03.png').convert_alpha(), (data["Units"][3]["UnitSize"], data["Units"][3]["UnitSize"])),
                pygame.transform.scale(pygame.image.load('Diva/divaatk04.png').convert_alpha(), (data["Units"][3]["UnitSize"], data["Units"][3]["UnitSize"])),
                pygame.transform.scale(pygame.image.load('Diva/divaatk05.png').convert_alpha(), (data["Units"][3]["UnitSize"], data["Units"][3]["UnitSize"])),
                pygame.transform.scale(pygame.image.load('Diva/divaatk06.png').convert_alpha(), (data["Units"][3]["UnitSize"], data["Units"][3]["UnitSize"])),
                pygame.transform.scale(pygame.image.load('Diva/divaatk07.png').convert_alpha(), (data["Units"][3]["UnitSize"], data["Units"][3]["UnitSize"])),
                pygame.transform.scale(pygame.image.load('Diva/divaatk08.png').convert_alpha(), (data["Units"][3]["UnitSize"], data["Units"][3]["UnitSize"])),
                pygame.transform.scale(pygame.image.load('Diva/divaatk08.png').convert_alpha(), (data["Units"][3]["UnitSize"], data["Units"][3]["UnitSize"])),
                pygame.transform.scale(pygame.image.load('Diva/divaatk08.png').convert_alpha(), (data["Units"][3]["UnitSize"], data["Units"][3]["UnitSize"])),
                pygame.transform.scale(pygame.image.load('Diva/divaatk09.png').convert_alpha(), (data["Units"][3]["UnitSize"], data["Units"][3]["UnitSize"])),
                                ]
                
    DivaPost = [pygame.transform.scale(pygame.image.load('Diva/divaatk10.png').convert_alpha(), (data["Units"][3]["UnitSize"], data["Units"][3]["UnitSize"])),
                    pygame.transform.scale(pygame.image.load('Diva/divaatk11.png').convert_alpha(), (data["Units"][3]["UnitSize"], data["Units"][3]["UnitSize"])),
                    pygame.transform.scale(pygame.image.load('Diva/divaatk12.png').convert_alpha(), (data["Units"][3]["UnitSize"], data["Units"][3]["UnitSize"])),
                    pygame.transform.scale(pygame.image.load('Diva/divaatk13.png').convert_alpha(), (data["Units"][3]["UnitSize"], data["Units"][3]["UnitSize"])),
                    pygame.transform.scale(pygame.image.load('Diva/divaatk14.png').convert_alpha(), (data["Units"][3]["UnitSize"], data["Units"][3]["UnitSize"])),
                    pygame.transform.scale(pygame.image.load('Diva/divaatk14.png').convert_alpha(), (data["Units"][3]["UnitSize"], data["Units"][3]["UnitSize"])),
                    pygame.transform.scale(pygame.image.load('Diva/divaatk15.png').convert_alpha(), (data["Units"][3]["UnitSize"], data["Units"][3]["UnitSize"])),                                              
                    pygame.transform.scale(pygame.image.load('Diva/divaatk15.png').convert_alpha(), (data["Units"][3]["UnitSize"], data["Units"][3]["UnitSize"])),                           
                    pygame.transform.scale(pygame.image.load('Diva/divaatk16.png').convert_alpha(), (data["Units"][3]["UnitSize"], data["Units"][3]["UnitSize"]))]                       

##########################################################
    BombWalk = [pygame.transform.scale(pygame.image.load('Bomb/bomb0.png').convert_alpha(), (data["Units"][4]["UnitSize"], data["Units"][4]["UnitSize"])),
                    pygame.transform.scale(pygame.image.load('Bomb/bomb1.png').convert_alpha(), (data["Units"][4]["UnitSize"], data["Units"][4]["UnitSize"])),
                    pygame.transform.scale(pygame.image.load('Bomb/bomb2.png').convert_alpha(), (data["Units"][4]["UnitSize"], data["Units"][4]["UnitSize"])),
                    pygame.transform.scale(pygame.image.load('Bomb/bomb3.png').convert_alpha(), (data["Units"][4]["UnitSize"], data["Units"][4]["UnitSize"])),
                    pygame.transform.scale(pygame.image.load('Bomb/bomb4.png').convert_alpha(), (data["Units"][4]["UnitSize"], data["Units"][4]["UnitSize"]))
                    ]
                        
    BombAtk = [pygame.transform.scale(pygame.image.load('Bomb/bombatk00.png').convert_alpha(), (data["Units"][4]["UnitSize"], data["Units"][4]["UnitSize"])),
                pygame.transform.scale(pygame.image.load('Bomb/bombatk01.png').convert_alpha(), (data["Units"][4]["UnitSize"], data["Units"][4]["UnitSize"])),
                pygame.transform.scale(pygame.image.load('Bomb/bombatk02.png').convert_alpha(), (data["Units"][4]["UnitSize"], data["Units"][4]["UnitSize"])),
                pygame.transform.scale(pygame.image.load('Bomb/bombatk03.png').convert_alpha(), (data["Units"][4]["UnitSize"], data["Units"][4]["UnitSize"])),
                pygame.transform.scale(pygame.image.load('Bomb/bombatk04.png').convert_alpha(), (data["Units"][4]["UnitSize"], data["Units"][4]["UnitSize"])),
                pygame.transform.scale(pygame.image.load('Bomb/bombatk05.png').convert_alpha(), (data["Units"][4]["UnitSize"], data["Units"][4]["UnitSize"])),
                pygame.transform.scale(pygame.image.load('Bomb/bombatk06.png').convert_alpha(), (data["Units"][4]["UnitSize"], data["Units"][4]["UnitSize"])),
                pygame.transform.scale(pygame.image.load('Bomb/bombatk07.png').convert_alpha(), (data["Units"][4]["UnitSize"], data["Units"][4]["UnitSize"])),
                pygame.transform.scale(pygame.image.load('Bomb/bombatk08.png').convert_alpha(), (data["Units"][4]["UnitSize"], data["Units"][4]["UnitSize"])),
                pygame.transform.scale(pygame.image.load('Bomb/bombatk09.png').convert_alpha(), (data["Units"][4]["UnitSize"], data["Units"][4]["UnitSize"])),
                                ]
                
    BombPost = [pygame.transform.scale(pygame.image.load('Bomb/bombatk10.png').convert_alpha(), (data["Units"][4]["UnitSize"], data["Units"][4]["UnitSize"])),
                pygame.transform.scale(pygame.image.load('Bomb/bombatk11.png').convert_alpha(), (data["Units"][4]["UnitSize"], data["Units"][4]["UnitSize"])),
                pygame.transform.scale(pygame.image.load('Bomb/bombatk12.png').convert_alpha(), (data["Units"][4]["UnitSize"], data["Units"][4]["UnitSize"])),
                pygame.transform.scale(pygame.image.load('Bomb/bombatk13.png').convert_alpha(), (data["Units"][4]["UnitSize"], data["Units"][4]["UnitSize"])),
                pygame.transform.scale(pygame.image.load('Bomb/bombatk14.png').convert_alpha(), (data["Units"][4]["UnitSize"], data["Units"][4]["UnitSize"])),
                pygame.transform.scale(pygame.image.load('Bomb/bombatk15.png').convert_alpha(), (data["Units"][4]["UnitSize"], data["Units"][4]["UnitSize"])),
                pygame.transform.scale(pygame.image.load('Bomb/bombatk16.png').convert_alpha(), (data["Units"][4]["UnitSize"], data["Units"][4]["UnitSize"])),
                pygame.transform.scale(pygame.image.load('Bomb/bombatk17.png').convert_alpha(), (data["Units"][4]["UnitSize"], data["Units"][4]["UnitSize"])),
                pygame.transform.scale(pygame.image.load('Bomb/bombatk18.png').convert_alpha(), (data["Units"][4]["UnitSize"], data["Units"][4]["UnitSize"])),
                pygame.transform.scale(pygame.image.load('Bomb/bombatk19.png').convert_alpha(), (data["Units"][4]["UnitSize"], data["Units"][4]["UnitSize"]))]                       
 #######################################
 # 
    TankmanWalk = [pygame.transform.scale(pygame.image.load('Tankman/tankman0.png').convert_alpha(), (data["Units"][5]["UnitSize"], data["Units"][5]["UnitSize"])),
                pygame.transform.scale(pygame.image.load('Tankman/tankman1.png').convert_alpha(), (data["Units"][5]["UnitSize"], data["Units"][5]["UnitSize"])),
                pygame.transform.scale(pygame.image.load('Tankman/tankman2.png').convert_alpha(), (data["Units"][5]["UnitSize"], data["Units"][5]["UnitSize"])),
                pygame.transform.scale(pygame.image.load('Tankman/tankman3.png').convert_alpha(), (data["Units"][5]["UnitSize"], data["Units"][5]["UnitSize"]))]
                    
    TankmanAtk = [pygame.transform.scale(pygame.image.load('Tankman/tankmanatk00.png').convert_alpha(), (data["Units"][5]["UnitSize"], data["Units"][5]["UnitSize"])),
                  pygame.transform.scale(pygame.image.load('Tankman/tankmanatk01.png').convert_alpha(), (data["Units"][5]["UnitSize"], data["Units"][5]["UnitSize"])),
                  pygame.transform.scale(pygame.image.load('Tankman/tankmanatk02.png').convert_alpha(), (data["Units"][5]["UnitSize"], data["Units"][5]["UnitSize"])),
                  pygame.transform.scale(pygame.image.load('Tankman/tankmanatk03.png').convert_alpha(), (data["Units"][5]["UnitSize"], data["Units"][5]["UnitSize"])),
                  pygame.transform.scale(pygame.image.load('Tankman/tankmanatk04.png').convert_alpha(), (data["Units"][5]["UnitSize"], data["Units"][5]["UnitSize"])),
                  pygame.transform.scale(pygame.image.load('Tankman/tankmanatk05.png').convert_alpha(), (data["Units"][5]["UnitSize"], data["Units"][5]["UnitSize"])),
                  pygame.transform.scale(pygame.image.load('Tankman/tankmanatk06.png').convert_alpha(), (data["Units"][5]["UnitSize"], data["Units"][5]["UnitSize"])),
                  pygame.transform.scale(pygame.image.load('Tankman/tankmanatk07.png').convert_alpha(), (data["Units"][5]["UnitSize"], data["Units"][5]["UnitSize"])),
                  pygame.transform.scale(pygame.image.load('Tankman/tankmanatk08.png').convert_alpha(), (data["Units"][5]["UnitSize"], data["Units"][5]["UnitSize"])),
                  pygame.transform.scale(pygame.image.load('Tankman/tankmanatk09.png').convert_alpha(), (data["Units"][5]["UnitSize"], data["Units"][5]["UnitSize"])),
                  pygame.transform.scale(pygame.image.load('Tankman/tankmanatk09.png').convert_alpha(), (data["Units"][5]["UnitSize"], data["Units"][5]["UnitSize"])),
                  pygame.transform.scale(pygame.image.load('Tankman/tankmanatk09.png').convert_alpha(), (data["Units"][5]["UnitSize"], data["Units"][5]["UnitSize"])),
                  pygame.transform.scale(pygame.image.load('Tankman/tankmanatk09.png').convert_alpha(), (data["Units"][5]["UnitSize"], data["Units"][5]["UnitSize"])),
                  pygame.transform.scale(pygame.image.load('Tankman/tankmanatk09.png').convert_alpha(), (data["Units"][5]["UnitSize"], data["Units"][5]["UnitSize"])),
                  pygame.transform.scale(pygame.image.load('Tankman/tankmanatk09.png').convert_alpha(), (data["Units"][5]["UnitSize"], data["Units"][5]["UnitSize"])),
                  pygame.transform.scale(pygame.image.load('Tankman/tankmanatk09.png').convert_alpha(), (data["Units"][5]["UnitSize"], data["Units"][5]["UnitSize"])),
                  pygame.transform.scale(pygame.image.load('Tankman/tankmanatk10.png').convert_alpha(), (data["Units"][5]["UnitSize"], data["Units"][5]["UnitSize"])),
                  pygame.transform.scale(pygame.image.load('Tankman/tankmanatk11.png').convert_alpha(), (data["Units"][5]["UnitSize"], data["Units"][5]["UnitSize"])),
                  pygame.transform.scale(pygame.image.load('Tankman/tankmanatk12.png').convert_alpha(), (data["Units"][5]["UnitSize"], data["Units"][5]["UnitSize"])),
                  pygame.transform.scale(pygame.image.load('Tankman/tankmanatk13.png').convert_alpha(), (data["Units"][5]["UnitSize"], data["Units"][5]["UnitSize"])),]
    TankmanPost = [pygame.transform.scale(pygame.image.load('Tankman/tankmanatk13.png').convert_alpha(), (data["Units"][5]["UnitSize"], data["Units"][5]["UnitSize"])),
                   pygame.transform.scale(pygame.image.load('Tankman/tankmanatk13.png').convert_alpha(), (data["Units"][5]["UnitSize"], data["Units"][5]["UnitSize"])),
                   pygame.transform.scale(pygame.image.load('Tankman/tankmanatk13.png').convert_alpha(), (data["Units"][5]["UnitSize"], data["Units"][5]["UnitSize"])),
                   pygame.transform.scale(pygame.image.load('Tankman/tankmanatk13.png').convert_alpha(), (data["Units"][5]["UnitSize"], data["Units"][5]["UnitSize"])),
                   pygame.transform.scale(pygame.image.load('Tankman/tankmanatk13.png').convert_alpha(), (data["Units"][5]["UnitSize"], data["Units"][5]["UnitSize"])),
                   pygame.transform.scale(pygame.image.load('Tankman/tankmanatk13.png').convert_alpha(), (data["Units"][5]["UnitSize"], data["Units"][5]["UnitSize"])),
                   pygame.transform.scale(pygame.image.load('Tankman/tankmanatk13.png').convert_alpha(), (data["Units"][5]["UnitSize"], data["Units"][5]["UnitSize"])),
                   pygame.transform.scale(pygame.image.load('Tankman/tankmanatk13.png').convert_alpha(), (data["Units"][5]["UnitSize"], data["Units"][5]["UnitSize"])),
                   pygame.transform.scale(pygame.image.load('Tankman/tankmanatk14.png').convert_alpha(), (data["Units"][5]["UnitSize"], data["Units"][5]["UnitSize"])),
                   pygame.transform.scale(pygame.image.load('Tankman/tankmanatk15.png').convert_alpha(), (data["Units"][5]["UnitSize"], data["Units"][5]["UnitSize"])),
                   pygame.transform.scale(pygame.image.load('Tankman/tankmanatk16.png').convert_alpha(), (data["Units"][5]["UnitSize"], data["Units"][5]["UnitSize"])),
                   pygame.transform.scale(pygame.image.load('Tankman/tankmanatk17.png').convert_alpha(), (data["Units"][5]["UnitSize"], data["Units"][5]["UnitSize"])),
                   pygame.transform.scale(pygame.image.load('Tankman/tankmanatk18.png').convert_alpha(), (data["Units"][5]["UnitSize"], data["Units"][5]["UnitSize"])),
                   pygame.transform.scale(pygame.image.load('Tankman/tankmanatk19.png').convert_alpha(), (data["Units"][5]["UnitSize"], data["Units"][5]["UnitSize"])),]
                        

###################################

    FishWalk = [pygame.transform.scale(pygame.image.load('Fish/fish0.png').convert_alpha(), (data["Units"][6]["UnitSize"], data["Units"][6]["UnitSize"])),
                pygame.transform.scale(pygame.image.load('Fish/fish1.png').convert_alpha(), (data["Units"][6]["UnitSize"], data["Units"][6]["UnitSize"])),
                pygame.transform.scale(pygame.image.load('Fish/fish2.png').convert_alpha(), (data["Units"][6]["UnitSize"], data["Units"][6]["UnitSize"])),
                pygame.transform.scale(pygame.image.load('Fish/fish3.png').convert_alpha(), (data["Units"][6]["UnitSize"], data["Units"][6]["UnitSize"])),
                pygame.transform.scale(pygame.image.load('Fish/fish4.png').convert_alpha(), (data["Units"][6]["UnitSize"], data["Units"][6]["UnitSize"])),
                pygame.transform.scale(pygame.image.load('Fish/fish5.png').convert_alpha(), (data["Units"][6]["UnitSize"], data["Units"][6]["UnitSize"])),
                pygame.transform.scale(pygame.image.load('Fish/fish6.png').convert_alpha(), (data["Units"][6]["UnitSize"], data["Units"][6]["UnitSize"])),
                pygame.transform.scale(pygame.image.load('Fish/fish7.png').convert_alpha(), (data["Units"][6]["UnitSize"], data["Units"][6]["UnitSize"]))]
    FishAtk = [pygame.transform.scale(pygame.image.load('Fish/fishatk00.png').convert_alpha(), (data["Units"][6]["UnitSize"], data["Units"][6]["UnitSize"])),
               pygame.transform.scale(pygame.image.load('Fish/fishatk01.png').convert_alpha(), (data["Units"][6]["UnitSize"], data["Units"][6]["UnitSize"])),
               pygame.transform.scale(pygame.image.load('Fish/fishatk02.png').convert_alpha(), (data["Units"][6]["UnitSize"], data["Units"][6]["UnitSize"])),
               pygame.transform.scale(pygame.image.load('Fish/fishatk03.png').convert_alpha(), (data["Units"][6]["UnitSize"], data["Units"][6]["UnitSize"])),
               pygame.transform.scale(pygame.image.load('Fish/fishatk04.png').convert_alpha(), (data["Units"][6]["UnitSize"], data["Units"][6]["UnitSize"])),
               pygame.transform.scale(pygame.image.load('Fish/fishatk05.png').convert_alpha(), (data["Units"][6]["UnitSize"], data["Units"][6]["UnitSize"])),
               pygame.transform.scale(pygame.image.load('Fish/fishatk06.png').convert_alpha(), (data["Units"][6]["UnitSize"], data["Units"][6]["UnitSize"])),
               pygame.transform.scale(pygame.image.load('Fish/fishatk07.png').convert_alpha(), (data["Units"][6]["UnitSize"], data["Units"][6]["UnitSize"])),
               pygame.transform.scale(pygame.image.load('Fish/fishatk08.png').convert_alpha(), (data["Units"][6]["UnitSize"], data["Units"][6]["UnitSize"])),
               pygame.transform.scale(pygame.image.load('Fish/fishatk09.png').convert_alpha(), (data["Units"][6]["UnitSize"], data["Units"][6]["UnitSize"])),
               pygame.transform.scale(pygame.image.load('Fish/fishatk09.png').convert_alpha(), (data["Units"][6]["UnitSize"], data["Units"][6]["UnitSize"])),
               pygame.transform.scale(pygame.image.load('Fish/fishatk09.png').convert_alpha(), (data["Units"][6]["UnitSize"], data["Units"][6]["UnitSize"])),
               pygame.transform.scale(pygame.image.load('Fish/fishatk09.png').convert_alpha(), (data["Units"][6]["UnitSize"], data["Units"][6]["UnitSize"])),
               pygame.transform.scale(pygame.image.load('Fish/fishatk09.png').convert_alpha(), (data["Units"][6]["UnitSize"], data["Units"][6]["UnitSize"])),
               pygame.transform.scale(pygame.image.load('Fish/fishatk09.png').convert_alpha(), (data["Units"][6]["UnitSize"], data["Units"][6]["UnitSize"])),
               pygame.transform.scale(pygame.image.load('Fish/fishatk10.png').convert_alpha(), (data["Units"][6]["UnitSize"], data["Units"][6]["UnitSize"])),
               pygame.transform.scale(pygame.image.load('Fish/fishatk11.png').convert_alpha(), (data["Units"][6]["UnitSize"], data["Units"][6]["UnitSize"])),
               pygame.transform.scale(pygame.image.load('Fish/fishatk12.png').convert_alpha(), (data["Units"][6]["UnitSize"], data["Units"][6]["UnitSize"])),
               pygame.transform.scale(pygame.image.load('Fish/fishatk13.png').convert_alpha(), (data["Units"][6]["UnitSize"], data["Units"][6]["UnitSize"])),
               pygame.transform.scale(pygame.image.load('Fish/fishatk14.png').convert_alpha(), (data["Units"][6]["UnitSize"], data["Units"][6]["UnitSize"])),
               pygame.transform.scale(pygame.image.load('Fish/fishatk15.png').convert_alpha(), (data["Units"][6]["UnitSize"], data["Units"][6]["UnitSize"])),
               pygame.transform.scale(pygame.image.load('Fish/fishatk16.png').convert_alpha(), (data["Units"][6]["UnitSize"], data["Units"][6]["UnitSize"])),]
    FishPost = [pygame.transform.scale(pygame.image.load('Fish/fishatk17.png').convert_alpha(), (data["Units"][6]["UnitSize"], data["Units"][6]["UnitSize"])),
                pygame.transform.scale(pygame.image.load('Fish/fishatk18.png').convert_alpha(), (data["Units"][6]["UnitSize"], data["Units"][6]["UnitSize"])),
                pygame.transform.scale(pygame.image.load('Fish/fishatk19.png').convert_alpha(), (data["Units"][6]["UnitSize"], data["Units"][6]["UnitSize"])),
                pygame.transform.scale(pygame.image.load('Fish/fishatk20.png').convert_alpha(), (data["Units"][6]["UnitSize"], data["Units"][6]["UnitSize"])),
                pygame.transform.scale(pygame.image.load('Fish/fishatk21.png').convert_alpha(), (data["Units"][6]["UnitSize"], data["Units"][6]["UnitSize"])),
                pygame.transform.scale(pygame.image.load('Fish/fishatk22.png').convert_alpha(), (data["Units"][6]["UnitSize"], data["Units"][6]["UnitSize"])),
                pygame.transform.scale(pygame.image.load('Fish/fishatk23.png').convert_alpha(), (data["Units"][6]["UnitSize"], data["Units"][6]["UnitSize"])),
                pygame.transform.scale(pygame.image.load('Fish/fishatk24.png').convert_alpha(), (data["Units"][6]["UnitSize"], data["Units"][6]["UnitSize"])),
                pygame.transform.scale(pygame.image.load('Fish/fishatk25.png').convert_alpha(), (data["Units"][6]["UnitSize"], data["Units"][6]["UnitSize"])),
                pygame.transform.scale(pygame.image.load('Fish/fishatk26.png').convert_alpha(), (data["Units"][6]["UnitSize"], data["Units"][6]["UnitSize"])),
                pygame.transform.scale(pygame.image.load('Fish/fishatk27.png').convert_alpha(), (data["Units"][6]["UnitSize"], data["Units"][6]["UnitSize"])),
                pygame.transform.scale(pygame.image.load('Fish/fishatk28.png').convert_alpha(), (data["Units"][6]["UnitSize"], data["Units"][6]["UnitSize"])),
                pygame.transform.scale(pygame.image.load('Fish/fishatk29.png').convert_alpha(), (data["Units"][6]["UnitSize"], data["Units"][6]["UnitSize"])),
                pygame.transform.scale(pygame.image.load('Fish/fishatk30.png').convert_alpha(), (data["Units"][6]["UnitSize"], data["Units"][6]["UnitSize"])),
                pygame.transform.scale(pygame.image.load('Fish/fishatk30.png').convert_alpha(), (data["Units"][6]["UnitSize"], data["Units"][6]["UnitSize"])),
                pygame.transform.scale(pygame.image.load('Fish/fishatk30.png').convert_alpha(), (data["Units"][6]["UnitSize"], data["Units"][6]["UnitSize"])),
                pygame.transform.scale(pygame.image.load('Fish/fishatk30.png').convert_alpha(), (data["Units"][6]["UnitSize"], data["Units"][6]["UnitSize"])),
                pygame.transform.scale(pygame.image.load('Fish/fishatk31.png').convert_alpha(), (data["Units"][6]["UnitSize"], data["Units"][6]["UnitSize"])),
                pygame.transform.scale(pygame.image.load('Fish/fishatk32.png').convert_alpha(), (data["Units"][6]["UnitSize"], data["Units"][6]["UnitSize"])),
                pygame.transform.scale(pygame.image.load('Fish/fishatk33.png').convert_alpha(), (data["Units"][6]["UnitSize"], data["Units"][6]["UnitSize"])),
                pygame.transform.scale(pygame.image.load('Fish/fishatk34.png').convert_alpha(), (data["Units"][6]["UnitSize"], data["Units"][6]["UnitSize"])),]
    

    WalkAnimations = [JohnWalk,CatWalk,TankWalk,DivaWalk,BombWalk,TankmanWalk,FishWalk]
    AtkAnimations = [JohnAtk,CatAtk,TankAtk,DivaAtk,BombAtk,TankmanAtk,FishAtk]
    PostAnimations = [JohnPost,CatPost,TankPost,DivaPost,BombPost,TankmanPost,FishPost]

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

    def spawn(self):
        self.Range = data["Units"][self.UnitType]["UnitRange"] + random.randint(-2, 2)