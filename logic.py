import pygame            

WIDTH,HEIGHT = 1250,750

def UnitOperations(UnitCount,UnitX,data,UnitType,UnitAnimation,FrameRate,EnemyCount,EnemyX,UnitCooldown,UnitAtkAnimation,UnitHealth,EnemyHealth,WalkAnimations,AtkAnimations,EnemyBaseHealth):
    
    for i in range(UnitCount):
        if UnitHealth[i] <= 0:
            UnitX[i] = 0
        if UnitCooldown[i] >= 0:
            UnitCooldown[i] -= 1
        if (UnitCooldown[i] <= 0 and data["Units"][UnitType[i]]["UnitPause"] == "True") or data["Units"][UnitType[i]]["UnitPause"] == "False":
            if (UnitX[i] + 120 < WIDTH - data["Units"][UnitType[i]]["UnitRange"] and abs(UnitX[i] - FrontmostEnemy(EnemyX,EnemyCount)) > data["Units"][UnitType[i]]["UnitRange"]) and UnitX[i] > 0:
                
                UnitX[i] += data["Units"][UnitType[i]]["UnitSpeed"]*24/FrameRate
                UnitAtkAnimation[i] = 0
                UnitAnimation[i] += 1 if UnitAnimation[i] < len(WalkAnimations[UnitType[i]])*FrameRate/12 else -UnitAnimation[i]
                
            elif UnitX[i] > 0:
                
                if UnitCooldown[i] <= 0:
                    if UnitAtkAnimation[i] >= (len(AtkAnimations[UnitType[i]])-1)*FrameRate/12:
                        UnitCooldown[i] = data["Units"][UnitType[i]]["UnitAtkCooldown"]*FrameRate
                        UnitAtkAnimation[i] = 0

                        if data["Units"][UnitType[i]]["UnitAttackType"] == "Area":
                            if UnitX[i] + 120 >= WIDTH - data["Units"][UnitType[i]]["UnitRange"]:
                                EnemyBaseHealth -= data["Units"][UnitType[i]]["UnitDamage"]
                            for j in range(EnemyCount):
                                if EnemyX[j] <= UnitX[i] + data["Units"][UnitType[i]]["UnitRange"] + data["Units"][UnitType[i]]["UnitPierce"] and EnemyX[j] >= UnitX[i] + data["Units"][UnitType[i]]["UnitBlindspot"]:
                                    EnemyHealth[j] -= data["Units"][UnitType[i]]["UnitDamage"]

                        elif data["Units"][UnitType[i]]["UnitAttackType"] == "Single":
                            if UnitX[i] + 120 >= WIDTH - data["Units"][UnitType[i]]["UnitRange"] and FrontmostEnemy(EnemyX,EnemyCount) > WIDTH - 120:
                                EnemyBaseHealth -= data["Units"][UnitType[i]]["UnitDamage"]
                            for j in range(EnemyCount):
                                if EnemyX[j] <= UnitX[i] + data["Units"][UnitType[i]]["UnitRange"] + data["Units"][UnitType[i]]["UnitPierce"] and EnemyX[j] >= UnitX[i] + data["Units"][UnitType[i]]["UnitBlindspot"]:
                                    if EnemyX[j] == FrontmostEnemy(EnemyX,EnemyCount):
                                        EnemyHealth[j] -= data["Units"][UnitType[i]]["UnitDamage"]
                                        break
                                
                    else:
                        UnitAtkAnimation[i] += 1
                else:
                    UnitCooldown[i] -= 1
                    UnitAtkAnimation[i] = 0

def EnemyOperations(EnemyCount,EnemyX,data,EnemyType,EnemyAnimation,FrameRate,UnitCount,UnitX,UnitHealth,EnemyHealth,EnemyCooldown,EnemyAtkAnimation,EnemyWalkAnimations,EnemyAtkAnimations,UnitBaseHealth):   
    
    for i in range(EnemyCount):
        if EnemyHealth[i] <= 0:
            EnemyX[i] = WIDTH
        if EnemyCooldown[i] >= 0:
            EnemyCooldown[i] -= 1
        if (EnemyCooldown[i] <= 0 and data["Enemy"][EnemyType[i]]["EnemyPause"] == "True") or data["Enemy"][EnemyType[i]]["EnemyPause"] == "False":
            if (EnemyX[i] + 50 > data["Enemy"][EnemyType[i]]["EnemyRange"] and abs(EnemyX[i] - FrontmostUnit(UnitX,UnitCount)) > data["Enemy"][EnemyType[i]]["EnemyRange"]) and EnemyX[i] < WIDTH:
                EnemyX[i] -= data["Enemy"][EnemyType[i]]["EnemySpeed"]*24/FrameRate
                EnemyAnimation[i] += 1 if EnemyAnimation[i] < len(EnemyWalkAnimations[EnemyType[i]])*FrameRate/12 else -EnemyAnimation[i]
                
            elif EnemyX[i] < WIDTH:
                        
                if EnemyCooldown[i] <= 0:
                        if EnemyAtkAnimation[i] >= (len(EnemyAtkAnimations[EnemyType[i]])-1)*FrameRate/12:
                            EnemyCooldown[i] = data["Enemy"][EnemyType[i]]["EnemyAtkCooldown"]*FrameRate
                            EnemyAtkAnimation[i] = 0
                            if data["Enemy"][EnemyType[i]]["EnemyAttackType"] == "Area":
                                if EnemyX[i] + 50 <= data["Enemy"][EnemyType[i]]["EnemyRange"]:
                                    UnitBaseHealth -= data["Enemy"][EnemyType[i]]["EnemyDamage"]
                                    print("attack")
                                for j in range(UnitCount):
                                    if UnitX[j] >= EnemyX[i] - data["Enemy"][EnemyType[i]]["EnemyRange"] - data["Enemy"][EnemyType[i]]["EnemyPierce"] and UnitX[j] <= EnemyX[i] - data["Enemy"][EnemyType[i]]["EnemyBlindspot"]:
                                        UnitHealth[j] -= data["Enemy"][EnemyType[i]]["EnemyDamage"]
                            elif data["Enemy"][EnemyType[i]]["EnemyAttackType"] == "Single":
                                if EnemyX[i] + 50 <= data["Enemy"][EnemyType[i]]["EnemyRange"] and FrontmostUnit(UnitX,UnitCount) < 50:
                                    UnitBaseHealth -= data["Enemy"][EnemyType[i]]["EnemyDamage"]
                                for j in range(UnitCount):
                                    if UnitX[j] >= EnemyX[i] - data["Enemy"][EnemyType[i]]["EnemyRange"] - data["Enemy"][EnemyType[i]]["EnemyPierce"] and UnitX[j] <= EnemyX[i] - data["Enemy"][EnemyType[i]]["EnemyBlindspot"]:
                                        if UnitX[j] == FrontmostUnit(UnitX, UnitCount):
                                            UnitHealth[j] -= data["Enemy"][EnemyType[i]]["EnemyDamage"]
                                            break
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