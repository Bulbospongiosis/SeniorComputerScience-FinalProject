import pygame

#Colors
WHITE = (255,255,255)
BLACK = (0,0,0)
BLUE = (50,150,255)
GREEN = (50,200,50)
RED = (255,0,0)
PURPLE = (128,0,128)
ORANGE = (255, 165, 0)

WIDTH,HEIGHT = 1250,750

def Draw(screen,data,UnitX,UnitType,UnitAnimation,EnemyX,UnitY,EnemyY,EnemyType,UnitCount,EnemyCount):
    screen.fill(WHITE)
    #pygame.draw.rect(screen,BLACK,(0,0,100,100))
    
    for i in range(UnitCount):
        if UnitX[i] > 0:
            
            pygame.draw.rect(screen,BLACK,(UnitX[i] - data["Units"][UnitType[i]]["UnitSize"],UnitY - data["Units"][UnitType[i]]["UnitSize"],data["Units"][UnitType[i]]["UnitSize"],data["Units"][UnitType[i]]["UnitSize"]))
    for i in range(EnemyCount):
        if EnemyX[i] < WIDTH:
            
            pygame.draw.rect(screen,BLACK,(EnemyX[i],EnemyY - data["Enemy"][EnemyType[i]]["EnemySize"],data["Enemy"][EnemyType[i]]["EnemySize"],data["Enemy"][EnemyType[i]]["EnemySize"]))
