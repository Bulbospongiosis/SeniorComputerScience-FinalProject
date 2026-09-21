import pygame            

WIDTH,HEIGHT = 1250,750

def UnitOperations(UnitCount,UnitX,data,UnitType,UnitAnimation,FrameRate,EnemyCount,EnemyX,UnitCooldown,UnitAtkAnimation,UnitHealth,EnemyHealth):
    
    for i in range(UnitCount):
        if UnitHealth[i] <= 0:
            UnitX[i] = 0
        if abs(UnitX[i] - FrontmostEnemy(EnemyX,EnemyCount)) > data["Units"][UnitType[i]]["UnitRange"] and UnitX[i] > 0:
            
            UnitX[i] += data["Units"][UnitType[i]]["UnitSpeed"]*24/FrameRate
            UnitAnimation[i] += 1 if UnitAnimation[i] < data["Units"][UnitType[i]]["UnitWalkFrames"]*FrameRate/12 else 1 - data["Units"][UnitType[i]]["UnitWalkFrames"]*FrameRate/12
        else:
            
            if UnitCooldown[i] <= 0:
                if UnitAtkAnimation[i] >= data["Units"][UnitType[i]]["UnitAtkFrames"]*FrameRate/12:
                    UnitCooldown[i] = data["Units"][UnitType[i]]["UnitAtkCooldown"]*FrameRate
                    UnitAtkAnimation[i] = 0
                    for j in range(EnemyCount):
                        if EnemyX[j] <= UnitX[i] + data["Units"][UnitType[i]]["UnitRange"] + data["Units"][UnitType[i]]["UnitPierce"] and EnemyX[j] >= UnitX[i] + data["Units"][UnitType[i]]["UnitBlindspot"]:
                            EnemyHealth[j] -= data["Units"][UnitType[i]]["UnitDamage"]
                            
                else:
                    UnitAtkAnimation[i] += 1
            else:
                UnitCooldown[i] -= 1
                UnitAtkAnimation[i] = 0

def EnemyOperations(EnemyCount,EnemyX,data,EnemyType,EnemyAnimation,FrameRate,UnitCount,UnitX,UnitHealth,EnemyHealth,EnemyCooldown,EnemyAtkAnimation):   
    
    for i in range(EnemyCount):
        if EnemyHealth[i] <= 0:
            EnemyX[i] = WIDTH
        if abs(EnemyX[i] - FrontmostUnit(UnitX,UnitCount)) > data["Enemy"][EnemyType[i]]["EnemyRange"] and EnemyX[i] < WIDTH:
            EnemyX[i] -= data["Enemy"][EnemyType[i]]["EnemySpeed"]*24/FrameRate
            EnemyAnimation[i] += 1 if EnemyAnimation[i] < data["Enemy"][EnemyType[i]]["EnemyWalkFrames"]*FrameRate/12 else 1 - data["Enemy"][EnemyType[i]]["EnemyWalkFrames"]*FrameRate/12
        else:
                    
            if EnemyCooldown[i] <= 0:
                if EnemyAtkAnimation[i] >= data["Enemy"][EnemyType[i]]["EnemyAtkFrames"]*FrameRate/12:
                    EnemyCooldown[i] = data["Enemy"][EnemyType[i]]["EnemyAtkCooldown"]*FrameRate
                    EnemyAtkAnimation[i] = 0
                    for j in range(UnitCount):
                        if UnitX[j] >= EnemyX[i] - data["Enemy"][EnemyType[i]]["EnemyRange"] - data["Enemy"][EnemyType[i]]["EnemyPierce"] and UnitX[j] <= EnemyX[i] - data["Enemy"][EnemyType[i]]["EnemyBlindspot"]:
                            UnitHealth[j] -= data["Enemy"][EnemyType[i]]["EnemyDamage"]
                            
                else:
                    EnemyAtkAnimation[i] += 1
            else:
                EnemyCooldown[i] -= 1
                EnemyAtkAnimation[i] = 0
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