import pygame            

WIDTH,HEIGHT = 1250,750

def UnitOperations(UnitCount,UnitX,data,UnitType,UnitAnimation,FrameRate,EnemyCount,EnemyX):
    
    for i in range(UnitCount):
        if abs(UnitX[i] - FrontmostEnemy(EnemyX,EnemyCount)) > data["Units"][UnitType[i]]["UnitRange"] and UnitX[i] > 0:
            
            UnitX[i] += data["Units"][UnitType[i]]["UnitSpeed"]*24/FrameRate
            UnitAnimation[i] += 1 if UnitAnimation[i] == data["Units"][UnitType[i]]["UnitWalkFrames"] else 1 - data["Units"][UnitType[i]]["UnitWalkFrames"]

def EnemyOperations(EnemyCount,EnemyX,data,EnemyType,EnemyAnimation,FrameRate,UnitCount,UnitX):   
    
    for i in range(EnemyCount):
        if abs(EnemyX[i] - FrontmostUnit(UnitX,UnitCount)) > data["Enemy"][EnemyType[i]]["EnemyRange"] and EnemyX[i] < WIDTH:
            EnemyX[i] -= data["Enemy"][EnemyType[i]]["EnemySpeed"]*24/FrameRate
            EnemyAnimation[i] += 1 if EnemyAnimation[i] == data["Enemy"][EnemyType[i]]["EnemyWalkFrames"] else 1 - data["Enemy"][EnemyType[i]]["EnemyWalkFrames"]
def FrontmostUnit(UnitX,UnitCount):
    FrontmostX = UnitX[0]
    for i in range(UnitCount):
        if UnitX[i] > FrontmostX:
            FrontmostX = UnitX[i]
    return FrontmostX

def FrontmostEnemy(EnemyX,EnemyCount):
    FrontmostEnemyX = EnemyX[0]
    for i in range(EnemyCount):
        if EnemyX[i] < FrontmostEnemyX:
            FrontmostEnemyX = EnemyX[i]
    return FrontmostEnemyX